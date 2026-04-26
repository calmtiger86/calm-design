# Design System: Inspired by Airbnb

> Source: calm-design 자체 작성 — "Inspired by" 정책. airbnb.com 공개 인터페이스 관찰 기반.
> LANGUAGE: en

## 1. Visual Theme & Atmosphere

여행 마켓플레이스 톤. 따뜻한 코랄 액센트 + 큰 사진 카드 + 둥근 UI. 사진이 콘텐츠 — 숙소·체험 사진이 시각 위계 담당. 친근하고 신뢰감 있는 톤.

## 2. Color Palette & Roles

| Canvas | `#FFFFFF` | 페이지 배경 |
| Surface Soft | `#F7F7F7` | 카드·섹션 |
| Ink | `#222222` | 본문 |
| Mute | `#717171` | 보조 |
| Border | `#DDDDDD` | 분할 |
| Accent | `#FF385C` | Airbnb Coral 톤 (CTA·활성·강조) |
| Accent Hover | `#E31C5F` | Hover 시 진한 코랄 |
| Star | `#FFB400` | 평점 별 |

규칙: 코랄은 강조에만, 사진이 색상 풍부함 담당.

## 3. Typography Rules

- Family: Circular (Airbnb 라이선스 — calm-design은 `Inter` 또는 `Geist` fallback)
- 한국어: Pretendard
- 디스플레이: `text-2xl md:text-4xl font-bold tracking-tight`
- 숙소명: `text-base font-semibold line-clamp-2`
- 위치·메타: `text-sm text-mute`
- 가격: `text-base font-semibold tabular-nums`
- 평점: `text-sm font-medium tabular-nums`

## 4. Component Stylings

### 숙소 카드 (시그니처)
- **Default**: `aspect-square` 이미지 (둥근 `rounded-xl`) + 하단 정보
- 이미지 carousel 인라인 (점 indicator)
- 하트(찜) 우측 상단 부유
- **Hover**: 이미지 scale 1.02 (절제)
- **Focus**: ring-2 ring-accent
- **Active**: scale 0.99
- **Disabled** (예약마감): opacity 60%
- **Loading**: skeleton (정사각 + 라인 3)

### Hero Search (시그니처)
- **Default**: 큰 가로 검색 박스 (위치·체크인·체크아웃·게스트 4 슬롯)
- 둥근 모서리 `rounded-full` (시그니처)
- 모바일: 풀스크린 시트로 전환

### Primary CTA
- **Default**: `h-12 px-6 rounded-md bg-gradient-to-r from-accent to-accent-hover text-white font-semibold`
- **Hover**: 그래디언트 강도 +10% (Airbnb는 동일 색조 그래디언트 — LILA BAN 회피)
- **Focus**: ring-2 ring-accent
- **Active**: scale 0.98
- **Disabled/Loading**: 표준 6상태

### Filter Chip
- 가로 스크롤 카테고리 (전체·해변·산·도시 등)
- **Default**: `rounded-full px-4 py-2 border border-zinc-300`
- **Active**: `bg-ink text-canvas`

## 5. Layout Principles

- **Top Bar 80px** sticky + Hero Search bar
- **카드 그리드**: `grid-cols-1 md:grid-cols-3 lg:grid-cols-4 gap-6` (큰 사진)
- **카테고리 필터**: 가로 스크롤
- min-h-[100dvh]
- 모바일: 단일 컬럼 + 하단 검색 시트

## 6. Depth & Elevation

- 카드 그림자 거의 없음 — 큰 이미지가 시각 위계
- 검색 박스: `shadow-md` (떠 있는 인상)
- Modal: shadow-lg + backdrop-blur

## 7. Motion & Interaction

- 200-300ms cubic-bezier
- 이미지 carousel: smooth swipe + fade
- 하트 클릭: bouncy spring (감정적)
- Modal 등장: scale + fade
- Reduced-motion 의무

## 8. Responsive Behavior

- 모바일·태블릿·데스크톱 모두 정통
- 모바일: 단일 컬럼 + 하단 검색 시트 + Bottom Tab
- 터치 타겟 ≥ 44px
- Airbnb 시그니처 둥근 UI (`rounded-xl`+) 모든 화면 유지

## 9. Anti-Patterns (Project-Specific Banned)

- ❌ 차가운 톤 (Airbnb는 따뜻·환영)
- ❌ 작은 사진 (큰 이미지가 시그니처)
- ❌ 광고적 카피 ("최저가!") — 사실 ("₩89,000/박부터")
- ❌ Stock photo 숙소 (실제 호스트 사진 우선)
- ❌ LILA BAN 그래디언트 (Airbnb는 동일 코랄 색조 그래디언트만)
