# Design System: Inspired by Apple

> Source: calm-design 자체 작성 — "Inspired by" 정책. apple.com 공개 인터페이스 관찰 기반.
> LANGUAGE: en

## 1. Visual Theme & Atmosphere

프리미엄 미니멀리즘의 정수. 화이트스페이스 마스터, 풀-블리드 사진, 거대한 헤드라인. SF Pro Display 시그니처 폰트(calm-design은 라이선스로 system-ui + Pretendard fallback). "제품이 주인공, UI는 사라진다." 큰 hero + 곡선 카드 + 미세한 그림자.

## 2. Color Palette & Roles

| Canvas | `#FFFFFF` | 페이지 배경 |
| Surface Soft | `#F5F5F7` | 카드·섹션 (Apple 시그니처 라이트 그레이) |
| Ink | `#1D1D1F` | 본문 (Pure Black 회피, 미세 따뜻) |
| Mute | `#86868B` | 보조 |
| Border | `#D2D2D7` | 분할 (라이트 모드만) |
| Accent | `#0066CC` | Apple Blue (CTA, 링크) |

다크 모드: Canvas `#000000` (Apple 정체성 — Pure Black 허용), Surface `#1D1D1F`, Ink `#F5F5F7`.

## 3. Typography Rules

- Family: SF Pro Display·SF Pro Text (라이선스 — calm-design은 `system-ui` fallback)
- 한국어: `Pretendard Variable` 강제
- 디스플레이: `text-6xl md:text-7xl lg:text-8xl tracking-tight font-semibold` (거대한 헤드라인)
- 본문: `text-xl md:text-2xl leading-snug`
- "큰 제목 + 큰 본문" 시그니처

## 4. Component Stylings

### Hero Section
- **Default**: 풀-너비 + 거대한 헤드라인 가운데 정렬 + 큰 제품 사진
- Background: Canvas 또는 Surface Soft

### Product Card
- **Default**: `bg-surface-soft rounded-3xl p-12` (큰 라운드, 큰 패딩)
- **Hover**: 미세 scale 1.01 (절제)
- **Focus**: `ring-2 ring-accent`
- **Active**: scale 0.99
- **Disabled**: opacity 50%
- **Loading**: skeleton

### CTA Button
- **Default**: `rounded-full px-6 py-3 bg-accent text-white text-sm font-medium`
- **Hover**: bg 명도 -10%
- **Focus**: ring-2
- **Active**: scale 0.99
- **Disabled**: opacity 50%
- **Loading**: spinner inline
- 모든 transition 300ms cubic-bezier (Apple 부드러움)

## 5. Layout Principles

- **Centered hero** — Apple 시그니처 (calm-design VARIANCE 다이얼 무시하고 centered 허용 시)
- **Generous whitespace** — 섹션 패딩 `py-32 md:py-40`
- **Full-bleed media** — 큰 이미지·비디오가 콘텐츠
- max-w-7xl mx-auto + 의도적 여백
- min-h-[100dvh]

## 6. Depth & Elevation

- 매우 미세한 그림자 — `shadow-[0_4px_30px_rgba(0,0,0,0.06)]`
- 카드 둥근 모서리 큼 (`rounded-3xl`)
- 다크 모드에서 그림자 대신 명도 변화

## 7. Motion & Interaction

- 300-500ms cubic-bezier (부드러운 톤)
- Hover scale 1.01 (절제)
- Smooth scroll + parallax 가벼움
- Reduced-motion 의무

## 8. Responsive Behavior

- 모바일·태블릿·데스크톱 정통
- 모바일에서도 거대한 헤드라인·여백 유지
- 한국어 환경: Pretendard 강제 + word-break: keep-all

## 9. Anti-Patterns (Project-Specific Banned)

- ❌ 다중 액센트 컬러 (Apple Blue 단일)
- ❌ 작은 헤드라인 (Apple 시그니처는 거대한 헤드라인)
- ❌ 화려한 그래디언트 (제품 사진이 주인공)
- ❌ 한국어 환경에서 SF Pro 강제 (Pretendard fallback 의무)
- ❌ Inter 폰트 (system-ui 또는 Pretendard)
