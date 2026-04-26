# Design System: Inspired by 오늘의집 (Ohou)

> Source: calm-design 자체 작성 — "Inspired by" 정책. ohou.se 공개 인터페이스 관찰 기반.
> LANGUAGE: ko

## 1. Visual Theme & Atmosphere

홈리빙 큐레이션 + 인스피레이션. 따뜻한 베이지·우드 톤. 사용자 집사진(랜선집들이) 중심 + 큐레이션 상품. 인스타그램 같은 사진 그리드 + 콘텐츠 큐레이션. 친근하고 따뜻한 한국어 카피("우리집을 더 예쁘게").

## 2. Color Palette & Roles

| Canvas | `#FFFFFF` | 페이지 배경 |
| Surface Soft | `#F8F6F3` | 카드 (베이지 톤) |
| Ink | `#262626` | 본문 |
| Mute | `#999999` | 보조 |
| Border | `#F0EDE8` | 분할 (베이지 보더) |
| Accent | `#35C5F0` | 오늘의집 청록 톤 (Primary CTA, 활성, 링크) |
| Accent Soft | `#E5F6FB` | 액센트 배경 |
| Wood | `#A88B65` | 우드 강조 (카테고리·태그) |

규칙: 베이지·우드가 베이스 톤, 청록은 강조에만.

## 3. Typography Rules

- Family: `'Pretendard Variable', Pretendard, system-ui, sans-serif`
- 헤드라인: `text-2xl md:text-3xl font-bold tracking-tight word-break:keep-all`
- 콘텐츠 제목 (랜선집들이): `text-base font-semibold line-clamp-2 break-keep`
- 작성자 (집주인): `text-sm font-medium`
- 좋아요·댓글 수: `text-xs text-mute tabular-nums`
- 가격: `text-base font-bold tabular-nums`

금지: Inter, font-thin/extralight.

## 4. Component Stylings

### 콘텐츠 카드 (랜선집들이)
- **Default**: `bg-white rounded-lg overflow-hidden`
- 큰 정사각 이미지 (`aspect-square`) + 하단 작성자 + 좋아요 + 댓글
- **Hover**: scale 1.01 (이미지 강조)
- **Focus**: ring-2 ring-accent
- **Active**: scale 0.99 (탭 피드백)
- **Disabled**: opacity 60%
- **Loading**: skeleton (정사각 + 라인 2)

### 상품 카드 (스토어)
- **Default**: 정사각 이미지 + 가격
- **Hover**: scale 1.01 + border-zinc-200
- **Focus/Active/Disabled/Loading**: 표준 6상태

### Primary CTA
- **Default**: `w-full h-12 rounded-lg bg-accent text-white font-bold`
- **Hover**: scale 1.01
- **Focus**: ring-2 ring-accent ring-offset-2
- **Active**: scale 0.99
- **Disabled**: bg-zinc-300 opacity-60
- **Loading**: spinner inline

### 좋아요 버튼 (heart)
- 클릭 시 bouncy spring (stiffness 400, damping 15) + 색상 변화
- 좋아요 수 카운트업

## 5. Layout Principles

- **Hero**: 큐레이션 영감 (랜선집들이 추천)
- **콘텐츠 그리드**: `grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-3` (정사각 이미지)
- **카테고리**: 가로 스크롤 큰 아이콘 (예: 거실·침실·주방·욕실)
- **무한 스크롤** (피드 시그니처)
- min-h-[100dvh] 강제
- **모바일 우선** (`max-w-md mx-auto`에선 grid-cols-2)

## 6. Depth & Elevation

- 카드 그림자 없음 — `border-zinc-100` 또는 베이지 톤
- 좋아요 버튼: 그림자 없음
- 모달: backdrop-blur + shadow-md
- z-index: nav=40, modal=50

## 7. Motion & Interaction

- 200-300ms cubic-bezier
- 좋아요 bouncy spring (감정적 인터랙션)
- 카드 등장 stagger 30ms
- 무한 스크롤 시 skeleton placeholder
- Reduced-motion 의무

## 8. Responsive Behavior

- 모바일 우선 (인스피레이션 피드는 모바일 비중 큼)
- 모바일: grid-cols-2 + Bottom Tab
- 터치 타겟 ≥ 44px
- 한국어 콘텐츠 제목 break-keep + max-w-[65ch]

## 9. Anti-Patterns (Project-Specific Banned)

- ❌ 차가운 톤 (오늘의집은 따뜻·라이프스타일)
- ❌ 광고적 카피 — 친근 한국어 ("우리집을 더 예쁘게", "이번 주 인기 집들이")
- ❌ Stock photo 인테리어 (실제 사용자 집 사진 우선)
- ❌ 다크모드 강제 (베이지 라이트 정체성)
- ❌ 가짜 좋아요 수·댓글 fabricated metrics

(글로벌 안티-슬롭 50개는 `references/ai-tells-blocklist.md` 자동 적용)
