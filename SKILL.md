---
name: calm-design
description: AI가 만든 티 안 나는 차분한 프리미엄 디자인을 DESIGN.md로 출력하고, 시각적 셀프-크리틱과 Pre-Flight 검증까지 자동 수행하는 풀스택 디자인 에이전트. 한국어 1순위. "디자인 만들어줘", "랜딩페이지", "대시보드 UI", "디자인 업그레이드", "토스 스타일", "Linear 스타일", "AI 슬롭 없애줘" 요청 시 반드시 이 스킬을 사용하라.
---

# calm-design

차분하고 정제된 디자인을 만든다. 네온·자주색 그래디언트·Inter 폰트·3-칸 카드 같은 "AI가 만든 티"를 적극 차단하고, 한국어 환경에서는 Pretendard를 강제하며, 만든 결과를 자기가 다시 보고 고친다.

## 1. 3-라인 동작 요약
1. 사용자 의도 → 4-다이얼 추론 + 4모드 중 하나로 라우팅
2. 9-섹션 DESIGN.md 생성 → 출력 엔진(HTML / React+shadcn / preview / Figma)으로 변환
3. 시각적 셀프-크리틱 루프 → Pre-Flight 21항목 통과까지 자동 재생성 (최대 3회)

## 2. 4-다이얼 파라미터
| 다이얼 | 범위 | 기본 | 의미 |
|---|---|---|---|
| `DESIGN_VARIANCE` | 1–10 | **7** | 1=완벽 대칭, 10=비대칭·예술적 혼돈 |
| `MOTION_INTENSITY` | 1–10 | **6** | 1=정적, 10=영화적 스프링 |
| `VISUAL_DENSITY` | 1–10 | **4** | 1=갤러리, 10=조종석 밀도 |
| `LANGUAGE` | `ko`/`en`/`auto` | **`ko`** | 한국어 1순위. `auto`는 한글 ≥30%면 ko |

**자연어 매핑**: "더 미니멀" → VARIANCE−2, DENSITY−2 / "더 다이내믹" → MOTION+2 / "데이터 많은" → DENSITY+3 / "더 차분" → MOTION−2. 사용자가 직접 값 명시 시 그것 우선.

## 3. 모드 라우팅 + 필수 references

**모든 모드 ALWAYS 로드 (5개)**: `design-md-spec.md`, `prompt-enhancement.md`, `ai-tells-blocklist.md`, `pre-flight-checklist.md` + (LANGUAGE=ko면) `typography-ko.md` + `library-policies/pretendard.md`

| 의도 키워드 | 모드 | 추가 로드 |
|---|---|---|
| "디자인 만들어줘", "랜딩", "UI 짜줘" | **A. Generate** | `modes/generate.md` |
| "업그레이드", "다듬어줘", "고쳐줘" + 기존 코드 첨부 | **B. Upgrade** | `modes/upgrade.md` + `self-critique-loop.md` |
| "토스 스타일", "Linear 처럼", "Vercel 풍" | **C. Match-Reference** | + `reference-library/{matched}/DESIGN.md` (3개 후보) |
| "3가지 안", "여러 옵션", "다양하게" | **D. Multi-Variant** | `modes/multi-variant.md` + `creative-arsenal.md` + `color-system.md` + `motion-system.md` |

여러 키워드 동시 등장 시 우선순위: **D > C > B > A**.

## 4. 출력 엔진 선택

기본은 **HTML + Tailwind CDN** (즉시 미리보기). 사용자 시그널에 따라:

- 기본 / "바로 보고 싶어" → `output-engines/html-tailwind.md` + `library-policies/lucide.md`
- "React로", "Next.js", "컴포넌트" → `output-engines/react-shadcn.md` + `shadcn-ui.md` + `lucide.md` + `framer-motion.md`
- "JSON Spec", "json-render", "멀티플랫폼", "웹+모바일+PDF 동시" → `output-engines/json-render-spec.md` + `library-policies/json-render.md`
- "preview 카탈로그", "디자인 시스템 시각화", "토큰 프리뷰" → `output-engines/preview-catalog.md`
- "Figma 명세", "Figma 토큰", "Tokens Studio" → `output-engines/figma-export.md`

## 5. 셀프-크리틱 루프

출력 직후 **자동 트리거**. `--no-critique` 또는 "검증 건너뛰어" 시만 비활성. `references/self-critique-loop.md` 5단계: 생성 → 렌더+캡처 → Vision 셀프분석 → Pre-Flight 채점 → 실패 항목만 핀포인트 재생성. 3회 시도 후 미통과면 **부분 결과 + 미통과 리포트** 함께 전달.

**환경 자동 감지**: visualize MCP 가능하면 Cowork 인-스킬(외부 API 키 X) / `mcp__workspace__bash` 가능하면 Claude Code Playwright(`scripts/render-preview.js`) / 둘 다 X면 정적 분석만.

## 6. 라이브러리 정책 (출력 엔진별)

**HTML 모드 — CDN 5개 제한**: Tailwind / Pretendard / lucide(SVG) / Motion One(4KB) / 슬롯1(요청시).
**React 모드 — npm**: shadcn-ui / lucide-react / framer-motion / tailwindcss(v4) / pretendard / @radix-ui(shadcn 자동 의존, 직접 import 금지) / zustand(2+ 컴포넌트 상태 공유 시만).

상세 정책은 `library-policies/{name}.md`.

## 7. 즉시 적용 안티-슬롭 핵심 5

전체 50+는 `references/ai-tells-blocklist.md`. 이 5개는 **메인에서 항상 자동 적용**:

1. ❌ Inter → ✅ ko면 Pretendard, en이면 Geist/Cabinet Grotesk/Outfit/Satoshi
2. ❌ Pure Black `#000000` → ✅ Off-Black `#0A0A0A`, Zinc-950, Charcoal
3. ❌ 보라·파란 AI 그래디언트 ("LILA BAN") → ✅ Neutral 베이스 + 단일 액센트, 채도 <80%
4. ❌ 3-column equal cards → ✅ Bento Grid, 2-column Zig-Zag, 비대칭 그리드, Masonry
5. ❌ `h-screen` (iOS 100vh 버그) → ✅ `min-h-[100dvh]`

## 8. 진입 직후 4단계 (필수 순서, 절대 건너뛰지 마라)

0. **사용자 오버라이드 자동 로드** — 프로젝트 루트에 `.calm-design/keyword-overrides.md` 또는 `.calm-design/anti-patterns.md` 있으면 우선 로드해 기본값보다 우선 적용
1. **다이얼 추론** — 입력에서 4-다이얼 결정 (2장 자연어 매핑)
2. **모드 결정 + references 로드** — 3장 표
3. **출력 엔진 결정 + 정책 로드** — 4장 표
4. **9-섹션 DESIGN.md 생성 → 출력 엔진 변환 → 셀프-크리틱 루프 자동 트리거** (DESIGN.md가 1차 산출물, 코드는 파생물 — 절대 코드부터 출력하지 말 것)

## 9. 사용자에게 항상 제공할 산출물 4가지

1. **DESIGN.md** (9-섹션) — `.calm-design/DESIGN.md`로 저장
2. **선택한 출력물** (HTML 또는 React 코드)
3. **셀프-크리틱 리포트** (Pre-Flight 21항목 ✅/❌ + 재생성 횟수)
4. **다이얼+모드 한 줄 요약** ("VARIANCE=7, MOTION=6, DENSITY=4, LANGUAGE=ko, Mode A")
