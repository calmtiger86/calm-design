# Design System: Inspired by Spotify

> Source: calm-design 자체 작성 — "Inspired by" 정책. spotify.com·Spotify 앱 관찰 기반.
> LANGUAGE: en

## 1. Visual Theme & Atmosphere

음악 스트리밍 D2C. 다크모드 정체성 + Spotify Green. 풍부한 앨범 아트 + 큰 카드 그리드. 음악 청취 경험 우선 — UI는 콘텐츠를 방해하지 않음. 친근하지만 프리미엄.

## 2. Color Palette & Roles

| Canvas | `#121212` | 다크 배경 (Spotify 정체성으로 거의 검정 허용) |
| Surface | `#181818` | 카드 |
| Surface Hover | `#282828` | 카드 hover |
| Ink | `#FFFFFF` | 본문 |
| Mute | `#B3B3B3` | 보조 |
| Border | `#2A2A2A` | 분할 (거의 안 보임) |
| Accent | `#1DB954` | Spotify Green 톤 (CTA·재생 버튼·활성) |
| Hot | `#FF6437` | 플레이리스트 강조·new releases |

라이트 모드도 정통 — 단 다크가 시그니처.

## 3. Typography Rules

- Family: Spotify Circular (라이선스 — calm-design은 `Inter` 또는 `Geist` fallback)
- 한국어: Pretendard
- 디스플레이: `text-3xl md:text-5xl font-bold tracking-tight`
- 트랙명·앨범명: `text-base font-semibold line-clamp-2`
- 아티스트: `text-sm text-mute`
- 메타·duration: `text-xs tabular-nums`

## 4. Component Stylings

### 앨범 카드 (시그니처)
- **Default**: 정사각 앨범 아트 + 하단 정보 (트랙·아티스트)
- `aspect-square` 이미지 + `mt-4` text
- **Hover**: `bg-surface-hover` 부드러운 등장 + 재생 버튼 (`bg-accent`) 우측 하단 부유
- **Focus**: ring-2 ring-accent
- **Active/Disabled/Loading**: 표준 6상태

### 재생 버튼 (Play)
- **Default**: `w-12 h-12 rounded-full bg-accent text-black flex items-center justify-center`
- **Hover**: scale 1.05 (Spotify 시그니처)
- **Focus/Active/Disabled/Loading**: 표준 6상태
- 시그니처 동그라미

### Player Bar (하단)
- **Default**: `fixed bottom-0 inset-x-0 h-20 bg-surface border-t border-border`
- 좌측: 현재 트랙 + 앨범아트 + 좋아요
- 중앙: 재생 컨트롤 + progress
- 우측: 볼륨·큐·디바이스

### Sidebar (좌측)
- 라이브러리 + 플레이리스트 리스트
- 다크 + 큰 클릭 영역

## 5. Layout Principles

- **Sidebar 240px** + **Main flex-1** + **Player Bar 80px** (하단 고정)
- **카드 그리드**: `grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-4` (밀도 높음)
- min-h-[100dvh] 강제 (Player Bar 영역 확보)
- 모바일: Bottom Tab + Player mini

## 6. Depth & Elevation

- 다크 모드에서 명도 변화로 위계
- Player Bar: 미세한 top border만
- Modal: backdrop-blur + shadow
- z-index: nav=20, modal=50, player=40

## 7. Motion & Interaction

- 200-300ms cubic-bezier
- 카드 hover: 재생 버튼 부유 (bottom from -10px)
- 재생 버튼 scale 1.05
- 음파·비주얼라이저 (실시간 음악 반응)
- Reduced-motion 의무

## 8. Responsive Behavior

- 데스크톱·태블릿·모바일 모두 정통
- 모바일: Bottom Tab + Player mini bar (40px)
- 터치 타겟 ≥ 44px

## 9. Anti-Patterns (Project-Specific Banned)

- ❌ 라이트 강제 (Spotify는 다크 우선)
- ❌ 다중 액센트 (Green 단일)
- ❌ 작은 앨범 아트 (음악 시각성 우선)
- ❌ Player Bar 부재 (Spotify 정체성)
