#!/usr/bin/env python3
"""
calm-design / scripts/validate-design-md.py

DESIGN.md 파일이 calm-design 9-섹션 표준을 준수하는지 검증.
references/design-md-spec.md 마지막의 "검증 기준" 7개를 자동 실행.

사용법:
    python scripts/validate-design-md.py <path/to/DESIGN.md>

Exit codes:
    0 — 모든 검증 통과
    1 — 입력 파일 없음
    2 — 검증 실패 (1개 이상 항목 실패)
"""

import re
import sys
from pathlib import Path
from dataclasses import dataclass


REQUIRED_SECTIONS = [
    (1, "Visual Theme & Atmosphere"),
    (2, "Color Palette & Roles"),
    (3, "Typography Rules"),
    (4, "Component Stylings"),
    (5, "Layout Principles"),
    (6, "Depth & Elevation"),
    (7, "Motion & Interaction"),
    (8, "Responsive Behavior"),
    (9, "Anti-Patterns"),
]

COMPONENT_STATES = ["Default", "Hover", "Focus", "Active", "Disabled", "Loading"]


@dataclass
class CheckResult:
    name: str
    passed: bool
    detail: str


def validate(content: str) -> list[CheckResult]:
    results = []

    # 1. 9개 섹션 모두 존재 + 각 섹션 ≥ 50자
    section_blocks = {}
    for num, title in REQUIRED_SECTIONS:
        pattern = re.compile(
            rf"^## {num}\..*?(?=^## \d+\.|\Z)", re.MULTILINE | re.DOTALL
        )
        match = pattern.search(content)
        if match:
            block = match.group(0)
            # 헤더 라인 제외한 본문
            body = re.sub(r"^## \d+\.[^\n]*\n", "", block, count=1).strip()
            section_blocks[num] = body
            if len(body) < 50:
                results.append(CheckResult(
                    f"Section {num} ({title})", False,
                    f"본문 {len(body)}자 — 50자 이상 필요"
                ))
            else:
                results.append(CheckResult(
                    f"Section {num} ({title})", True,
                    f"본문 {len(body)}자 ✓"
                ))
        else:
            results.append(CheckResult(
                f"Section {num} ({title})", False,
                "섹션 헤더 미발견"
            ))

    # 2. 색상 hex 유효성 (Section 2)
    if 2 in section_blocks:
        hexes = re.findall(r"#[0-9a-fA-F]{3,8}\b", section_blocks[2])
        valid_hexes = [h for h in hexes if re.match(r"^#[0-9a-fA-F]{6}([0-9a-fA-F]{2})?$", h)]
        if hexes and len(valid_hexes) >= 4:
            results.append(CheckResult(
                "Section 2: 색상 hex 4개 이상", True,
                f"{len(valid_hexes)}개 유효 hex 발견"
            ))
        else:
            results.append(CheckResult(
                "Section 2: 색상 hex 4개 이상", False,
                f"유효 hex {len(valid_hexes)}개 — 4개 이상 필요"
            ))

    # 3. Pure Black이 사용 의도로 명시되지 않음
    #    예외 컨텍스트(브랜드 정체성·다크 모드 정체성·회피·허용 명시)는 OK
    if 2 in section_blocks:
        used_pure = False
        for line in section_blocks[2].split("\n"):
            if re.search(r"#000000\b|#000\b", line):
                # 예외·정체성·회피 키워드 (한 라인 내)
                exception = re.search(
                    r"회피|미사용|정체성|허용|예외|exception|identity|반대|Off-Black|Zinc-?950|금지|❌",
                    line, re.IGNORECASE
                )
                if not exception:
                    used_pure = True
                    break
        results.append(CheckResult(
            "Section 2: Pure Black 미포함 (정체성 명시는 예외)",
            not used_pure,
            "Pure Black이 사용 의도로 명시 — Off-Black/Zinc-950 사용 또는 정체성 컨텍스트 명시 필요" if used_pure
            else "Pure Black 미사용 또는 정체성·예외 컨텍스트로 명시 ✓"
        ))

    # 4. Inter 폰트가 "사용" 컨텍스트로 등장하는지 (금지 컨텍스트는 OK)
    if 3 in section_blocks:
        # "Inter"가 등장하는 모든 라인을 찾아 금지 컨텍스트 여부 판정
        used_as_font = False
        for line in section_blocks[3].split("\n"):
            if re.search(r"\bInter\b", line):
                # 부정·금지 컨텍스트 키워드 (한 라인 내)
                negative = re.search(
                    r"금지|banned|❌|절대\s*(안|X)|미사용|forbidden|don't|do not|avoid",
                    line, re.IGNORECASE
                )
                if not negative:
                    # 추가 안전망: 같은 라인에 Pretendard/Geist 등 권장 폰트 명시되면 비교 컨텍스트로 OK
                    is_comparison = bool(re.search(
                        r"Pretendard|Geist|Cabinet Grotesk|Outfit|Satoshi", line
                    ))
                    if not is_comparison:
                        used_as_font = True
                        break
        results.append(CheckResult(
            "Section 3: Inter 폰트가 사용 의도로 명시되지 않음",
            not used_as_font,
            "Inter가 사용 폰트로 명시됨 — Pretendard/Geist 등으로 교체 필요" if used_as_font
            else "Inter 사용 컨텍스트 없음 (금지·비교 컨텍스트는 OK) ✓"
        ))

    # 5. 한국어 환경에서 Pretendard 명시
    if 3 in section_blocks:
        is_ko = "ko" in content.lower()[:500]  # 헤더 영역
        has_pretendard = "Pretendard" in section_blocks[3]
        if is_ko:
            results.append(CheckResult(
                "Section 3: 한국어 환경 Pretendard 명시",
                has_pretendard,
                "Pretendard 명시 ✓" if has_pretendard else "한국어 환경인데 Pretendard 미언급"
            ))

    # 6. Section 4 컴포넌트 6상태 명시
    if 4 in section_blocks:
        block = section_blocks[4]
        found_states = [s for s in COMPONENT_STATES if re.search(rf"\b{s}\b", block)]
        if len(found_states) >= 5:
            results.append(CheckResult(
                "Section 4: 컴포넌트 6상태 명시",
                True,
                f"{len(found_states)}/6 상태 명시: {found_states}"
            ))
        else:
            results.append(CheckResult(
                "Section 4: 컴포넌트 6상태 명시",
                False,
                f"{len(found_states)}/6 상태만 명시 — 5개 이상 필요"
            ))

    # 7. h-screen 사용 의도 검사 (Section 5)
    #    금지 컨텍스트(❌, 금지, banned)는 OK
    if 5 in section_blocks:
        block = section_blocks[5]
        has_dvh = "100dvh" in block

        h_screen_used_for_real = False
        for line in block.split("\n"):
            if re.search(r"\bh-screen\b", line):
                negative = re.search(
                    r"금지|banned|❌|절대|미사용|forbidden|don't|do not|avoid|X\b",
                    line, re.IGNORECASE
                )
                # min-h-[100dvh]와 함께 등장하면 비교 컨텍스트로 OK
                is_comparison = "100dvh" in line
                if not negative and not is_comparison:
                    h_screen_used_for_real = True
                    break

        if h_screen_used_for_real:
            results.append(CheckResult(
                "Section 5: h-screen이 사용 의도로 명시되지 않음",
                False,
                "h-screen이 사용 의도로 명시 — min-h-[100dvh]로 교체 필요"
            ))
        elif has_dvh:
            results.append(CheckResult(
                "Section 5: min-h-[100dvh] 사용 또는 h-screen 미사용",
                True,
                "min-h-[100dvh] 명시 또는 h-screen 미사용 ✓"
            ))
        else:
            results.append(CheckResult(
                "Section 5: full-height 섹션 미사용",
                True,
                "Full-height 섹션 부재 (자연 스크롤 레이아웃) ✓"
            ))

    # 8. Section 9 Anti-Patterns 비어있지 않음 또는 명시적 None
    if 9 in section_blocks:
        block = section_blocks[9]
        is_explicit_none = "Project-specific bans: None" in block
        has_items = bool(re.search(r"^[-*]\s+❌", block, re.MULTILINE))
        if is_explicit_none or has_items:
            results.append(CheckResult(
                "Section 9: Anti-Patterns 명시 또는 'None' 표기",
                True,
                "Anti-Patterns 명시됨" if has_items else "프로젝트 고유 금지 None 명시"
            ))
        else:
            results.append(CheckResult(
                "Section 9: Anti-Patterns 명시 또는 'None' 표기",
                False,
                "프로젝트 고유 금지 항목 또는 'None' 표기 부재"
            ))

    return results


def main():
    if len(sys.argv) < 2:
        print("사용법: python scripts/validate-design-md.py <DESIGN.md>")
        sys.exit(1)

    md_path = Path(sys.argv[1])
    if not md_path.exists():
        print(f"❌ 파일 없음: {md_path}")
        sys.exit(1)

    content = md_path.read_text(encoding="utf-8")
    results = validate(content)

    passed = sum(1 for r in results if r.passed)
    failed = sum(1 for r in results if not r.passed)

    print(f"\n📐 DESIGN.md 검증: {md_path}")
    print(f"   ✅ {passed}  ❌ {failed}  / 총 {len(results)}\n")

    for r in results:
        icon = "✅" if r.passed else "❌"
        print(f"  {icon} {r.name}")
        print(f"     {r.detail}")

    sys.exit(0 if failed == 0 else 2)


if __name__ == "__main__":
    main()
