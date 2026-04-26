# Design System: Inspired by 네이버 (Naver)

> Source: calm-design 자체 작성 — "Inspired by" 정책. naver.com 공개 인터페이스 관찰 기반.
> LANGUAGE: ko · 시그니처: NaverSearchSuggest

## 1. Visual Theme & Atmosphere

한국 포털·검색 톤. 네이버 그린 시그니처. 정보 밀도 매우 높음 (DENSITY 8+) — 실시간 인기 검색어, 카테고리, 이미지·동영상 통합. "한 페이지에 모든 정보". 검색창이 모든 UI의 중심.

## 2. Color Palette & Roles

| Canvas | `#FFFFFF` | 페이지 배경 |
| Surface Soft | `#F8F9FA` | 카드·섹션 |
| Ink | `#212124` | 본문 |
| Mute | `#767676` | 보조·메타 |
| Border | `#E5E5E5` | 분할 |
| Accent | `#03C75A` | 네이버 그린 톤 — 강조·활성·링크 |
| Hot | `#FF4040` | 실시간 인기 변동 (red ↑) |

규칙: 그린은 강조·검색 활성에만, 본문은 Ink·Mute. 채도 70% 미만.

## 3. Typography Rules

- Family: `'Pretendard Variable', Pretendard, system-ui, sans-serif`
- 검색창 입력: `text-base font-medium`
- 헤드라인: `text-lg font-semibold tracking-tight word-break:keep-all`
- 본문/링크: `text-sm leading-relaxed`
- 메타·시간·번호: `text-xs tabular-nums`

금지: Inter, font-thin/extralight (한국어 가독성).

## 4. Component Stylings

### NaverSearchSuggest — 핵심 시그니처
- **Default**: `absolute top-full left-0 right-0 mt-2 bg-white rounded-xl border border-zinc-200 shadow-md`
- **Hover** (suggestion item): `bg-zinc-50`
- **Focus** (키보드 ↑↓): `bg-accent/10`
- **Active** (선택): `bg-accent/20`
- **Disabled**: 미사용 (suggest는 항상 활성)
- **Loading**: 자동완성 fetch 중 skeleton 라인 3개
- 매칭 키워드 강조 `<strong className="text-accent">`
- 실시간 인기 검색어: 1, 2, 3 번호 + 변동 ↑ 표시

### 검색창 (Search Input)
- **Default**: `h-12 px-4 rounded-full border border-zinc-200 text-base bg-white`
- **Focus**: `border-accent ring-2 ring-accent/20`
- 우측 검색 버튼 + 마이크 아이콘
- 자동완성 dropdown 트리거

### 메인 카드 (정보 블록)
- `bg-white rounded-md border border-zinc-200 p-4`
- 정보 밀도 높게 — `text-sm` 본문
- Hover: `border-zinc-300`

## 5. Layout Principles

- **Top Bar**: 검색창 중심 (sticky, 56px)
- **Grid**: 12-column 비대칭 (좌측 메인 콘텐츠 8, 우측 사이드바 4)
- **정보 밀도 우선**: DENSITY 8 (조밀)
- min-h-[100dvh] 강제
- **모바일**: 검색 + 가로 스크롤 카테고리 + 단일 컬럼 콘텐츠

## 6. Depth & Elevation

- Suggest dropdown: `shadow-[0_4px_20px_rgba(0,0,0,0.06)]`
- 카드 그림자 거의 없음 — border만
- z-index: nav=40, search-suggest=45, modal=50

## 7. Motion & Interaction

- Suggest 등장: instant (<100ms) — 검색은 빨라야
- Cubic-bezier 200ms (다른 transition)
- 카드 hover: 색상 변화만 (transform X — 정보 밀도 유지)
- Reduced-motion 의무

## 8. Responsive Behavior

- 데스크톱·모바일 정통
- 모바일: 사이드바 hide, 12-column → 1-column
- 한국어 본문 너비 max-w-[65ch]
- 검색창: 모든 화면에서 sticky top

## 9. Anti-Patterns (Project-Specific Banned)

- ❌ 빈 페이지·카드 (네이버는 정보 가득 차야)
- ❌ 큰 hero 섹션 (네이버는 곧장 검색 + 콘텐츠)
- ❌ 채도 100% 빨강·노랑 (그린 시그니처와 충돌)
- ❌ 카드 큰 그림자 (정보 밀도 톤 깨짐)
- ❌ 다크모드 강제 (네이버는 라이트 우선)

(글로벌 안티-슬롭 50개는 `references/ai-tells-blocklist.md` 자동 적용)
