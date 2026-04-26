# Design System: Inspired by Linear

> Source: calm-design 자체 작성 — "Inspired by" 정책. linear.app 공개 인터페이스 관찰 기반.
> LANGUAGE: en (한국어 환경에서도 사용 가능, Pretendard fallback)

## 1. Visual Theme & Atmosphere

엔지니어링 톤 프로젝트 관리 도구. 극도의 미니멀리즘, 키보드-first, 다크 모드 우선. 정보 밀도가 높지만 시각적 노이즈는 최소. Cabinet Grotesk·Inter 톤의 조밀한 타이포그래피 + 보라색 단일 액센트. "버튼·메뉴 보지 말고 ⌘K로 끝내라"는 철학.

## 2. Color Palette & Roles

| Canvas | `#08090A` | 페이지 배경 (거의 검정, Off-Black) |
| Surface | `#101113` | 카드·시트 배경 |
| Ink | `#F7F8F8` | 본문·헤드라인 |
| Mute | `#8A8F98` | 보조 텍스트 |
| Border | `#23262C` | 1px 분할선 |
| Accent | `#5E6AD2` | Linear Purple — 활성·강조·CTA |
| Success | `#26A65B` | 완료 |
| Warning | `#F5A623` | 진행 중 |

규칙: 다크모드 우선, Pure Black 회피 (Off-Black `#08090A`), 단일 보라 액센트, 채도 50% 미만(절제).

## 3. Typography Rules

- Family: Inter Display 또는 Geist (calm-design은 Geist 권장 — Inter 회피)
- 한국어 환경: `Pretendard Variable` fallback
- 디스플레이: `tracking-tight leading-none font-medium` (절제)
- 본문: `text-sm leading-normal` (조밀)
- 라벨/메타: `text-xs tracking-wide text-mute uppercase`
- 숫자: `tabular-nums font-mono` (Geist Mono)

## 4. Component Stylings

### Issue Card (시그니처)
- **Default**: `bg-surface border border-border rounded-md px-3 py-2`
- **Hover**: `bg-[#15171A]` (미세 명도 변화만, scale X)
- **Focus**: `ring-1 ring-accent`
- **Active** (선택): `bg-accent/10 border-accent/30`
- **Disabled**: `opacity-50`
- **Loading**: skeleton (실제 라인 매칭)

### Button (Primary)
- Default: `h-7 px-3 rounded-md bg-accent text-white text-sm font-medium`
- Hover: 색상 명도 +5% (transform X)
- Active: `bg-accent/90`
- 모든 인터랙션 200ms `cubic-bezier(0.16, 1, 0.3, 1)`

### Command Palette (⌘K)
- 모달 중앙 띄우기, `max-w-2xl bg-surface border border-border rounded-lg`
- 검색 입력 + 결과 리스트 + 키보드 네비게이션 시각화 (`↑↓ ⏎`)

## 5. Layout Principles

- **Sidebar 240px** + Main flex-1
- **Top Bar 44px** (얇음 — Linear 시그니처)
- **그리드**: 정보 밀도 높음, 그러나 카드 사이 gap 최소 (border 1px만)
- **min-h-[100dvh]** 강제
- **금지**: 큰 카드, 풀-블리드 콘텐츠, 3-column equal

## 6. Depth & Elevation

- **그림자 거의 없음** — 1px border가 깊이 표현
- 모달: `bg-surface backdrop-blur-md` + `border border-border`
- z-index: nav=40, modal=50

## 7. Motion & Interaction

- 모든 transition 200ms `cubic-bezier(0.16, 1, 0.3, 1)`
- transform 거의 사용 X (Linear 절제 톤) — 색상·명도 변화만
- 키보드 네비게이션 시각화 우선 (`↑↓ ⏎ esc`)
- Reduced-motion 의무

## 8. Responsive Behavior

- **데스크톱 우선** — Linear는 모바일이 부차
- 태블릿 이하: Sidebar collapsible
- 모바일: 매우 제한적 (full-app 경험은 데스크톱만)

## 9. Anti-Patterns (Project-Specific Banned)

- ❌ 화려한 그라디언트·네온 (Linear 절제 정체성과 충돌)
- ❌ 라이트 모드 강제 (다크 우선)
- ❌ 큰 hero 섹션 (Linear는 곧장 작업 화면)
- ❌ 일러스트·이모지 UI 라벨 (조밀한 텍스트만)

(글로벌 안티-슬롭 50개는 `references/ai-tells-blocklist.md` 자동 적용)
