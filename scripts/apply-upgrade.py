#!/usr/bin/env python3
"""
calm-design / scripts/apply-upgrade.py

Mode B (Upgrade) Step 5 — 진단 결과를 받아 안전한 핀포인트 수정 자동 적용.
보존 계약과 충돌하면 자동 롤백 또는 사용자 확인 모드로 전환.

사용법:
    python scripts/apply-upgrade.py \\
        --code <기존-코드.html> \\
        --diagnosis .calm-design/upgrade-diagnosis.json \\
        --contract .calm-design/preservation-contract.yaml  # 선택
        --output <수정된-코드.html> \\
        --diff .calm-design/upgrade-diff.md

자동 수정 대상 (안전 4종):
    - Inter 폰트 → Pretendard (한국어 환경)
    - Pure Black `#000000`/`bg-black`/`text-black` → Off-Black `#0A0A0A`/`bg-zinc-950`/`text-ink`
    - h-screen → min-h-[100dvh]
    - 한국어 환경 font-thin/extralight/light → font-medium

검토 필요 (자동 X):
    - LILA BAN (그래디언트 → 단일 액센트, 보존 계약 의존)
    - 3-column equal → Bento (구조 변경)
    - AI 카피 클리셰 (의미 변경)
    - 라벨 누락 (라벨 텍스트 모호)
    - 광고 명령형 카피 (브랜드 톤 의존)

Exit codes:
    0 — 모든 자동 수정 적용 완료
    1 — 입력 오류
    2 — 보존 계약 위반 검출 (롤백)
"""

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Edit:
    fix_id: str
    title: str
    before: str
    after: str
    line_no: int = 0
    risk: str = "safe"  # "safe" | "review"


# ============================================================
# 자동 수정 함수들 (안전한 4종만)
# ============================================================

def fix_inter_to_pretendard(code: str, language: str) -> tuple[str, list[Edit]]:
    """Inter 폰트 → Pretendard (한국어 환경에서만 자동, 영문은 review)."""
    edits = []
    if language != "ko":
        return code, edits

    # font-family에서 Inter를 Pretendard로 교체
    pattern = re.compile(r"font-family\s*:\s*['\"]?Inter['\"]?(\s*,\s*[^;}]+)?", re.IGNORECASE)
    def repl(m):
        rest = m.group(1) or ", system-ui, sans-serif"
        new_value = f"font-family: 'Pretendard Variable', Pretendard{rest}"
        edits.append(Edit(
            "fix-inter", "Inter → Pretendard", m.group(0), new_value, risk="safe"
        ))
        return new_value
    return pattern.sub(repl, code), edits


def fix_pure_black(code: str) -> tuple[str, list[Edit]]:
    """Pure Black → Off-Black."""
    edits = []
    replacements = [
        (r"#000000\b", "#0A0A0A"),
        (r"#000\b(?![0-9a-fA-F])", "#0A0A0A"),
        (r"\bbg-black\b", "bg-zinc-950"),
        (r"\btext-black\b", "text-ink"),
    ]
    new_code = code
    for pat, replacement in replacements:
        matches = list(re.finditer(pat, new_code))
        if matches:
            new_code = re.sub(pat, replacement, new_code)
            edits.append(Edit(
                "fix-pure-black",
                f"Pure Black 교체 ({pat} → {replacement})",
                pat, replacement, risk="safe",
            ))
    return new_code, edits


def fix_h_screen(code: str) -> tuple[str, list[Edit]]:
    """h-screen → min-h-[100dvh] (iOS Safari 100vh 버그 회피)."""
    edits = []
    pattern = re.compile(r"\bh-screen\b")
    if pattern.search(code):
        new_code = pattern.sub("min-h-[100dvh]", code)
        edits.append(Edit(
            "fix-h-screen", "h-screen → min-h-[100dvh]",
            "h-screen", "min-h-[100dvh]", risk="safe",
        ))
        return new_code, edits
    return code, edits


def fix_korean_thin_weight(code: str, language: str) -> tuple[str, list[Edit]]:
    """한국어 환경 font-thin/extralight/light → font-medium (가독성)."""
    edits = []
    if language != "ko":
        return code, edits
    pattern = re.compile(r"\bfont-(thin|extralight|light)\b")
    if pattern.search(code):
        new_code = pattern.sub("font-medium", code)
        edits.append(Edit(
            "fix-thin-weight",
            "한국어 환경 얇은 weight → font-medium",
            "font-thin/extralight/light", "font-medium", risk="safe",
        ))
        return new_code, edits
    return code, edits


# ============================================================
# 보존 계약 검증
# ============================================================

def load_contract(path: str | None) -> dict:
    if not path or not Path(path).exists():
        return {}
    text = Path(path).read_text(encoding="utf-8")
    # 단순 YAML 파서 — 1단계 키만 처리 (의존성 추가 회피)
    contract: dict = {}
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" in line:
            k, _, v = line.partition(":")
            contract[k.strip()] = v.strip().strip('"').strip("'")
    return contract


def detect_contract_violations(
    before: str, after: str, contract: dict
) -> list[str]:
    """수정 후 코드가 보존 계약을 위반하는지 검사."""
    violations = []

    # 액센트 색상 hex 보존
    accent = contract.get("accent_hex")
    if accent and accent in before and accent not in after:
        violations.append(f"액센트 색상 {accent} 제거됨")

    # Hero 카피 보존
    hero = contract.get("hero_copy")
    if hero and hero in before and hero not in after:
        violations.append(f"Hero 카피 \"{hero}\" 변경됨")

    # 명시 라이브러리 제거 검출
    libs = contract.get("libraries", "")
    if isinstance(libs, str):
        libs = [s.strip() for s in libs.split(",") if s.strip()]
    for lib in libs:
        if lib and lib in before and lib not in after:
            violations.append(f"명시 라이브러리 '{lib}' 제거됨")

    return violations


# ============================================================
# 메인
# ============================================================

def render_diff_report(edits: list[Edit], violations: list[str]) -> str:
    lines = ["# 🔧 calm-design Upgrade Diff Report (Mode B Step 5)", ""]

    safe_edits = [e for e in edits if e.risk == "safe"]
    review_edits = [e for e in edits if e.risk == "review"]

    lines.append(f"**자동 수정 적용**: {len(safe_edits)}건")
    lines.append(f"**검토 필요 (수동)**: {len(review_edits)}건")
    lines.append("")

    if violations:
        lines.append("## 🚨 보존 계약 위반 검출 — 자동 롤백됨")
        for v in violations:
            lines.append(f"- {v}")
        lines.append("")
        lines.append("→ 수정을 적용하지 않았습니다. 보존 계약을 조정한 뒤 재실행하세요.")
        lines.append("")
        return "\n".join(lines)

    if safe_edits:
        lines.append("## ✅ 자동 적용된 수정")
        for e in safe_edits:
            lines.append(f"### {e.title} (`{e.fix_id}`)")
            lines.append(f"- Before: `{e.before}`")
            lines.append(f"- After:  `{e.after}`")
            lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Mode B 자동 핀포인트 수정")
    parser.add_argument("--code", required=True)
    parser.add_argument("--diagnosis", required=True, help="upgrade-diagnose.py JSON 출력")
    parser.add_argument("--contract", help="보존 계약 YAML (선택)")
    parser.add_argument("--output", required=True, help="수정된 코드 저장 경로")
    parser.add_argument("--diff", default=".calm-design/upgrade-diff.md")
    parser.add_argument("--language", default="ko", choices=["ko", "en", "auto"])
    args = parser.parse_args()

    code_path = Path(args.code)
    if not code_path.exists():
        print(f"❌ 입력 파일 없음: {code_path}")
        sys.exit(1)

    code = code_path.read_text(encoding="utf-8")
    diagnosis = json.loads(Path(args.diagnosis).read_text(encoding="utf-8"))
    contract = load_contract(args.contract) if args.contract else {}

    print(f"🔧 자동 수정 시작 — 진단 점수: {diagnosis.get('score', '?')}/100")

    all_edits: list[Edit] = []
    new_code = code

    # 안전한 자동 수정 4종 순차 적용
    new_code, e = fix_inter_to_pretendard(new_code, args.language)
    all_edits += e
    new_code, e = fix_pure_black(new_code)
    all_edits += e
    new_code, e = fix_h_screen(new_code)
    all_edits += e
    new_code, e = fix_korean_thin_weight(new_code, args.language)
    all_edits += e

    # 보존 계약 검증
    violations = detect_contract_violations(code, new_code, contract)
    if violations:
        # 자동 롤백
        print("🚨 보존 계약 위반 검출 — 자동 롤백")
        for v in violations:
            print(f"   - {v}")
        # diff 리포트만 작성, 수정은 적용 X
        diff_md = render_diff_report(all_edits, violations)
        Path(args.diff).parent.mkdir(parents=True, exist_ok=True)
        Path(args.diff).write_text(diff_md, encoding="utf-8")
        sys.exit(2)

    # 수정 적용
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(new_code, encoding="utf-8")

    diff_md = render_diff_report(all_edits, [])
    Path(args.diff).parent.mkdir(parents=True, exist_ok=True)
    Path(args.diff).write_text(diff_md, encoding="utf-8")

    print(f"✅ 자동 수정 완료: {len(all_edits)}건")
    for e in all_edits:
        print(f"   - {e.title}")
    print(f"📝 출력: {args.output}")
    print(f"📝 Diff: {args.diff}")


if __name__ == "__main__":
    main()
