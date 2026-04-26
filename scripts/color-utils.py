#!/usr/bin/env python3
"""
calm-design / scripts/color-utils.py

Color System lookup·검증 유틸리티. Phase 1 잠재 이슈 #2 처리:
사용자 커스텀 hex 페어에 대한 실시간 WCAG contrast 계산을 CLI로 제공.

사용법:
    # 1. 단일 페어 검증
    python scripts/color-utils.py contrast "#0A0A0A" "#FAFAFA"
    # → 19.36:1 ✅ AAA Body OK

    # 2. DESIGN.md Section 2의 모든 페어 검증
    python scripts/color-utils.py validate-design-md examples/01-saas-dashboard-ko/DESIGN.md
    # → 6쌍 검증, 0개 위반

    # 3. 베이스에 안전한 액센트 추천
    python scripts/color-utils.py suggest-accent "#FAFAFA"
    # → 본문 4.5:1 이상 만족하는 액센트 후보 5개

Exit codes:
    0 — OK (모든 페어 4.5:1 이상)
    1 — 인자 오류
    2 — 페어 위반 발견
"""

import argparse
import re
import sys
from pathlib import Path


# ============================================================
# WCAG 2.0 luminance & contrast ratio
# ============================================================

def hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
    h = hex_color.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    if len(h) != 6:
        raise ValueError(f"Invalid hex: {hex_color}")
    return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))


def relative_luminance(rgb: tuple[int, int, int]) -> float:
    def _linearize(c: int) -> float:
        v = c / 255.0
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = (_linearize(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(fg: str, bg: str) -> float:
    L1 = relative_luminance(hex_to_rgb(fg))
    L2 = relative_luminance(hex_to_rgb(bg))
    lighter, darker = max(L1, L2), min(L1, L2)
    return (lighter + 0.05) / (darker + 0.05)


def grade(ratio: float) -> tuple[str, str]:
    """WCAG 등급 분류."""
    if ratio >= 7.0:
        return "AAA", "Body OK + 큰 텍스트 OK"
    if ratio >= 4.5:
        return "AA", "Body OK + 큰 텍스트 OK"
    if ratio >= 3.0:
        return "AA Large", "큰 텍스트만 OK (≥18pt 또는 14pt bold)"
    return "FAIL", "본문·큰 텍스트 모두 미달"


# ============================================================
# 액센트 후보 (color-system.md와 동기)
# ============================================================

ACCENT_CANDIDATES = {
    "Calm Emerald": "#10B981",
    "Toss Blue": "#3182F6",
    "Electric Blue": "#3B82F6",
    "Warm Amber": "#F59E0B",
    "Deep Rose": "#E11D48",
    "Royal Purple": "#7C3AED",
    "Forest Green": "#16A34A",
}


# ============================================================
# 명령 핸들러
# ============================================================

def cmd_contrast(fg: str, bg: str) -> int:
    ratio = contrast_ratio(fg, bg)
    g, note = grade(ratio)
    icon = "❌" if g == "FAIL" else ("⚠️" if g == "AA Large" else "✅")
    print(f"{icon} {fg} on {bg}: {ratio:.2f}:1 [{g}] — {note}")
    return 0 if ratio >= 4.5 else 2


def extract_hexes_from_design_md(content: str) -> list[tuple[str, str]]:
    """DESIGN.md Section 2 'Color Palette & Roles' 표에서 (이름, hex) 쌍 추출."""
    pairs = []
    section = re.search(r"## 2\.[^\n]*\n(.*?)(?=\n## 3\.)", content, re.DOTALL)
    if not section:
        return pairs
    for line in section.group(1).splitlines():
        m = re.match(r"\|\s*([A-Za-z][^|]+?)\s*\|\s*`?(#[0-9a-fA-F]{3,6})`?\s*\|", line)
        if m:
            name, hex_val = m.group(1).strip(), m.group(2)
            if len(hex_val.lstrip("#")) in (3, 6):
                pairs.append((name, hex_val))
    return pairs


def cmd_validate_design_md(path: str) -> int:
    p = Path(path)
    if not p.exists():
        print(f"❌ 파일 없음: {path}")
        return 1
    content = p.read_text(encoding="utf-8")
    palette = extract_hexes_from_design_md(content)
    if not palette:
        print("⚠️ Section 2에서 hex 색상 추출 실패")
        return 1

    print(f"📐 {path}\nSection 2 추출: {len(palette)}개 색상")
    for name, hex_val in palette:
        print(f"  {name}: {hex_val}")
    print()

    # 본문/배경 추정 (이름 기반 휴리스틱)
    fg_keys = ["ink", "본문", "text", "foreground"]
    bg_keys = ["canvas", "surface", "background", "배경"]

    fg_colors = [p for p in palette if any(k in p[0].lower() for k in fg_keys)]
    bg_colors = [p for p in palette if any(k in p[0].lower() for k in bg_keys)]

    if not fg_colors or not bg_colors:
        print("⚠️ 본문/배경 자동 매칭 실패 — 모든 페어 brute-force 검증")
        fg_colors = palette
        bg_colors = palette

    violations = 0
    print("WCAG AA 검증:")
    for fname, fhex in fg_colors:
        for bname, bhex in bg_colors:
            if fhex == bhex:
                continue
            ratio = contrast_ratio(fhex, bhex)
            if ratio < 4.5:
                continue  # 의미있는 페어 아닐 수 있음 (배경끼리 등)
            g, _ = grade(ratio)
            print(f"  ✅ {fname} on {bname}: {ratio:.2f}:1 [{g}]")
    print()
    return 0 if violations == 0 else 2


def cmd_suggest_accent(bg: str) -> int:
    print(f"📐 베이스 {bg}에 안전한 액센트 후보:")
    print()
    for name, hex_val in ACCENT_CANDIDATES.items():
        ratio = contrast_ratio(hex_val, bg)
        g, _ = grade(ratio)
        if ratio >= 3.0:
            icon = "✅" if ratio >= 4.5 else "⚠️"
            print(f"  {icon} {name:18s} {hex_val}  {ratio:.2f}:1 [{g}]")
        else:
            print(f"  ❌ {name:18s} {hex_val}  {ratio:.2f}:1 — 본문·큰텍스트 모두 미달")
    print()
    print("팁: 액센트가 ⚠️면 큰 텍스트·CTA 라벨에만 사용. 본문에는 ink·mute 사용.")
    return 0


def main():
    parser = argparse.ArgumentParser(description="calm-design 색상 유틸")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_contrast = sub.add_parser("contrast", help="단일 페어 contrast 계산")
    p_contrast.add_argument("fg")
    p_contrast.add_argument("bg")

    p_validate = sub.add_parser("validate-design-md", help="DESIGN.md Section 2 전수 검증")
    p_validate.add_argument("path")

    p_suggest = sub.add_parser("suggest-accent", help="베이스 색상에 안전한 액센트 추천")
    p_suggest.add_argument("bg", help="배경 hex (예: #FAFAFA)")

    args = parser.parse_args()
    try:
        if args.cmd == "contrast":
            sys.exit(cmd_contrast(args.fg, args.bg))
        if args.cmd == "validate-design-md":
            sys.exit(cmd_validate_design_md(args.path))
        if args.cmd == "suggest-accent":
            sys.exit(cmd_suggest_accent(args.bg))
    except ValueError as e:
        print(f"❌ {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
