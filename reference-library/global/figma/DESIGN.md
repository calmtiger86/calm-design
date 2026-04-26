# Design System: Inspired by Figma

> Source: calm-design 자체 작성 — "Inspired by" 정책. figma.com 공개 인터페이스 관찰 기반.
> LANGUAGE: en

## 1. Visual Theme & Atmosphere

협업 디자인 도구. 다중 컬러 액센트 시그니처(블루·핑크·그린·옐로우·보라·오렌지) — 디자인 도구가 컬러풀해야 디자이너가 친근감. 흰색 베이스 + 다양한 컬러 dots·icons. 친근하고 전문적.

## 2. Color Palette & Roles

| Canvas | `#FFFFFF` | 페이지 배경 |
| Surface Soft | `#F5F5F5` | 카드 |
| Ink | `#0D0D0D` | 본문 (Off-Black) |
| Mute | `#787878` | 보조 |
| Border | `#E5E5E5` | 분할 |
| Accent (multi) | — | Figma 시그니처 다중 (아래) |
| - Blue | `#0D99FF` | 정보·링크 |
| - Pink | `#FF24BD` | 디자인 강조 |
| - Green | `#0FA958` | 성공·승인 |
| - Yellow | `#FFCD29` | 주의 |
| - Purple | `#9747FF` | 컴포넌트·variants |
| - Orange | `#F24E1E` | 활동 |

규칙: 다중 액센트는 Figma 정체성. 일반 calm-design 출력에 적용 시 1-2개로 축소 권장 (단, "Figma 풍" 명시 시 다중 허용).

## 3. Typography Rules

- Family: Inter (Figma 자체 — calm-design은 `Geist` 또는 시스템 fallback)
- 한국어: Pretendard
- 디스플레이: `text-2xl md:text-4xl font-bold tracking-tight`
- 본문: `text-base leading-relaxed`
- 라벨: `text-xs font-medium`

## 4. Component Stylings

### Toolbar (시그니처)
- **Default**: 상단 또는 좌측 fixed, 컴팩트 아이콘 + 다중 컬러 인디케이터
- 6상태 표준

### Color Swatches
- 작은 정사각 (`w-8 h-8`) + border + 클릭 시 picker
- 컬러 hex 표시

### File Card
- **Default**: `bg-white rounded-lg border border-zinc-200 overflow-hidden`
- 큰 thumbnail (4:3) + 파일명 + 협업자 아바타 stack
- **Hover**: scale 1.01 + border-zinc-300
- **6상태 표준**

### Primary CTA
- **Default**: `h-10 px-4 rounded-md bg-blue-500 text-white font-medium`
- **Hover/Focus/Active/Disabled/Loading**: 표준 6상태

## 5. Layout Principles

- **Toolbar fixed** (좌·상단)
- **Canvas flex-1** (중앙)
- **Inspector 우측** (240px, 컴포넌트·스타일 패널)
- min-h-[100dvh]
- 모바일: 거의 미지원 (Figma 정체성은 데스크톱)

## 6. Depth & Elevation

- 카드 미세 그림자 — `shadow-sm`
- Modal: `shadow-lg` + backdrop-blur
- 컴포넌트 dragging: scale 1.02 + shadow-md

## 7. Motion & Interaction

- 150-200ms ease-out (즉각 반응 — 디자인 도구는 빨라야)
- Drag·resize·zoom 부드러움
- 협업 커서: spring (실시간 위치)
- Reduced-motion 의무

## 8. Responsive Behavior

- 데스크톱 우선 (Figma 정체성)
- 태블릿: Inspector collapsible
- 모바일: 뷰어만 (편집 불가)

## 9. Anti-Patterns (Project-Specific Banned)

- ❌ 단일 액센트 강제 (Figma는 다중 컬러 정체성)
- ❌ 차분 톤 (Figma는 친근·활기)
- ❌ 큰 hero 일러스트 (Figma는 도구 화면이 hero)
- ❌ 모바일 최적화 강제
