# Design System: Inspired by 카카오 (Kakao)

> Source: calm-design 자체 작성 — "Inspired by" 정책. kakao.com·kakaotalk 인터페이스 관찰 기반.
> LANGUAGE: ko · 시그니처: KakaoChatBubble

## 1. Visual Theme & Atmosphere

친근한 한국 메시징·플랫폼 톤. 노란색 시그니처(브랜드 색)와 채팅 인터페이스의 따뜻함. 말풍선·반응·이모지 중심. 한국 사용자에게 가장 익숙한 UI 언어 중 하나.

## 2. Color Palette & Roles

| Canvas | `#FFFFFF` | 페이지 배경 |
| Surface Soft | `#FAFAFA` | 카드 배경 |
| Ink | `#191919` | 본문 |
| Mute | `#8B8B8B` | 보조 텍스트 |
| Border | `#EBEBEB` | 분할선 |
| Accent | `#FEE500` | 카카오 옐로우 톤 (브랜드 시그니처) |
| Accent Ink | `#191919` | 옐로우 위 텍스트는 거의 검정 (대비 충분) |

규칙: 옐로우는 브랜드 강조에만 사용 (Primary CTA에 단독 사용 시 contrast 검증 필요 — 옐로우 위는 항상 검정 텍스트). 본문 강조는 회색·검정으로.

## 3. Typography Rules

- Family: `'Pretendard Variable', Pretendard, system-ui, sans-serif`
- 채팅 메시지 텍스트: `text-sm leading-relaxed word-break:keep-all`
- 친근 카피·UI 텍스트: `text-base font-medium`
- 발신자 이름: `text-xs text-mute mb-1`
- 시간: `text-[10px] text-mute tabular-nums`

금지: Inter, font-thin/extralight (한국어 가독성).

## 4. Component Stylings

### KakaoChatBubble — 핵심 시그니처
- **Default** (내 메시지): `bg-[#FEE500] text-ink rounded-2xl rounded-br-sm px-3 py-2 max-w-[70%]` (꼬리 sharp)
- **Default** (상대 메시지): `bg-white text-ink border border-zinc-200 rounded-2xl rounded-bl-sm px-3 py-2 max-w-[70%]`
- **Hover** (interactive only): 거의 변화 없음 (메시지 자체는 hover 효과 X), 단 액션 버튼은 reaction picker 노출
- **Focus** (키보드 탐색 시): `ring-2 ring-accent ring-offset-1`
- **Active** (선택·롱프레스): `scale-[0.98]` 짧게
- **Disabled**: 미사용 (메시지는 disable 안 됨)
- **Loading** (전송 중): 상대 우측에 작은 spinner `<Loader2 className="animate-spin w-3 h-3" />`
- 시간: 메시지 하단 끝, `text-[10px] text-mute tabular-nums`
- 발신자 아바타: `w-9 h-9 rounded-full` (상대 메시지에만)
- 반응: 메시지 우측 하단 작은 이모지 + 카운트

### ReactionPicker
- **Default**: `inline-flex gap-1 bg-white rounded-full px-2 py-1.5 border border-zinc-200 shadow-md`
- **Hover** (이모지 버튼): scale 1.3 + y -4 (mac dock 스타일)
- **Focus**: `ring-2 ring-accent`
- **Active**: scale 1.1
- **Disabled**: `opacity-50`
- **Loading**: 적용 시 짧은 fade

### Input (메시지 입력창)
- **Default**: `flex-1 h-11 px-4 rounded-full bg-zinc-100 border-0 text-base`
- **Hover**: 변화 없음
- **Focus**: `bg-white ring-2 ring-accent/20`
- **Active**: 동일 focus
- **Disabled**: `opacity-50 cursor-not-allowed`
- **Loading** (전송 후): placeholder "전송 중..." + disabled

## 5. Layout Principles

- 채팅 화면: 헤더 56px + 메시지 리스트 (역시간순) + 입력 바닥 고정
- `max-w-md mx-auto`로 모바일 비율 유지
- min-h-[100dvh] 강제

## 6. Depth & Elevation

- 메시지 카드: 그림자 없음 (border만)
- Reaction Picker: `shadow-[0_2px_12px_rgba(0,0,0,0.08)]`
- z-index: nav=40, modal=50

## 7. Motion & Interaction

- 메시지 등장: 짧은 fade+up 200ms
- Reaction picker: spring stiffness 400, damping 25 (bouncy)
- 이모지 hover: scale 1.3 + y -4
- Reduced-motion 의무

## 8. Responsive Behavior

- **모바일 우선**: 카카오톡은 모바일 채팅 앱이 핵심 — `max-w-md mx-auto` 데스크톱에서도 모바일 비율 유지
- **터치 타겟 ≥ 44px**: 메시지 길게누르기·이모지 picker 영역 충분히 확보
- **메시지 영역**: 모바일에서 max-width 70% (말풍선 가로 폭 제한 — 가독성)
- **반응 picker**: 모바일에선 메시지 하단, 데스크톱에선 hover 시 메시지 우측 부유

## 9. Anti-Patterns (Project-Specific Banned)

- ❌ 옐로우를 본문 텍스트로 사용 (대비 부족)
- ❌ 차가운 톤·다크모드 강제 (카카오는 친근·라이트 우선)
- ❌ 이모지·스티커 없는 채팅 UI (카카오 정체성 상실)
- ❌ 가짜 사용자 이름 ("John Doe") — 한국 이름 사용

(글로벌 안티-슬롭 50개는 `references/ai-tells-blocklist.md` 자동 적용)
