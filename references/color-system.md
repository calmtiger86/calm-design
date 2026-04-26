# Color System — 컬러 팔레트·역할·변형 표준

calm-design의 색상 결정 알고리즘 + Mode D Multi-Variant 컬러 베리언트 생성용 자산.

> Phase 1 활성화. SKILL.md ALWAYS 로드는 아니며, Mode D 또는 사용자가 "다른 색상 옵션" 요청 시 sparse load.

## 0. 절대 원칙 5개

1. **Pure Black `#000000` 절대 금지** → Off-Black `#0A0A0A`, Zinc-950 `#09090B`, Charcoal `#18181B`
2. **한 페이지 액센트 1개만** (의도적 듀얼은 예외 — 차트·데이터 비교)
3. **채도 < 80%** (액센트 색상)
4. **LILA BAN** — 보라/파란 그래디언트 절대 금지
5. **색온도 일관성** — 차가우면 Zinc/Slate, 따뜻하면 Stone (혼용 X)

## 1. 표준 Neutral 베이스 (5개)

| 베이스 | 톤 | 추천 환경 |
|---|---|---|
| **Zinc** (기본) | 차가운 중립 | B2B SaaS, 개발자 도구, 신뢰 |
| **Gray** | 정통 중립 | 보수적 기업, 금융 |
| **Slate** | 차갑고 미세한 청 | 테크·엔지니어 |
| **Stone** | 따뜻한 중립 | 라이프스타일, 콘텐츠, 프리미엄 |
| **Neutral** | 거의 백·흑만 | 미니멀·갤러리 톤 |

## 2. 액센트 컬러 라이브러리 (Mode D 베리언트 풀)

calm-design이 권장하는 7개 액센트 (모두 채도 60-75%):

| 이름 | Hex | 톤 | 적합 시나리오 |
|---|---|---|---|
| **Calm Emerald** | `#10B981` | 차분·신뢰·성공 | SaaS 대시보드 (기본 권장) |
| **Toss Blue** | `#3182F6` | 신뢰·핀테크 | 핀테크, B2B SaaS |
| **Electric Blue** | `#3B82F6` | 테크·엔지니어 | 개발자 도구 |
| **Warm Amber** | `#F59E0B` | 친근·에너지 | 라이프스타일, 마케팅 |
| **Deep Rose** | `#E11D48` | 강렬·감성 | 콘텐츠, 미디어 |
| **Royal Purple** | `#7C3AED` | 고급·창의 | 디자인 도구 (단, 그래디언트 X — LILA BAN 회피) |
| **Forest Green** | `#16A34A` | 자연·지속가능 | 환경·식품 |

## 3. 6-역할 컬러 토큰 표준

모든 calm-design 출력은 다음 6개 역할로 컬러 매핑:

| 역할 | 의미 | 라이트 모드 예 | 다크 모드 예 |
|---|---|---|---|
| `canvas` | 페이지 배경 | `#FAFAFA` (Zinc-50) | `#09090B` (Zinc-950) |
| `surface` | 카드·시트 배경 | `#FFFFFF` | `#18181B` (Zinc-900) |
| `ink` | 본문·헤드라인 | `#0A0A0A` (Off-Black) | `#FAFAFA` |
| `mute` | 보조 텍스트, 메타 | `#71717A` (Zinc-500) | `#A1A1AA` (Zinc-400) |
| `border` | 1px 분할선 | `#E4E4E7` (Zinc-200) | `#27272A` (Zinc-800) |
| `accent` | CTA, 강조, 활성 | (위 라이브러리에서 1개) | (라이트와 동일 또는 미세 보정) |

추가 시멘틱 토큰 (선택):
- `success` — `#22C55E`
- `warning` — `#F59E0B`
- `danger` — `#EF4444`
- `info` — `#3B82F6`

## 4. Mode D 컬러 베리언트 생성 알고리즘

3안 생성 시 다음 매트릭스로 각 베리언트의 색상 자동 결정:

| Variant | 베이스 | 액센트 | 톤 |
|---|---|---|---|
| **Variant 1 (미니멀 차분)** | Stone | Calm Emerald | 따뜻한 중립 + 차분 액센트 |
| **Variant 2 (트렌디 다이내믹)** | Zinc | Warm Amber 또는 Deep Rose | 차가운 중립 + 강렬 액센트 |
| **Variant 3 (도메인 매칭)** | (Mode A 기본 — Zinc) | (사용자 의도 기반) | (Mode A 기본) |

각 Variant는 색온도 일관 강제 — Stone(따뜻) + Slate(차가움) 혼용 X.

## 5. Match-Reference 컬러 매핑 (Mode C, Phase 3)

| 브랜드 | 액센트 | 베이스 | 추출 노트 |
|---|---|---|---|
| Toss | Toss Blue `#3182F6` | Stone-50 (따뜻) | Pretendard + 핀테크 신뢰 |
| Linear | Royal Purple (단색만, 그래디언트 X) | Zinc-950 다크 우선 | 엔지니어링 톤 |
| Vercel | (단일 흑백) | Zinc-50 / 950 | 흑백+미세 액센트만 |
| Stripe | Indigo 비슷 톤 | Cool Gray | 핀테크 정제 |
| Notion | Soft Gray | Stone-50 | 거의 무액센트, 텍스트 위계로 |
| 당근 | Carrot Orange `#F26E22` | White | 친근·따뜻 |
| 카카오 | Yellow `#FEE500` | White | 브랜드 시그니처 |
| 네이버 | Green `#03C75A` | White | 브랜드 시그니처 |

## 6. WCAG 2.2 AA 자동 검증 페어

각 시멘틱 페어의 contrast 사전 계산값 (4.5:1 본문 / 3:1 큰 텍스트 기준):

| 페어 | Contrast | 본문 OK? |
|---|---|:-:|
| `ink #0A0A0A` on `surface #FFFFFF` | 20.31:1 | ✅ |
| `ink #0A0A0A` on `canvas #FAFAFA` | 19.36:1 | ✅ |
| `mute #71717A` on `surface #FFFFFF` | 4.83:1 | ✅ (경계) |
| `mute #71717A` on `canvas #FAFAFA` | 4.61:1 | ✅ (경계) |
| `accent Emerald` on `surface #FFFFFF` (텍스트로) | 3.10:1 | ⚠️ 큰 텍스트만 |
| `accent Emerald` on `surface white` (배경으로 + white text) | 3.05:1 | ⚠️ |

→ 액센트를 텍스트 색상으로 쓸 때 작은 본문은 피할 것. 큰 텍스트·CTA 라벨만.

## 7. 다크모드 자동 매핑

라이트 → 다크 자동 변환 규칙:

```
canvas:  #FAFAFA → #09090B (Zinc-950)
surface: #FFFFFF → #18181B (Zinc-900)
ink:     #0A0A0A → #FAFAFA
mute:    #71717A → #A1A1AA (한 단계 밝게)
border:  #E4E4E7 → #27272A (한 단계 어둡게)
accent:  (그대로) — 단, 채도 -10% 권장 (다크 환경 눈부심 방지)
```

CSS 구현:

```css
:root {
  --canvas: 0 0% 98%;
  --surface: 0 0% 100%;
  --ink: 0 0% 4%;
  --mute: 240 4% 46%;
  --border: 240 6% 90%;
  --accent: 158 64% 40%;
}

.dark {
  --canvas: 0 0% 4%;
  --surface: 240 4% 10%;
  --ink: 0 0% 98%;
  --mute: 240 5% 65%;
  --border: 240 4% 16%;
  --accent: 158 50% 45%;
}
```

## 8. Phase 1+ 확장 예정

- Phase 2: 그래디언트 정책 (LILA BAN 회피하는 안전한 그래디언트 패턴)
- Phase 3: 브랜드 컬러 자동 추출 (Match-Reference의 디자인 시스템 분석)
- Phase 4: WCAG 2.2 AAA 옵션 (대비 7:1 강제)
