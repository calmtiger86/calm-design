# Pre-Flight Checklist — 30항목 출력 검증

> **Inspired by**: [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) — Pre-Flight Checklist 17-21항목 원조
>
> **calm-design 확장**: 30항목 (Phase 1)으로 확장 — 한국어 환경 4항목, 접근성 4항목, 폼 1항목, 환경·SEO 3항목, 성능 2항목 추가. WCAG 2.0 luminance 정밀 계산(`scripts/color-utils.py`) 통합. ⚠️ 부분 통과 단계 도입 (단순 ✅/❌ 이분법 회피).

calm-design이 어떤 출력이든 사용자에게 전달하기 직전 자동 실행하는 검증 게이트. 30항목 중 1개라도 ❌면 → `self-critique-loop`가 핀포인트 재생성.

## 채점 방식

각 항목은 **`✅ 통과 / ⚠️ 부분 / ❌ 실패`** 3-단계.

| 채점 결과 | 처리 |
|---|---|
| 21개 모두 ✅ | 통과 → 사용자에게 전달 |
| ❌ 1개 이상 | 자동 재생성 (해당 항목만 핀포인트 수정) |
| ⚠️ 3개 이상 + ❌ 0개 | 통과하되 사용자에게 경고 리포트 동봉 |
| 3회 재생성 후에도 ❌ 잔존 | 부분 결과 + 미통과 항목 명시 리포트 함께 전달 |

## 21개 체크 항목 (카테고리별)

---

### 📐 카테고리 1: 레이아웃 (5항목)

#### 1. 모바일 레이아웃 붕괴 가드
- ✅ `<768px`에서 다중 컬럼이 단일 컬럼으로 자동 붕괴
- ❌ Horizontal scroll 발생 (의도된 carousel 제외)
- 검증: `md:grid-cols-N` 패턴 + `grid-cols-1` 기본값 존재 여부

#### 2. Full-height 섹션 안전
- ✅ `min-h-[100dvh]` 사용 (또는 `min-h-screen` + dvh fallback)
- ❌ `h-screen` 사용 → iOS Safari 100vh 버그
- 검증: 코드에 `h-screen` 문자열 미포함

#### 3. Max-width 제약 강제
- ✅ 본문 컨테이너 `max-w-7xl mx-auto px-4 md:px-6` 또는 `max-w-[65ch]`
- ❌ 본문이 화면 끝까지 풀-블리드 (1920px+ 모니터에서 가독성 깨짐)

#### 4. 섹션 다양화 (VARIANCE ≥ 5일 때)
- ✅ 인접 섹션이 서로 다른 레이아웃 패턴 (Hero Split → Features Bento → Testimonials Masonry)
- ❌ 모든 섹션이 동일 패턴 (예: 4개 섹션 모두 centered)

#### 5. 3-column equal cards 부재
- ✅ Features는 Bento, Zig-Zag, Masonry 중 하나
- ❌ `grid-cols-3` + 동일 크기 카드 3개 (AI 슬롭 #1)

---

### 🎨 카테고리 2: 색상·타이포 (5항목)

#### 6. Pure Black 부재
- ✅ Off-Black `#0A0A0A`, Zinc-950, Charcoal 사용
- ❌ `#000000`, `#000`, `bg-black`, `text-black` 사용

#### 7. LILA BAN — 보라/파란 AI 그래디언트 부재
- ✅ Neutral 베이스 + 단일 액센트
- ❌ `from-purple-` `to-blue-`, 자주색 글로우 그림자

#### 8. 단일 액센트 색상
- ✅ 한 페이지 액센트 1개 (Emerald 또는 Blue 또는 Amber 또는 Rose 중 하나)
- ⚠️ 액센트 2개 (의도적 듀얼 톤일 때만 허용)
- ❌ 3개 이상

#### 9. Inter 폰트 부재
- ✅ ko: Pretendard / en: Geist, Cabinet Grotesk, Outfit, Satoshi
- ❌ `font-family: Inter` 또는 Inter Google Fonts import

#### 10. 한국어 환경 Pretendard 강제 (LANGUAGE=ko일 때)
- ✅ `font-family`에 Pretendard 1순위
- ❌ Noto Sans KR, Roboto, Malgun Gothic 사용

---

### 🇰🇷 카테고리 3: 한국어 친화 (4항목, LANGUAGE=ko일 때만)

#### 11. `word-break: keep-all` 적용
- ✅ 모든 한국어 헤드라인·본문 컨테이너에 적용
- ❌ 한국어 텍스트 + `word-break: normal` 또는 미설정

#### 12. 한국어 줄높이 충분
- ✅ 헤드라인 `leading-tight` 이상 (1.25), 본문 `leading-relaxed` 이상 (1.625)
- ❌ 한국어 본문 `leading-normal` (1.5) 또는 `leading-tight`

#### 13. 한국어 weight 적정
- ✅ 본문 ≥ 400 (`font-medium`), 헤드라인 ≥ 600 (`font-semibold`)
- ❌ 한국어 텍스트에 `font-thin`, `font-extralight`, `font-light`

#### 14. 한국어 본문 너비 제약
- ✅ `max-w-[65ch]` 또는 32–38rem 범위
- ⚠️ `max-w-prose` (라틴 75자 → 한국어 너무 길음)

---

### 🎭 카테고리 4: 모션·인터랙션 (3항목)

#### 15. GPU 친화 애니메이션
- ✅ `transform`, `opacity`만 애니메이션
- ❌ `top`, `left`, `width`, `height` 애니메이션

#### 16. Spring physics 적용
- ✅ `cubic-bezier(0.16, 1, 0.3, 1)` 또는 Framer Motion `spring`
- ❌ `ease-linear` 마이크로 인터랙션, default `transition`

#### 17. 컴포넌트 6개 상태 명시
- ✅ Button/Input 등 인터랙티브 요소에 Default/Hover/Focus/Active/Disabled/Loading 6개 상태 모두 정의
- ⚠️ 5개 상태 (Loading 누락이 가장 흔함)
- ❌ 3개 미만

---

### 📝 카테고리 5: 콘텐츠 품질 (3항목)

#### 18. AI 카피 클리셰 부재
- ✅ 구체적 동사 사용
- ❌ "Elevate", "Seamless", "Unleash", "Next-Gen", "Revolutionary" 등 등장

#### 19. Generic placeholder 부재
- ✅ ko: 김민서·박지호·주식회사 정민 / en: Maya Chen·Liam Park·Northwave 같은 자연스러운 이름
- ❌ "John Doe", "Jane Smith", "Acme", "Lorem ipsum"

#### 20. Filler UI 텍스트 부재
- ✅ 의미 있는 콘텐츠로 첫 폴드 채움
- ❌ "Scroll to explore", "Swipe down", scroll 화살표 아이콘

---

### 🛡️ 카테고리 6: 상태 처리 (1항목)

#### 21. Empty / Error / Loading 상태 명시
- ✅ 데이터를 보여주는 모든 컴포넌트에 3가지 상태(빈 / 오류 / 로딩) 명시
  - Empty: 컴포지션된 일러스트 + 가이드 카피
  - Error: 인라인 에러 메시지 + 재시도 액션
  - Loading: skeleton (실제 레이아웃 매칭) — `Loading...` 단순 텍스트 X
- ⚠️ 2개만 명시
- ❌ 모두 미명시 (raw 데이터 컨테이너만)

---

## 자동 검증 실행 흐름

```
출력 생성 완료
   ↓
21항목 자동 스캔 (정규식 + AST 분석 + Vision 호출 일부)
   ↓
점수 계산 → ✅/⚠️/❌ 매핑
   ↓
[모두 ✅] → 통과
[❌ 있음] → self-critique-loop으로 전달, 위반 항목만 핀포인트 재생성
[3회 시도 후 잔존] → 부분 통과 결과 + 미통과 리포트
```

## 사용자에게 동봉되는 리포트 포맷

```markdown
## 🛫 Pre-Flight Report

✅ 통과: 19/21
⚠️ 경고: 1
❌ 실패: 1

### ✅ 통과 항목 (19개)
1. 모바일 레이아웃 붕괴 가드
2. Full-height 섹션 안전 (`min-h-[100dvh]`)
3. Max-width 제약 강제
4. 3-column equal cards 부재
5. Pure Black 부재
... (생략)

### ⚠️ 경고
- 항목 17 (컴포넌트 상태): Button에 Loading 상태 누락. 요청 시 추가 가능.

### ❌ 실패 (자동 재생성 후에도 잔존)
- 항목 21 (Empty State): KPI 카드의 데이터 0건일 때 빈 컨테이너만 출력. → 사용자가 빈 상태 카피를 직접 정의 필요.

### 재생성 횟수: 2회
```

## ♿ Phase 1 확장: 접근성·SEO·환경 항목 (22-30, 활성화됨)

Phase 1에서 9개 항목 추가. 총 30개 항목 활성화. 검증 방법은 정적 분석 + Vision 보완.

### 카테고리 7: 접근성 (Accessibility, 4항목)

#### 22. WCAG 2.2 AA 색상 대비
- ✅ 본문 텍스트 색상-배경 대비 ≥ 4.5:1
- ✅ 큰 텍스트(18pt+, 14pt bold+) 대비 ≥ 3:1
- ✅ UI 컴포넌트(버튼·아이콘) 대비 ≥ 3:1
- ❌ Mute text on light bg 대비 < 4.5:1 (가장 흔한 함정)
- 검증: hex 추출 후 WCAG luminance 계산 (정적 분석)

#### 23. ARIA 라벨 명시 (인터랙티브 요소)
- ✅ 아이콘만 있는 버튼에 `aria-label` 또는 시각적으로 숨겨진 텍스트
- ✅ 모달/Dialog에 `role="dialog"` + `aria-labelledby`
- ✅ 토글 버튼에 `aria-pressed`, 탭에 `role="tab"` + `aria-selected`
- ❌ `<button><Icon/></button>` 라벨 없음
- 검증: AST 분석 — 텍스트 콘텐츠 없는 버튼·링크 검출

#### 24. 키보드 포커스 가시성
- ✅ 모든 인터랙티브 요소에 `focus-visible:ring-2 focus-visible:ring-accent focus-visible:ring-offset-2`
- ❌ `outline-none` 후 대체 포커스 스타일 부재
- 검증: 정규식 — `outline-none` 단독 사용 검출

#### 25. 이미지 alt 속성 의미있는 설명
- ✅ 모든 `<img>`에 `alt` 속성 존재 + 비어있지 않음 또는 장식용은 `alt=""`
- ❌ `alt` 누락, `alt="image"`, `alt="photo"` 같은 무의미 alt
- 검증: 정규식 — `<img` 태그 alt 속성 추출

### 카테고리 8: 폼·UX (3항목)

#### 26. Form input 라벨 연결
- ✅ 모든 `<input>`에 `<label htmlFor="id">` 또는 `aria-label`
- ❌ `<label>` 부재 또는 `htmlFor` 미연결
- 검증: AST 분석 — input id ↔ label htmlFor 매칭

### 카테고리 9: 환경·다크모드·SEO (3항목)

#### 27. 다크모드 색상 토큰 매핑
- ✅ `dark:` Tailwind 클래스 또는 CSS 변수 `:root` + `.dark` 분기 존재
- ⚠️ 다크모드 미지원 (작은 페이지면 OK, B2B SaaS는 권장)
- 검증: 정규식 — `dark:` 클래스 또는 `[data-theme="dark"]` 패턴

#### 28. SEO meta tags
- ✅ `<title>`, `<meta name="description">`, `<meta property="og:image">` 모두 존재
- ⚠️ 일부 누락 (랜딩페이지면 ❌, 대시보드 내부면 OK)
- 검증: HTML head 파싱

### 카테고리 10: 성능·모션 (2항목)

#### 29. Sticky header z-index 충돌 부재
- ✅ Sticky 요소들이 명시적 z-index (nav=40, top-bar=30, modal=50 식)
- ❌ z-index 미명시로 다른 요소와 겹침 발생 가능
- 검증: 정적 분석 — `sticky` 또는 `fixed` 클래스 + z-index 매칭

#### 30. Reduced-motion 미디어 쿼리 지원
- ✅ `@media (prefers-reduced-motion: reduce)` 또는 Framer Motion `useReducedMotion` 사용
- ⚠️ 미지원 (모션 강도 ≥ 6일 때 권장)
- 검증: 정규식 매칭

---

## Phase 2+ 확장 예정 항목 (참고, 30+ 단계)

추후 추가 예정:
- 31. 색상만으로 정보 전달 부재 (색맹 대응)
- 32. 폼 에러 메시지 시각적 명시 (붉은 색상 + 아이콘 + 텍스트)
- 33. 이미지 lazy loading 명시 (`loading="lazy"`)
- 34. Critical CSS 인라인 (Phase 4 — preview-catalog 통합)

이상 4개는 Phase 2+에서 추가. 현재 Phase 1은 30항목으로 동작.
