# Design System: Inspired by 29CM

> Source: calm-design 자체 작성 — "Inspired by" 정책. 29cm.co.kr 공개 인터페이스 관찰 기반.
> LANGUAGE: ko

## 1. Visual Theme & Atmosphere

셀렉트 커머스 + 에디토리얼 매거진 톤. 모노크롬 흑백 시그니처에 큰 사진. 큐레이션·브랜드 스토리텔링이 핵심 — 단순 상품 나열이 아닌 콘텐츠로 풀어냄. "이번주의 발견" 같은 에디토리얼 카피. 패션 매거진 인상.

## 2. Color Palette & Roles

| Canvas | `#FFFFFF` | 페이지 배경 |
| Surface Soft | `#FAFAFA` | 카드 |
| Ink | `#000000` | 본문 — 29CM 흑백 정체성으로 Pure Black 허용 |
| Mute | `#999999` | 보조 |
| Border | `#EEEEEE` | 분할 (얇게) |
| Accent | `#000000` | 무채색 정체성 — 검정이 액센트 (29CM 정체성 — Pure Black 허용) |
| Sale | `#E04A4A` | 세일·할인 (절제 사용) |

규칙: 흑백이 정체성, 컬러는 거의 사용 X — 사진이 색상 풍부함을 담당.

## 3. Typography Rules

- Family: `'Pretendard Variable', Pretendard, system-ui, sans-serif`
- 디스플레이: `text-3xl md:text-5xl tracking-tight font-bold word-break:keep-all` (큰 헤드라인)
- 에디토리얼 본문: `text-base md:text-lg leading-relaxed break-keep max-w-[65ch]`
- 상품명: `text-sm font-medium uppercase tracking-wide` (브랜드명) + `text-sm` (상품명)
- 가격: `text-base font-semibold tabular-nums`

금지: Inter, font-thin/extralight (한국어 가독성).

## 4. Component Stylings

### 에디토리얼 카드 (시그니처)
- **Default**: 큰 이미지 + 짧은 카피 + 브랜드명
- 가로 풀-블리드 또는 큰 정사각
- 텍스트는 이미지 위 또는 하단
- **Hover**: 이미지 scale 1.02 + 텍스트 미세 변화
- **Focus**: ring-2 ring-ink
- **Active**: scale 0.99
- **Disabled**: opacity 60%
- **Loading**: skeleton (정사각/4:3)

### 상품 카드
- **Default**: 큰 이미지 (`aspect-[3/4]`) + 하단 정보 (브랜드 + 상품명 + 가격)
- 그림자·border 없음 — 이미지가 시각 위계
- **Hover**: scale 1.02
- **Focus**: ring-2
- **Active/Disabled/Loading**: 표준 6상태

### Primary CTA
- **Default**: `h-12 px-8 rounded-md bg-ink text-white text-sm font-medium uppercase tracking-wide`
- **Hover**: bg 명도 -10%
- **Focus**: ring-2 ring-ink
- **Active**: scale 0.99
- **Disabled**: opacity 60%
- **Loading**: spinner inline

## 5. Layout Principles

- **Hero**: 풀-블리드 큐레이션 이미지
- **에디토리얼 섹션**: 매거진 그리드 (asymmetric 비율)
- **상품 그리드**: `grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4` (큰 이미지)
- **여백 generous** — 패션 매거진 톤
- min-h-[100dvh] 강제

## 6. Depth & Elevation

- 그림자 거의 없음 (29CM는 평면 매거진 톤)
- 카드 분리: 이미지·여백으로
- z-index: nav=40, modal=50

## 7. Motion & Interaction

- 200-300ms cubic-bezier
- 이미지 hover scale 1.02 (절제)
- Smooth scroll
- Reduced-motion 의무

## 8. Responsive Behavior

- 모바일·데스크톱 모두 정통
- 모바일: 단일 컬럼 또는 grid-cols-2
- 터치 타겟 ≥ 44px
- 한국어 에디토리얼 본문 max-w-[65ch] + leading-loose

## 9. Anti-Patterns (Project-Specific Banned)

- ❌ 화려한 색상 액센트 (29CM는 흑백 정체성)
- ❌ "지금 사세요!" 광고 톤 (에디토리얼 톤 우선)
- ❌ 작은 사진·정보 가득 카드 (큰 이미지·여백 시그니처)
- ❌ Stock photo (실제 큐레이션 사진만)
- ❌ Inter (Pretendard 강제)

(글로벌 안티-슬롭 50개는 `references/ai-tells-blocklist.md` 자동 적용)
