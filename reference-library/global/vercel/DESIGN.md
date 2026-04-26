# Design System: Inspired by Vercel

> Source: calm-design 자체 작성 — "Inspired by" 정책. vercel.com 공개 인터페이스 관찰 기반.
> LANGUAGE: en

## 1. Visual Theme & Atmosphere

기하학적 흑백 미니멀리즘. Geist 폰트 시그니처. 단일 톤(검정·흰색)으로 정보 위계 표현, 액센트는 거의 없음. 개발자 인프라 도구이나 화려함 대신 정밀함·신뢰. Geist Sans + Geist Mono 페어링.

## 2. Color Palette & Roles

| Canvas | `#000000` 또는 `#FFFFFF` | 다크/라이트 모드 (이때만 Pure Black 허용) |
| Surface | `#0A0A0A` (다크) / `#FAFAFA` (라이트) | 카드 |
| Ink | `#FFFFFF` (다크) / `#000000` (라이트) | 본문 — Vercel 흑백 정체성으로 Pure Black 허용 |
| Mute | `#A1A1A1` | 보조 |
| Border | `#1F1F1F` (다크) / `#EAEAEA` (라이트) | 1px 분할 |
| Accent | (거의 사용 X — 회색 명도로 위계) | — |
| Success | `#0070F3` | 청색 (제한적) |

규칙: Vercel은 Pure Black을 사용하는 예외 (정체성). 단 calm-design 다른 출력에선 Off-Black 유지. Vercel inspired 시만 허용.

## 3. Typography Rules

- Family: **Geist Sans** 시그니처 + **Geist Mono** (숫자·코드)
- 한국어: Pretendard fallback
- 디스플레이: `tracking-tighter leading-none font-semibold`
- 본문: `text-base leading-normal`
- 코드: Geist Mono 강제

## 4. Component Stylings

### Card
- **Default**: `bg-surface border border-border rounded-lg p-6`
- **Hover** (interactive): `border-mute` (미세)
- **Focus**: `ring-1 ring-blue-500`
- **Active**: 동일 focus
- **Disabled**: `opacity-50`
- **Loading**: shimmer skeleton

### Button (Primary)
- Default: `h-10 px-4 rounded-md bg-ink text-canvas text-sm font-medium` (검정 위 흰색 또는 반대)
- Hover: 명도 변화 (95%)
- Active: 명도 변화 (90%)
- 모든 transition 150ms ease-out

## 5. Layout Principles

- **Geometric grid** — 12-column 정렬
- max-w-7xl + 의도적 화이트스페이스
- Top Bar 64px (sticky + backdrop-blur)
- min-h-[100dvh] 강제

## 6. Depth & Elevation

- 그림자 사용 **거의 0** — border와 명도로 깊이
- 다크 모드 우선이지만 라이트도 정통
- z-index 절제 (nav=40만)

## 7. Motion & Interaction

- 150-200ms ease-out (Linear보다 약간 빠름)
- transform 거의 X — 색상·명도만
- Reduced-motion 의무

## 8. Responsive Behavior

- 모바일·태블릿·데스크톱 모두 정통 지원, 모든 화면에서 흑백 정체성 유지
- max-w-7xl 제약 + 의도적 여백 (모바일에서도 generous spacing 유지)
- 한국어 환경: Pretendard fallback + word-break: keep-all
- 터치 타겟 ≥ 44px, Geist Mono 코드 블록은 가로 스크롤 허용

## 9. Anti-Patterns (Project-Specific Banned)

- ❌ 다중 액센트 컬러 (Vercel은 흑백 정체성)
- ❌ 컬러풀한 일러스트·아이콘 (단색 유지)
- ❌ 둥근 corner 과사용 (`rounded-2xl+` X — `rounded-md` 정도)
- ❌ Pretendard·Inter (Geist 강제)
