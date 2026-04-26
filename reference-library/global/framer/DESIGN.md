# Design System: Inspired by Framer

> Source: calm-design 자체 작성 — "Inspired by" 정책. framer.com 공개 인터페이스 관찰 기반.
> LANGUAGE: en

## 1. Visual Theme & Atmosphere

웹 디자인 + 모션 그래픽 도구. 다크 베이스 + 풍부한 그래디언트(주의: calm-design LILA BAN과 충돌 — 단색 또는 절제된 그래디언트로 보정). Bold 디스플레이 폰트 + 큰 모션·트랜지션. 영화적·인터랙티브.

## 2. Color Palette & Roles

| Canvas | `#0F0F0F` | 다크 배경 (Off-Black) |
| Surface | `#1A1A1A` | 카드 |
| Ink | `#FAFAFA` | 본문 |
| Mute | `#888888` | 보조 |
| Border | `#2E2E2E` | 분할 |
| Accent | `#0099FF` | Framer Blue (CTA, 활성) |
| Highlight | `#FF5C5C` | 강조·실시간 표시 |

라이트 모드: Canvas `#FFFFFF`, Ink `#000000`(Framer 정체성으로 Pure Black 허용), 액센트 동일.

규칙: 그래디언트는 동일 색조 안에서만 (purple→blue 같은 LILA BAN X). 매우 절제.

## 3. Typography Rules

- Family: Inter Display (Framer 자체) — calm-design은 `Geist Display` 또는 `Cabinet Grotesk` fallback
- 한국어: Pretendard
- 디스플레이: `text-5xl md:text-7xl tracking-tight font-bold` (큰 헤드라인 시그니처)
- 본문: `text-base md:text-lg leading-relaxed`

## 4. Component Stylings

### Hero (모션 강조 시그니처)
- **Default**: 풀 너비 + 거대한 헤드라인 + 미세 모션 (scale·rotate·parallax)
- 인터랙티브 데모 임베드 가능

### Canvas Editor
- 다크 워크스페이스 + 인스펙터 우측
- 컴포넌트 drag·resize 풍부한 모션

### Primary CTA
- **Default**: `h-12 px-6 rounded-md bg-accent text-canvas font-medium`
- **Hover**: scale 1.02 (Framer는 Hover 모션이 시그니처)
- **Active/Focus/Disabled/Loading**: 표준 6상태

## 5. Layout Principles

- **풀-블리드 hero** (Framer 정체성)
- **인터랙티브 데모** 임베드 (실시간 모션)
- 큰 섹션 패딩 `py-32+`
- min-h-[100dvh]

## 6. Depth & Elevation

- 다크 모드에서 그래디언트·glow로 깊이 (단, LILA BAN 회피 — 동일 색조만)
- 카드: shadow + 미세 border
- Modal: shadow-xl + backdrop-blur

## 7. Motion & Interaction

- **모션 시그니처** — 모든 인터랙션에 풍부한 트랜지션
- 300-500ms cubic-bezier (영화적)
- Hover scale·rotate·gradient shift
- Scroll trigger 풍부 (parallax·counter·stagger)
- Reduced-motion 의무 (전정 장애 보호)

## 8. Responsive Behavior

- 데스크톱·태블릿·모바일 모두 정통 (Framer는 반응형 도구)
- 모바일에서도 모션 유지 (전력 효율 고려)

## 9. Anti-Patterns (Project-Specific Banned)

- ❌ 정적 디자인 (Framer는 모션이 시그니처)
- ❌ 라이트 강제 (다크 우선)
- ❌ Linear 같은 절제 모션 (Framer는 풍부)
- ❌ LILA BAN 그래디언트 (단색 또는 동일 색조 그래디언트만)
