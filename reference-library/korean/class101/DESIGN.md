# Design System: Inspired by 클래스101 (Class101)

> Source: calm-design 자체 작성 — "Inspired by" 정책. class101.net 공개 인터페이스 관찰 기반.
> LANGUAGE: ko

## 1. Visual Theme & Atmosphere

온라인 클래스 + 키트 커머스. 친근한 보라·핑크 톤. 강사 사진 + 클래스 영상 썸네일이 시각 위계. "취미 시작·성장" 감성. 따뜻한 라이프스타일 톤. 영상 콘텐츠 미리보기 + 키트 박스 사진.

## 2. Color Palette & Roles

| Canvas | `#FFFFFF` | 페이지 배경 |
| Surface Soft | `#FAFAFA` | 카드 |
| Ink | `#222222` | 본문 |
| Mute | `#999999` | 보조 |
| Border | `#EEEEEE` | 분할 |
| Accent | `#FF4785` | 클래스101 핑크 톤 (Primary CTA, 활성) |
| Accent Soft | `#FFE5EE` | 액센트 배경 |
| Premium | `#7C3AED` | 프리미엄 멤버십 (보라) |
| Live | `#FF4040` | 라이브 클래스 라벨 (빨강) |

## 3. Typography Rules

- Family: `'Pretendard Variable', Pretendard, system-ui, sans-serif`
- 디스플레이: `text-2xl md:text-4xl font-bold tracking-tight word-break:keep-all`
- 클래스 제목: `text-base font-semibold line-clamp-2 break-keep`
- 강사명: `text-sm font-medium`
- 카테고리·메타: `text-xs text-mute`
- 가격·할인: `text-base font-bold tabular-nums`
- 수강생 수: `text-xs tabular-nums` ("12,847명 수강 중")

금지: Inter, font-thin/extralight.

## 4. Component Stylings

### 클래스 카드
- **Default**: `bg-white rounded-xl overflow-hidden`
- 큰 16:9 영상 썸네일 + 재생 아이콘 hover
- 하단 정보: 카테고리 + 클래스 제목 + 강사명 + 수강생 수 + 가격
- **Hover**: 영상 썸네일 미세 zoom-in (1.05) + 재생 아이콘 부유
- **Focus**: ring-2 ring-accent
- **Active**: scale 0.99
- **Disabled** (수강마감): opacity 60% + "수강마감" 라벨
- **Loading**: skeleton (16:9 + 라인 3개)

### Hero Banner
- 큰 가로 카로셀 (인기 클래스·라이브 클래스 추천)
- 자동 스크롤 + 사용자 제어

### Primary CTA (지금 시작하기)
- **Default**: `w-full h-12 rounded-xl bg-accent text-white font-bold`
- **Hover**: scale 1.01, bg 명도 -5%
- **Focus**: ring-2 ring-accent ring-offset-2
- **Active**: scale 0.99
- **Disabled**: bg-zinc-300 opacity-60
- **Loading**: spinner inline + "결제 처리 중..."

### Live 라벨 (시그니처)
- `inline-flex bg-live text-white text-xs font-bold px-2 py-0.5 rounded-full animate-pulse`
- 라이브 클래스에만 표시, 펄스 애니메이션

## 5. Layout Principles

- **Hero**: 큰 가로 카로셀 (큐레이션·라이브)
- **카테고리 탭**: 가로 스크롤 (요리·뜨개·운동·코딩 등)
- **클래스 그리드**: `grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4`
- **모바일**: 단일 컬럼 + Bottom Tab
- min-h-[100dvh] 강제

## 6. Depth & Elevation

- 카드 미세한 그림자 — `shadow-[0_2px_8px_rgba(0,0,0,0.04)]`
- Hero Banner: 그림자 없음 (큰 이미지가 시각 위계)
- 모달·시트: backdrop-blur + shadow-lg
- z-index: nav=40, modal=50

## 7. Motion & Interaction

- 200-300ms cubic-bezier
- 영상 썸네일 hover zoom + 재생 아이콘 (감정적 트리거)
- 라이브 라벨 `animate-pulse` (시그니처)
- 카드 stagger 30ms cascade
- Reduced-motion 의무

## 8. Responsive Behavior

- 모바일·데스크톱 모두 정통
- 모바일: 단일 컬럼 + Bottom Tab + 가로 스크롤 카테고리
- 터치 타겟 ≥ 44px
- 한국어 클래스 제목·설명 break-keep + max-w-[65ch]

## 9. Anti-Patterns (Project-Specific Banned)

- ❌ 차가운 톤 (클래스101은 따뜻·친근 라이프스타일)
- ❌ 광고적 카피 ("지금 가입!") — 친근 한국어 ("같이 시작해봐요")
- ❌ Stock photo 강사·클래스 (실제 강사·클래스 사진 우선)
- ❌ 가짜 수강생 수·평점 fabricated metrics
- ❌ 다크모드 강제 (라이트 우선)

(글로벌 안티-슬롭 50개는 `references/ai-tells-blocklist.md` 자동 적용)
