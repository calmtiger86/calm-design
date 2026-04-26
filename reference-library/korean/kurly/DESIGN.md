# Design System: Inspired by 컬리 (Kurly)

> Source: calm-design 자체 작성 — "Inspired by" 정책. kurly.com 공개 인터페이스 관찰 기반.
> LANGUAGE: ko

## 1. Visual Theme & Atmosphere

프리미엄 식품 이커머스. 컬리 보라색 시그니처(차분한 톤). 신선·고급·정성을 담은 톤. 새벽배송 시그니처 + 큐레이션·에디토리얼 콘텐츠. 식품 사진이 풍부한 이미지 카드 중심.

## 2. Color Palette & Roles

| Canvas | `#FFFFFF` | 페이지 배경 |
| Surface Soft | `#FAFAFA` | 카드 |
| Ink | `#222222` | 본문 |
| Mute | `#999999` | 보조 |
| Border | `#EEEEEE` | 분할 |
| Accent | `#5F0080` | 컬리 보라 톤 (Primary CTA, 강조, 새벽배송 표시) |
| Accent Soft | `#F5E9F8` | 액센트 배경 |
| Sale | `#FA622F` | 세일·할인 |

규칙: 보라는 강조에만. 식품 사진이 색상 풍부함 담당.

## 3. Typography Rules

- Family: `'Pretendard Variable', Pretendard, system-ui, sans-serif`
- 헤드라인: `text-2xl md:text-3xl font-bold tracking-tight word-break:keep-all`
- 상품명: `text-sm font-medium leading-relaxed break-keep`
- 가격: `text-base font-bold tabular-nums` (천 단위 콤마)
- 새벽배송 라벨: `text-xs font-semibold text-accent`
- 신선도: `text-xs font-medium`

금지: Inter, font-thin/extralight (한국어 가독성).

## 4. Component Stylings

### 상품 카드 (식품)
- **Default**: `bg-white rounded-lg overflow-hidden` + 사진(`aspect-square`) + 하단 정보
- **Hover**: scale 1.01 (절제) + border-zinc-300
- **Focus**: ring-2 ring-accent
- **Active**: scale 0.99
- **Disabled**: opacity 60% + "품절" 라벨
- **Loading**: skeleton (정사각 + 라인 2개)

### Primary CTA (장바구니 담기)
- **Default**: `w-full h-12 rounded-md bg-accent text-white font-bold`
- **Hover**: bg-accent 명도 -10%
- **Focus**: ring-2 ring-accent ring-offset-2
- **Active**: scale 0.99
- **Disabled**: opacity 60% bg-zinc-300
- **Loading**: spinner inline + 텍스트 "담는 중..."

### 새벽배송 배지
- `inline-flex bg-accent-soft text-accent text-xs font-semibold px-2 py-1 rounded-md`
- 시그니처 강조

## 5. Layout Principles

- **Hero Banner** (큐레이션·신상품) 큰 가로 카로셀
- **카테고리 그리드**: 6-column 작은 아이콘 + 라벨
- **상품 그리드**: `grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4`
- **에디토리얼 섹션**: 큐레이션 콘텐츠 (큰 이미지 + 짧은 카피)
- min-h-[100dvh]
- **모바일**: 카로셀 + grid-cols-2

## 6. Depth & Elevation

- 카드 그림자 없음 — 미세한 border와 명도로
- Hero Banner: 그림자 거의 없음, 큰 이미지만
- 모달: backdrop-blur + shadow-lg
- z-index: nav=40, modal=50

## 7. Motion & Interaction

- 200-300ms cubic-bezier
- Hover scale 1.01 (절제 — 프리미엄 톤)
- 카로셀 자동 스크롤 (선택, 모바일에선 사용자 제어)
- 카드 stagger 30ms cascade
- Reduced-motion 의무

## 8. Responsive Behavior

- 데스크톱·모바일 정통
- 모바일: 카로셀 swipe, grid-cols-2
- 터치 타겟 ≥ 44px
- 한국어 상품명 + 설명 break-keep + max-w-[65ch]

## 9. Anti-Patterns (Project-Specific Banned)

- ❌ "지금 가입하세요!" 광고 톤 (컬리는 큐레이션·에디토리얼 톤)
- ❌ 채도 100% 색상 (보라 시그니처와 충돌)
- ❌ Hero 영상 자동재생 음성 ON
- ❌ Stock photo 식품 (실제 큐레이션 사진 우선)
- ❌ 가짜 신선도·평점 fabricated

(글로벌 안티-슬롭 50개는 `references/ai-tells-blocklist.md` 자동 적용)
