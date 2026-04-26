# Prompt Enhancement — 4기법 + 한국어 키워드 매핑

> **Inspired by**: [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills) (Apache 2.0) — enhance-prompt 4기법 원조 (UI/UX 키워드 변환·분위기 증폭·페이지 구조화·색상 형식화)
>
> **calm-design 확장**: 한국어 매핑 30+ 항목 (한국 SaaS 디자인 시스템 관찰 기반) + 사용자 오버라이드 메커니즘 (`.calm-design/keyword-overrides.md`) + 한국어 분위기 단어 증폭

사용자의 모호한 디자인 요청을 calm-design 출력 엔진이 최적으로 작동할 수 있는 구조화된 프롬프트로 변환.

> 이 파일은 SKILL.md가 모든 모드에서 ALWAYS 로드한다.

## 0. 강화 파이프라인 한 줄 요약

```
[사용자 입력]
   ↓
A. UI/UX 키워드 변환 (한국어/영문 매핑)
   ↓
B. 분위기 증폭 (한 단어 → 구체적 묘사 5-7개)
   ↓
C. 페이지 구조 자동 생성 (섹션 번호 매김)
   ↓
D. 색상·타이포 형식화 (이름 + hex + 역할)
   ↓
[강화된 프롬프트] → DESIGN.md 생성으로 전달
```

## A. UI/UX 키워드 변환

사용자가 모호하게 말한 것을 **명확하고 표준화된 디자인 어휘**로 변환.

### A.0 매핑 표 출처와 한계 (정직한 명시)

> 아래 한국어 매핑 표는 **Phase 0 단계의 경험적 가이드라인**이며, 다음 출처를 기반으로 작성:
> - 토스(toss.im), 당근(daangn.com), 카카오엔터프라이즈, 네이버, 라인의 공개 디자인 시스템 문서
> - 한국 SaaS 인터페이스 관찰 (2024-2026 표준 패턴)
> - 한국 UX 커뮤니티의 일반적 어휘 사용
>
> **한계**: 한국 디자인 커뮤니티의 모든 표준 어휘를 포괄하지 않으며, 회사·도메인마다 같은 한국어 단어가 다른 의미일 수 있다. Phase 1에서 한국 공공 디자인 시스템(KDS·정부24 등) 검증 후 업데이트 예정.

> **사용자가 매핑을 추가·수정하려면**: 프로젝트 루트에 `.calm-design/keyword-overrides.md` 파일을 만들어 다음 형식으로 추가:
> ```yaml
> overrides:
>   - korean: "장바구니 아이콘"
>     standard: "Cart Icon Button"
>     english: "cart, shopping bag"
>   - korean: "결제하기"
>     standard: "Checkout CTA"
>     english: "checkout, pay now"
> ```
> 스킬은 매 호출 시 이 파일을 자동 로드하여 우선 적용한다 (기본 매핑보다 우선).

### A.1 한국어 → 표준 디자인 용어 매핑

| 사용자가 말함 | 표준 디자인 용어 | 영문 키워드 |
|---|---|---|
| "맨 위 메뉴", "상단 메뉴" | Navigation Bar / Header | `nav`, `header` |
| "햄버거 버튼" | Hamburger Menu | `mobile menu`, `nav drawer` |
| "큰 글씨 영역", "첫 화면 큰 글" | Hero Section | `hero`, `above-the-fold` |
| "특징 박스들", "장점 카드" | Feature Cards / Bento Grid | `features`, `bento`, `grid` |
| "후기", "리뷰", "사용자 말" | Testimonials / Social Proof | `testimonials`, `reviews` |
| "신청하기 버튼", "구매 버튼" | Primary CTA Button | `primary cta`, `conversion button` |
| "팝업", "모달창" | Modal / Dialog | `modal`, `dialog`, `overlay` |
| "메시지 풍선", "알림" | Toast / Notification | `toast`, `notification`, `alert` |
| "입력칸", "검색창" | Input Field / Search | `input`, `text field`, `search bar` |
| "선택 메뉴", "드롭다운" | Dropdown / Select | `dropdown`, `select`, `menu` |
| "탭", "전환 메뉴" | Tabs | `tabs`, `tab navigation` |
| "표", "데이터 목록" | Data Table | `table`, `data grid` |
| "그래프", "차트" | Chart / Graph | `chart`, `data viz` |
| "사이드바", "옆 메뉴" | Sidebar | `sidebar`, `side nav` |
| "푸터", "맨 아래" | Footer | `footer` |
| "로딩 중 표시" | Skeleton / Spinner | `skeleton`, `loader`, `spinner` |
| "비어있을 때 화면" | Empty State | `empty state`, `placeholder view` |
| "오류 화면" | Error State | `error state`, `error boundary` |
| "확인창", "삭제 확인" | Confirmation Dialog | `confirm dialog`, `destructive action` |
| "사용자 프로필" | User Profile / Avatar | `profile`, `avatar`, `user card` |

### A.2 영문 → 표준 매핑 (동일하지만 변별 포인트)

| Vague | Enhanced |
|---|---|
| "menu at top" | Navigation bar with logo + menu items + auth CTA |
| "button" | Primary call-to-action button (filled, accent color) |
| "box" | Card container (white surface, rounded-2xl, border) |
| "popup" | Modal overlay with backdrop blur, centered card |
| "image and text" | Split-screen 60/40 (text left, visual right) |

## B. 분위기 증폭 (Atmosphere Amplification)

사용자가 한 단어로 말한 분위기를 **5-7개의 구체적 묘사**로 증폭.

### B.1 한국어 분위기 단어 매핑

| 사용자 단어 | 증폭된 묘사 |
|---|---|
| "깔끔한", "심플한" | Generous whitespace · refined neutral palette · Pretendard semibold · single accent · no decorative noise |
| "고급스러운", "프리미엄" | Off-Black backgrounds · Pretendard 700+ weight · Spring physics motion · subtle inset highlights · single Emerald or Amber accent |
| "신뢰감", "전문적" | Cool neutral (Slate/Zinc) · structured grid · tabular numerics · clear hierarchy · no playful illustrations |
| "재미있는", "발랄한" | Warm accent (Amber/Rose) · bouncy spring motion (stiffness 200) · rounded corners (16-24px) · hand-drawn or geometric illustrations |
| "차분한", "조용한" | Stone neutrals · `MOTION_INTENSITY=3` · longer transition durations (400-600ms) · single muted accent · generous line-height |
| "강렬한", "역동적" | High-contrast (Off-Black + Electric Blue) · bold display weight · staggered entry animations · asymmetric layout |
| "트렌디한", "요즘 느낌" | Bento Grid · inline image typography · `clamp()` responsive type · Cabinet Grotesk display · `MOTION_INTENSITY=7` |
| "데이터 중심", "분석적" | High `VISUAL_DENSITY=8+` · monospace numerics · sparklines · table-first layout · Grayscale UI + accent for key metrics |
| "B2B SaaS" | Linear/Vercel inspired · dark mode primary · functional UI · keyboard-first hints (`⌘K`) · tabular numerics |
| "랜딩페이지" | Hero with single CTA · Social proof strip · Feature Bento · Testimonials · Pricing · CTA banner · Footer (7개 섹션 의무) |

### B.2 영문 분위기 단어 매핑

| Vague | Amplified |
|---|---|
| "modern" | clean · minimal · generous whitespace · neutral palette · sans-serif display |
| "professional" | sophisticated · trustworthy · subtle shadows · structured grid · cool neutrals |
| "playful" | vibrant · rounded corners · bouncy springs · warm accents · illustrative |
| "luxury" | dramatic · refined typography · tinted shadows · single deep accent · slow motion |
| "tech" | dark mode · monospace numerics · grid lines · asymmetric · electric accent |

## C. 페이지 구조 자동 생성

사용자가 페이지 종류만 말하면 (예: "랜딩페이지 만들어줘"), 스킬은 **자동으로 표준 섹션 구조**를 제안.

### C.1 페이지 타입별 표준 섹션

#### 랜딩페이지 (Conversion-focused)
```
1. Navigation (Logo + 메뉴 3-5개 + 우측 CTA)
2. Hero (헤드라인 + 부제 + Primary CTA + 비주얼)
3. Social Proof Strip (로고 클라우드 또는 사용자 수)
4. Features (Bento Grid 3-5개, 비대칭)
5. Use Cases / Testimonials
6. Pricing (선택, B2B SaaS면 필수)
7. CTA Banner (재방문 유도)
8. Footer (링크·법적 고지·소셜)
```

#### SaaS 대시보드
```
1. Sidebar (Logo + Nav + 사용자 프로필 하단)
2. Top Bar (검색 + 알림 + 사용자 메뉴)
3. Page Header (제목 + 액션 버튼들)
4. KPI Cards (4개, 비대칭 가능)
5. Main Chart 또는 Data Table
6. Secondary Sections (활동 피드, 빠른 작업 등)
```

#### 모바일 앱 화면
```
1. Status Bar 영역 (notch 고려)
2. Top Bar (뒤로 + 제목 + 액션)
3. Main Content (스크롤 가능)
4. Bottom Tab Bar (4-5개 탭)
또는
4'. Floating Action Button + Bottom Sheet
```

#### 마케팅 콘텐츠 페이지 (블로그/아티클)
```
1. Header (얇은 nav)
2. Article Hero (제목 + 메타 + 커버 이미지)
3. Body (본문 max-w-[65ch])
4. Related Articles
5. Footer
```

### C.2 섹션 다양화 규칙

`DESIGN_VARIANCE ≥ 5`일 때 강제: **인접 섹션은 다른 레이아웃 패턴** 사용.

```
✅ 허용:
Hero (Split 60/40) → Features (Bento) → Testimonials (Masonry) → CTA (Full-bleed) → Footer (Minimal)

❌ 금지:
Hero (Centered) → Features (Centered) → Testimonials (Centered) → CTA (Centered)
```

## D. 색상·타이포 형식화

사용자가 색상을 말하면 **이름 + hex + 역할 3-필드** 강제.

### D.1 색상 입력 변환

| 사용자 입력 | 변환 결과 |
|---|---|
| "파란색" | `Electric Blue (#3B82F6) — Primary accent for CTAs and links` |
| "녹색 강조" | `Calm Emerald (#10B981) — Success states and primary CTA` |
| "다크모드" | `Off-Black (#0A0A0A) canvas + Surface (#171717) cards + Mute (#71717A) text` |
| "베이지·따뜻한 톤" | `Stone-50 (#FAFAF9) canvas + Stone-900 (#1C1917) ink + Warm Amber (#F59E0B) accent` |
| "토스 분위기" | `Toss Blue (#3182F6) accent + Pretendard + Soft white surface + 채도 ↓ 70%` (Match-Reference 모드 트리거) |

### D.2 타이포 입력 변환

| 사용자 입력 | 변환 결과 |
|---|---|
| "큰 제목" | `text-5xl md:text-6xl lg:text-7xl tracking-tight font-bold leading-tight word-break:keep-all` |
| "본문 글" | `text-base md:text-lg leading-relaxed max-w-[65ch] text-mute` |
| "라벨" | `text-xs font-medium tracking-wide uppercase text-mute` |
| "숫자 강조 (대시보드)" | `text-3xl md:text-4xl font-semibold tabular-nums font-mono` |

## E. 강화 결과 출력 포맷

스킬이 내부적으로 사용자 입력을 다음 구조화된 객체로 변환:

```yaml
intent_summary: "한국 SaaS B2B 대시보드, 차분하고 신뢰감 있는 톤"
mode: A (Generate)
language: ko
dials:
  variance: 5
  motion: 4
  density: 7
  language: ko
amplified_atmosphere:
  - "Cool neutral (Slate/Zinc)"
  - "structured grid"
  - "tabular numerics"
  - "clear hierarchy"
  - "no playful illustrations"
  - "Pretendard 600+ weight"
page_structure:
  type: "SaaS dashboard"
  sections:
    - { name: "Sidebar", layout: "fixed-left, 240px" }
    - { name: "Top Bar", layout: "sticky, 64px" }
    - { name: "Page Header", layout: "title + actions" }
    - { name: "KPI Cards", layout: "Bento Grid 4 cards, 비대칭" }
    - { name: "Main Chart", layout: "full-width" }
    - { name: "Data Table", layout: "below chart" }
color_palette:
  - { name: "Canvas", hex: "#FAFAFA", role: "page background" }
  - { name: "Surface", hex: "#FFFFFF", role: "card background" }
  - { name: "Ink", hex: "#0A0A0A", role: "primary text" }
  - { name: "Mute", hex: "#71717A", role: "secondary text" }
  - { name: "Border", hex: "#E4E4E7", role: "1px dividers" }
  - { name: "Accent", hex: "#10B981", role: "primary CTA, success" }
typography:
  font_family_ko: "Pretendard, system-ui, sans-serif"
  display: "text-4xl md:text-5xl tracking-tight font-bold"
  body: "text-base leading-relaxed max-w-[65ch]"
  numeric: "tabular-nums font-mono"
```

이 객체가 `references/design-md-spec.md`의 9-섹션 DESIGN.md 생성기로 전달된다.

## F. 강화 실패 케이스 (사용자 확인 필요)

다음 상황에선 강화하지 말고 **사용자에게 명시적 질문**:

1. 페이지 종류 모호: "디자인 만들어줘" (랜딩? 대시보드? 모바일?)
2. 모순: "미니멀하면서 데이터 많은" (VARIANCE↓ vs DENSITY↑ 충돌)
3. 레퍼런스 모호: "트렌디하게" (어떤 트렌드? 글래스모피즘? 브루탈리즘?)

→ AskUserQuestion 트리거로 2-4개 옵션 제시 후 진행.
