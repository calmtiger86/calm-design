# Design System: Inspired by Replicate

> Source: calm-design 자체 작성 — "Inspired by" 정책. replicate.com 공개 인터페이스 관찰 기반.
> LANGUAGE: en (글로벌 AI 플랫폼)

## 1. Visual Theme & Atmosphere

Terminal-first AI model platform. Near-black canvas with monospaced code blocks, subtle syntax highlighting, and a single warm accent. The interface feels like a premium CLI wrapper — dense but never chaotic. Developers are the primary audience: every affordance is functional, not decorative. Whitespace is earned, not given freely.

## 2. Color Palette & Roles

| Canvas   | `#0A0A0B` | 페이지 배경 — Off-Black, not Pure Black |
| Surface  | `#111114` | 카드·코드블록·패널 배경 |
| Elevated | `#1A1A1F` | 호버 상태·드롭다운·입력 필드 |
| Ink      | `#F2F2F5` | 본문·헤드라인 (Off-White) |
| Mute     | `#6B7280` | 보조 텍스트·메타데이터 |
| Border   | `#2A2A30` | 1px 분할선·카드 테두리 |
| Accent   | `#6366F1` | CTA·강조·인터랙션 (Indigo 계열) |
| Code     | `#A3E635` | 코드 하이라이트·터미널 출력 (Lime) |
| Danger   | `#EF4444` | 오류·삭제·경고 |
| Success  | `#22C55E` | 완료·성공·실행 완료 상태 |

규칙: Pure Black `#000000` 금지 — Off-Black `#0A0A0B` 사용. 단일 Indigo 액센트. 코드 전용 Lime 하이라이트는 텍스트에만.

## 3. Typography Rules

- Family: `Geist Mono` (코드·터미널 전용), `Geist` (본문·UI 텍스트)
- Display / H1: `text-4xl md:text-5xl`, `tracking-tight`, `leading-tight`, `font-semibold`
- Body: `text-sm md:text-base`, `leading-relaxed`, `max-w-[72ch]`
- Code blocks: `font-mono text-sm leading-6` — Geist Mono 강제
- Labels / Meta: `text-xs tracking-wide text-mute uppercase font-medium`
- Numeric / Stats: `tabular-nums font-mono text-ink`
- 금지: Inter (보편화돼 변별력 없음), Helvetica, Times, Georgia

## 4. Component Stylings

### Model Card (시그니처 컴포넌트)

- **Default**: `bg-surface border border-border rounded-lg p-4 cursor-pointer`
- **Hover**: `bg-elevated border-[#3A3A42]` — 명도 미세 상승, transform X
- **Focus**: `ring-2 ring-accent ring-offset-2 ring-offset-canvas outline-none`
- **Active**: `bg-elevated border-accent/40 scale-[0.99]` — 200ms ease-out
- **Disabled**: `opacity-40 cursor-not-allowed pointer-events-none`
- **Loading**: shimmer skeleton — `bg-elevated animate-pulse rounded-lg` (실제 카드 치수 유지)

### Button (Primary — Run Model)

- **Default**: `h-9 px-4 rounded-md bg-accent text-white text-sm font-medium tracking-tight`
- **Hover**: `bg-[#4F52D4]` — 명도 하강 10%, transform X
- **Focus**: `ring-2 ring-accent ring-offset-2 ring-offset-canvas`
- **Active**: `bg-[#4347C0] scale-[0.98]` — 150ms
- **Disabled**: `opacity-50 cursor-not-allowed`
- **Loading**: 인라인 spinner `animate-spin` + 버튼 텍스트 "Running..." 유지

### Code Input / Prompt Field

- **Default**: `bg-elevated border border-border rounded-md px-3 py-2 font-mono text-sm text-ink`
- **Hover**: `border-[#3A3A42]`
- **Focus**: `border-accent ring-1 ring-accent/30 outline-none`
- **Active**: focus 상태와 동일
- **Disabled**: `opacity-50 cursor-not-allowed bg-surface`
- **Loading**: `animate-pulse border-accent/20` — 처리 중 시각 표시

## 5. Layout Principles

- **Sidebar 260px** (모델 탐색·필터) + Main `flex-1`
- **Top Bar 48px** — 로고 + 검색 + 계정 아이콘만
- **Content max-width**: `max-w-6xl mx-auto px-4 md:px-6`
- **Full-height**: `min-h-[100dvh]` 강제 — `h-screen` 금지 (iOS 100vh 버그)
- **그리드**: Model grid `grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4`
- **코드 블록**: 전체 너비, 좌우 스크롤 허용 (`overflow-x-auto`)
- **금지**: 큰 marketing hero, 과도한 padding, 3-column equal cards

## 6. Depth & Elevation

- **그림자 최소화** — 다크 배경에서는 1px border가 깊이 표현
- **Elevated surface**: `bg-elevated` 색상 차이로만 계층 표현, shadow X
- **모달**: `bg-surface border border-border rounded-xl` + `backdrop-blur-sm`
- **Dropdown**: `bg-elevated border border-border shadow-[0_4px_16px_rgba(0,0,0,0.6)] rounded-lg`
- **Code highlight line**: `bg-accent/10 border-l-2 border-accent` (인라인 강조)
- **z-index 계층**: nav=40, overlay=50, tooltip=60

## 7. Motion & Interaction

- **기본 easing**: `cubic-bezier(0.16, 1, 0.3, 1)` — 200ms 표준
- **GPU 속성만**: `transform`, `opacity` 애니메이션. `top/left/width/height` 애니메이션 금지
- **Skeleton loading**: shimmer `animate-pulse` — 실제 레이아웃 유지, "Loading..." 텍스트 X
- **Progress bar** (모델 실행 중): `bg-accent h-0.5 transition-all duration-300` 상단 고정
- **Staggered list entry**: 모델 카드 `delay: index * 40ms` cascade
- **Reduced-motion 의무**: `@media (prefers-reduced-motion: reduce)` 처리

## 8. Responsive Behavior

- **데스크톱 우선** — 코드·API 중심 도구, 모바일은 보조
- **Breakpoints**: 모바일 `<768px`, 태블릿 `768–1024px`, 데스크톱 `≥1024px`
- **Sidebar**: 태블릿 이하 collapsible → 햄버거 토글
- **모바일**: 단일 컬럼, 코드 블록 수평 스크롤 허용, 버튼 `min-h-[44px]` (iOS HIG)
- **Navigation**: 데스크톱 사이드바 → 모바일 바텀 시트 또는 상단 드롭다운
- **Typography scaling**: `clamp(0.875rem, 1.5vw + 0.5rem, 1rem)` 본문 기준

## 9. Anti-Patterns (Project-Specific Banned)

- ❌ 밝은 배경(Light mode) 강제 — Replicate는 다크 우선 플랫폼, 라이트 전환 제공 X
- ❌ 장식적 일러스트·이모지 UI 라벨 — 개발자 도구 정체성과 충돌
- ❌ 마케팅 hero 섹션 (대형 tagline + CTA 배너) — 모델 카탈로그가 바로 첫 화면
- ❌ 비-monospace 폰트 코드 블록 — Geist Mono 이외 폰트 코드 영역 사용 금지
- ❌ 색상 과다 사용 — Indigo 단일 액센트 + Lime 코드 전용, 추가 색상 남발 금지
- ❌ 애니메이션 스케일 과장 (`scale-110` 이상) — 터미널 톤과 충돌

(글로벌 안티-슬롭 50개는 `references/ai-tells-blocklist.md` 자동 적용)
