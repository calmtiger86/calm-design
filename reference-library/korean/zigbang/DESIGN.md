# Design System: Inspired by 직방 (Zigbang)

> Source: calm-design 자체 작성 — "Inspired by" 정책. zigbang.com 공개 인터페이스 관찰 기반.
> LANGUAGE: ko

## 1. Visual Theme & Atmosphere

부동산 검색·매물 SaaS. 직방 파랑 시그니처 + 큰 지도 통합. 정보 밀도 높음 (DENSITY 7+) — 매물 카드에 가격·면적·층·층수·관리비·옵션 가득. 신뢰·정확 톤. 모바일·데스크톱 모두 지원.

## 2. Color Palette & Roles

| Canvas | `#FFFFFF` | 페이지 배경 |
| Surface Soft | `#F7F8FA` | 카드 |
| Ink | `#222222` | 본문 |
| Mute | `#999999` | 보조 |
| Border | `#EEEEEE` | 분할 |
| Accent | `#0074E4` | 직방 파랑 (Primary CTA, 활성, 링크) |
| Accent Soft | `#E6F1FB` | 액센트 배경 |
| New | `#FF7B6E` | 신규 매물 라벨 |
| Hot | `#FF4A4A` | 인기·급매 |

## 3. Typography Rules

- Family: `'Pretendard Variable', Pretendard, system-ui, sans-serif`
- 헤드라인: `text-xl md:text-2xl font-bold tracking-tight word-break:keep-all`
- 매물 가격: `text-lg font-bold tabular-nums` (전세·월세·매매 구분)
- 면적·층: `text-sm tabular-nums`
- 위치·메타: `text-xs text-mute`
- 옵션 라벨: `text-xs font-medium`

금지: Inter, font-thin/extralight.

## 4. Component Stylings

### 매물 카드 (정보 밀도)
- **Default**: `bg-white border border-zinc-100 rounded-md p-4` (얇은 보더)
- 좌측 사진 정사각 + 우측 정보 (`flex gap-3`)
- 가격·면적·층·옵션 1줄·1줄 정렬
- **Hover**: `bg-zinc-50` + border-zinc-300
- **Focus**: ring-2 ring-accent
- **Active**: scale 0.98
- **Disabled** (계약완료): opacity 60% + "계약완료" 라벨
- **Loading**: skeleton

### 지도 + 매물 클러스터
- **Default**: 지도 위 클러스터 마커 (가격 표시)
- **Hover**: 마커 scale 1.1 + 매물 카드 미니 팝업
- **Active**: 마커 색 변화

### Primary CTA (문의하기·연락하기)
- **Default**: `w-full h-12 rounded-md bg-accent text-white font-bold`
- **Hover**: bg 명도 -5%
- **Focus**: ring-2 ring-accent ring-offset-2
- **Active**: scale 0.99
- **Disabled**: bg-zinc-300 opacity-60
- **Loading**: spinner inline

### 필터 박스
- 가격·면적·옵션·매물타입 등 다중 필터 슬롯
- 적용 후 매물 카드·지도 동기 갱신

## 5. Layout Principles

- **데스크톱**: 좌측 매물 리스트 + 우측 지도 (`grid-cols-2`, 50/50 또는 60/40)
- **모바일**: 매물 리스트 우선, 지도 토글 (전체 보기)
- **Top Bar 56px**: 검색·필터·지역
- min-h-[100dvh] 강제

## 6. Depth & Elevation

- 카드 그림자 없음 — 얇은 border
- 지도 마커: 미세한 shadow `shadow-[0_2px_8px_rgba(0,0,0,0.1)]`
- 모달·시트: backdrop-blur + shadow-lg
- z-index: nav=40, map-marker=30, modal=50

## 7. Motion & Interaction

- 200ms cubic-bezier (빠른 검색 인터랙션)
- 마커 hover scale 1.1
- 매물 카드 tap: scale 0.98
- 지도 zoom·pan smooth
- Reduced-motion 의무

## 8. Responsive Behavior

- 데스크톱·모바일 모두 정통
- 모바일: 지도 토글 (지도/리스트 전환)
- 터치 타겟 ≥ 44px
- 한국어 매물 정보 break-keep + max-w-[60ch]

## 9. Anti-Patterns (Project-Specific Banned)

- ❌ 가짜 매물·가격 fabricated data (부동산은 신뢰가 핵심)
- ❌ 차가운 어두운 톤 (직방은 신뢰·밝음)
- ❌ 광고적 톤 ("최저가 보장!") — 사실 ("실시간 매물 1,247건")
- ❌ Stock photo 매물 사진 (실제 매물 사진 의무)
- ❌ 다크모드 강제 (라이트 우선)

(글로벌 안티-슬롭 50개는 `references/ai-tells-blocklist.md` 자동 적용)
