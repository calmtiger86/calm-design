#!/usr/bin/env python3
"""
calm-design / scripts/upgrade-diagnose.py

Mode B (Upgrade) Step 2 — 기존 디자인의 진단 리포트 자동 생성.
self-critique.py의 정적 분석 결과를 받아서 P0/P1/P2 우선순위로 분류 + 점수화.

사용법:
    python scripts/upgrade-diagnose.py <기존-코드.html> [--language ko|en]

출력:
    .calm-design/upgrade-diagnosis.md    (사용자에게 보여줄 리포트)
    .calm-design/upgrade-diagnosis.json  (Mode B Step 5 핀포인트 수정 입력)

Exit codes:
    0 — 진단 완료 (점수 무관)
    1 — 입력 파일 없음
"""

import argparse
import json
import sys
from pathlib import Path
import importlib.util


def load_self_critique():
    """self-critique.py를 동적 import (파일명에 - 포함이라 importlib 필요)."""
    spec = importlib.util.spec_from_file_location(
        "self_critique", Path(__file__).parent / "self-critique.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


# ============================================================
# 항목별 우선순위 매핑 (P0=Critical, P1=High, P2=Medium)
# ============================================================
PRIORITY_MAP = {
    # P0 — 즉시 수정 (Critical Anti-Slop)
    6: "P0",   # Pure Black
    7: "P0",   # LILA BAN
    9: "P0",   # Inter 폰트
    10: "P0",  # Pretendard 강제 (한국어)
    11: "P0",  # word-break: keep-all
    14: "P0",  # 한국어 본문 너비
    25: "P0",  # alt 속성 누락
    26: "P0",  # 라벨 미연결

    # P1 — 빠른 수정 (Layout & Visibility)
    1: "P1",   # 모바일 붕괴
    2: "P1",   # h-screen
    3: "P1",   # max-width
    5: "P1",   # 3-column equal
    13: "P1",  # 한국어 weight
    15: "P1",  # GPU 친화 애니메이션
    21: "P1",  # Empty/Error/Loading
    22: "P1",  # WCAG AA 색상 대비
    24: "P1",  # 키보드 포커스
    35: "P1",  # AT-35 광고 카피
    36: "P1",  # AT-36 한국어 lorem

    # P2 — 보강 (Polish)
    4: "P2",   # 섹션 다양화
    8: "P2",   # 단일 액센트
    12: "P2",  # 한국어 줄높이
    16: "P2",  # Spring physics
    17: "P2",  # 컴포넌트 6상태
    18: "P2",  # AI 카피 클리셰
    19: "P2",  # Generic placeholder
    20: "P2",  # Filler UI
    23: "P2",  # ARIA 라벨
    27: "P2",  # 다크모드
    28: "P2",  # SEO meta
    29: "P2",  # z-index 충돌
    30: "P2",  # Reduced-motion
    37: "P2",  # AT-37 autoplay
    38: "P2",  # AT-38 stock photo
}


PRIORITY_WEIGHT = {"P0": 5, "P1": 3, "P2": 1}


def compute_weighted_score(static_results: list) -> tuple[int, dict]:
    """
    P0/P1/P2 가중치 적용된 100점 만점 점수.

    각 항목 점수:
      ✅ pass  → 가중치 그대로
      ⚠️ warn  → 가중치 × 1/3
      ❌ fail  → 0

    breakdown으로 카테고리별 기여도도 반환.
    """
    if not static_results:
        return 0, {}

    earned_by_prio = {"P0": 0, "P1": 0, "P2": 0}
    max_by_prio = {"P0": 0, "P1": 0, "P2": 0}

    for r in static_results:
        prio = PRIORITY_MAP.get(r["item_id"], "P2")
        weight = PRIORITY_WEIGHT[prio]
        max_by_prio[prio] += weight

        if r["status"] == "pass":
            earned_by_prio[prio] += weight
        elif r["status"] == "warn":
            earned_by_prio[prio] += weight / 3.0
        # fail은 0

    total_max = sum(max_by_prio.values())
    total_earned = sum(earned_by_prio.values())

    score = round((total_earned / total_max) * 100) if total_max else 0
    breakdown = {
        prio: {
            "earned": round(earned_by_prio[prio], 1),
            "max": max_by_prio[prio],
            "pct": round(earned_by_prio[prio] / max_by_prio[prio] * 100) if max_by_prio[prio] else 0,
        }
        for prio in ["P0", "P1", "P2"]
    }
    return score, breakdown


def classify_findings(static_results: list) -> dict:
    """정적 분석 결과를 P0/P1/P2로 분류."""
    by_priority: dict[str, list] = {"P0": [], "P1": [], "P2": []}
    for r in static_results:
        prio = PRIORITY_MAP.get(r["item_id"], "P2")
        if r["status"] in ("fail", "warn"):
            by_priority[prio].append(r)
    return by_priority


def render_markdown_report(score: int, summary: dict, by_priority: dict) -> str:
    bd = summary.get("breakdown", {})
    lines = [
        "# 🩺 Upgrade 진단 리포트 (Mode B Step 2-3)",
        "",
        f"**현재 점수**: {score}/100 (P0/P1/P2 가중치 적용)",
        f"**상태**: ✅ {summary['passed']} · ⚠️ {summary['warned']} · ❌ {summary['failed']} / 총 {summary['total']}",
        "",
        "**카테고리별 기여도**:",
    ]
    if bd:
        for prio in ["P0", "P1", "P2"]:
            d = bd.get(prio, {})
            lines.append(f"- {prio}: {d.get('earned', 0)}/{d.get('max', 0)}점 ({d.get('pct', 0)}%)")
    lines += [
        "",
        "---",
        "",
    ]

    titles = {
        "P0": "🚨 P0 Critical (즉시 수정 권장)",
        "P1": "⚡ P1 High (빠른 수정)",
        "P2": "✨ P2 Polish (보강)",
    }

    for prio, items in by_priority.items():
        if not items:
            continue
        lines.append(f"## {titles[prio]}")
        lines.append("")
        for r in items:
            icon = "❌" if r["status"] == "fail" else "⚠️"
            lines.append(f"- {icon} **#{r['item_id']} {r['title']}**")
            lines.append(f"  - {r['detail']}")
        lines.append("")

    lines += [
        "---",
        "",
        "## 다음 단계 — 어떻게 진행하시겠어요?",
        "",
        "1. **모두 자동 수정** (전 항목 한 번에 — 변경 폭 큼)",
        "2. **P0 Critical만 수정** (안전한 점진 개선) ← 권장",
        "3. **카테고리별 선택** (폰트만 / 색상만 / 접근성만)",
        "4. **사용자 명시 항목만** (직접 항목 선택)",
        "",
        "선택 후 Mode B Step 4 (보존 계약) 진행.",
    ]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Mode B 진단 자동화")
    parser.add_argument("code_path")
    parser.add_argument("--language", default="ko", choices=["ko", "en", "auto"])
    parser.add_argument("--output-dir", default=".calm-design")
    args = parser.parse_args()

    code_path = Path(args.code_path)
    if not code_path.exists():
        print(f"❌ 입력 파일 없음: {code_path}")
        sys.exit(1)

    sc = load_self_critique()
    code = code_path.read_text(encoding="utf-8")
    static_results = [r.__dict__ if hasattr(r, "__dict__") else r
                       for r in sc.static_analysis(code, "", args.language)]

    passed = sum(1 for r in static_results if r["status"] == "pass")
    warned = sum(1 for r in static_results if r["status"] == "warn")
    failed = sum(1 for r in static_results if r["status"] == "fail")
    total = len(static_results)
    score, breakdown = compute_weighted_score(static_results)

    summary = {
        "passed": passed, "warned": warned, "failed": failed,
        "total": total, "score": score, "breakdown": breakdown,
    }
    by_priority = classify_findings(static_results)

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    md = render_markdown_report(score, summary, by_priority)
    (out_dir / "upgrade-diagnosis.md").write_text(md, encoding="utf-8")

    json_data = {
        "input": str(code_path),
        "language": args.language,
        "score": score,
        "summary": summary,
        "findings_by_priority": by_priority,
    }
    (out_dir / "upgrade-diagnosis.json").write_text(
        json.dumps(json_data, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    print(f"📊 진단 완료: {score}/100")
    print(f"   P0 Critical: {len(by_priority['P0'])}개")
    print(f"   P1 High:     {len(by_priority['P1'])}개")
    print(f"   P2 Polish:   {len(by_priority['P2'])}개")
    print(f"📝 리포트: {out_dir / 'upgrade-diagnosis.md'}")


if __name__ == "__main__":
    main()
