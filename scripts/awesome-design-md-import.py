#!/usr/bin/env python3
"""
calm-design / scripts/awesome-design-md-import.py

awesome-design-md(VoltAgent) 큐레이션의 69개 브랜드 DESIGN.md를 calm-design
9-섹션 표준에 맞게 자동 변환 + reference-library/global/에 저장.

awesome-design-md vs calm-design 9-섹션 차이:
  | # | awesome-design-md      | calm-design        |
  |---|------------------------|--------------------|
  | 1 | Visual Theme           | Visual Theme       |  ← 동일
  | 2 | Color Palette          | Color Palette      |  ← 동일
  | 3 | Typography             | Typography         |  ← 동일
  | 4 | Component Stylings     | Component Stylings |  ← 동일
  | 5 | Layout                 | Layout             |  ← 동일
  | 6 | Depth & Elevation      | Depth & Elevation  |  ← 동일
  | 7 | Do's and Don'ts        | Motion             |  ← 변환: 'Don'ts'를 motion 섹션으로 흡수, 나머지 폐기
  | 8 | Responsive Behavior    | Responsive         |  ← 동일
  | 9 | Agent Prompt Guide     | Anti-Patterns      |  ← 변환: 'Don'ts'에서 추출, Agent Prompt는 폐기

변환 워크플로우:
1. GitHub API로 design-md/ 디렉토리 목록 fetch
2. 각 브랜드의 raw DESIGN.md 다운로드 (실제 파일은 getdesign.md에 호스팅이라 README만 가져옴)
3. 9-섹션 파싱
4. Section 7 (Do's/Don'ts) → Motion(7) + Anti-Patterns(9) 분할
5. Section 9 (Agent Prompt Guide) 폐기
6. calm-design 9-섹션 헤더 + Inspired by 메타 추가
7. reference-library/global/{brand}/DESIGN.md 저장

사용법:
    python scripts/awesome-design-md-import.py \\
        --output reference-library/global \\
        --limit 5  # 시범 5개만 import (전체는 --limit 0)

요구사항:
    - urllib (Python 표준 라이브러리)
    - GitHub API rate limit 대응 — limit 옵션으로 점진 import 권장

Exit codes:
    0 — 성공
    1 — 네트워크/API 오류
    2 — 변환 실패
"""

import argparse
import json
import re
import sys
import urllib.request
import urllib.error
from pathlib import Path


GITHUB_API = "https://api.github.com/repos/VoltAgent/awesome-design-md/contents/design-md"
RAW_BASE = "https://raw.githubusercontent.com/VoltAgent/awesome-design-md/main/design-md"


def fetch_json(url: str) -> dict | list:
    """GitHub API JSON fetch."""
    req = urllib.request.Request(url, headers={"User-Agent": "calm-design-importer"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read().decode("utf-8"))


def fetch_text(url: str) -> str:
    """raw 파일 fetch."""
    req = urllib.request.Request(url, headers={"User-Agent": "calm-design-importer"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        return resp.read().decode("utf-8")


def list_brands() -> list[str]:
    """awesome-design-md/design-md/ 하위 디렉토리(브랜드) 목록."""
    try:
        items = fetch_json(GITHUB_API)
    except urllib.error.URLError as e:
        print(f"❌ GitHub API 호출 실패: {e}")
        sys.exit(1)
    return [it["name"] for it in items if it["type"] == "dir"]


# ============================================================
# 9-섹션 파싱·변환
# ============================================================

def parse_sections(content: str) -> dict[int, str]:
    """awesome-design-md DESIGN.md의 ## 1. ~ ## 9. 섹션 분리."""
    sections: dict[int, str] = {}
    for num in range(1, 10):
        pattern = rf"^## {num}\.[^\n]*\n(.*?)(?=\n## \d+\.|\Z)"
        m = re.search(pattern, content, re.MULTILINE | re.DOTALL)
        if m:
            sections[num] = m.group(1).strip()
    return sections


def split_dos_donts(section_7: str) -> tuple[str, str]:
    """awesome 7번 (Do's and Don'ts) → Motion + Anti-Patterns로 분할.

    awesome-design-md의 Section 7 Do's/Don'ts에는 종종 motion 관련 do/don't가 섞여
    있음. 안전한 휴리스틱: motion·animation·transition 키워드 매칭은 motion으로,
    나머지 don't는 anti-patterns로.
    """
    motion_lines: list[str] = []
    anti_lines: list[str] = []

    for line in section_7.splitlines():
        lower = line.lower()
        # motion 키워드 우선
        if any(k in lower for k in ["motion", "animation", "transition", "spring",
                                    "ease", "fade", "slide", "scroll"]):
            motion_lines.append(line)
        elif "don't" in lower or "❌" in line or "절대" in line or "금지" in line:
            anti_lines.append(line)

    motion = "\n".join(motion_lines).strip() or "(원본에 motion 정책 부재 — calm-design Phase 4+에서 보강 예정)"
    anti = "\n".join(anti_lines).strip() or "(원본에 명시적 anti-pattern 부재 — 글로벌 ai-tells-blocklist.md만 적용)"
    return motion, anti


def transform_to_calm_format(brand: str, original: str) -> str:
    """awesome-design-md 9-섹션 → calm-design 9-섹션 변환."""
    sections = parse_sections(original)

    # Section 7 분할 (Do's/Don'ts → Motion + Anti)
    motion_section, anti_section = split_dos_donts(sections.get(7, ""))

    # 출력 구성
    output = f"""# Design System: {brand} (Inspired by — Imported)

> Source: [awesome-design-md / {brand}](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/{brand})
> Original License: MIT
> Imported by calm-design — converted from 9-section format (Do's/Don'ts → Motion + Anti-Patterns)
> "Inspired by" policy: 이 문서는 {brand}의 공개 디자인 시스템 관찰을 영감으로 차용한 것이며, 직접 복제·재배포가 아니다.

## 1. Visual Theme & Atmosphere

{sections.get(1, "(원본에 부재)")}

## 2. Color Palette & Roles

{sections.get(2, "(원본에 부재)")}

## 3. Typography Rules

{sections.get(3, "(원본에 부재)")}

## 4. Component Stylings

{sections.get(4, "(원본에 부재)")}

## 5. Layout Principles

{sections.get(5, "(원본에 부재)")}

## 6. Depth & Elevation

{sections.get(6, "(원본에 부재)")}

## 7. Motion & Interaction

{motion_section}

## 8. Responsive Behavior

{sections.get(8, "(원본에 부재)")}

## 9. Anti-Patterns (Project-Specific Banned)

{anti_section}
"""
    return output


# ============================================================
# import 메인
# ============================================================

def import_brand(brand: str, output_dir: Path) -> tuple[bool, str]:
    """단일 브랜드 import. 성공 여부 + 메시지 반환.

    URL 시도 순서 (실제 호스팅 구조 반영):
    1. getdesign.md/{brand}/design-md (HTML 페이지에 본문)
    2. getdesign.md/{brand}/raw 또는 .md (raw markdown 시도)
    3. raw.githubusercontent.com/.../{brand}/DESIGN.md (저장소 직접)
    4. raw.githubusercontent.com/.../{brand}/README.md (메타만 — fallback)
    """
    raw_urls = [
        f"https://getdesign.md/{brand}/design-md.md",   # raw markdown 시도 (확장자)
        f"https://getdesign.md/{brand}/design-md",       # HTML 페이지 (markdown 추출 필요)
        f"{RAW_BASE}/{brand}/DESIGN.md",                 # 저장소에 있을 수도
        f"{RAW_BASE}/{brand}/README.md",                 # 최후 fallback (메타만)
    ]
    content: str | None = None
    source: str = ""
    for url in raw_urls:
        try:
            content = fetch_text(url)
            source = url
            break
        except urllib.error.HTTPError as e:
            if e.code == 404:
                continue
            return False, f"HTTP {e.code} on {url}"
        except urllib.error.URLError as e:
            return False, f"네트워크 오류: {e}"
    if not content:
        return False, "DESIGN.md·README.md 모두 부재"

    # README.md fallback인 경우 9-섹션이 없을 가능성 큼 → 메타만 저장
    sections = parse_sections(content)
    if len(sections) < 5:
        # 본문이 9-섹션 표준이 아니면 메타·링크만 보존
        brand_dir = output_dir / brand
        brand_dir.mkdir(parents=True, exist_ok=True)
        (brand_dir / "DESIGN.md").write_text(
            f"""# Design System: {brand} (Inspired by — Stub)

> Source: [{source}]({source})
> Status: STUB — 원본이 9-섹션 표준 아님. 풀 DESIGN.md는 https://getdesign.md/{brand} 에서 fetch 필요 (Phase 3.5에서 자동화 예정).
> Imported by calm-design

## 원본 README

{content[:2000]}
""",
            encoding="utf-8",
        )
        return True, f"stub 저장 ({len(sections)}/9 섹션만 검출)"

    # 정상 9-섹션 변환
    transformed = transform_to_calm_format(brand, content)
    brand_dir = output_dir / brand
    brand_dir.mkdir(parents=True, exist_ok=True)
    (brand_dir / "DESIGN.md").write_text(transformed, encoding="utf-8")
    return True, f"✅ 9섹션 변환 완료"


def main():
    parser = argparse.ArgumentParser(description="awesome-design-md → calm-design 변환·import")
    parser.add_argument("--output", default="reference-library/global",
                        help="출력 디렉토리 (기본: reference-library/global)")
    parser.add_argument("--limit", type=int, default=5,
                        help="import할 브랜드 개수 (0=전체, 기본 5 = 시범)")
    parser.add_argument("--dry-run", action="store_true", help="실제 다운로드 없이 목록만")
    args = parser.parse_args()

    print("📡 awesome-design-md 브랜드 목록 조회 중...")
    brands = list_brands()
    print(f"   총 {len(brands)}개 브랜드 발견")

    if args.limit > 0:
        brands = brands[:args.limit]
        print(f"   ⚡ 시범 import: 처음 {len(brands)}개만")

    if args.dry_run:
        for b in brands:
            print(f"   - {b}")
        return

    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    succeeded, failed = [], []
    for brand in brands:
        try:
            ok, msg = import_brand(brand, output_dir)
            if ok:
                succeeded.append((brand, msg))
                print(f"  ✓ {brand}: {msg}")
            else:
                failed.append((brand, msg))
                print(f"  ✗ {brand}: {msg}")
        except Exception as e:
            failed.append((brand, str(e)))
            print(f"  ✗ {brand}: 예외 — {e}")

    # 메타 정보 저장
    summary = {
        "total_brands_in_repo": len(list_brands()) if not args.dry_run else 0,
        "imported": len(succeeded),
        "failed": len(failed),
        "succeeded": [{"brand": b, "note": m} for b, m in succeeded],
        "failed": [{"brand": b, "error": m} for b, m in failed],
        "source_repo": "https://github.com/VoltAgent/awesome-design-md",
        "source_license": "MIT",
        "imported_by": "calm-design / scripts/awesome-design-md-import.py",
    }
    (output_dir / "_import_summary.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    print(f"\n📦 Import 완료: 성공 {len(succeeded)}, 실패 {len(failed)}")
    print(f"📝 요약: {output_dir / '_import_summary.json'}")


if __name__ == "__main__":
    main()
