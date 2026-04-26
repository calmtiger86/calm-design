# Design System: Inspired by Sanity

> Source: calm-design 자체 작성 — "Inspired by" 정책. sanity.io 공개 인터페이스 관찰 기반.
> LANGUAGE: en (글로벌 헤드리스 CMS 플랫폼)

## 1. Visual Theme & Atmosphere

Structured content platform bridging developers and content editors. Crisp white canvas with a bold red accent — confident without being aggressive. The Studio UI is dense and functional; the marketing site is airy and editorial. Both share the same typographic rigor: tight headlines, generous line-height in body copy, and zero decorative noise. The red is reserved strictly for action and attention, never decoration.

## 2. Color Palette & Roles

| Canvas   | `#FFFFFF` | 페이지 배경 (순백 — Studio 전통) |
| Surface  | `#F5F5F5` | 카드·패널·사이드바 배경 |
| Elevated | `#EBEBEB` | 호버 상태·드롭다운 배경 |
| Ink      | `#1A1A1A` | 본문·헤드라인 (Off-Black) |
| Mute     | `#737373` | 보조 텍스트·메타데이터·플레이스홀더 |
| Border   | `#E0E0E0` | 1px 분할선·카드 테두리 |
| Accent   | `#F03E2F` | Sanity Red — CTA·강조·활성 상태 |
| AccentHover | `#D32F20` | Accent hover/pressed |
| Danger   | `#C62828` | 삭제·비가역 작업 (Accent와 구분) |
| Success  | `#2E7D32` | 저장 완료·퍼블리시 성공 |

규칙: Pure Black `#000000` 금지 — Off-Black `#1A1A1A` 사용. Sanity Red 단일 액센트, 남발 금지. 라이트 모드 우선.

## 3. Typography Rules

- Family: `Outfit` (마케팅·헤드라인), `Cabinet Grotesk` (Studio UI·본문·라벨)
- Display / H1: `text-5xl md:text-6xl lg:text-7xl`, `tracking-tighter`, `leading-none`, `font-bold`
- Body: `text-base md:text-lg`, `leading-relaxed`, `max-w-[68ch]`
- Studio UI text: `text-sm`, `leading-normal`, `Cabinet Grotesk` — 밀도 있는 편집기 환경
- Labels / Meta: `text-xs tracking-wide text-mute uppercase font-semibold`
- Code / Schema: `font-mono text-sm` — `ui-monospace, SFMono-Regular, Menlo` fallback
- 금지: Inter (변별력 없음), Helvetica, Times, Georgia, 시스템 기본 sans-serif 단독 사용

## 4. Component Stylings

### Document Card (Studio 시그니처)

- **Default**: `bg-white border border-border rounded-lg p-4 cursor-pointer`
- **Hover**: `bg-surface border-[#C8C8C8]` — 명도 미세 하강, transform X
- **Focus**: `ring-2 ring-accent ring-offset-2 outline-none`
- **Active**: `bg-elevated border-accent/50 scale-[0.99]` — 150ms ease-out
- **Disabled**: `opacity-50 cursor-not-allowed pointer-events-none`
- **Loading**: skeleton shimmer `bg-gradient-to-r from-surface via-elevated to-surface animate-pulse rounded-lg`

### Button (Primary — Publish)

- **Default**: `h-9 px-5 rounded-full bg-accent text-white text-sm font-semibold tracking-tight`
- **Hover**: `bg-[#D32F20]` — AccentHover, transform X
- **Focus**: `ring-2 ring-accent ring-offset-2`
- **Active**: `bg-[#B71C1C] scale-[0.97]` — 120ms
- **Disabled**: `opacity-50 cursor-not-allowed`
- **Loading**: 인라인 spinner `animate-spin` + "Publishing..." 텍스트 유지

### Field Input (Studio 편집기)

- **Default**: `bg-white border border-border rounded-md px-3 py-2 text-sm text-ink`
- **Hover**: `border-[#C0C0C0]`
- **Focus**: `border-accent ring-2 ring-accent/20 outline-none`
- **Active**: focus 상태와 동일
- **Disabled**: `bg-surface opacity-60 cursor-not-allowed`
- **Loading**: `animate-pulse border-accent/30` — 비동기 검증 중 표시

## 5. Layout Principles

- **Studio 3-panel**: Navigator 240px + Document Editor flex-1 + Inspector 320px
- **Top Bar 52px** — 로고 + 워크스페이스 선택 + 유저 아바타
- **마케팅 사이트**: `max-w-7xl mx-auto px-4 md:px-8`
- **Full-height**: `min-h-[100dvh]` 강제 — `h-screen` 금지 (iOS 100vh 버그)
- **콘텐츠 그리드**: `grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6` (피처 섹션)
- **Variance**: Hero(Split-text) → Features(Bento) → Testimonials(Masonry) → CTA(Full-bleed red) → Footer(Minimal)
- **금지**: 3-column equal cards, 수평 스크롤 (Studio 제외), 과도한 padding `py-48+`

## 6. Depth & Elevation

- **라이트 배경 그림자 최소화** — border 1px가 우선, shadow는 계층 필요 시만
- **카드 hover**: `shadow-sm` — `box-shadow: 0 1px 4px rgba(0,0,0,0.08)` 수준
- **모달**: `bg-white border border-border rounded-2xl shadow-[0_8px_32px_rgba(0,0,0,0.12)]`
- **Dropdown**: `bg-white border border-border shadow-[0_4px_16px_rgba(0,0,0,0.10)] rounded-xl`
- **Toast / Notification**: `bg-ink text-white` 인버스 처리 + 미세 shadow
- **z-index 계층**: nav=40, panel=45, modal=50, tooltip=60

## 7. Motion & Interaction

- **기본 easing**: `cubic-bezier(0.16, 1, 0.3, 1)` — 250ms 표준 (Studio 신중한 톤)
- **GPU 속성만**: `transform`, `opacity`. `top/left/width` 애니메이션 금지
- **Panel slide**: `translate-x` — 사이드 패널 열기/닫기 300ms spring
- **Publish 성공**: 체크마크 SVG path draw 애니메이션 400ms → `text-success`
- **Staggered form fields**: 새 문서 열릴 때 `delay: index * 30ms` cascade
- **Reduced-motion 의무**: `@media (prefers-reduced-motion: reduce)` 처리 — 모든 transition off

## 8. Responsive Behavior

- **데스크톱 우선** — Studio는 넓은 화면 전제 (3-panel)
- **Breakpoints**: 모바일 `<768px`, 태블릿 `768–1024px`, 데스크톱 `≥1024px`
- **마케팅 사이트**: 모바일 완전 지원 — 단일 컬럼, `px-4`, 버튼 full-width
- **Studio 태블릿**: Navigator 숨김 → 햄버거, Inspector 숨김 → 슬라이드 오버레이
- **Studio 모바일**: 제한적 지원 — 단일 패널 뷰, 탭 네비게이션
- **Touch targets**: 최소 `44×44px` (iOS HIG 준수) — 모든 인터랙티브 요소
- **Typography scaling**: `clamp(1rem, 2vw + 0.75rem, 1.125rem)` 본문 기준

## 9. Anti-Patterns (Project-Specific Banned)

- ❌ 다크 모드 강제 — Sanity Studio는 라이트 우선, 다크 선택은 사용자 권한
- ❌ Red accent 남용 — Sanity Red는 CTA·활성 상태 전용, 배경색·텍스트 데코 사용 금지
- ❌ 경고·삭제 버튼에 Accent Red 재사용 — Danger는 별도 `#C62828` 사용
- ❌ 유려한 마케팅 애니메이션 내 Studio UI — 에디터 영역은 정적·집중형
- ❌ 비-Sanity CMS 레퍼런스 UI 패턴 차용 (WordPress 스타일 어드민 등)
- ❌ 폼 필드 라벨 생략 — 접근성 및 Studio 표준 위반

(글로벌 안티-슬롭 50개는 `references/ai-tells-blocklist.md` 자동 적용)
