# Design System: Inspired by 쿠팡 (Coupang)

> Source: calm-design 자체 작성 — "Inspired by" 정책. coupang.com 공개 인터페이스 관찰 기반.
> LANGUAGE: ko

## 1. Visual Theme & Atmosphere

빠른 배송·로켓 시그니처 이커머스. 정보 밀도 매우 높음 (DENSITY 8+) — 가격·할인율·로켓배송·로켓프레시 라벨이 카드마다 가득. 빨강·핑크 톤 액센트. "지금 사면 내일 도착" 긴급감 + 친근 한국어 카피.

## 2. Color Palette & Roles

| Canvas | `#FFFFFF` | 페이지 배경 |
| Surface Soft | `#F9F9F9` | 카드·섹션 |
| Ink | `#212121` | 본문 |
| Mute | `#909090` | 보조 |
| Border | `#EEEEEE` | 분할 (얇게) |
| Accent | `#F02E2E` | 쿠팡 빨강 톤 (Primary CTA, 가격 강조, 로켓 배지) |
| Sale | `#F02E2E` | 할인율 강조 |
| Rocket | `#0074E4` | 로켓배송·로켓프레시 라벨 |
| Premium | `#FFB800` | 와우 회원 라벨 |

규칙: 빨강은 가격·할인·CTA에만, 본문은 Ink. 채도 80% 미만 유지.

## 3. Typography Rules

- Family: `'Pretendard Variable', Pretendard, system-ui, sans-serif`
- 디스플레이: `text-2xl md:text-3xl font-bold tracking-tight word-break:keep-all`
- 상품명: `text-sm leading-snug line-clamp-2 break-keep`
- 가격: `text-base md:text-lg font-bold tabular-nums`
- 할인율: `text-base font-extrabold text-sale tabular-nums`
- 라벨: `text-xs font-semibold`

금지: Inter, font-thin/extralight (한국어 가독성).

## 4. Component Stylings

### 상품 카드 (정보 밀도)
- **Default**: `bg-white border border-zinc-100 rounded-md overflow-hidden` (얇은 보더)
- 이미지 정사각 + 하단 정보 영역
- 라벨 영역: 로켓배송·할인·와우 다중 배지
- **Hover**: `border-zinc-300`
- **Focus**: `ring-2 ring-rocket`
- **Active**: scale 0.98
- **Disabled** (품절): opacity 60% + "일시품절" 오버레이
- **Loading**: skeleton

### 로켓배송 배지 (시그니처)
- `inline-flex bg-rocket text-white text-xs font-bold px-2 py-0.5 rounded` ("🚀" 아이콘 + "로켓배송")
- Inline 텍스트와 함께 등장

### Primary CTA (담기·바로구매)
- **Default**: `w-full h-12 rounded-md bg-accent text-white font-bold`
- **Hover**: bg-accent 명도 -5% (절제)
- **Focus**: `ring-2 ring-accent ring-offset-2`
- **Active**: scale 0.99
- **Disabled**: bg-zinc-300 opacity-60
- **Loading**: spinner inline + "담는 중..." 카피

## 5. Layout Principles

- **Top Bar 56px**: 검색창 중심 + 카테고리 탭
- **Hero Banner**: 가로 카로셀 + 자동 스크롤
- **상품 그리드**: `grid-cols-2 md:grid-cols-4 lg:grid-cols-5 gap-2` (정보 밀도)
- **모바일**: grid-cols-2 + Bottom Tab
- min-h-[100dvh] 강제

## 6. Depth & Elevation

- 카드 그림자 거의 없음 — 얇은 border만
- 배지: 그림자 없음
- 모달: backdrop-blur + shadow-md
- z-index: nav=40, modal=50

## 7. Motion & Interaction

- 200ms cubic-bezier (빠른 인터랙션)
- 카드 tap: scale 0.98 (즉각 피드백)
- 카로셀 자동 스크롤 (사용자 제어 가능)
- 가격 변동 카운트업 (할인 강조)
- Reduced-motion 의무

## 8. Responsive Behavior

- 모바일·데스크톱 모두 정통 (모바일 비중 80%+)
- 모바일: grid-cols-2 + Bottom Tab + 가로 스크롤 카로셀
- 터치 타겟 ≥ 44px
- 한국어 break-keep + max-w-[60ch]

## 9. Anti-Patterns (Project-Specific Banned)

- ❌ 광고 명령형 카피 ("지금 사세요!") — 정보 우선 ("로켓배송으로 빠르게")
- ❌ 차분·미니멀 톤 (쿠팡은 정보 밀도·긴급감)
- ❌ 다크모드 강제 (라이트 우선)
- ❌ Stock photo 상품 (실제 상품 사진 우선)
- ❌ 가짜 평점·리뷰 fabricated metrics — 실제 데이터만

(글로벌 안티-슬롭 50개는 `references/ai-tells-blocklist.md` 자동 적용)
