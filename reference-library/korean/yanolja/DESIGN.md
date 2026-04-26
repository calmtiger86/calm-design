# Design System: Inspired by 야놀자 (Yanolja)

> Source: calm-design 자체 작성 — "Inspired by" 정책. yanolja.com 공개 인터페이스 관찰 기반.
> LANGUAGE: ko

## 1. Visual Theme & Atmosphere

여행·숙박 슈퍼앱. 친근한 핑크 액센트 + 큰 숙소 사진 카드. 평점·리뷰·할인 정보 밀도 높음. 호텔·펜션·게스트하우스·해외여행까지 통합. "여행 가고 싶다"는 감성을 자극하는 큰 이미지 우선.

## 2. Color Palette & Roles

| Canvas | `#FFFFFF` | 페이지 배경 |
| Surface Soft | `#F8F8F8` | 카드 |
| Ink | `#212121` | 본문 |
| Mute | `#9E9E9E` | 보조 |
| Border | `#EEEEEE` | 분할 |
| Accent | `#FF7B6E` | 야놀자 핑크 톤 (Primary CTA, 활성, 할인) |
| Accent Soft | `#FFEDEB` | 액센트 배경 |
| Rating | `#FFB800` | 평점 별 |

## 3. Typography Rules

- Family: `'Pretendard Variable', Pretendard, system-ui, sans-serif`
- 헤드라인: `text-2xl md:text-3xl font-bold tracking-tight word-break:keep-all`
- 숙소명: `text-base font-semibold line-clamp-2 break-keep`
- 가격: `text-lg font-bold tabular-nums` (1박 단위)
- 평점: `text-sm font-semibold tabular-nums` (별 + 4.5)
- 리뷰 수: `text-xs text-mute tabular-nums` (괄호 안)

금지: Inter, font-thin/extralight.

## 4. Component Stylings

### 숙소 카드
- **Default**: `bg-white rounded-xl overflow-hidden`
- 큰 이미지 (`aspect-[4/3]`) + 정보 영역
- 평점·리뷰·위치 한 줄 + 가격 강조
- **Hover**: scale 1.01 (절제) + border-zinc-300
- **Focus**: ring-2 ring-accent
- **Active**: scale 0.99
- **Disabled** (만실): opacity 60% + "예약 마감" 라벨
- **Loading**: skeleton (4:3 + 라인 3개)

### Hero Search
- 큰 검색 박스 (가로 카드) — 위치·체크인·체크아웃·인원 4 슬롯
- 모바일에선 풀스크린 시트로 전환

### Primary CTA (예약하기)
- **Default**: `w-full h-12 rounded-xl bg-accent text-white font-bold`
- **Hover**: scale 1.01, bg 명도 -5%
- **Focus**: ring-2 ring-accent ring-offset-2
- **Active**: scale 0.99
- **Disabled**: bg-zinc-300 opacity-60
- **Loading**: spinner inline + "예약 처리 중..." 카피

## 5. Layout Principles

- **Top Bar 56px**: 검색·필터·카테고리
- **Hero Banner**: 가로 카로셀 (특가·이벤트)
- **숙소 그리드**: `grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4`
- **카테고리 탭**: 가로 스크롤 (호텔·펜션·해외 등)
- min-h-[100dvh] 강제
- **모바일**: 단일 컬럼 + Bottom Tab

## 6. Depth & Elevation

- 카드 미세한 그림자 — `shadow-[0_2px_8px_rgba(0,0,0,0.04)]`
- 큰 이미지가 깊이 표현 담당
- 모달·시트: backdrop-blur + shadow-lg
- z-index: nav=40, modal=50

## 7. Motion & Interaction

- 200-300ms cubic-bezier
- 카드 hover scale 1.01 (이미지 강조 절제)
- 카로셀 자동 스크롤 (사용자 제어)
- Heart 즐겨찾기 애니메이션 (bouncy)
- Reduced-motion 의무

## 8. Responsive Behavior

- 모바일 우선 (여행 검색은 모바일 비중 큼)
- 모바일: 단일 컬럼 카드 + Bottom Tab
- 터치 타겟 ≥ 44px
- 한국어 숙소명·설명 break-keep + max-w-[65ch]

## 9. Anti-Patterns (Project-Specific Banned)

- ❌ 차가운 톤 (야놀자는 따뜻·친근 여행 톤)
- ❌ 정보 부족 카드 (가격·평점·위치 명시 의무)
- ❌ 광고적 카피 ("최저가 보장!") — 사실 기반 ("최저가 ₩59,000")
- ❌ Stock photo 호텔 (실제 숙소 사진 우선)
- ❌ 가짜 평점·리뷰 수 fabricated metrics

(글로벌 안티-슬롭 50개는 `references/ai-tells-blocklist.md` 자동 적용)
