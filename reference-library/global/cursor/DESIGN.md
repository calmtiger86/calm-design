# Design System: Inspired by Cursor

> Source: calm-design 자체 작성 — "Inspired by" 정책. cursor.com·Cursor IDE 관찰 기반.
> LANGUAGE: en

## 1. Visual Theme & Atmosphere

AI-native 코드 에디터. 다크모드 우선, 키보드-first, 정보 밀도 매우 높음. VS Code 톤 위에 AI 어시스턴트 사이드바·인라인 채팅 통합. 개발자만의 도구 톤 — 정밀하고 절제됨.

## 2. Color Palette & Roles

| Canvas | `#1E1E1E` | 에디터 배경 (다크) — Cursor 정체성으로 거의 검정 허용 |
| Surface | `#252526` | 사이드바·패널 |
| Ink | `#D4D4D4` | 코드·본문 |
| Mute | `#858585` | 보조·comment |
| Border | `#3E3E3E` | 분할 |
| Accent | `#0098FF` | Cursor Blue (AI 액션·하이라이트) |
| Success | `#4EC9B0` | git diff added |
| Danger | `#F48771` | error·diff removed |

규칙: 다크 정체성, 액센트는 AI·키보드 활성에만.

## 3. Typography Rules

- Family: `'JetBrains Mono', 'SF Mono', Consolas, monospace` (코드)
- UI: `Inter` 또는 시스템 (calm-design 외부 활용 시 Geist 권장)
- 한국어: `Pretendard Variable` fallback
- 코드: `text-sm font-mono`
- UI 라벨: `text-xs tracking-wide uppercase`
- AI 채팅 본문: `text-sm leading-relaxed`

## 4. Component Stylings

### AI 사이드바 (시그니처)
- **Default**: `bg-surface border-l border-border w-80` (우측 고정)
- AI 채팅 + 파일 컨텍스트 표시
- **Hover/Focus/Active/Disabled/Loading**: 표준 6상태

### Inline Chat (⌘K)
- 코드 라인 위 인라인 입력 박스
- **Default**: `bg-canvas/80 backdrop-blur-md border border-accent rounded-md`
- AI 응답 stream 시 typewriter 효과
- 6상태 표준

### Diff View
- Side-by-side 또는 inline
- Added: `bg-success/10`
- Removed: `bg-danger/10`
- Hover: 라인 강조

### Command Palette (⌘P, ⌘K)
- 중앙 모달 + fuzzy search + 키보드 네비

## 5. Layout Principles

- **Sidebar 240px** (좌측 파일 트리) + **Editor flex-1** + **AI Sidebar 320px** (우측, 토글)
- **Top Bar 30px** (얇음 — 코드 영역 최대)
- **Bottom Status 22px**
- min-h-[100dvh]
- 모바일: 사실상 미지원 (Cursor는 데스크톱 IDE)

## 6. Depth & Elevation

- 그림자 거의 없음 — border + 명도 변화
- Modal·Command Palette: `shadow-[0_8px_40px_rgba(0,0,0,0.4)]` + backdrop-blur
- z-index: editor=10, sidebar=20, modal=50

## 7. Motion & Interaction

- 100-200ms ease-out (즉각 반응)
- AI typing indicator: 부드러운 dot pulse
- Inline chat 등장: fade + 짧은 slide
- Reduced-motion 의무

## 8. Responsive Behavior

- 데스크톱 전용 (Cursor 정체성)
- 1280px 미만에선 AI sidebar 자동 collapse
- 한국어 fallback Pretendard

## 9. Anti-Patterns (Project-Specific Banned)

- ❌ 라이트 모드 강제 (Cursor는 다크 정체성)
- ❌ 큰 hero·landing 섹션 (Cursor IDE는 곧장 코드)
- ❌ 일러스트·이모지 UI 라벨 (정밀 도구 톤)
- ❌ 모바일 최적화 강제 (데스크톱 우선)
