#!/usr/bin/env python3
from __future__ import annotations
"""
calm-design / scripts/design-md-to-figma.py

DESIGN.md → Figma Variables JSON (W3C Design Tokens 표준) 변환.
Phase 4 산출물. output-engines/figma-export.md 명세 구현.

사용법:
    python scripts/design-md-to-figma.py --design <DESIGN.md> --output <output.json>

옵션:
    --format dtcg|tokens-studio   포맷 (기본: dtcg)
    --include-descriptions        $description 필드 포함

Exit codes:
    0 — 성공
    1 — 입력 파일 없음
    2 — 파싱 실패
"""

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


# ============================================================
# Data classes
# ============================================================

@dataclass
class ColorToken:
    name: str
    value: str
    description: str = ""


@dataclass
class TypographyTokens:
    font_family: str = "system-ui, sans-serif"
    font_sizes: dict[str, str] = field(default_factory=dict)
    line_heights: dict[str, str] = field(default_factory=dict)


@dataclass
class ShadowToken:
    name: str
    offset_x: str = "0"
    offset_y: str = "0"
    blur: str = "0"
    spread: str = "0"
    color: str = "rgba(0,0,0,0.1)"


@dataclass
class DesignTokens:
    project_name: str = "Design System"
    language: str = "en"
    colors: list[ColorToken] = field(default_factory=list)
    typography: TypographyTokens = field(default_factory=TypographyTokens)
    spacing: dict[str, str] = field(default_factory=dict)
    border_radius: dict[str, str] = field(default_factory=dict)
    shadows: list[ShadowToken] = field(default_factory=list)


# ============================================================
# Parsers
# ============================================================

def extract_section(content: str, section_num: int) -> str:
    pattern = re.compile(
        rf"^## {section_num}\..*?(?=^## \d+\.|\Z)", re.MULTILINE | re.DOTALL
    )
    match = pattern.search(content)
    return match.group(0) if match else ""


def parse_colors(section: str) -> list[ColorToken]:
    colors = []
    for line in section.splitlines():
        m = re.match(
            r"\|\s*([A-Za-z][^|]*?)\s*\|\s*`?(#[0-9a-fA-F]{3,6})`?\s*\|\s*([^|]*)\s*\|",
            line
        )
        if m:
            name, hex_val, desc = m.group(1).strip(), m.group(2), m.group(3).strip()
            if len(hex_val.lstrip("#")) in (3, 6):
                token_name = name.lower().replace(" ", "_").replace("-", "_")
                colors.append(ColorToken(name=token_name, value=hex_val, description=desc))
    return colors


def parse_typography(section: str, language: str) -> TypographyTokens:
    tokens = TypographyTokens()

    family_match = re.search(r"Family:\s*`([^`]+)`", section)
    if family_match:
        tokens.font_family = family_match.group(1)
    elif language == "ko":
        tokens.font_family = "Pretendard Variable, Pretendard, system-ui, sans-serif"
    else:
        tokens.font_family = "Geist, system-ui, sans-serif"

    tokens.font_sizes = {
        "xs": "12px", "sm": "14px", "base": "16px", "lg": "18px",
        "xl": "20px", "2xl": "24px", "3xl": "30px", "4xl": "36px", "5xl": "48px"
    }

    tokens.line_heights = {
        "tight": "1.1", "snug": "1.25", "normal": "1.5", "relaxed": "1.625"
    }

    return tokens


def parse_shadows(section: str) -> list[ShadowToken]:
    shadows = []

    shadow_pattern = re.compile(r"shadow-\[([^\]]+)\]")
    for match in shadow_pattern.finditer(section):
        value = match.group(1)
        parts = value.split("_")

        shadow = ShadowToken(name=f"custom_{len(shadows)}")

        if len(parts) >= 4:
            shadow.offset_x = parts[0]
            shadow.offset_y = parts[1]
            shadow.blur = parts[2]
            if parts[3].startswith("rgba") or parts[3].startswith("#"):
                shadow.color = "_".join(parts[3:])
            else:
                shadow.spread = parts[3]
                if len(parts) > 4:
                    shadow.color = "_".join(parts[4:])

        shadows.append(shadow)

    if "shadow-sm" in section:
        shadows.append(ShadowToken(
            name="sm", offset_y="1px", blur="2px", color="rgba(0,0,0,0.05)"
        ))
    if "shadow-md" in section:
        shadows.append(ShadowToken(
            name="md", offset_y="4px", blur="6px", spread="-1px", color="rgba(0,0,0,0.1)"
        ))
    if "shadow-lg" in section:
        shadows.append(ShadowToken(
            name="lg", offset_y="10px", blur="15px", spread="-3px", color="rgba(0,0,0,0.1)"
        ))

    return shadows


def detect_language(content: str) -> str:
    header = content[:500].lower()
    if "language: ko" in header or "language=ko" in header:
        return "ko"
    if "language: en" in header or "language=en" in header:
        return "en"
    korean_chars = len(re.findall(r"[가-힣]", content[:2000]))
    return "ko" if korean_chars >= 30 else "en"


def extract_project_name(content: str) -> str:
    m = re.search(r"^#\s*Design System:\s*(.+)", content, re.MULTILINE)
    if m:
        return m.group(1).strip()
    m = re.search(r"^#\s*(.+)", content, re.MULTILINE)
    return m.group(1).strip() if m else "Design System"


def parse_design_md(content: str) -> DesignTokens:
    tokens = DesignTokens()
    tokens.project_name = extract_project_name(content)
    tokens.language = detect_language(content)

    section2 = extract_section(content, 2)
    tokens.colors = parse_colors(section2)

    section3 = extract_section(content, 3)
    tokens.typography = parse_typography(section3, tokens.language)

    tokens.spacing = {
        "1": "4px", "2": "8px", "3": "12px", "4": "16px",
        "6": "24px", "8": "32px", "12": "48px", "16": "64px"
    }

    tokens.border_radius = {
        "sm": "4px", "md": "8px", "lg": "12px",
        "xl": "16px", "2xl": "24px", "full": "9999px"
    }

    section6 = extract_section(content, 6)
    tokens.shadows = parse_shadows(section6)

    return tokens


# ============================================================
# JSON Generator
# ============================================================

def generate_dtcg_json(tokens: DesignTokens, include_descriptions: bool = False) -> dict[str, Any]:
    output: dict[str, Any] = {
        "$schema": "https://design-tokens.github.io/community-group/format/",
        "$metadata": {
            "name": tokens.project_name,
            "language": tokens.language,
            "generator": "calm-design"
        }
    }

    output["color"] = {}
    for color in tokens.colors:
        token_obj: dict[str, Any] = {"$value": color.value, "$type": "color"}
        if include_descriptions and color.description:
            token_obj["$description"] = color.description
        output["color"][color.name] = token_obj

    output["typography"] = {
        "fontFamily": {
            "sans": {"$value": tokens.typography.font_family, "$type": "fontFamily"}
        },
        "fontSize": {},
        "lineHeight": {}
    }

    for name, value in tokens.typography.font_sizes.items():
        output["typography"]["fontSize"][name] = {"$value": value, "$type": "dimension"}

    for name, value in tokens.typography.line_heights.items():
        output["typography"]["lineHeight"][name] = {"$value": value, "$type": "number"}

    output["spacing"] = {}
    for name, value in tokens.spacing.items():
        output["spacing"][name] = {"$value": value, "$type": "dimension"}

    output["borderRadius"] = {}
    for name, value in tokens.border_radius.items():
        output["borderRadius"][name] = {"$value": value, "$type": "dimension"}

    output["shadow"] = {}
    for shadow in tokens.shadows:
        output["shadow"][shadow.name] = {
            "$value": {
                "offsetX": shadow.offset_x,
                "offsetY": shadow.offset_y,
                "blur": shadow.blur,
                "spread": shadow.spread,
                "color": shadow.color
            },
            "$type": "shadow"
        }

    return output


def generate_tokens_studio_json(tokens: DesignTokens, include_descriptions: bool = False) -> dict[str, Any]:
    output: dict[str, Any] = {}

    output["color"] = {}
    for color in tokens.colors:
        token_obj: dict[str, Any] = {"value": color.value, "type": "color"}
        if include_descriptions and color.description:
            token_obj["description"] = color.description
        output["color"][color.name] = token_obj

    output["fontFamilies"] = {
        "sans": {"value": tokens.typography.font_family, "type": "fontFamilies"}
    }

    output["fontSize"] = {}
    for name, value in tokens.typography.font_sizes.items():
        output["fontSize"][name] = {"value": value, "type": "fontSizes"}

    output["lineHeight"] = {}
    for name, value in tokens.typography.line_heights.items():
        output["lineHeight"][name] = {"value": value, "type": "lineHeights"}

    output["spacing"] = {}
    for name, value in tokens.spacing.items():
        output["spacing"][name] = {"value": value, "type": "spacing"}

    output["borderRadius"] = {}
    for name, value in tokens.border_radius.items():
        output["borderRadius"][name] = {"value": value, "type": "borderRadius"}

    output["boxShadow"] = {}
    for shadow in tokens.shadows:
        output["boxShadow"][shadow.name] = {
            "value": {
                "x": shadow.offset_x,
                "y": shadow.offset_y,
                "blur": shadow.blur,
                "spread": shadow.spread,
                "color": shadow.color,
                "type": "dropShadow"
            },
            "type": "boxShadow"
        }

    return output


# ============================================================
# Main
# ============================================================

def main() -> None:
    parser = argparse.ArgumentParser(
        description="DESIGN.md → Figma Variables JSON 변환"
    )
    parser.add_argument("--design", required=True, help="DESIGN.md 파일 경로")
    parser.add_argument("--output", required=True, help="출력 JSON 파일 경로")
    parser.add_argument(
        "--format", choices=["dtcg", "tokens-studio"], default="dtcg",
        help="출력 포맷 (기본: dtcg)"
    )
    parser.add_argument(
        "--include-descriptions", action="store_true",
        help="$description 필드 포함"
    )

    args = parser.parse_args()

    design_path = Path(args.design)
    if not design_path.exists():
        print(f"❌ 파일 없음: {args.design}")
        sys.exit(1)

    content = design_path.read_text(encoding="utf-8")

    try:
        tokens = parse_design_md(content)
    except Exception as e:
        print(f"❌ 파싱 실패: {e}")
        sys.exit(2)

    if args.format == "dtcg":
        output_json = generate_dtcg_json(tokens, args.include_descriptions)
    else:
        output_json = generate_tokens_studio_json(tokens, args.include_descriptions)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(output_json, indent=2, ensure_ascii=False),
        encoding="utf-8"
    )

    print(f"✅ 생성 완료: {args.output}")
    print(f"   프로젝트: {tokens.project_name}")
    print(f"   포맷: {args.format.upper()}")
    print(f"   언어: {tokens.language}")
    print(f"   색상: {len(tokens.colors)}개")
    print(f"   그림자: {len(tokens.shadows)}개")


if __name__ == "__main__":
    main()
