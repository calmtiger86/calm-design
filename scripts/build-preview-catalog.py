#!/usr/bin/env python3
from __future__ import annotations
"""
calm-design / scripts/build-preview-catalog.py

DESIGN.md → 디자인 시스템 시각 카탈로그 HTML 자동 생성.
Phase 4 산출물. output-engines/preview-catalog.md 명세 구현.

사용법:
    python scripts/build-preview-catalog.py --design <DESIGN.md> --output <output.html>

옵션:
    --language ko|en    언어 (기본: DESIGN.md에서 자동 감지)
    --no-contrast       WCAG contrast 계산 스킵

Exit codes:
    0 — 성공
    1 — 입력 파일 없음
    2 — 파싱 실패
"""

import argparse
import html
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path


# ============================================================
# WCAG 2.0 luminance & contrast (color-utils.py에서 복사)
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


def wcag_grade(ratio: float) -> tuple[str, str]:
    if ratio >= 7.0:
        return "AAA", "✅"
    if ratio >= 4.5:
        return "AA", "✅"
    if ratio >= 3.0:
        return "AA Large", "⚠️"
    return "FAIL", "❌"


# ============================================================
# Data classes
# ============================================================

@dataclass
class ColorToken:
    name: str
    hex: str
    role: str = ""


@dataclass
class TypographyLevel:
    name: str
    classes: str
    sample_ko: str = "차분한 디자인"
    sample_en: str = "Calm Design"


@dataclass
class ComponentState:
    name: str
    styles: str


@dataclass
class Component:
    name: str
    states: list[ComponentState] = field(default_factory=list)


@dataclass
class ShadowToken:
    name: str
    value: str


@dataclass
class DesignSystem:
    project_name: str = "Design System"
    language: str = "ko"
    colors: list[ColorToken] = field(default_factory=list)
    typography: list[TypographyLevel] = field(default_factory=list)
    components: list[Component] = field(default_factory=list)
    spacing: list[int] = field(default_factory=lambda: [4, 8, 16, 24, 32, 48, 64])
    shadows: list[ShadowToken] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)


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
            name, hex_val, role = m.group(1).strip(), m.group(2), m.group(3).strip()
            if len(hex_val.lstrip("#")) in (3, 6):
                colors.append(ColorToken(name=name, hex=hex_val, role=role))
    return colors


def parse_typography(section: str, language: str) -> list[TypographyLevel]:
    levels = []
    patterns = [
        (r"디스플레이|Display|H1", "Display / H1", "차분한 디자인 시스템", "Calm Design System"),
        (r"H2|섹션 제목", "Heading H2", "섹션 제목입니다", "Section Heading"),
        (r"본문|Body|text-base", "Body", "안녕하세요, 반갑습니다. 차분하고 정제된 디자인을 만듭니다.", "Hello, nice to meet you. We create calm and refined designs."),
        (r"라벨|Label|메타|Meta", "Label / Meta", "라벨 텍스트", "Label Text"),
        (r"KPI|숫자|Number", "KPI Number", "1,234,567", "1,234,567"),
    ]

    for pattern, name, sample_ko, sample_en in patterns:
        for line in section.splitlines():
            if re.search(pattern, line, re.IGNORECASE):
                classes_match = re.search(r"`([^`]+)`", line)
                classes = classes_match.group(1) if classes_match else ""
                levels.append(TypographyLevel(
                    name=name,
                    classes=classes,
                    sample_ko=sample_ko,
                    sample_en=sample_en
                ))
                break

    return levels


def parse_components(section: str) -> list[Component]:
    components = []
    current_component: Component | None = None
    state_pattern = re.compile(r"^-\s*(Default|Hover|Focus|Active|Disabled|Loading):\s*(.+)", re.IGNORECASE)

    for line in section.splitlines():
        if line.startswith("### ") or line.startswith("**") and line.endswith("**"):
            name = re.sub(r"^###\s*|^\*\*|\*\*$", "", line).strip()
            if name and not name.startswith("-"):
                if current_component:
                    components.append(current_component)
                current_component = Component(name=name)
        elif current_component:
            m = state_pattern.match(line.strip())
            if m:
                state_name, styles = m.group(1), m.group(2)
                current_component.states.append(ComponentState(name=state_name, styles=styles))

    if current_component:
        components.append(current_component)

    return components


def parse_shadows(section: str) -> list[ShadowToken]:
    shadows = []
    shadow_pattern = re.compile(r"shadow[-_]?\[?([^\]:\s]+)\]?|shadow[-_]?(sm|md|lg|xl|2xl|none)")
    value_pattern = re.compile(r"`(shadow-\[[^\]]+\]|shadow-(?:sm|md|lg|xl|2xl|none))`|`([^`]*shadow[^`]*)`")

    for line in section.splitlines():
        m = value_pattern.search(line)
        if m:
            value = m.group(1) or m.group(2)
            name_match = re.search(r"(카드|Card|Modal|Overlay|기본|Default)", line, re.IGNORECASE)
            name = name_match.group(1) if name_match else "Shadow"
            shadows.append(ShadowToken(name=name, value=value))

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


def parse_design_md(content: str, language: str | None = None) -> DesignSystem:
    ds = DesignSystem()
    ds.project_name = extract_project_name(content)
    ds.language = language or detect_language(content)

    section2 = extract_section(content, 2)
    ds.colors = parse_colors(section2)
    if len(ds.colors) < 4:
        ds.warnings.append("색상 토큰이 4개 미만입니다.")

    section3 = extract_section(content, 3)
    ds.typography = parse_typography(section3, ds.language)
    if not ds.typography:
        ds.warnings.append("타이포그래피 스케일을 파싱하지 못했습니다.")

    section4 = extract_section(content, 4)
    ds.components = parse_components(section4)
    if not ds.components:
        ds.warnings.append("컴포넌트를 파싱하지 못했습니다.")

    section6 = extract_section(content, 6)
    ds.shadows = parse_shadows(section6)

    return ds


# ============================================================
# HTML Generator
# ============================================================

def generate_color_card(color: ColorToken, bg_color: str, calc_contrast: bool) -> str:
    contrast_html = ""
    if calc_contrast and color.hex.lower() != bg_color.lower():
        try:
            ratio = contrast_ratio(color.hex, bg_color)
            grade, icon = wcag_grade(ratio)
            contrast_html = f'<p class="text-xs mt-2">{icon} {ratio:.2f}:1 {grade}</p>'
        except ValueError:
            pass

    text_color = "#FFFFFF" if relative_luminance(hex_to_rgb(color.hex)) < 0.5 else "#000000"

    return f'''
    <div class="swatch">
      <div class="w-20 h-20 rounded-xl mb-3" style="background-color: {color.hex};"></div>
      <p class="font-medium text-sm">{html.escape(color.name)}</p>
      <p class="copy-hex text-xs text-zinc-500 font-mono" data-hex="{color.hex}">{color.hex}</p>
      {contrast_html}
    </div>
    '''


def generate_typography_card(level: TypographyLevel, language: str) -> str:
    sample = level.sample_ko if language == "ko" else level.sample_en
    size_class = "text-4xl" if "Display" in level.name or "H1" in level.name else (
        "text-2xl" if "H2" in level.name else (
            "text-3xl font-semibold tabular-nums" if "KPI" in level.name else "text-base"
        )
    )

    return f'''
    <div class="border-b border-zinc-200 pb-6">
      <p class="text-sm text-zinc-500 mb-2">{html.escape(level.name)}</p>
      <p class="{size_class} tracking-tight" style="word-break: keep-all;">{html.escape(sample)}</p>
      <p class="text-xs text-zinc-400 mt-3 font-mono">{html.escape(level.classes)}</p>
    </div>
    '''


def generate_component_card(component: Component) -> str:
    states_html = ""
    all_states = ["Default", "Hover", "Focus", "Active", "Disabled", "Loading"]
    found_states = {s.name.lower(): s for s in component.states}

    for state_name in all_states:
        state = found_states.get(state_name.lower())
        if state:
            states_html += f'''
            <div class="text-center">
              <p class="text-xs text-zinc-500 mb-2">{state_name}</p>
              <div class="bg-zinc-100 rounded-lg p-4 min-h-[60px] flex items-center justify-center">
                <span class="text-xs text-zinc-600 break-all">{html.escape(state.styles[:50])}...</span>
              </div>
            </div>
            '''
        else:
            states_html += f'''
            <div class="text-center">
              <p class="text-xs text-zinc-500 mb-2">{state_name}</p>
              <div class="bg-zinc-50 rounded-lg p-4 min-h-[60px] flex items-center justify-center border-2 border-dashed border-zinc-200">
                <span class="text-xs text-zinc-400">미정의</span>
              </div>
            </div>
            '''

    return f'''
    <div class="bg-white rounded-2xl border border-zinc-200 p-6">
      <h3 class="font-semibold mb-4">{html.escape(component.name)}</h3>
      <div class="grid grid-cols-3 md:grid-cols-6 gap-4">
        {states_html}
      </div>
    </div>
    '''


def generate_spacing_bar(px: int) -> str:
    return f'''
    <div class="flex items-center gap-4">
      <span class="w-12 text-sm text-zinc-500 text-right font-mono">{px}px</span>
      <div class="h-4 bg-emerald-500 rounded" style="width: {px * 2}px;"></div>
    </div>
    '''


def generate_shadow_card(shadow: ShadowToken) -> str:
    shadow_style = ""
    if "shadow-[" in shadow.value:
        m = re.search(r"shadow-\[([^\]]+)\]", shadow.value)
        if m:
            shadow_style = f"box-shadow: {m.group(1)};"
    elif "shadow-sm" in shadow.value:
        shadow_style = "box-shadow: 0 1px 2px 0 rgb(0 0 0 / 0.05);"
    elif "shadow-md" in shadow.value:
        shadow_style = "box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);"
    elif "shadow-lg" in shadow.value:
        shadow_style = "box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1);"

    return f'''
    <div class="text-center">
      <div class="bg-white rounded-xl p-8 mb-4" style="{shadow_style}">
        <p class="text-sm text-zinc-600">Card Example</p>
      </div>
      <p class="text-sm font-medium">{html.escape(shadow.name)}</p>
      <p class="text-xs text-zinc-500 font-mono mt-1">{html.escape(shadow.value)}</p>
    </div>
    '''


def generate_html(ds: DesignSystem, calc_contrast: bool = True) -> str:
    bg_color = next((c.hex for c in ds.colors if "canvas" in c.name.lower() or "surface" in c.name.lower()), "#FAFAFA")

    colors_html = "".join(generate_color_card(c, bg_color, calc_contrast) for c in ds.colors)
    typography_html = "".join(generate_typography_card(t, ds.language) for t in ds.typography)
    components_html = "".join(generate_component_card(c) for c in ds.components)
    spacing_html = "".join(generate_spacing_bar(px) for px in ds.spacing)
    shadows_html = "".join(generate_shadow_card(s) for s in ds.shadows) if ds.shadows else '<p class="text-zinc-500">Shadow 토큰이 정의되지 않았습니다.</p>'

    warnings_html = ""
    if ds.warnings:
        warnings_list = "".join(f"<li>{html.escape(w)}</li>" for w in ds.warnings)
        warnings_html = f'''
        <div class="bg-amber-50 border border-amber-200 rounded-xl p-4 mb-8">
          <p class="font-semibold text-amber-800 mb-2">⚠️ 파싱 경고</p>
          <ul class="text-sm text-amber-700 list-disc list-inside">{warnings_list}</ul>
        </div>
        '''

    font_link = '''<link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>
  <link rel="stylesheet" as="style" crossorigin
    href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable.min.css" />''' if ds.language == "ko" else ""

    font_family = "'Pretendard Variable', Pretendard, system-ui, sans-serif" if ds.language == "ko" else "system-ui, sans-serif"

    return f'''<!DOCTYPE html>
<html lang="{ds.language}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Design System Preview — {html.escape(ds.project_name)}</title>

  {font_link}

  <script src="https://cdn.tailwindcss.com"></script>

  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          fontFamily: {{
            sans: [{repr(font_family.split(", "))}],
          }},
        }},
      }},
    }};
  </script>

  <style>
    .copy-hex {{ cursor: pointer; }}
    .copy-hex:hover {{ text-decoration: underline; }}
    .swatch {{ transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1); }}
    .swatch:hover {{ transform: scale(1.05); }}
  </style>
</head>
<body class="font-sans bg-zinc-50 text-zinc-900 antialiased">

  <header class="sticky top-0 z-40 bg-white/80 backdrop-blur-md border-b border-zinc-200">
    <div class="max-w-6xl mx-auto px-6 py-4 flex items-center justify-between">
      <h1 class="text-xl font-bold tracking-tight">{html.escape(ds.project_name)}</h1>
      <span class="text-sm text-zinc-500">Generated by calm-design</span>
    </div>
  </header>

  <main class="max-w-6xl mx-auto px-6 py-12 space-y-16">

    {warnings_html}

    <section id="colors">
      <h2 class="text-2xl font-bold tracking-tight mb-8">Color Palette</h2>
      <div class="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-6">
        {colors_html}
      </div>
    </section>

    <section id="typography">
      <h2 class="text-2xl font-bold tracking-tight mb-8">Typography Scale</h2>
      <div class="space-y-8">
        {typography_html}
      </div>
    </section>

    <section id="components">
      <h2 class="text-2xl font-bold tracking-tight mb-8">Component States</h2>
      <div class="space-y-8">
        {components_html}
      </div>
    </section>

    <section id="spacing">
      <h2 class="text-2xl font-bold tracking-tight mb-8">Spacing System</h2>
      <div class="space-y-4">
        {spacing_html}
      </div>
    </section>

    <section id="shadows">
      <h2 class="text-2xl font-bold tracking-tight mb-8">Shadow Tokens</h2>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        {shadows_html}
      </div>
    </section>

  </main>

  <footer class="border-t border-zinc-200 py-8 mt-16">
    <div class="max-w-6xl mx-auto px-6 text-center text-sm text-zinc-500">
      Generated by <a href="https://github.com/min86k/calm-design" class="underline hover:text-zinc-700">calm-design</a>
    </div>
  </footer>

  <script>
    document.querySelectorAll('.copy-hex').forEach(el => {{
      el.addEventListener('click', () => {{
        navigator.clipboard.writeText(el.dataset.hex);
        const original = el.textContent;
        el.textContent = 'Copied!';
        setTimeout(() => {{ el.textContent = original; }}, 1000);
      }});
    }});
  </script>

</body>
</html>'''


# ============================================================
# Main
# ============================================================

def main() -> None:
    parser = argparse.ArgumentParser(
        description="DESIGN.md → 디자인 시스템 시각 카탈로그 HTML 생성"
    )
    parser.add_argument("--design", required=True, help="DESIGN.md 파일 경로")
    parser.add_argument("--output", required=True, help="출력 HTML 파일 경로")
    parser.add_argument("--language", choices=["ko", "en"], help="언어 (기본: 자동 감지)")
    parser.add_argument("--no-contrast", action="store_true", help="WCAG contrast 계산 스킵")

    args = parser.parse_args()

    design_path = Path(args.design)
    if not design_path.exists():
        print(f"❌ 파일 없음: {args.design}")
        sys.exit(1)

    content = design_path.read_text(encoding="utf-8")

    try:
        ds = parse_design_md(content, args.language)
    except Exception as e:
        print(f"❌ 파싱 실패: {e}")
        sys.exit(2)

    html_content = generate_html(ds, calc_contrast=not args.no_contrast)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html_content, encoding="utf-8")

    print(f"✅ 생성 완료: {args.output}")
    print(f"   프로젝트: {ds.project_name}")
    print(f"   언어: {ds.language}")
    print(f"   색상: {len(ds.colors)}개")
    print(f"   타이포: {len(ds.typography)}개")
    print(f"   컴포넌트: {len(ds.components)}개")
    print(f"   그림자: {len(ds.shadows)}개")
    if ds.warnings:
        print(f"   ⚠️ 경고: {len(ds.warnings)}개")


if __name__ == "__main__":
    main()
