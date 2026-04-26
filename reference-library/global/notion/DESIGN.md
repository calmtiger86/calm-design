# Design System: Inspired by Notion

> Source: calm-design 자체 작성 — "Inspired by" 정책. notion.so 공개 인터페이스 관찰 기반.
> LANGUAGE: en (한국어 환경에서도 사용 가능)

## 1. Visual Theme & Atmosphere

에디토리얼·문서 중심 워크스페이스. Soft Gray 베이스, 거의 무액센트(텍스트 위계로만). 콘텐츠가 주인공, UI는 거의 보이지 않음. "글을 쓰는데 방해되지 않는" 미니멀리즘. 다크모드도 정통 지원 (콘텐츠 일관성).

## 2. Color Palette & Roles

| Canvas | `#FFFFFF` (라이트) / `#191919` (다크) | 페이지 배경 |
| Surface Soft | `#F7F6F3` | 사이드바·블록 hover (Notion 시그니처 베이지 톤) |
| Ink | `#37352F` | 본문 (검정보다 미세 따뜻한 톤) |
| Mute | `#9B9A97` | 보조 |
| Border | `#E9E9E7` | 분할 |
| Accent | `#37352F` (텍스트 위계로 강조 — 거의 무액센트) | — |
| Accent Color (선택적 사용) | `#2383E2` | 링크·버튼 (Notion Blue) |

규칙: 액센트 컬러 사용 최소. 텍스트 위계와 화이트스페이스로 정보 구조 표현.

## 3. Typography Rules

- Family: ui-sans-serif (시스템 폰트) 우선, **Inter는 회피** (calm-design 방침)
- 한국어: `Pretendard Variable` 강제
- 디스플레이: `text-3xl md:text-4xl font-bold tracking-tight`
- 본문: `text-base leading-relaxed` (콘텐츠 가독성 1순위)
- max-w-prose 또는 한국어 max-w-[65ch]
- 인라인 코드: `bg-zinc-100 text-rose-600 rounded px-1.5 py-0.5 font-mono text-[0.9em]`

## 4. Component Stylings

### Block (시그니처)
- **Default**: 보더 없음, 배경 transparent, padding `py-1`
- **Hover**: `bg-surface-soft` (베이지 톤 미세)
- **Focus**: `outline-none` + 좌측 hover 액션 (drag handle, +)
- **Active** (drag): 약간의 opacity 변화
- **Disabled**: 미사용 (블록은 disabled 안 됨)
- **Loading**: skeleton

### Sidebar Nav
- **Default**: text-sm + 좌측 작은 이모지·아이콘
- **Hover**: `bg-surface-soft`
- **Active** (현재 페이지): `bg-zinc-200` 또는 좌측 1px 보더 액센트

### Page Header
- 작은 emoji/icon 위 + 큰 제목 + 하위 설명 (Notion 시그니처 emoji 페이지 아이콘)

## 5. Layout Principles

- **Sidebar 240px** + 메인 영역 `max-w-3xl mx-auto`
- 콘텐츠 가독성 우선 — 모바일에선 사이드바 hide
- 무한 페이지 트리 (depth 제한 없음)
- min-h-[100dvh]

## 6. Depth & Elevation

- 그림자 거의 없음 — `bg-surface-soft` 명도로 위계
- Sidebar 분리: `border-r border-border`
- 모달: `bg-canvas border border-border shadow-lg rounded-md`

## 7. Motion & Interaction

- 매우 짧은 transition 100-150ms (콘텐츠 우선, 모션은 부차)
- 블록 등장/이동: spring (자연스러운 슬롯 정렬)
- Reduced-motion 의무

## 8. Responsive Behavior

- 모바일·태블릿·데스크톱 정통
- 모바일: sidebar drawer로 전환
- 한국어 본문 max-w-[65ch] 강제

## 9. Anti-Patterns (Project-Specific Banned)

- ❌ 화려한 색상·그라디언트 (Notion 시그니처는 무채색 + 콘텐츠)
- ❌ 큰 hero·landing 섹션 (Notion은 곧장 콘텐츠로)
- ❌ Inter 강제 (시스템 폰트 fallback이 정통)
- ❌ 카드 그림자 남용 (border와 명도로만)
