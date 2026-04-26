# Design System: Inspired by 라인 (LINE)

> Source: calm-design 자체 작성 — "Inspired by" 정책. line.me 공개 인터페이스 관찰 기반.
> LANGUAGE: ko · 시그니처: LineReactionPicker

## 1. Visual Theme & Atmosphere

한·일 메시징 시그니처. 라인 그린 액센트. 스티커·반응 중심의 표현력 풍부한 UI. 카카오톡과 비슷한 친근 톤이지만 더 글로벌·정제된 느낌. 캐릭터(브라운·코니 등) 일러스트가 정체성.

## 2. Color Palette & Roles

| Canvas | `#FFFFFF` | 페이지 배경 |
| Surface Soft | `#F7F8FA` | 카드 |
| Ink | `#212121` | 본문 |
| Mute | `#8C8C8C` | 보조 |
| Border | `#E6E6E6` | 분할 |
| Accent | `#06C755` | LINE Green 톤 — Primary CTA, 활성, 링크 |
| Accent Soft | `#E8F8EF` | 액센트 배경 |

## 3. Typography Rules

- Family: `'Pretendard Variable', Pretendard, system-ui, sans-serif`
- 메시지: `text-sm leading-relaxed word-break:keep-all`
- 헤드라인: `text-lg font-bold tracking-tight word-break:keep-all`
- 라벨: `text-xs font-medium`
- 시간: `text-[10px] text-mute tabular-nums`

금지: Inter, font-thin/extralight.

## 4. Component Stylings

### LineReactionPicker — 핵심 시그니처
- **Default**: `inline-flex gap-1 bg-white rounded-full px-2 py-1.5 border border-zinc-200 shadow-md`
- **Hover** (개별 이모지): `scale-1.3 -translate-y-1` (mac dock 스타일, bouncy spring)
- **Focus**: `ring-2 ring-accent ring-offset-1`
- **Active**: scale 1.1
- **Disabled**: opacity 50%
- **Loading**: 적용 시 짧은 fade

### 메시지 버블 (LINE 스타일)
- **Default** (내 메시지): `bg-accent text-white rounded-2xl rounded-br-sm px-3 py-2 max-w-[70%]`
- **Default** (상대): `bg-zinc-100 text-ink rounded-2xl rounded-bl-sm`
- **Hover**: 인터랙션 부유 액션 노출
- **Focus**: ring-2
- **Active**: scale 0.98
- **Disabled**: 미사용
- **Loading** (전송 중): spinner 우측 작게

### Sticker Picker
- 그리드 4-column, 큰 정사각 스티커 셀
- hover/active scale 변화

### Primary CTA
- **Default**: `w-full h-12 rounded-xl bg-accent text-white font-bold`
- **Hover/Active**: scale 1.01/0.99 200ms
- **Focus/Disabled/Loading**: 표준 6상태

## 5. Layout Principles

- 모바일 우선 (`max-w-md mx-auto`)
- 채팅 화면: header 56px + 메시지 리스트 + 입력 바닥
- min-h-[100dvh]
- Bottom tab 4-5개 (Home·채팅·뉴스·기타)

## 6. Depth & Elevation

- 메시지: 그림자 없음
- Reaction picker: `shadow-[0_2px_12px_rgba(0,0,0,0.08)]`
- 모달: backdrop-blur

## 7. Motion & Interaction

- Bouncy spring (stiffness 400, damping 25) — 이모지·반응
- 메시지 등장: fade+up 200ms
- 카드 등장: stagger 50ms
- Reduced-motion 의무

## 8. Responsive Behavior

- 모바일 우선, 데스크톱은 max-w-md 유지
- 터치 타겟 ≥ 44px
- 한국어 본문 max-w-[65ch]

## 9. Anti-Patterns (Project-Specific Banned)

- ❌ 그린을 본문 텍스트로 (대비 부족)
- ❌ 다크모드 강제 (라인은 라이트 우선)
- ❌ 캐릭터·이모지 없는 채팅 UI (라인 정체성 상실)
- ❌ 가짜 사용자 이름 — 한국·일본 이름 사용

(글로벌 안티-슬롭 50개는 `references/ai-tells-blocklist.md` 자동 적용)
