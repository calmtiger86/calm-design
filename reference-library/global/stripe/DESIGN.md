# Design System: Inspired by Stripe

> Source: calm-design 자체 작성 — "Inspired by" 정책. stripe.com 공개 인터페이스 관찰 기반.
> LANGUAGE: en

## 1. Visual Theme & Atmosphere

핀테크 정제된 우아함. Signature 보라/블루 그래디언트(주의: calm-design LILA BAN과 충돌하므로 **단색**으로 보정해 사용), weight-300 얇은 헤드라인, 충분한 화이트스페이스. 개발자 + 비개발자 양쪽에 친화. Sohne·Söhne 폰트 톤.

## 2. Color Palette & Roles

| Canvas | `#FFFFFF` | 페이지 배경 |
| Surface | `#FAFAFA` | 카드 |
| Ink | `#0A2540` | 본문 (Stripe 다크 블루 톤, Pure Black X) |
| Mute | `#425466` | 보조 |
| Border | `#E3E8EE` | 분할 |
| Accent | `#635BFF` | Stripe Indigo (단색만, 그래디언트 X) |
| Accent Soft | `#EFF1FE` | 액센트 배경 |

**중요**: 원본 Stripe는 `from-purple to-blue` 그래디언트가 시그니처지만, calm-design은 **LILA BAN**으로 차단. Inspired by Stripe는 **Indigo 단색 #635BFF**로 보정.

## 3. Typography Rules

- Family: Söhne 또는 Inter 톤 (calm-design은 Inter 회피 → Geist 권장)
- 한국어: Pretendard fallback
- 디스플레이: `font-light tracking-tight` (weight-300 시그니처)
- 본문: `text-base leading-relaxed`
- 코드: Söhne Mono 또는 JetBrains Mono

## 4. Component Stylings

### Hero Card
- **Default**: `bg-surface rounded-2xl p-12 shadow-[0_4px_20px_rgba(0,0,0,0.04)]`
- **Hover**: 그림자 강도 +20%
- **Focus**: `ring-2 ring-accent ring-offset-2`
- **Active**: 동일
- **Disabled**: opacity 50%
- **Loading**: skeleton

### Button (Primary)
- Default: `h-10 px-5 rounded-md bg-accent text-white text-sm font-medium`
- Hover: `bg-accent` 명도 보정 + 미세 그림자
- Active: scale[0.98]
- 200ms cubic-bezier

## 5. Layout Principles

- **Generous whitespace** — Stripe 시그니처 (큰 섹션 패딩 `py-32+`)
- max-w-6xl 중앙 정렬
- Asymmetric whitespace (좌측 텍스트, 큰 우측 여백)
- min-h-[100dvh]

## 6. Depth & Elevation

- 미세한 그림자 — `shadow-[0_4px_20px_rgba(0,0,0,0.04)]` 시그니처 부드러움
- 카드는 그림자로, sticky는 backdrop-blur로

## 7. Motion & Interaction

- 200-300ms cubic-bezier
- 페이지 전환 시 fade + 미세 translate
- Counter Up 자주 사용 (KPI 강조)
- Reduced-motion 의무

## 8. Responsive Behavior

- 모바일·태블릿·데스크톱 모두 정통 지원
- 모바일에서도 generous spacing 유지 (Stripe 시그니처 호흡감)
- 한국어 환경: Pretendard fallback + word-break: keep-all
- 터치 타겟 ≥ 44px, 인터랙티브 카드 전체 영역 클릭 가능

## 9. Anti-Patterns (Project-Specific Banned)

- ❌ **그라디언트 시그니처 직접 복제** (calm-design LILA BAN — `from-purple to-blue` 절대 X)
  - ✅ 대신: 단색 Indigo `#635BFF`, 또는 매우 절제된 미세 그래디언트 (15도 미만 + 동일 색조 안)
- ❌ font-light를 한국어에 적용 (한국어 가독성 부족)
- ❌ 광고적 카피 톤 (Stripe는 정확한 기능 설명)
- ❌ 너무 많은 액센트 (단일 Indigo만)
