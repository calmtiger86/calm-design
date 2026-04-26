# Design System: Inspired by 스타벅스코리아 (Starbucks Korea)

> Source: calm-design 자체 작성 — "Inspired by" 정책. starbucks.co.kr·스타벅스 앱 관찰 기반.
> LANGUAGE: ko

## 1. Visual Theme & Atmosphere

스타벅스 그린 시그니처 + 한국 현지화. 사이렌오더 시그니처 워크플로우. 따뜻한 라이프스타일 톤 + 카페·매장 사진. 글로벌 스타벅스 톤 위에 한국 사용자 친화 레이어 (Pretendard·한국어 카피·매장 위치 한국 우선). 별·리워드 시스템 시그니처.

## 2. Color Palette & Roles

| Canvas | `#FFFFFF` | 페이지 배경 |
| Surface Soft | `#F9F9F9` | 카드 |
| Ink | `#1E1E1E` | 본문 |
| Mute | `#888888` | 보조 |
| Border | `#EEEEEE` | 분할 |
| Accent | `#006241` | 스타벅스 그린 톤 (Primary CTA, 활성, 별·리워드) |
| Accent Soft | `#E8F0EE` | 액센트 배경 |
| Gold | `#CBA258` | 골드 멤버십 |
| Star | `#CC0033` | 별 색상 (스타벅스 시그니처) |

## 3. Typography Rules

- Family: `'Pretendard Variable', Pretendard, system-ui, sans-serif` (한국 환경)
- 글로벌 SoDo Sans는 라이선스로 미사용 — Pretendard fallback
- 헤드라인: `text-2xl md:text-3xl font-bold tracking-tight word-break:keep-all`
- 메뉴명 (한국어): `text-base font-semibold break-keep`
- 메뉴명 (영어 보조): `text-xs text-mute uppercase tracking-wide`
- 가격: `text-base font-bold tabular-nums`
- 별 카운트: `text-3xl font-bold tabular-nums` (시그니처 강조)

금지: Inter, font-thin/extralight.

## 4. Component Stylings

### 메뉴 카드
- **Default**: `bg-white rounded-lg overflow-hidden` + 정사각 메뉴 사진
- 메뉴명 한·영 병기 + 가격
- **Hover**: scale 1.01 + border-zinc-300
- **Focus**: ring-2 ring-accent
- **Active**: scale 0.99
- **Disabled** (품절): opacity 60% + "품절" 라벨
- **Loading**: skeleton (정사각 + 라인 2개)

### 사이렌오더 카드 (시그니처 워크플로우)
- 큰 카드 + 매장 선택 + 메뉴 + 결제
- 4단계 stepper: 매장 → 메뉴 → 결제 → 완료
- Primary CTA 시그니처 그린

### 별·리워드 디스플레이
- 큰 별 카운트 + 다음 등급까지 progress bar
- **시각 위계**: `text-3xl font-bold` 별 수, 작은 메타

### Primary CTA (주문하기)
- **Default**: `w-full h-12 rounded-full bg-accent text-white font-bold` (스타벅스 라운드)
- **Hover**: scale 1.01, bg 명도 -5%
- **Focus**: ring-2 ring-accent ring-offset-2
- **Active**: scale 0.99
- **Disabled**: bg-zinc-300 opacity-60
- **Loading**: spinner inline + "주문 처리 중..." 카피

## 5. Layout Principles

- **Hero**: 매장·시즌 메뉴 큐레이션 (큰 이미지)
- **카테고리 탭**: 가로 스크롤 (음료·푸드·MD)
- **메뉴 그리드**: `grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4`
- **사이렌오더**: 단일 풀-스크린 흐름 (모바일 우선)
- min-h-[100dvh] 강제
- **모바일 우선** + Bottom Tab (홈·오더·페이·기프트·MY)

## 6. Depth & Elevation

- 카드 미세 그림자 — `shadow-[0_2px_8px_rgba(0,0,0,0.04)]`
- Hero Banner: 큰 이미지 (그림자 X)
- 모달·시트: backdrop-blur + shadow-lg
- z-index: nav=40, modal=50

## 7. Motion & Interaction

- 300ms cubic-bezier (스타벅스 부드러운 톤)
- 별 적립: bouncy spring (감정적 강조)
- 사이렌오더 stepper: smooth slide
- 카드 hover scale 1.01
- Reduced-motion 의무

## 8. Responsive Behavior

- 모바일 우선 (앱 비중 큼) — `max-w-md mx-auto`
- 데스크톱은 grid 확장
- 터치 타겟 ≥ 44px
- 한국어 메뉴명 break-keep + 영어 병기 라벨

## 9. Anti-Patterns (Project-Specific Banned)

- ❌ 차가운 톤·다크모드 강제 (스타벅스는 따뜻·라이프스타일)
- ❌ 광고적 카피 ("지금 사세요") — 친근 ("오늘의 추천")
- ❌ Stock photo 음료·매장 (실제 스타벅스 메뉴 사진 우선)
- ❌ Sodo Sans 폰트 강제 (라이선스 — Pretendard fallback)
- ❌ 영어 위주 메뉴명 (한·영 병기, 한국어 우선)

(글로벌 안티-슬롭 50개는 `references/ai-tells-blocklist.md` 자동 적용)
