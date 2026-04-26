# AI Tells Blocklist — 글로벌 안티-슬롭 패턴 카탈로그

> **Inspired by**:
> - [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) — anti-slop 철학 + 40+ AI Tells 원조
> - [uxjoseph/supanova-design-skill](https://github.com/uxjoseph/supanova-design-skill) — ABSOLUTE ZERO DIRECTIVE 13개 금지 규칙
>
> **calm-design 확장 부분**: 50개로 확장 (한국어 친화 5개 추가) + 자동 검증 정규식 + `❌ 금지 / ✅ 대신 / 💡 이유` 3-블록 구조 + 카테고리 7-12 (접근성·콘텐츠·UX·미세 디테일·성능)

calm-design이 만드는 모든 출력에 **자동 적용**되는 글로벌 금지 목록.

> **역할 분리**: 이 파일은 **글로벌 금지** 전담. 프로젝트 고유 금지(브랜드 톤·도메인 제약·법적 요구사항)는 `references/design-md-spec.md`의 Section 9가 담당하며, 이 파일과 중복하지 않는다.

> **Phase 0 범위**: 30+ 항목으로 시작. Phase 1+에서 50+로 확장.

## 적용 방식

각 패턴은 **`❌ 금지 / ✅ 대신 / 💡 이유` 3-블록 구조**. 스킬은 출력 직후 자동으로 모든 항목을 패턴 매칭하여 위반 시 즉시 재생성.

---

## 카테고리 1: 폰트 (5개)

### 1. ❌ Inter 폰트 사용 금지
- ✅ 대신: `LANGUAGE=ko` → Pretendard / `LANGUAGE=en` → Geist, Cabinet Grotesk, Outfit, Satoshi 중 하나
- 💡 이유: Inter는 라틴 환경 보편화 → 변별력 없음. AI 생성 디자인의 99%가 사용. `font-family: Inter`만 봐도 슬롭 의심.

### 2. ❌ 한국어에 Noto Sans KR / Roboto / Malgun Gothic / Apple SD Gothic Neo 강제 금지
- ✅ 대신: Pretendard 1순위, system 폴백은 가능
- 💡 이유: Noto Sans KR은 Google 기본값(템플릿 99%), 나머지는 OS 의존 → 다른 환경 깨짐

### 3. ❌ 한국어에 `font-thin` (100), `font-extralight` (200), `font-light` (300) 사용 금지
- ✅ 대신: 본문 `font-medium` (500), 헤드라인 `font-semibold` (600) 이상
- 💡 이유: 한국어는 획이 많아 얇은 weight에서 가독성 급감

### 4. ❌ Times New Roman / Georgia / Garamond / Palatino 등 Serif를 대시보드·SaaS UI에 사용 금지
- ✅ 대신: Sans-serif (Pretendard 또는 Geist)
- 💡 이유: Serif는 에디토리얼·블로그용. 대시보드 UI에서 가독성 떨어짐

### 5. ❌ Helvetica를 디스플레이 폰트로 사용 금지
- ✅ 대신: Geist, Cabinet Grotesk (라틴), Pretendard (한국어)
- 💡 이유: Helvetica는 보편화돼 변별력 없음. 프리미엄 톤 생성 불가.

---

## 카테고리 2: 색상 (6개)

### 6. ❌ Pure Black `#000000` 사용 금지
- ✅ 대신: Off-Black `#0A0A0A`, Zinc-950 `#09090B`, Charcoal `#18181B`
- 💡 이유: Pure Black은 화면에서 너무 강해 눈 피로. 깊이감 없음. 미세하게 따뜻하거나 차가운 톤이 들어가야 프리미엄.

### 7. ❌ "LILA BAN" — 보라/파란색 AI 그래디언트 금지
- ✅ 대신: Neutral 베이스(Zinc/Slate/Stone) + 단일 액센트(Emerald, Electric Blue, Warm Amber, Deep Rose)
- 💡 이유: `from-purple-500 to-blue-500` 또는 자주색 글로우 그래디언트는 AI 생성의 가장 강한 지문

### 8. ❌ 채도 80% 이상 액센트 색상 사용 금지
- ✅ 대신: 채도 60–75% 색상 (예: Tailwind `emerald-500`, `blue-500`은 OK / `pink-400`, `purple-500`은 채도 너무 높음)
- 💡 이유: 과채도 색상은 "유아용 앱" 또는 "AI 생성" 인상

### 9. ❌ 한 페이지에 액센트 색상 2개 이상 사용 금지
- ✅ 대신: Neutral + 단일 액센트. 위계는 명도/채도 변화로
- 💡 이유: 다중 액센트는 시선 분산 → 정보 위계 무너짐

### 10. ❌ 네온/외부 글로우 그림자 금지 (`shadow-[0_0_30px_#7c3aed]` 등)
- ✅ 대신: 다음 두 가지만 — (a) 계층 필요 시 미세한 drop shadow `shadow-[0_2px_8px_rgba(0,0,0,0.06)]`, (b) Inset highlight `shadow-[inset_0_1px_1px_rgba(255,255,255,0.15)]`
- 💡 이유: 네온 글로우는 게이밍 UI 또는 AI 슬롭 인상

### 11. ❌ 색온도 혼합 금지 (따뜻한 그레이 + 차가운 그레이 동시 사용)
- ✅ 대신: 한 톤 일관 — 차가우면 Zinc/Slate, 따뜻하면 Stone
- 💡 이유: 색온도 충돌은 의도하지 않은 부조화 인상

---

## 카테고리 3: 레이아웃 (5개)

### 12. ❌ 3-column equal card layout 금지 (`grid-cols-3` 동일 크기 카드 3개)
- ✅ 대신: Bento Grid (비대칭 카드 크기), 2-column Zig-Zag, Masonry, Horizontal scroll
- 💡 이유: AI 생성의 가장 흔한 지문 — "Features" 섹션 90%가 이 패턴

### 13. ❌ Centered Hero (`text-center` H1 + 단일 CTA) 강제 금지 (DESIGN_VARIANCE ≥ 5일 때)
- ✅ 대신: Split Screen (60/40 텍스트:비주얼), Left-aligned, Asymmetric whitespace
- 💡 이유: 모든 AI 생성 랜딩이 centered hero. 차별화 안 됨

### 14. ❌ `h-screen` 사용 금지
- ✅ 대신: `min-h-[100dvh]`
- 💡 이유: iOS Safari 100vh 버그 — 주소창 표시/숨김 시 레이아웃 깨짐. `dvh`는 동적 viewport

### 15. ❌ Overlapping elements (의도적 디자인 외 요소 겹침) 금지
- ✅ 대신: 모든 요소가 자기 공간 차지, padding/margin으로 명확한 분리
- 💡 이유: AI는 종종 z-index를 헷갈려 의도치 않은 overlap 생성

### 16. ❌ `max-width` 없는 풀-블리드 본문 텍스트 금지
- ✅ 대신: `max-w-7xl mx-auto` 또는 본문은 `max-w-[65ch]`
- 💡 이유: 1920px 모니터에서 본문이 화면 끝까지 가면 가독성 파괴

---

## 카테고리 4: 타이포그래피 패턴 (4개)

### 17. ❌ 한국어 텍스트에 `word-break: normal` (기본값) 사용 금지
- ✅ 대신: 모든 한국어 컨테이너에 `word-break: keep-all` 강제
- 💡 이유: 한국어는 단어 사이 공백이 적어 단어 중간에서 줄바꿈 → 가독성 파괴

### 18. ❌ 한국어 본문 줄높이 `leading-normal` (1.5) 이하 금지
- ✅ 대신: `leading-relaxed` (1.625) 이상, 긴 본문은 `leading-loose` (2.0)
- 💡 이유: 한국어는 글자 높이가 커서 라틴보다 줄 사이 공기가 더 필요

### 19. ❌ 한국어 헤드라인에 `tracking-tighter` (-0.05em) 금지
- ✅ 대신: 한국어 디스플레이 `tracking-tight` (-0.025em), 헤드라인 `tracking-normal` (0)
- 💡 이유: 한국어 자형은 좁히면 글자 겹침. 라틴과 다름.

### 20. ❌ Oversized H1 (텍스트가 화면 가로 90% 이상 차지) 금지
- ✅ 대신: `clamp(2.5rem, 5vw + 1rem, 5rem)` 또는 `text-5xl md:text-6xl lg:text-7xl`
- 💡 이유: 큰 H1은 인상적이지만, 90% 초과는 모바일에서 깨지고 데스크톱에서 가독성 떨어짐

---

## 카테고리 5: 카피라이팅 (4개)

### 21. ❌ AI 카피 클리셰 단어 금지 — "Elevate", "Seamless", "Unleash", "Next-Gen", "Revolutionary", "Cutting-edge"
- ✅ 대신: 구체적 동사 — "줄인다", "연결한다", "본다", "정렬한다" / 영문 "ship", "track", "compose", "render"
- 💡 이유: 이 단어들은 AI 생성 마케팅 카피의 90% 이상에서 등장 → 즉시 슬롭 의심

### 22. ❌ Filler UI 텍스트 금지 — "Scroll to explore", "Swipe down", "↓" 화살표 아이콘
- ✅ 대신: 첫 폴드 자체에 매력적인 콘텐츠 → 사용자가 스크롤하고 싶게 만들기. "스크롤하라"고 명령하지 말 것.
- 💡 이유: AI는 빈 공간을 채우려고 이런 텍스트를 자주 넣음. 디자이너는 절대 안 함.

### 23. ❌ Fabricated metrics / 가짜 통계 금지 — "99.99% Uptime", "124ms avg response", "10K+ users", "50% faster"
- ✅ 대신: 실제 데이터가 있으면 정확히 인용, 없으면 비워둠. 또는 "초당 X 요청" 같은 비통계 표현.
- 💡 이유: AI는 "그럴듯해 보이는" 숫자를 마구 만들어냄 → 신뢰도 0

### 24. ❌ Generic placeholder 이름 금지 — "John Doe", "Jane Smith", "Acme Corp", "Nexus", "Lorem ipsum"
- ✅ 대신: ko 환경 → "김민서", "박지호", "주식회사 정민" / en 환경 → "Maya Chen", "Liam Park", "Northwave"
- 💡 이유: Lorem ipsum과 Acme는 AI 생성의 가장 명확한 자국

---

## 카테고리 6: 모션 (3개)

### 25. ❌ Linear easing (`ease-linear`) 사용 금지 (마이크로 인터랙션에서)
- ✅ 대신: Spring physics — `cubic-bezier(0.16, 1, 0.3, 1)` 또는 Framer Motion `spring(stiffness: 100, damping: 20)`
- 💡 이유: Linear는 기계적·저렴한 느낌. Spring은 자연스럽고 프리미엄.

### 26. ❌ `top`, `left`, `width`, `height` 애니메이션 금지
- ✅ 대신: `transform: translate3d()`, `transform: scale()`, `opacity`
- 💡 이유: GPU 가속 안 됨 → 모바일에서 끊김. 60fps 깨짐.

### 27. ❌ `useState` 기반 React 애니메이션 금지 (Framer Motion 환경에서)
- ✅ 대신: `useMotionValue` + `useTransform`
- 💡 이유: useState는 매 프레임 re-render 트리거 → 성능 저하

---

## 카테고리 7: 이미지·아이콘 (3개)

### 28. ❌ 임의 Unsplash URL 사용 금지 (`source.unsplash.com/random/` 등)
- ✅ 대신: `picsum.photos/seed/{descriptive_name}/{w}/{h}` (안정적 + seed 기반 일관성), 아바타는 `i.pravatar.cc/150?u={name}`
- 💡 이유: Unsplash random URL은 자주 깨짐. 캐시 안 되고 매번 다른 이미지 로드.

### 29. ❌ Mixed icon sets 금지 (Material + Lucide + Font Awesome 동시 사용)
- ✅ 대신: 한 세트만 — 기본 lucide. Iconify Solar는 명시 요청 시.
- 💡 이유: 아이콘 세트마다 stroke 두께·corner radius 다름 → 디자인 일관성 파괴

### 30. ❌ Emoji를 UI 라벨/버튼/네비게이션에 사용 금지
- ✅ 대신: lucide 아이콘
- 💡 이유: Emoji는 OS마다 렌더링 다름, 디자인 컨트롤 불가, AI 생성 인상

---

## 자동 검증 — 출력 직후 패턴 매칭

스킬은 모든 출력에 대해 다음을 자동 실행:

```
[스캔 대상]
- 코드 텍스트 전체 (HTML/JSX/CSS/Tailwind 클래스)
- 인라인 스타일
- 폰트 import URL
- 그라디언트 정의

[패턴 매칭]
- "Inter" 문자열 → ❌ #1
- "#000000" 또는 "#000;" → ❌ #6
- "from-purple-" + "to-blue-" → ❌ #7
- "grid-cols-3" + 동일 카드 3개 → ❌ #12
- "h-screen" → ❌ #14
- "Elevate", "Seamless", "Unleash" 등 → ❌ #21
- "John Doe", "Jane Smith", "Acme", "Lorem ipsum" → ❌ #24
- "useState" + Framer Motion + animate → ❌ #27
- "source.unsplash.com" → ❌ #28
- 한국어 텍스트 + word-break 미설정 → ❌ #17

[위반 시]
1. 위반 항목 리스트 생성
2. 자동 재생성 트리거 (최대 3회)
3. 3회 후에도 위반 시 → Pre-Flight 점수 차감 + 사용자에게 미통과 리포트
```

## 🟡 Phase 1 확장: 31-50번 (활성화됨)

총 50개 글로벌 안티-슬롭 패턴 활성화. 카테고리 8-12 신설.

---

### 카테고리 8: 접근성·포용성 (4개)

#### 31. ❌ 색상만으로 정보 전달 금지
- ✅ 대신: 색상 + 아이콘 + 텍스트 라벨 3중 명시 (예: 에러는 빨간색 + AlertCircle + "오류:")
- 💡 이유: 색맹 사용자(전체 ~8%) 정보 누락. WCAG 2.2 SC 1.4.1 위반.

#### 32. ❌ `outline-none` 단독 사용 금지 (대체 포커스 스타일 부재)
- ✅ 대신: `focus-visible:ring-2 focus-visible:ring-accent focus-visible:ring-offset-2`
- 💡 이유: 키보드 사용자는 포커스 위치 파악 불가 → 사용 불능

#### 33. ❌ 아이콘만 있는 버튼에 라벨 없음
- ✅ 대신: `aria-label="검색"` 또는 시각적으로 숨겨진 텍스트 (`<span class="sr-only">검색</span>`)
- 💡 이유: 스크린리더가 "버튼"으로만 읽음 → 의도 알 수 없음

#### 34. ❌ 이미지에 의미 없는 alt (`alt=""`, `alt="image"`)
- ✅ 대신: 콘텐츠 의미를 담은 alt 또는 장식용은 명시적 `alt=""` (빈 alt는 OK, 단 의도 명확)
- 💡 이유: 스크린리더가 "image image image"만 반복 → UX 파탄

---

### 카테고리 9: 콘텐츠·카피 추가 (4개)

#### 35. ❌ 광고 명령형 CTA 카피 금지
- ✅ 대신: 부드러운 행동 유도 — "시작하기", "둘러보기", "데모 보기" / 영문 "Try free", "See demo", "Start now"
- ❌ 금지: "지금 사세요!", "Click Here!", "Buy now!" 같은 1990년대 광고 톤

#### 36. ❌ 한국어 페이지에 영문 Lorem ipsum 사용 금지
- ✅ 대신: 의미있는 한국어 더미 또는 실제 콘텐츠 초안. 어쩔 수 없으면 `한글 더미 텍스트로 영역을 채워 넣어` 같은 자연스러운 한국어
- 💡 이유: 한국어 페이지의 라틴 lorem은 줄바꿈 정책·자간·줄높이 검증 모두 무력화

#### 37. ❌ 자동재생 비디오 음성 ON 금지
- ✅ 대신: `<video autoplay muted playsinline>` (음성 OFF) 또는 사용자 클릭 후 재생
- 💡 이유: 모바일에서 강제 재생 불가, 데스크톱에서도 사용자 충격 → 즉시 이탈

#### 38. ❌ 가짜 사용자 프로필 (Stock photo 얼굴) 금지
- ✅ 대신: `i.pravatar.cc/150?u={name}` 추상 아바타, SVG 이니셜, 실제 사용자 (동의 후)
- 💡 이유: Stock 얼굴은 한국 사이트에서 100% 인지됨 → 신뢰도 폭락

---

### 카테고리 10: 인터랙션·UX (4개)

#### 39. ❌ 의미 없는 hover 효과 (모든 요소가 transform·scale)
- ✅ 대신: hover는 클릭 가능한 요소(버튼·링크·카드)에만. 텍스트·아이콘 단독에는 hover 효과 X
- 💡 이유: hover 남용은 시각 노이즈 → 진짜 클릭 가능한 것 식별 어려움

#### 40. ❌ 모바일 터치 타겟 44×44px 미만 금지
- ✅ 대신: 모든 클릭 가능 요소 최소 `h-11 w-11` (44px) 또는 `p-3` 이상으로 hit area 확보
- 💡 이유: iOS HIG·Material Design 표준. 손가락 평균 너비 기반.

#### 41. ❌ 색상만으로 폼 에러 표시 금지 (`text-red-500` 단독)
- ✅ 대신: 에러는 색상 + 아이콘(`AlertCircle`) + 명확한 카피("이메일 형식이 올바르지 않습니다")
- 💡 이유: WCAG SC 3.3.1·1.4.1 모두 위반. 색맹 사용자 차단.

#### 42. ❌ Skeleton 모양이 실제 레이아웃과 안 맞음
- ✅ 대신: skeleton은 실제 콘텐츠와 동일한 박스·줄 높이·배치. `animate-pulse bg-zinc-200` + 정확한 사이즈
- 💡 이유: 안 맞는 skeleton은 layout shift 발생 → 사용자 피로

---

### 카테고리 11: 브랜드·미세 디테일 (4개)

#### 43. ❌ Sticky header에 그림자·blur 모두 부재
- ✅ 대신: `sticky top-0 bg-white/80 backdrop-blur-md border-b border-zinc-200` 또는 grain shadow
- 💡 이유: 본문과 navigation 분리감 없으면 스크롤 시 텍스트 nav 위로 겹쳐 가독성 파괴

#### 44. ❌ Bento Grid가 사실상 3-column equal (`col-span-1` 카드만 6개)
- ✅ 대신: 진짜 비대칭 — `col-span-2 row-span-2` + 작은 카드들 혼합
- 💡 이유: AI는 종종 grid-cols-3 회피한다고 grid-cols-6+col-span-2 6개를 만듦 → 시각적으로 동일

#### 45. ❌ 텍스트 그림자 남용 (모든 헤드라인에 `text-shadow`)
- ✅ 대신: 텍스트는 평면. 깊이는 배경·spacing으로
- 💡 이유: 텍스트 그림자는 1990년대 PowerPoint 톤. 모던 디자인에선 거의 안 씀.

#### 46. ❌ 광고 톤 카운트다운 타이머 ("⏰ 23:14:55 남음")
- ✅ 대신: 진짜 데드라인이 있을 때만, 차분하게 표시 ("4월 30일까지 가입 시")
- 💡 이유: 가짜 긴급감은 사용자에게 즉시 인지됨 → 신뢰도 0

---

### 카테고리 12: 성능·환경 (4개)

#### 47. ❌ `<img>` lazy loading 누락
- ✅ 대신: 첫 폴드 외 모든 이미지 `loading="lazy" decoding="async"`
- 💡 이유: 초기 페이지 로드 무거워짐 → LCP 점수 폭락

#### 48. ❌ Reduced-motion 미디어 쿼리 미지원
- ✅ 대신: `@media (prefers-reduced-motion: reduce) { animation: none; }` 또는 Framer Motion `useReducedMotion()`
- 💡 이유: 전정 장애 사용자에게 모션은 멀미·구토 유발

#### 49. ❌ Critical CSS 미인라인 (Tailwind CDN만 사용 시 FOUC)
- ✅ 대신: `<head>`에 critical inline `<style>` (Above-the-fold 스타일만) + Tailwind CDN async
- 💡 이유: Tailwind CDN 로드 전 unstyled 콘텐츠 깜박임 (FOUC)

#### 50. ❌ Self-closing void element 잘못된 슬래시 처리 (HTML5)
- ✅ 대신: HTML5는 `<img src="..." alt="...">` 슬래시 없음. JSX는 `<img />` (자동 변환)
- 💡 이유: HTML 검증기·일부 브라우저에서 경고. 일관성 문제.

---

## Phase 2+ 확장 예정 (참고)

추후 추가될 패턴:
- 51. RSC vs Client Component 잘못된 경계
- 52. Suspense boundary 부재
- 53. SEO sitemap·robots.txt 부재
- 54. Open Graph 이미지 사이즈 (1200×630 권장)
- 55. ... 등

Phase 1 현재 50개 활성화.
