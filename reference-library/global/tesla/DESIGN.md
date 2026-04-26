# Design System: Inspired by Tesla

> Source: calm-design 자체 작성 — "Inspired by" 정책. tesla.com 공개 인터페이스 관찰 기반.
> LANGUAGE: en

## 1. Visual Theme & Atmosphere

미래적 미니멀리즘. 흑백 모노크롬 + 풀-블리드 자동차 사진. 거대한 헤드라인 + 짧은 카피. 대시보드·앱 UI에선 다크모드 우선. "기술이 아닌 경험"을 강조하는 톤.

## 2. Color Palette & Roles

| Canvas | `#FFFFFF` (라이트) / `#000000` (다크 — Tesla 정체성) | 페이지 |
| Surface | `#F4F4F4` (라이트) / `#171717` (다크) | 카드 |
| Ink | `#171A20` (라이트) / `#FFFFFF` (다크) | 본문 |
| Mute | `#5C5E62` | 보조 |
| Border | `#E1E1E1` (라이트) / `#3E3E3E` (다크) | 분할 |
| Accent | `#CC0000` | Tesla Red (CTA, 활성) — 절제 사용 |

규칙: 흑백이 정체성, 빨간색은 강조에만 (CTA·경고).

## 3. Typography Rules

- Family: Gotham 또는 Tesla 자체 폰트 (라이선스 — calm-design은 Geist + Pretendard fallback)
- 한국어: Pretendard
- 디스플레이: `text-5xl md:text-7xl tracking-tight font-medium` (거대 헤드라인)
- 본문: `text-lg leading-relaxed`
- 짧은 카피 + 큰 여백

## 4. Component Stylings

### Hero Section
- **Default**: 풀-블리드 자동차 사진 + 하단 중앙 헤드라인 + 우측 하단 CTA
- 모든 인터랙션: 표준 6상태

### Primary CTA (Order Now)
- **Default**: `rounded-md px-8 py-3 bg-ink text-canvas text-sm font-medium uppercase tracking-wide`
- **Hover**: `bg-mute`
- **Focus/Active/Disabled/Loading**: 표준 6상태

## 5. Layout Principles

- **풀-블리드 미디어** 시그니처
- 큰 섹션 패딩 `py-32+`
- Centered hero (Tesla 정체성)
- min-h-[100dvh]

## 6. Depth & Elevation

- 그림자 거의 없음 (Tesla 미니멀 정체성)
- 다크 모드에서 명도 변화로 위계 표현
- 모달·시트: backdrop-blur로 분리감, 그림자는 매우 미세
- z-index: nav=40, modal=50 (절제)

## 7. Motion & Interaction

- 300-500ms cubic-bezier (부드러운 톤)
- 자동차 사진 미세 zoom-in/parallax
- 페이지 전환 fade + 미세 translate
- Reduced-motion 의무

## 8. Responsive Behavior

- 풀-블리드는 모바일·데스크톱 모두 유지 (Tesla 정체성)
- 모바일에서도 큰 헤드라인 유지 (`text-5xl` 모바일 기준)
- 한국어 환경: Pretendard fallback + word-break: keep-all
- 터치 타겟 ≥ 44px, CTA는 항상 화면 하단 고정 가능

## 9. Anti-Patterns (Project-Specific Banned)

- ❌ 다중 액센트 컬러 (Tesla Red 단일)
- ❌ 작은 헤드라인·작은 사진
- ❌ 화려한 그래디언트
- ❌ 대시보드·B2B SaaS 톤 적용 (Tesla는 D2C·소비자 톤)
