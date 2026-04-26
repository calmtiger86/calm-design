# Design System: Inspired by 무신사 (Musinsa)

> Source: calm-design 자체 작성 — "Inspired by" 정책. musinsa.com 공개 인터페이스 관찰 기반.
> LANGUAGE: ko · 시그니처: MusinsaFilterSidebar

## 1. Visual Theme & Atmosphere

정통 한국 패션 이커머스 톤. 검정·흰색 모노크롬에 큰 상품 사진. Filter Sidebar로 카탈로그 탐색이 핵심. 도쿄·서울 트렌디 패션 매거진 인상. 정보 밀도 높음 (브랜드명·가격·평점 + 무신사 추천 등급 등).

## 2. Color Palette & Roles

| Canvas | `#FFFFFF` | 페이지 배경 |
| Surface Soft | `#F8F8F8` | 카드·섹션 |
| Ink | `#191919` | 본문·헤드라인 |
| Mute | `#7B7B7B` | 보조·메타 |
| Border | `#EEEEEE` | 분할 (얇게) |
| Accent | `#191919` | 무채색 정체성 — 검정이 액센트 (CTA·강조) |
| Sale | `#FF3B3B` | 세일·할인 표시 |
| Premium | `#A88B65` | 무신사 추천·프리미엄 |

규칙: 검정·흰색이 주, 컬러는 세일·등급 표시에만. 패션 사진이 색상 풍부함을 담당.

## 3. Typography Rules

- Family: `'Pretendard Variable', Pretendard, system-ui, sans-serif`
- 디스플레이: `text-3xl md:text-4xl font-bold tracking-tight word-break:keep-all`
- 상품명: `text-sm font-medium line-clamp-2 break-keep`
- 브랜드명: `text-xs font-bold tracking-wide uppercase`
- 가격: `text-base font-bold tabular-nums`
- 할인율: `text-sm font-bold text-sale tabular-nums`

금지: Inter, font-thin (한국어 가독성).

## 4. Component Stylings

### MusinsaFilterSidebar — 핵심 시그니처
- **Default** (컨테이너): `w-60 shrink-0 border-r border-zinc-200 bg-white`
- **Header sticky**: `sticky top-0 bg-white border-b p-4`
- **Hover** (필터 항목): `text-ink` (mute → ink)
- **Focus** (체크박스): `ring-2 ring-accent`
- **Active** (선택): 체크 ✓ + 카운트
- **Disabled**: opacity 50%
- **Loading**: 카운트 부분 skeleton
- `<fieldset><legend>` 의무 (접근성)

### 상품 카드
- **Default**: `bg-white aspect-[3/4] overflow-hidden` (이미지 우선) + 하단 정보
- **Hover**: scale 1.02 (이미지 zoom-in 효과)
- **Focus**: ring-2 ring-accent
- **Active**: scale 0.98 (탭 피드백)
- **Disabled** (품절): opacity 60% + "품절" 오버레이
- **Loading**: skeleton (실제 비율 매칭)
- 상품명 line-clamp-2 (한국어)
- 가격 + 할인율 강조

### Primary CTA
- **6상태 표준**: Default(검정 배경 흰색) / Hover(opacity 90) / Focus(ring) / Active(scale 0.98) / Disabled / Loading

## 5. Layout Principles

- **Sidebar 240px** + 메인 카탈로그 그리드 (3-5 column)
- **Top Bar 64px** sticky
- **카드 그리드**: `grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4` (정보 밀도)
- min-h-[100dvh] 강제
- **모바일**: Sidebar drawer 전환, 카드 grid-cols-2

## 6. Depth & Elevation

- 카드 그림자 없음 — 이미지 + 얇은 border만
- Sidebar 분리: `border-r` (그림자 X)
- 모달: backdrop-blur + shadow-lg

## 7. Motion & Interaction

- Hover scale 1.02 (이미지 강조)
- 200ms cubic-bezier
- 카드 등장 stagger 30ms (cascade)
- 무한 스크롤 시 skeleton placeholder
- Reduced-motion 의무

## 8. Responsive Behavior

- 데스크톱 우선 (이커머스 특성), 모바일도 정통 지원
- 모바일: Sidebar drawer, grid-cols-2
- 한국어 상품명 max-w 65자

## 9. Anti-Patterns (Project-Specific Banned)

- ❌ 화려한 색상 액센트 (무신사는 모노크롬 정체성)
- ❌ Hero 영상·자동재생 (상품 카탈로그가 우선)
- ❌ "지금 사세요!" 광고 톤 (정통 패션 톤 — "STYLE", "LOOK")
- ❌ Stock photo 모델 얼굴 (실제 한국 모델 또는 상품만)
- ❌ 가짜 평점·리뷰 fabricated metrics

(글로벌 안티-슬롭 50개는 `references/ai-tells-blocklist.md` 자동 적용)
