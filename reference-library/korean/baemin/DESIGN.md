# Design System: Inspired by 배달의민족 (Baemin)

> Source: calm-design 자체 작성 — "Inspired by" 정책. baemin.com·배민 앱 관찰 기반.
> LANGUAGE: ko

## 1. Visual Theme & Atmosphere

친근·B급 감성 한국 시그니처. 한나체·도현체 같은 한국 캘리그래피 톤(라이선스로 calm-design은 Pretendard fallback). 민트색 액센트, 카피 톤이 시그니처("주문도 안 하고 사라지면 안 될까요"). 음식 사진 + 가격 + 배달비 강조.

## 2. Color Palette & Roles

| Canvas | `#FFFFFF` | 페이지 배경 |
| Surface Soft | `#FAFAFA` | 카드 |
| Ink | `#222222` | 본문 |
| Mute | `#888888` | 보조 |
| Border | `#EEEEEE` | 분할 |
| Accent | `#2AC1BC` | 배민 민트 톤 (Primary CTA, 활성, 강조) |
| Accent Soft | `#E0F7F6` | 액센트 배경 |
| Sale | `#FF5A5A` | 쿠폰·할인 |
| Premium | `#FFC700` | 배민 클럽·프리미엄 |

## 3. Typography Rules

- Family: `'Pretendard Variable', Pretendard, system-ui, sans-serif`
- 한나체·도현체는 라이선스로 차용 X — Pretendard 또는 사용자 명시 폰트
- 헤드라인: `text-2xl md:text-3xl font-bold tracking-tight word-break:keep-all`
- 가게명: `text-base font-semibold break-keep`
- 메뉴명: `text-sm font-medium break-keep`
- 가격: `text-base font-bold tabular-nums`
- 배달비·시간: `text-xs text-mute tabular-nums`
- 카피 톤: 친근하고 유머 있는 한국어 ("주문하시면 빠르게 배달해드릴게요")

금지: Inter, font-thin/extralight (한국어 가독성).

## 4. Component Stylings

### 가게 카드
- **Default**: `bg-white rounded-lg border border-zinc-100 p-3` (얇은 보더)
- 가게 사진 좌측 + 정보 우측 (`flex gap-3`) — 모바일 친화
- **Hover**: `bg-zinc-50` + border-zinc-300
- **Focus**: ring-2 ring-accent
- **Active**: scale 0.98
- **Disabled** (영업종료): opacity 60% + "영업종료" 라벨
- **Loading**: skeleton

### 메뉴 카드
- **Default**: `flex items-center gap-3 p-4 border-b border-zinc-100`
- 메뉴 사진 정사각 작게 우측 + 메뉴명·설명 좌측
- 가격 우측 끝
- **Hover**: `bg-zinc-50`
- **Focus/Active/Disabled/Loading**: 표준 6상태

### Primary CTA (주문하기)
- **Default**: `w-full h-14 rounded-xl bg-accent text-white font-bold text-base`
- **Hover**: scale 1.01
- **Focus**: ring-2 ring-accent ring-offset-2
- **Active**: scale 0.99
- **Disabled**: bg-zinc-300 opacity-60
- **Loading**: spinner inline + "주문 처리 중..." 카피

### 쿠폰·배지
- `inline-flex bg-accent-soft text-accent text-xs font-bold px-2 py-0.5 rounded-md`
- 친근 카피: "오늘만 1,000원 할인", "신규회원 쿠폰"

## 5. Layout Principles

- **모바일 우선** (`max-w-md mx-auto`)
- **Top Bar 56px** + 위치·검색
- **Bottom Tab 4-5개**: 홈·검색·주문내역·찜·마이
- 가게 리스트: 단일 컬럼 (모바일 친화)
- min-h-[100dvh] 강제

## 6. Depth & Elevation

- 카드 그림자 없음 — `border-zinc-100` (매우 얇음)
- Bottom Tab: `border-t` + `bg-white/95 backdrop-blur-md`
- 모달·시트: shadow-lg + backdrop-blur

## 7. Motion & Interaction

- 200-300ms cubic-bezier
- 카드 tap: scale 0.98 (즉각 피드백)
- 카운트업: 가격·할인 강조
- Reduced-motion 의무

## 8. Responsive Behavior

- 모바일 우선 (배민은 99% 모바일 사용)
- 터치 타겟 ≥ 44px
- 한국어 카피 break-keep + max-w-[65ch]
- 가로 스크롤 카테고리 (snap-x)

## 9. Anti-Patterns (Project-Specific Banned)

- ❌ 영어 위주 카피 (배민 시그니처는 친근 한국어 + 유머)
- ❌ 차가운 톤 (배민은 따뜻·친근)
- ❌ 다크모드 강제 (라이트 우선)
- ❌ 데스크톱 사이드바 (모바일 정체성)
- ❌ Stock photo 음식 (실제 가게 음식 사진 우선)
- ❌ "Click here", "Buy now" 같은 영어 광고 톤

(글로벌 안티-슬롭 50개는 `references/ai-tells-blocklist.md` 자동 적용)
