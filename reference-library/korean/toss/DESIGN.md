# Design System: Inspired by 토스 (Toss)

> Source policy: calm-design 자체 작성 — "Inspired by" 정책. 토스(toss.im)의 공개 디자인 시스템·인터페이스 관찰 기반. 직접 복제·재배포 X. 브랜드 로고·정확한 hex·독점 폰트 사용 X.
> calm-design 9-섹션 표준 준수 · LANGUAGE: ko · 시그니처 패턴: TossBottomSheet, TossInput, TossPrimaryButton

## 1. Visual Theme & Atmosphere

차분한 한국 핀테크 톤. 충분한 호흡감, 단일 신뢰 색상(파란색 톤), Pretendard 한국어 우선. "친구가 알려주는 듯한" 친근함 + 금융 신뢰감의 균형. 모서리 28px 둥근 라운드(일반 24px보다 약간 큼)로 부드러운 인상. 모바일·결제 흐름이 핵심 UX 포인트.

## 2. Color Palette & Roles

| 이름 | Hex | 역할 |
|---|---|---|
| Canvas | `#FFFFFF` | 페이지 배경 (순백) |
| Surface Soft | `#F9FAFB` | 카드·섹션 배경 |
| Ink | `#191F28` | 본문·헤드라인 (Toss 톤 다크) |
| Mute | `#8B95A1` | 보조 텍스트 |
| Border | `#E5E8EB` | 분할선 |
| Accent | `#3182F6` | Toss Blue 톤 — Primary CTA, 링크, 강조 |
| Accent Soft | `#E8F3FF` | 액센트 배경 (배지·info 박스) |
| Danger | `#F04438` | 오류·삭제 |

규칙: 한 페이지 액센트 1개만, Pure Black 절대 X (Ink는 `#191F28`), 채도 75% 미만, LILA BAN 적용.

## 3. Typography Rules

한국어 환경 강제:
- Family: `'Pretendard Variable', Pretendard, system-ui, sans-serif`
- 디스플레이/H1: `text-4xl md:text-5xl lg:text-6xl tracking-tight leading-tight word-break:keep-all`
- 섹션 제목 H2: `text-2xl md:text-3xl font-bold tracking-tight word-break:keep-all`
- 본문: `text-base md:text-lg leading-relaxed text-mute max-w-[65ch]`
- 입력 라벨: `text-base font-medium`
- 메타·라벨: `text-xs font-medium text-mute`

금지: Inter, Noto Sans KR, Roboto, Malgun Gothic, font-thin/extralight/light.

## 4. Component Stylings

### TossInput (Floating Label) — 핵심 시그니처
- Default: `h-14 px-4 pt-6 pb-1 rounded-xl bg-zinc-50 border border-zinc-200 text-base font-medium`
- Focus: `bg-white border-accent ring-2 ring-accent/20`
- Error: `border-danger`
- Active/Loading: 동일, disabled는 `opacity-60`
- 라벨: input 안에서 자연스럽게 위로 떠오름 (peer-focus 변형)

### TossPrimaryButton — 핵심 시그니처
- Default: `w-full h-14 rounded-2xl bg-accent text-white font-bold text-base`
- Hover: `scale-[1.01]` 200ms `cubic-bezier(0.16,1,0.3,1)`
- Active: `scale-[0.99]`
- Disabled: `opacity-60 cursor-not-allowed`
- Loading: spinner `w-4 h-4 border-2 border-white/30 border-t-white animate-spin` 인라인 + 텍스트 유지

### TossBottomSheet — 시그니처 모바일 컴포넌트
- 컨테이너: `fixed inset-x-0 bottom-0 max-w-md mx-auto bg-white rounded-t-[28px] pb-8 shadow-[0_-8px_40px_rgba(0,0,0,0.08)]`
- 핸들: `w-12 h-1 bg-zinc-300 rounded-full mx-auto mt-3` (얇음·차분)
- Spring: stiffness 300, damping 35 (꽉 찬 느낌)
- 드래그 핸들 + 100px 이하 드래그면 닫힘
- `role="dialog"` + `aria-labelledby` 의무

### Card (일반)
- `bg-white rounded-2xl border border-zinc-200 p-5 shadow-[0_2px_8px_rgba(25,31,40,0.04)]` (매우 부드러움)
- Hover (interactive only): `border-zinc-300`
- Empty: 컴포지션 일러스트 + 친근 카피 ("아직 데이터가 없어요")
- Loading: skeleton (실제 레이아웃 매칭)

## 5. Layout Principles

- **모바일 우선**: `max-w-md mx-auto` (약 480px)로 모바일 비율 유지 (데스크톱에서도)
- **min-h-[100dvh]** 강제 (h-screen 금지)
- **섹션 패딩**: 모바일 `p-5` (20px), 데스크톱 `p-8`
- **그리드**: 단일 컬럼이 기본 (모바일 흐름)
- **Top Bar**: 모바일 표준 56px (`h-14`)
- **Bottom Sheet**: 핵심 인터랙션 — 결제·인증 흐름은 모두 시트로
- **금지**: 데스크톱 우선 그리드, 3-column equal cards

## 6. Depth & Elevation

- **카드 그림자**: `shadow-[0_2px_8px_rgba(25,31,40,0.04)]` — 미세한 부드러움 (Toss 톤)
- **Bottom Sheet**: `shadow-[0_-8px_40px_rgba(0,0,0,0.08)]` (위에서 내려오는 깊이)
- **Backdrop**: `bg-black/40 backdrop-blur-sm` (시트 뒤)
- **z-index**: nav=40, modal-backdrop=49, modal=50
- **금지**: 네온 글로우, Pure Black 그림자, 큰 drop shadow

## 7. Motion & Interaction

- **Spring**: `cubic-bezier(0.16, 1, 0.3, 1)` 200-300ms (대부분의 transition)
- **Bottom Sheet**: spring stiffness 300, damping 35 (꽉 찬 등장)
- **CTA hover**: `scale-[1.01]` (절제) → tap `scale-[0.99]`
- **GPU 친화**: transform·opacity만
- **Reduced-motion 의무 지원** (전정 장애 보호)
- **금지**: linear easing, top/left 애니메이션, useState 기반 React 애니메이션

## 8. Responsive Behavior

- **Breakpoints**: 모바일 `<768px`, 태블릿 `768-1024px`, 데스크톱 `≥1024px`
- **최대 너비**: `max-w-md mx-auto` 데스크톱에서도 모바일 비율 유지 (특수)
- **터치 타겟**: 모든 input/button 최소 `h-14` (56px, ≥44px iOS HIG 충족)
- **한국어**: word-break: keep-all + leading-relaxed 강제
- **한국어 본문 너비**: `max-w-[65ch]` (약 한국어 65자)

## 9. Anti-Patterns (Project-Specific Banned)

토스 톤 적용 시 다음 절대 금지:
- ❌ 광고적 카피 ("지금 가입하세요!", "혁신적인 핀테크") — 차분 신뢰 톤 유지
- ❌ 가짜 통계·100% 만족도 같은 fabricated metrics — 핀테크 신뢰성 저하
- ❌ Stock photo 얼굴 사용자 (한국인 인종 + 광고 인상)
- ❌ 자동재생 비디오 (음성 ON 절대 X)
- ❌ 햇볕 노란색·채도 100% 색상 (Toss 톤은 절제)
- ❌ Apple SD Gothic Neo 의존 (다른 OS에서 깨짐)
- ❌ Centered Hero (모바일 흐름은 좌측 정렬·자연 스크롤)
- ❌ 대시보드용 사이드바 (Toss는 항상 모바일 단일 컬럼)

(글로벌 안티-슬롭 50개는 `references/ai-tells-blocklist.md` 자동 적용)
