#!/usr/bin/env python3
"""
calm-design / scripts/self-critique.py

Phase 1+ 셀프-크리틱 루프의 [3] Vision Self-Analysis + [4] Pre-Flight Scoring 통합 실행.

워크플로우:
1. render-preview.js가 만든 캡처 PNG를 입력으로
2. Anthropic Vision API에 5가지 자기 점검 질문 전송
3. 응답 JSON + 정적 분석 결과 결합 → Pre-Flight 21항목(Phase 1은 30+) 채점
4. 결과 리포트 출력 (실패 항목은 핀포인트 재생성용 프롬프트 자동 생성)

사용법:
    python scripts/self-critique.py \\
        --shots .calm-design/critique-shots \\
        --code examples/01-saas-dashboard-ko/index.html \\
        --design-md examples/01-saas-dashboard-ko/DESIGN.md \\
        --output .calm-design/critique-report.json

환경변수:
    ANTHROPIC_API_KEY — 필수

의존성 설치 (세션 디스크에):
    export PIP_TARGET=$(echo /sessions/*/pip_packages)
    mkdir -p $PIP_TARGET
    export PYTHONPATH=$PIP_TARGET:$PYTHONPATH
    pip install anthropic
"""

import argparse
import base64
import json
import os
import re
import sys
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any


# ============================================================
# Pre-Flight 21항목 정적 분석 (코드 텍스트 기반)
# Phase 1에서는 30+로 확장 예정
# ============================================================

@dataclass
class CheckResult:
    item_id: int
    title: str
    status: str  # "pass" | "warn" | "fail"
    detail: str = ""
    location: str = ""


# ============================================================
# WCAG 2.2 색상 대비 계산 (이슈 1 정밀화)
# ============================================================

# Tailwind 기본 neutral 팔레트 hex 매핑 (Phase 1 — Phase 2+에서 다른 색상도 추가)
TAILWIND_HEX = {
    "white": "#FFFFFF", "black": "#000000",
    "zinc-50": "#FAFAFA", "zinc-100": "#F4F4F5", "zinc-200": "#E4E4E7",
    "zinc-300": "#D4D4D8", "zinc-400": "#A1A1AA", "zinc-500": "#71717A",
    "zinc-600": "#52525B", "zinc-700": "#3F3F46", "zinc-800": "#27272A",
    "zinc-900": "#18181B", "zinc-950": "#09090B",
    "gray-50": "#F9FAFB", "gray-100": "#F3F4F6", "gray-200": "#E5E7EB",
    "gray-300": "#D1D5DB", "gray-400": "#9CA3AF", "gray-500": "#6B7280",
    "gray-600": "#4B5563", "gray-700": "#374151", "gray-800": "#1F2937",
    "gray-900": "#111827", "gray-950": "#030712",
    "stone-50": "#FAFAF9", "stone-100": "#F5F5F4", "stone-400": "#A8A29E",
    "stone-500": "#78716C", "stone-900": "#1C1917",
    "slate-50": "#F8FAFC", "slate-400": "#94A3B8", "slate-500": "#64748B",
    "slate-900": "#0F172A", "slate-950": "#020617",
    # 의미 토큰 (calm-design 표준)
    "ink": "#0A0A0A", "mute": "#71717A", "accent": "#10B981",
}


def hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
    h = hex_color.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))


def relative_luminance(rgb: tuple[int, int, int]) -> float:
    """WCAG 2.0 relative luminance — sRGB 보정 후 가중 합."""
    def _linearize(c: int) -> float:
        v = c / 255.0
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = (_linearize(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(fg_hex: str, bg_hex: str) -> float:
    """WCAG contrast ratio (1:1 ~ 21:1)."""
    L1 = relative_luminance(hex_to_rgb(fg_hex))
    L2 = relative_luminance(hex_to_rgb(bg_hex))
    lighter, darker = max(L1, L2), min(L1, L2)
    return (lighter + 0.05) / (darker + 0.05)


# 흔한 위험 조합 (Tailwind 기본 패턴) — 본문 4.5 미만이면 fail
RISKY_PAIRS = [
    ("zinc-400", "white"),  # ~2.85:1 — 본문 미달
    ("zinc-300", "white"),  # ~1.79:1 — 큰 텍스트도 미달
    ("gray-400", "white"),
    ("gray-300", "white"),
    ("zinc-400", "zinc-50"),
    ("mute", "white"),  # mute=#71717A → ~4.83:1, 본문 경계
    ("stone-400", "stone-50"),
]


def detect_contrast_issues(code: str) -> list[dict]:
    """코드에서 위험 색상 쌍 검출 + 실제 contrast 계산."""
    issues = []
    for fg, bg in RISKY_PAIRS:
        if f"text-{fg}" in code and f"bg-{bg}" in code:
            ratio = contrast_ratio(TAILWIND_HEX[fg], TAILWIND_HEX[bg])
            if ratio < 4.5:
                issues.append({
                    "fg": fg, "bg": bg, "ratio": round(ratio, 2),
                    "verdict": "fail" if ratio < 3.0 else "warn",
                })
    return issues


def static_analysis(code: str, design_md: str = "", language: str = "ko") -> list[CheckResult]:
    """정적 분석으로 17/21 항목 검증. Vision 보완 필요한 4개는 별도."""
    results = []

    # 1. 모바일 레이아웃 붕괴 가드
    has_responsive = bool(re.search(r"\bmd:grid-cols-", code)) and bool(
        re.search(r"\bgrid-cols-1\b", code)
    )
    results.append(CheckResult(
        1, "모바일 레이아웃 붕괴 가드",
        "pass" if has_responsive else "warn",
        "md:grid-cols-N + grid-cols-1 패턴 확인" if has_responsive else "반응형 grid 패턴 부재"
    ))

    # 2. h-screen 부재 (min-h-[100dvh] 사용)
    has_h_screen = bool(re.search(r"\bh-screen\b", code))
    has_dvh = "min-h-[100dvh]" in code
    if has_h_screen:
        results.append(CheckResult(2, "Full-height 섹션 안전", "fail",
                                    "h-screen 사용 발견 (iOS Safari 100vh 버그 위험)"))
    elif has_dvh:
        results.append(CheckResult(2, "Full-height 섹션 안전", "pass",
                                    "min-h-[100dvh] 사용 ✓"))
    else:
        results.append(CheckResult(2, "Full-height 섹션 안전", "pass",
                                    "Full-height 섹션 없음 (자연 스크롤)"))

    # 3. Max-width 제약
    has_max_width = bool(re.search(r"max-w-(7xl|6xl|\[\d+ch\])", code))
    results.append(CheckResult(
        3, "Max-width 제약", "pass" if has_max_width else "warn",
        "max-w-7xl 또는 max-w-[Nch] 사용" if has_max_width
        else "max-width 제약 부재 — 1920px+ 모니터에서 가독성 위험"
    ))

    # 4. 섹션 다양화 — Vision 보완 필요
    results.append(CheckResult(4, "섹션 다양화", "warn",
                                "Vision 보완 검증 필요 (아래 vision_findings 참조)"))

    # 5. 3-column equal cards 부재
    grid_cols_3 = code.count("grid-cols-3")
    results.append(CheckResult(
        5, "3-column equal cards 부재",
        "warn" if grid_cols_3 > 0 else "pass",
        f"grid-cols-3 사용 {grid_cols_3}회 — 비대칭 Bento 권장" if grid_cols_3 > 0
        else "3-column equal 패턴 미발견"
    ))

    # 6. Pure Black 부재
    has_pure_black = bool(re.search(r"#000(?:000)?\b|\bbg-black\b|\btext-black\b", code))
    results.append(CheckResult(
        6, "Pure Black 부재", "fail" if has_pure_black else "pass",
        "Pure Black 발견 — Off-Black `#0A0A0A` 또는 Zinc-950 사용" if has_pure_black
        else "Pure Black 미사용 ✓"
    ))

    # 7. LILA BAN
    has_lila = bool(re.search(r"from-purple-.*to-blue-|shadow.*purple|drop-shadow.*purple", code))
    results.append(CheckResult(
        7, "LILA BAN — 보라/파란 그래디언트 부재",
        "fail" if has_lila else "pass",
        "보라/파란 AI 그래디언트 발견" if has_lila else "LILA BAN 통과 ✓"
    ))

    # 8. 단일 액센트 — 정밀 검사는 Vision 보완
    accent_colors = set(re.findall(r"#[0-9a-fA-F]{6}", code))
    results.append(CheckResult(
        8, "단일 액센트", "warn" if len(accent_colors) > 8 else "pass",
        f"코드 내 hex 색상 {len(accent_colors)}종 (8 초과 시 Vision으로 정밀 검증)"
    ))

    # 9. Inter 폰트 부재
    has_inter = bool(re.search(r"\bInter\b", code))
    results.append(CheckResult(
        9, "Inter 폰트 부재", "fail" if has_inter else "pass",
        "Inter 폰트 발견" if has_inter else "Inter 미사용 ✓"
    ))

    # 10. Pretendard 강제 (LANGUAGE=ko)
    if language == "ko":
        has_pretendard = "Pretendard" in code
        results.append(CheckResult(
            10, "Pretendard 강제 (LANGUAGE=ko)",
            "pass" if has_pretendard else "fail",
            "Pretendard 사용 ✓" if has_pretendard else "Pretendard 미사용 — 한국어 환경에서 필수"
        ))

    # 11. word-break: keep-all (LANGUAGE=ko)
    if language == "ko":
        has_keep_all = "word-break: keep-all" in code or "break-keep" in code
        results.append(CheckResult(
            11, "word-break: keep-all 적용",
            "pass" if has_keep_all else "fail",
            "word-break: keep-all 적용 ✓" if has_keep_all
            else "한국어 줄바꿈 정책 미적용 — 단어 중간 끊김 위험"
        ))

    # 12. 한국어 줄높이
    if language == "ko":
        has_relaxed = bool(re.search(r"leading-(relaxed|loose)", code))
        results.append(CheckResult(
            12, "한국어 줄높이 충분",
            "pass" if has_relaxed else "warn",
            "leading-relaxed/loose 사용" if has_relaxed
            else "leading-tight/normal만 사용 — 한국어에 부족할 수 있음"
        ))

    # 13. 한국어 weight 적정
    if language == "ko":
        has_thin = bool(re.search(r"\bfont-(thin|extralight|light)\b", code))
        results.append(CheckResult(
            13, "한국어 weight 적정",
            "fail" if has_thin else "pass",
            "font-thin/extralight/light 발견" if has_thin
            else "한국어에 부적절한 얇은 weight 미사용 ✓"
        ))

    # 14. 한국어 본문 너비
    if language == "ko":
        has_max_ch = "max-w-[65ch]" in code or "max-w-[55ch]" in code or "max-w-[45ch]" in code
        results.append(CheckResult(
            14, "한국어 본문 너비",
            "pass" if has_max_ch else "warn",
            "max-w-[Nch] 사용" if has_max_ch else "본문 너비 가이드 미적용"
        ))

    # ----- 영어 환경 전용 (LANGUAGE=en) -----
    if language == "en":
        # 11e. 영문 본문 너비 (60-75자 가이드)
        has_en_width = bool(re.search(
            r"max-w-(prose|\[(60|65|70|75)ch\])", code
        ))
        results.append(CheckResult(
            11, "영문 본문 너비 (60-75자)",
            "pass" if has_en_width else "warn",
            "max-w-prose 또는 max-w-[60-75ch] 사용 ✓" if has_en_width
            else "본문 너비 가이드 미적용 — max-w-prose 또는 max-w-[65ch] 권장"
        ))

        # 12e. 영문 디스플레이 폰트 권장
        has_premium_en_font = bool(re.search(
            r"\b(Geist|Cabinet Grotesk|Outfit|Satoshi)\b", code
        ))
        # Inter는 9번에서 별도 검출되므로 여기선 권장 폰트 존재만 체크
        results.append(CheckResult(
            12, "영문 프리미엄 폰트 권장",
            "pass" if has_premium_en_font else "warn",
            f"권장 폰트 사용 ✓" if has_premium_en_font
            else "Geist/Cabinet Grotesk/Outfit/Satoshi 중 하나 권장 (Helvetica는 변별력 부족)"
        ))

        # 13e. Pretendard는 영어 환경에서 강제 X (한국어 혼용 시 OK, 단독 사용 시 warn)
        has_pretendard = "Pretendard" in code
        # html lang 추출 시도
        html_lang_match = re.search(r"<html\s+lang=[\"']([^\"']+)[\"']", code)
        html_lang = html_lang_match.group(1) if html_lang_match else None
        if has_pretendard and html_lang and html_lang.startswith("en"):
            results.append(CheckResult(
                13, "영문 환경 폰트 정합성",
                "warn",
                f"Pretendard 사용 + lang=\"{html_lang}\" — 한·영 혼용 의도 명시 필요"
            ))
        else:
            results.append(CheckResult(
                13, "영문 환경 폰트 정합성",
                "pass",
                "영문 환경에 적절한 폰트 구성 ✓"
            ))

        # 14e. <html lang="en"> 명시
        if html_lang:
            ok = html_lang.startswith("en")
            ok_mark = "✓" if ok else "— 영어 환경엔 lang=en 권장"
            detail_14 = "lang=" + repr(html_lang) + " " + ok_mark
            results.append(CheckResult(
                14, '<html lang="en"> 명시',
                "pass" if ok else "warn",
                detail_14,
            ))
        else:
            results.append(CheckResult(
                14, '<html lang="en"> 명시',
                "warn",
                "<html lang=...> 속성 미발견",
            ))

    # 15. GPU 친화 애니메이션
    has_bad_anim = bool(re.search(
        r"animate-\[.*(top|left|width|height).*\]|transition-(top|left|width|height)\b",
        code
    ))
    results.append(CheckResult(
        15, "GPU 친화 애니메이션",
        "fail" if has_bad_anim else "pass",
        "top/left/width/height 애니메이션 발견" if has_bad_anim
        else "transform/opacity만 사용 ✓"
    ))

    # 16. Spring physics
    has_spring = "cubic-bezier(0.16, 1, 0.3, 1)" in code or "spring(" in code or 'easing="spring"' in code
    has_linear = "ease-linear" in code
    results.append(CheckResult(
        16, "Spring physics 적용",
        "warn" if has_linear else ("pass" if has_spring else "warn"),
        "ease-linear 사용 — Spring으로 교체 권장" if has_linear
        else ("Spring/cubic-bezier 사용 ✓" if has_spring else "모션 easing 명시 부재")
    ))

    # 17. 컴포넌트 6상태 — Loading 상태 체크 (대표값)
    has_loading = "Loader2" in code or "animate-spin" in code or "loading" in code.lower()
    results.append(CheckResult(
        17, "컴포넌트 6상태 (Loading)",
        "pass" if has_loading else "warn",
        "Loading 상태 처리 발견" if has_loading
        else "Loader2/animate-spin/loading 패턴 부재 — 데이터 컴포넌트 검증 필요"
    ))

    # 18. AI 카피 클리셰
    cliches = ["Elevate", "Seamless", "Unleash", "Next-Gen", "Revolutionary", "Cutting-edge"]
    found_cliches = [c for c in cliches if c in code]
    results.append(CheckResult(
        18, "AI 카피 클리셰 부재",
        "fail" if found_cliches else "pass",
        f"클리셰 발견: {found_cliches}" if found_cliches else "AI 카피 클리셰 미사용 ✓"
    ))

    # 19. Generic placeholder
    placeholders = ["John Doe", "Jane Smith", "Acme", "Lorem ipsum", "Lorem Ipsum"]
    found_pl = [p for p in placeholders if p in code]
    results.append(CheckResult(
        19, "Generic placeholder 부재",
        "fail" if found_pl else "pass",
        f"Placeholder 발견: {found_pl}" if found_pl else "Generic placeholder 미사용 ✓"
    ))

    # 20. Filler UI 텍스트
    fillers = ["Scroll to explore", "Swipe down", "스크롤하세요"]
    found_fillers = [f for f in fillers if f in code]
    results.append(CheckResult(
        20, "Filler UI 텍스트 부재",
        "fail" if found_fillers else "pass",
        f"Filler 발견: {found_fillers}" if found_fillers else "Filler 미사용 ✓"
    ))

    # 21. Empty/Error/Loading 상태
    has_empty = "empty" in code.lower() or "비어있" in code or "데이터가 없" in code
    has_error = "error" in code.lower() or "오류" in code
    has_skeleton = "skeleton" in code.lower() or "animate-pulse" in code
    state_count = sum([has_empty, has_error, has_skeleton])
    results.append(CheckResult(
        21, "Empty/Error/Loading 상태",
        "pass" if state_count >= 2 else ("warn" if state_count == 1 else "warn"),
        f"상태 처리: empty={has_empty}, error={has_error}, loading={has_skeleton}"
    ))

    # ----- Phase 1 확장: 22-30 (접근성·SEO·환경) -----

    # 22. WCAG 2.2 AA 색상 대비 — 실제 luminance 계산으로 정밀화 (Phase 1+)
    contrast_issues = detect_contrast_issues(code)
    if contrast_issues:
        worst = min(contrast_issues, key=lambda x: x["ratio"])
        any_fail = any(i["verdict"] == "fail" for i in contrast_issues)
        detail = f"{len(contrast_issues)}개 위험 쌍 검출 — 최저 대비: text-{worst['fg']} on bg-{worst['bg']} = {worst['ratio']}:1"
        results.append(CheckResult(
            22, "WCAG AA 색상 대비",
            "fail" if any_fail else "warn",
            detail,
        ))
    else:
        results.append(CheckResult(
            22, "WCAG AA 색상 대비", "pass",
            "Tailwind 기본 위험 쌍 미검출 (커스텀 hex는 Vision 보완 권장)"
        ))

    # 23. ARIA 라벨 명시 — 아이콘만 있는 버튼 검출
    icon_only_btn = bool(re.search(
        r"<button[^>]*>\s*<(i|svg|Icon|[A-Z]\w*)[^>]*/?>\s*</button>",
        code
    ))
    has_aria_label = "aria-label" in code or 'role="button"' in code
    if icon_only_btn and not has_aria_label:
        results.append(CheckResult(
            23, "ARIA 라벨 명시", "fail",
            "아이콘만 있는 버튼에 aria-label 누락"
        ))
    else:
        results.append(CheckResult(
            23, "ARIA 라벨 명시", "pass",
            "아이콘 버튼 라벨 처리 ✓ 또는 해당 패턴 없음"
        ))

    # 24. 키보드 포커스 가시성
    has_outline_none = "outline-none" in code
    has_focus_ring = bool(re.search(r"focus(-visible)?:ring-\d", code))
    if has_outline_none and not has_focus_ring:
        results.append(CheckResult(
            24, "키보드 포커스 가시성", "fail",
            "outline-none 사용 + 대체 focus 스타일 부재"
        ))
    elif has_focus_ring:
        results.append(CheckResult(
            24, "키보드 포커스 가시성", "pass",
            "focus-visible:ring-N 사용 ✓"
        ))
    else:
        results.append(CheckResult(
            24, "키보드 포커스 가시성", "warn",
            "포커스 스타일 명시 부재 — 인터랙티브 요소 검증 필요"
        ))

    # 25. 이미지 alt 속성
    img_tags = re.findall(r"<img[^>]*>", code)
    img_no_alt = [t for t in img_tags if "alt=" not in t]
    img_bad_alt = [t for t in img_tags
                    if re.search(r'alt="(image|photo|picture|이미지|사진)"', t)]
    if img_no_alt:
        results.append(CheckResult(
            25, "이미지 alt 속성", "fail",
            f"alt 누락 {len(img_no_alt)}개"
        ))
    elif img_bad_alt:
        results.append(CheckResult(
            25, "이미지 alt 속성", "warn",
            f"무의미 alt {len(img_bad_alt)}개 — 의미있는 설명 필요"
        ))
    elif img_tags:
        results.append(CheckResult(
            25, "이미지 alt 속성", "pass",
            f"{len(img_tags)}개 이미지 모두 alt 명시 ✓"
        ))
    else:
        results.append(CheckResult(
            25, "이미지 alt 속성", "pass", "이미지 없음"
        ))

    # 26. Form input 라벨 연결 (React/shadcn/JSX 패턴 모두 지원)
    # 라벨 후보: <label>·<Label> (대소문자) + htmlFor·for, 또는 input의 aria-label
    input_count = len(re.findall(
        r"<input(?!\s+type=[\"'](hidden|submit|button|reset|image)[\"'])", code
    ))
    # HTML 소문자, JSX 대문자, shadcn <Label htmlFor=...>
    label_for_count = len(re.findall(r"<[Ll]abel[^>]*\bhtmlFor=", code)) + \
                      len(re.findall(r"<[Ll]abel[^>]*\bfor=", code))
    # input의 aria-label 또는 aria-labelledby
    aria_label_count = len(re.findall(
        r"<[iI]nput[^>]*\b(aria-label|aria-labelledby)=", code
    ))
    # input id가 label htmlFor와 매칭되는지 추가 검증 (확실한 매칭)
    input_ids = re.findall(r"<[iI]nput[^>]*\bid=[\"']([^\"']+)[\"']", code)
    label_for_ids = re.findall(r"<[Ll]abel[^>]*\b(?:htmlFor|for)=[\"']([^\"']+)[\"']", code)
    matched_ids = set(input_ids) & set(label_for_ids)

    coverage = len(matched_ids) + aria_label_count
    has_input_labels = coverage >= input_count if input_count else True

    if not input_count:
        results.append(CheckResult(
            26, "Form input 라벨 연결", "pass", "input 요소 없음"
        ))
    elif has_input_labels:
        results.append(CheckResult(
            26, "Form input 라벨 연결", "pass",
            f"input {input_count}개 모두 라벨 연결 (htmlFor 매칭 {len(matched_ids)} + aria-label {aria_label_count}) ✓"
        ))
    else:
        missing = input_count - coverage
        results.append(CheckResult(
            26, "Form input 라벨 연결", "fail",
            f"input {input_count}개 중 라벨 미연결 {missing}개 (htmlFor/aria-label/Label 모두 미매칭)"
        ))

    # 27. 다크모드 색상 토큰 매핑
    has_dark_mode = bool(re.search(r"\bdark:[a-z]", code)) or '[data-theme="dark"]' in code
    results.append(CheckResult(
        27, "다크모드 색상 토큰",
        "pass" if has_dark_mode else "warn",
        "dark: 클래스 또는 [data-theme=dark] 분기 존재 ✓" if has_dark_mode
        else "다크모드 미지원 (작은 페이지면 OK, 권장은 지원)"
    ))

    # 28. SEO meta tags
    has_title = bool(re.search(r"<title>[^<]+</title>", code))
    has_description = bool(re.search(r'<meta\s+name=[\"\']description[\"\']', code))
    has_og_image = bool(re.search(r'<meta\s+property=[\"\']og:image[\"\']', code))
    seo_count = sum([has_title, has_description, has_og_image])
    results.append(CheckResult(
        28, "SEO meta tags",
        "pass" if seo_count == 3 else ("warn" if seo_count >= 1 else "warn"),
        f"title/description/og:image: {seo_count}/3 명시"
    ))

    # 29. Sticky header z-index 충돌
    has_sticky_or_fixed = bool(re.search(r"\b(sticky|fixed)\b", code))
    has_z_index = bool(re.search(r"\bz-(40|30|50|10|20)\b", code))
    if has_sticky_or_fixed and not has_z_index:
        results.append(CheckResult(
            29, "Sticky header z-index", "warn",
            "sticky/fixed 요소 발견 + 명시적 z-index 부재"
        ))
    else:
        results.append(CheckResult(
            29, "Sticky header z-index", "pass",
            "z-index 명시 ✓ 또는 sticky 요소 없음"
        ))

    # 30. Reduced-motion 지원
    has_reduced_motion = "prefers-reduced-motion" in code or "useReducedMotion" in code
    has_animation = bool(re.search(r"animate-|transition-|motion\.", code))
    if has_animation and not has_reduced_motion:
        results.append(CheckResult(
            30, "Reduced-motion 지원", "warn",
            "애니메이션 사용 + reduced-motion 미지원 — 전정 장애 사용자 위험"
        ))
    else:
        results.append(CheckResult(
            30, "Reduced-motion 지원", "pass",
            "reduced-motion 지원 ✓ 또는 애니메이션 없음"
        ))

    # ----- AI Tells 자동 검증 추가 (Phase 1, #35·36·37·38) -----
    # 이슈 3 처리: 4개 자동화 가능 항목

    # AT-35. 광고 명령형 CTA 카피
    ad_phrases = [
        "지금 사세요", "지금 구매", "지금 가입하세요", "절대 놓치지",
        "Buy now!", "Click Here!", "Order Today!", "Don't Miss Out",
    ]
    found_ad = [p for p in ad_phrases if p in code]
    if found_ad:
        results.append(CheckResult(
            35, "AT-35 광고 명령형 카피 부재", "fail",
            f"광고 톤 카피 발견: {found_ad}"
        ))
    else:
        results.append(CheckResult(35, "AT-35 광고 명령형 카피 부재", "pass",
                                    "광고 명령형 카피 미사용 ✓"))

    # AT-36. 한국어 페이지 + 영문 Lorem ipsum
    is_ko_page = (
        bool(re.search(r"<html\s+lang=[\"']ko", code))
        or language == "ko"
    )
    has_lorem = bool(re.search(r"\bLorem\s+ipsum\b", code, re.IGNORECASE))
    if is_ko_page and has_lorem:
        results.append(CheckResult(
            36, "AT-36 한국어 페이지 라틴 lorem 부재", "fail",
            "한국어 페이지에 영문 Lorem ipsum 사용 — 한국어 더미로 교체 필요"
        ))
    else:
        results.append(CheckResult(
            36, "AT-36 한국어 페이지 라틴 lorem 부재", "pass",
            "한국어 페이지 lorem 부재 ✓ 또는 한국어 페이지 아님"
        ))

    # AT-37. 자동재생 비디오 음성 ON
    autoplay_videos = re.findall(r"<video[^>]*\bautoplay\b[^>]*>", code, re.IGNORECASE)
    bad_autoplay = [v for v in autoplay_videos if "muted" not in v.lower()]
    if bad_autoplay:
        results.append(CheckResult(
            37, "AT-37 자동재생 음성 OFF", "fail",
            f"autoplay video {len(bad_autoplay)}개에 muted 누락"
        ))
    else:
        results.append(CheckResult(
            37, "AT-37 자동재생 음성 OFF", "pass",
            "autoplay video는 모두 muted ✓ 또는 autoplay 없음"
        ))

    # AT-38. Stock photo URL (가짜 사용자 얼굴)
    stock_patterns = [
        r"unsplash\.com/photos?/",
        r"shutterstock\.com",
        r"gettyimages\.com",
        r"stockphoto",
    ]
    found_stock = [p for p in stock_patterns if re.search(p, code, re.IGNORECASE)]
    if found_stock:
        results.append(CheckResult(
            38, "AT-38 Stock photo URL 부재", "warn",
            f"Stock photo URL 패턴 발견 — pravatar/picsum 또는 실제 이미지로 교체 권장"
        ))
    else:
        results.append(CheckResult(38, "AT-38 Stock photo URL 부재", "pass",
                                    "Stock photo URL 미사용 ✓"))

    return results


# ============================================================
# Vision 호출 (5가지 자기 점검 질문)
# ============================================================

VISION_PROMPT = """이 디자인 스크린샷을 calm-design 기준으로 평가해줘. 5가지 질문에 JSON으로 답해.

질문:
Q1. 이 화면은 "AI가 만든 티"가 나는가?
    체크: 보라/네온 그래디언트, Inter 폰트 인상, 3-column equal cards, centered hero 강요,
    fabricated 통계, 이모지 UI 라벨

Q2. 한국어 가독성이 적절한가? (한국어 환경 한정)
    체크: 단어 중간 줄바꿈, 줄높이 부족, 본문 너무 김, 얇은 weight

Q3. 시각 위계가 명확한가?
    체크: 가장 중요한 액션이 즉시 식별되는가? CTA가 1개로 명확한가?

Q4. 화이트스페이스가 충분한가?
    체크: 섹션 패딩 ≥ py-24, 카드 안 패딩 충분, 텍스트 줄 사이 호흡

Q5. 다이얼 값이 시각적으로 반영됐는가?
    VARIANCE={variance}, MOTION={motion}, DENSITY={density}
    체크: VARIANCE=7인데 모두 centered면 실패, DENSITY=4인데 데이터 가득이면 실패

JSON 형식으로만 답해. 다른 설명 없이:
```json
{{
  "ai_tells_detected": ["..."],
  "ko_typography_issues": ["..."],
  "hierarchy_score": 0-10,
  "whitespace_score": 0-10,
  "dial_match": {{
    "variance_actual": 0-10,
    "delta_from_target": -10 to 10,
    "needs_correction": true|false
  }},
  "overall_assessment": "한 줄 요약"
}}
```"""


def vision_critique(
    desktop_png: Path,
    mobile_png: Path,
    dials: dict,
    api_key: str,
) -> dict:
    """Anthropic Vision API 호출. 미설치 시 스킵 + 정적 분석만으로 진행."""
    try:
        import anthropic
    except ImportError:
        return {
            "skipped": True,
            "reason": "anthropic 패키지 미설치 — 정적 분석만으로 진행",
            "ai_tells_detected": [],
            "hierarchy_score": None,
            "whitespace_score": None,
        }

    client = anthropic.Anthropic(api_key=api_key)

    # 두 이미지를 base64로
    def encode(p: Path) -> str:
        return base64.standard_b64encode(p.read_bytes()).decode("utf-8")

    prompt = VISION_PROMPT.format(
        variance=dials.get("variance", 7),
        motion=dials.get("motion", 6),
        density=dials.get("density", 4),
    )

    response = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=1024,
        messages=[{
            "role": "user",
            "content": [
                {"type": "text", "text": "데스크톱 뷰:"},
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": "image/png",
                        "data": encode(desktop_png),
                    },
                },
                {"type": "text", "text": "모바일 뷰:"},
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": "image/png",
                        "data": encode(mobile_png),
                    },
                },
                {"type": "text", "text": prompt},
            ],
        }],
    )

    text = response.content[0].text
    # JSON 블록 추출
    m = re.search(r"```json\s*(\{.*?\})\s*```", text, re.DOTALL)
    if m:
        return json.loads(m.group(1))
    # 직접 파싱 시도
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return {"raw": text, "parse_error": True}


# ============================================================
# 결과 종합 + 핀포인트 재생성 프롬프트
# ============================================================

def build_regen_prompt(failed: list[CheckResult], vision: dict) -> str:
    if not failed and not vision.get("ai_tells_detected"):
        return ""

    lines = ["다음 항목만 핀포인트로 수정하라. 다른 부분은 절대 건드리지 마라.\n"]

    for r in failed:
        if r.status == "fail":
            lines.append(f"❌ Pre-Flight #{r.item_id} ({r.title})")
            lines.append(f"   문제: {r.detail}")
            lines.append("")

    if vision.get("ai_tells_detected"):
        for tell in vision["ai_tells_detected"]:
            lines.append(f"🔧 Vision 발견: {tell}")
        lines.append("")

    if vision.get("dial_match", {}).get("needs_correction"):
        lines.append(f"🔧 다이얼 미스매치: {vision['dial_match']}")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="calm-design 셀프-크리틱 실행")
    parser.add_argument("--shots", required=True, help="render-preview.js 출력 디렉토리")
    parser.add_argument("--code", required=True, help="검증할 HTML/JSX 파일")
    parser.add_argument("--design-md", required=False, default="", help="DESIGN.md 경로 (선택)")
    parser.add_argument("--output", default=".calm-design/critique-report.json")
    parser.add_argument("--language", default="ko", choices=["ko", "en", "auto"])
    parser.add_argument("--variance", type=int, default=7)
    parser.add_argument("--motion", type=int, default=6)
    parser.add_argument("--density", type=int, default=4)
    parser.add_argument("--no-vision", action="store_true", help="Vision 호출 스킵 (정적 분석만)")
    args = parser.parse_args()

    code = Path(args.code).read_text(encoding="utf-8")
    design_md = Path(args.design_md).read_text(encoding="utf-8") if args.design_md else ""

    # 정적 분석
    print("🔍 정적 분석 실행 중...")
    static_results = static_analysis(code, design_md, args.language)

    # Vision (선택)
    vision = {"skipped": True}
    if not args.no_vision:
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            print("⚠️ ANTHROPIC_API_KEY 환경변수 없음 — Vision 스킵")
        else:
            shots_dir = Path(args.shots)
            desktop = shots_dir / "desktop.png"
            mobile = shots_dir / "mobile.png"
            if desktop.exists() and mobile.exists():
                print("👁  Vision 호출 중...")
                vision = vision_critique(
                    desktop, mobile,
                    {"variance": args.variance, "motion": args.motion, "density": args.density},
                    api_key,
                )
            else:
                print(f"⚠️ 캡처 파일 없음 ({shots_dir}) — Vision 스킵")

    # 종합
    passed = [r for r in static_results if r.status == "pass"]
    warned = [r for r in static_results if r.status == "warn"]
    failed = [r for r in static_results if r.status == "fail"]

    report = {
        "summary": {
            "passed": len(passed),
            "warned": len(warned),
            "failed": len(failed),
            "total": len(static_results),
        },
        "static_analysis": [asdict(r) for r in static_results],
        "vision": vision,
        "regen_prompt": build_regen_prompt(failed, vision if isinstance(vision, dict) else {}),
    }

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    Path(args.output).write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")

    # 콘솔 요약
    print(f"\n📊 Pre-Flight 결과: ✅{len(passed)} ⚠️{len(warned)} ❌{len(failed)} / {len(static_results)}")
    if failed:
        print("\n❌ 실패 항목:")
        for r in failed:
            print(f"  #{r.item_id} {r.title} — {r.detail}")
    if warned:
        print("\n⚠️ 경고 항목:")
        for r in warned:
            print(f"  #{r.item_id} {r.title} — {r.detail}")
    print(f"\n📝 리포트 저장: {args.output}")

    # Exit code
    sys.exit(0 if not failed else 1)


if __name__ == "__main__":
    main()
