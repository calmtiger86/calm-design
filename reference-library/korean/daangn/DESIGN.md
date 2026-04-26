# Design System: Inspired by 당근 (Daangn)

> Source: calm-design 자체 작성 — "Inspired by" 정책. daangn.com·당근마켓 앱 관찰 기반.
> LANGUAGE: ko · 시그니처: DaangnRecommendCarousel

## 1. Visual Theme & Atmosphere

따뜻한 로컬 마켓플레이스 톤. 당근 오렌지 시그니처. 친근한 한국어 카피("오늘 추천드려요"·"동네 이웃과"). 가로 스크롤 카드·정사각 이미지 중심. 사용자가 "이웃과의 거래"라는 정서를 느끼도록.

## 2. Color Palette & Roles

| Canvas | `#FFFFFF` | 페이지 배경 |
| Surface Soft | `#FAFAFA` | 카드 배경 |
| Ink | `#212124` | 본문 |
| Mute | `#868E96` | 보조 텍스트, 위치, 시간 |
| Border | `#F2F4F6` | 분할선 (얇게) |
| Accent | `#F26E22` | 당근 오렌지 톤 — Primary CTA, 활성, 가격 |
| Success | `#52C41A` | 거래 완료 |

규칙: 오렌지는 강조에만, 본문은 Ink·Mute. 채도 75% 미만 유지 (`#F26E22`는 70% 정도).

## 3. Typography Rules

- Family: `'Pretendard Variable', Pretendard, system-ui, sans-serif`
- 섹션 제목: `text-xl font-bold tracking-tight word-break:keep-all` ("오늘 추천드려요")
- 카드 제목: `text-sm font-semibold line-clamp-2 word-break:keep-all`
- 가격: `text-base font-bold tabular-nums` (천 단위 콤마, "원" 단위)
- 위치·시간: `text-xs text-mute`

금지: Inter, font-thin (한국어 가독성).

## 4. Component Stylings

### DaangnRecommendCarousel — 핵심 시그니처
- 컨테이너: `flex gap-3 px-4 overflow-x-auto snap-x snap-mandatory scrollbar-hide pb-2`
- 카드: `snap-start shrink-0 w-44 bg-white rounded-2xl border border-zinc-100 overflow-hidden`
- 이미지: `aspect-square object-cover` (정사각, 시각 일관성)
- 내용 padding: `p-3`
- 가격 강조: `text-base font-bold` + 천 단위 콤마

### 일반 카드 (피드용)
- `bg-white rounded-2xl border border-zinc-100 p-4` (얇은 보더)
- Hover: `bg-zinc-50` (interactive)
- 이미지 좌측 + 텍스트 우측 (`flex gap-3`) — 모바일 친화

### Primary CTA
- **Default**: `w-full h-12 rounded-xl bg-accent text-white font-bold`
- **Hover**: `scale-[1.01]` 200ms `cubic-bezier(0.16,1,0.3,1)`
- **Focus**: `ring-2 ring-accent ring-offset-2`
- **Active**: `scale-[0.99]`
- **Disabled**: `opacity-60 cursor-not-allowed bg-zinc-300 text-mute`
- **Loading**: spinner 인라인 `<Loader2 className="animate-spin w-4 h-4" />` + 텍스트 유지
- 라운드 12px (Toss보다 약간 작음 — 친근함)

### Bottom Tab (모바일)
- 4개 탭 (홈·검색·채팅·마이) `fixed bottom-0 max-w-md mx-auto h-14 grid grid-cols-4`
- 활성 탭: 오렌지 색

## 5. Layout Principles

- **모바일 우선**: `max-w-md mx-auto` 데스크톱에서도 모바일 비율
- **min-h-[100dvh]** 강제
- **가로 스크롤 + snap**: 추천 섹션의 핵심 패턴
- **피드**: 단일 컬럼, 카드 사이 8px gap
- **Top Bar**: 모바일 56px + 검색 아이콘
- **Bottom Tab**: 4개, fixed bottom

## 6. Depth & Elevation

- 카드 그림자 거의 없음 — `border-zinc-100` (매우 얇은 라이트 그레이)
- Top Bar: `border-b` 사용 (그림자 X)
- z-index: nav=40, bottom-tab=40, modal=50

## 7. Motion & Interaction

- Spring `cubic-bezier(0.16, 1, 0.3, 1)` 200ms
- 카드 tap: `scale-[0.98]`
- 이미지 로딩: skeleton (실제 정사각 박스 매칭)
- 페이드인: `delay: index * 30ms` (cascade)
- Reduced-motion 의무

## 8. Responsive Behavior

- 모바일 우선 (95% 사용자가 모바일)
- 터치 타겟 ≥ 44px (카드 hit area `w-44 h-auto` 충분)
- 가로 스크롤은 모바일 친화 (`snap-mandatory`)
- 한국어 본문 너비 `max-w-[55ch]` (약간 좁게 — 모바일 화면 친화)

## 9. Anti-Patterns (Project-Specific Banned)

- ❌ 광고적 톤 ("최저가!", "지금 사세요!") — 친근 한국어 카피 우선 ("좋은 가격이에요")
- ❌ Stock photo 얼굴 (실제 거래 사용자 인상 깨짐)
- ❌ 영어 lorem ipsum (한국어 더미 사용)
- ❌ 다크모드 강제 (당근은 라이트 우선)
- ❌ 데스크톱 사이드바 레이아웃 (모바일 우선 정체성)
- ❌ 채도 100% 빨간색·파란색 (오렌지 시그니처와 충돌)

(글로벌 안티-슬롭 50개는 `references/ai-tells-blocklist.md` 자동 적용)
