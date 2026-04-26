# Design System: Inspired by Supabase

> Source: calm-design 자체 작성 — "Inspired by" 정책. supabase.com 공개 인터페이스 관찰 기반.
> LANGUAGE: en

## 1. Visual Theme & Atmosphere

오픈소스 백엔드 BaaS. Emerald 그린 시그니처 + 다크모드 우선. 개발자 콘솔 톤 — 데이터 밀도 높음(테이블·로그·SQL 에디터). Vercel 미니멀과 Linear 정밀의 중간. 친근하지만 기술적.

## 2. Color Palette & Roles

| Canvas | `#0F1117` | 다크 배경 |
| Surface | `#1C1F26` | 카드·패널 |
| Ink | `#EDEDED` | 본문 |
| Mute | `#888888` | 보조 |
| Border | `#2A2D34` | 분할 |
| Accent | `#3ECF8E` | Supabase Emerald (CTA·활성·success) |
| Warning | `#F5A623` | warning |
| Danger | `#FF4D4F` | error |

라이트 모드도 정통 — Canvas `#FFFFFF`, Ink `#1F2937`, 액센트 동일 Emerald.

## 3. Typography Rules

- Family: Custom Sans (Supabase) — calm-design은 `Inter` 또는 `Geist` fallback
- 한국어: Pretendard
- 디스플레이: `text-3xl md:text-5xl font-bold tracking-tight`
- 본문: `text-base leading-relaxed`
- 코드: `font-mono text-sm` (JetBrains Mono 또는 SF Mono)

## 4. Component Stylings

### Database Table (시그니처)
- **Default**: `bg-surface border border-border rounded-md`
- 헤더 sticky + sortable
- 행 hover: `bg-canvas/50`
- 인라인 편집 가능
- 6상태 표준

### SQL Editor
- 다크 모노스페이스 + syntax highlight
- 실행 버튼: `bg-accent text-canvas font-medium rounded-md`
- 결과 패널 하단 분할

### Primary CTA
- **Default**: `h-10 px-4 rounded-md bg-accent text-canvas text-sm font-medium`
- **Hover**: bg 명도 -5%
- **Focus**: ring-2 ring-accent
- **Active/Disabled/Loading**: 표준 6상태

### Code Block (Hero)
- 다크 배경 + 그린 prompt + 인라인 copy 버튼
- `npx supabase init` 같은 명령 hero에 노출

## 5. Layout Principles

- **Sidebar 240px** (다크) + Main flex-1
- **Hero Section** (랜딩): 큰 코드 블록 + 짧은 카피
- **대시보드**: 12-column 그리드, KPI 카드 비대칭
- min-h-[100dvh]
- 모바일: Sidebar drawer

## 6. Depth & Elevation

- 다크 모드에서 명도 변화로 위계
- 카드 그림자 거의 없음 — border 1px
- Modal: backdrop-blur + shadow-lg

## 7. Motion & Interaction

- 200ms cubic-bezier
- 코드 블록 typing 효과 (선택, hero용)
- 데이터 테이블 정렬: smooth swap
- Reduced-motion 의무

## 8. Responsive Behavior

- 데스크톱·모바일 모두 정통
- 모바일: Sidebar drawer + 카드 단일 컬럼
- 코드 블록: 가로 스크롤 + 작은 폰트

## 9. Anti-Patterns (Project-Specific Banned)

- ❌ 라이트 강제 (다크 우선)
- ❌ 다중 액센트 (Emerald 단일)
- ❌ 큰 hero 일러스트 (코드 블록이 hero)
- ❌ 광고적 카피 ("Get Started Free!") — 기술적 ("`npx supabase init`")
