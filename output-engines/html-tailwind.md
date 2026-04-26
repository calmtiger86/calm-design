# Output Engine: HTML + Tailwind CDN (기본)

calm-design의 기본 출력 엔진. 단일 `.html` 파일로 즉시 미리보기 가능. 빌드 과정 불필요. 디자이너·마케터·비개발자에게 최적.

## 1. 표준 HTML 골격 (필수 템플릿)

모든 HTML 출력은 이 골격으로 시작:

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{프로젝트 제목}</title>
  <meta name="description" content="{설명}">

  <!-- ① Pretendard (한국어 환경 필수) -->
  <link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>
  <link rel="stylesheet" as="style" crossorigin
    href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable.min.css" />

  <!-- ② Tailwind CSS -->
  <script src="https://cdn.tailwindcss.com"></script>

  <!-- ③ Tailwind 커스텀 설정 (Pretendard 폰트 등록 + 한국어 줄바꿈 유틸) -->
  <script>
    tailwind.config = {
      theme: {
        extend: {
          fontFamily: {
            sans: ['Pretendard Variable', 'Pretendard', 'system-ui', 'sans-serif'],
          },
          wordBreak: { 'keep': 'keep-all' }, // class="break-keep" 사용 가능
          colors: {
            // 9-섹션 DESIGN.md Section 2 컬러를 여기에 매핑
            ink: '#0A0A0A',
            mute: '#71717A',
            accent: '#10B981', // 단일 액센트
          },
        },
      },
    };
  </script>

  <!-- ④ Lucide 아이콘 (SVG inline) -->
  <script src="https://unpkg.com/lucide@latest"></script>

  <!-- ⑤ Motion One (4KB 경량 애니메이션) -->
  <script type="module">
    import { animate, stagger, inView } from "https://cdn.jsdelivr.net/npm/motion@10/+esm";
    window.motion = { animate, stagger, inView };
  </script>

  <!-- 한국어 줄바꿈 base 스타일 -->
  <style>
    h1, h2, h3, h4, h5, h6, p, li, dt, dd {
      word-break: keep-all;
      overflow-wrap: break-word;
    }
    .tabular { font-variant-numeric: tabular-nums; }
  </style>
</head>
<body class="font-sans bg-zinc-50 text-ink antialiased">

  <!-- 페이지 콘텐츠 (DESIGN.md Section 5의 페이지 구조에 따라) -->

  <!-- 모션 트리거 (Motion One) -->
  <script type="module">
    // 스크롤 진입 시 페이드+슬라이드
    document.querySelectorAll('[data-motion="fade-up"]').forEach((el, i) => {
      window.motion.inView(el, () => {
        window.motion.animate(el, 
          { opacity: [0, 1], transform: ['translateY(20px)', 'translateY(0)'] },
          { duration: 0.6, delay: i * 0.05, easing: [0.16, 1, 0.3, 1] }
        );
      }, { amount: 0.3 });
    });

    // Lucide 아이콘 렌더
    lucide.createIcons();
  </script>

</body>
</html>
```

## 2. CDN 5개 슬롯 (절대 초과 금지)

`SKILL.md` Section 6의 CDN 5개 제한 강제:

| # | CDN | 용도 | 금지 |
|---|---|---|---|
| 1 | Pretendard CDN | 한국어 폰트 | LANGUAGE=ko 환경에서 누락 시 ❌ |
| 2 | Tailwind CDN | 스타일링 | 다른 CSS 프레임워크 추가 금지 |
| 3 | Lucide | 아이콘 | Material/FontAwesome 동시 사용 금지 |
| 4 | Motion One | 애니메이션 | GSAP·anime.js 동시 사용 금지 |
| 5 | (선택 슬롯) | 사용자 요청 시 — Alpine.js, htmx 등 | 6개째 추가 금지 |

## 3. 페이지 타입별 표준 골격 (5가지)

`modes/generate.md` Step 3의 페이지 타입 분류에 따라 다른 골격 적용. 아래 5가지 케이스 모두 표준 HTML 골격(Section 1)에서 시작.

### 3a. 랜딩페이지 (7-섹션, 가장 자주 사용)

```html
<!-- 1. Navigation (sticky, 64px) -->
<nav class="sticky top-0 z-40 bg-white/80 backdrop-blur-md border-b border-zinc-200">
  <div class="max-w-7xl mx-auto px-4 md:px-6 h-16 flex items-center justify-between">
    <a href="/" class="font-bold text-lg">{Logo}</a>
    <div class="hidden md:flex gap-6 text-sm font-medium text-mute">
      <a href="#features">기능</a>
      <a href="#pricing">가격</a>
      <a href="#contact">문의</a>
    </div>
    <a href="#cta" class="rounded-full bg-accent text-white px-5 py-2 text-sm font-semibold hover:scale-[1.02] transition-transform">
      시작하기
    </a>
  </div>
</nav>

<!-- 2. Hero (Split 60/40, py-24+) -->
<section class="py-24 md:py-32 lg:py-40 bg-zinc-50">
  <div class="max-w-7xl mx-auto px-4 md:px-6 grid md:grid-cols-12 gap-8 items-center">
    <div class="md:col-span-7" data-motion="fade-up">
      <h1 class="text-5xl md:text-6xl lg:text-7xl font-bold tracking-tight leading-tight break-keep">
        {한국어 헤드라인 — word-break:keep-all 자동 적용}
      </h1>
      <p class="mt-6 text-lg md:text-xl text-mute leading-relaxed max-w-[65ch]">
        {부제 — 한국어 본문 65자 가이드}
      </p>
      <div class="mt-10 flex gap-3">
        <a href="#" class="rounded-full bg-accent text-white px-6 py-3 font-semibold hover:scale-[1.02] transition-transform">
          {Primary CTA}
        </a>
        <a href="#" class="rounded-full border border-zinc-300 px-6 py-3 font-semibold hover:bg-zinc-100">
          {Secondary CTA}
        </a>
      </div>
    </div>
    <div class="md:col-span-5" data-motion="fade-up">
      <!-- 비주얼 (이미지·영상·일러스트). 깨지는 Unsplash URL 금지 -->
      <img src="https://picsum.photos/seed/hero/640/480" 
           alt="{의미있는 alt}" 
           class="rounded-2xl shadow-[0_2px_8px_rgba(0,0,0,0.06)]"
           loading="lazy" decoding="async" />
    </div>
  </div>
</section>

<!-- 3. Social Proof (로고 클라우드 또는 사용자 수) -->
<section class="py-12 border-y border-zinc-200">
  <div class="max-w-7xl mx-auto px-4 md:px-6">
    <p class="text-center text-sm text-mute mb-6">{사용 중인 회사 / 사용자 수}</p>
    <div class="flex flex-wrap items-center justify-center gap-8 opacity-60">
      <!-- 로고 SVG들 -->
    </div>
  </div>
</section>

<!-- 4. Features (Bento Grid - 비대칭 강제) -->
<section id="features" class="py-24 md:py-32">
  <div class="max-w-7xl mx-auto px-4 md:px-6">
    <h2 class="text-4xl md:text-5xl font-bold tracking-tight break-keep">
      {Features 헤드라인}
    </h2>
    <!-- Bento Grid: 큰 카드 1 + 작은 카드 4 (비대칭) -->
    <div class="mt-12 grid grid-cols-1 md:grid-cols-3 gap-6 auto-rows-fr">
      <div class="md:col-span-2 md:row-span-2 bg-white rounded-2xl border border-zinc-200 p-8" data-motion="fade-up">
        <i data-lucide="zap" class="w-8 h-8 text-accent"></i>
        <h3 class="mt-4 text-2xl font-semibold">{큰 기능}</h3>
        <p class="mt-2 text-mute leading-relaxed">{설명}</p>
      </div>
      <!-- 작은 카드 4개 -->
    </div>
  </div>
</section>

<!-- 5. Testimonials (Masonry 또는 Carousel) -->
<!-- 6. CTA Banner (재방문 유도) -->
<!-- 7. Footer -->
```

**금지 패턴 자동 적용**:
- `grid-cols-3` + 동일 카드 3개 → ❌ (대신 Bento)
- `text-center` Hero → DESIGN_VARIANCE ≥ 5일 때 ❌

### 3b. SaaS 대시보드 (Sidebar + 메인)

```html
<div class="min-h-[100dvh] flex bg-zinc-50">
  <!-- Sidebar (고정 240px) -->
  <aside class="hidden md:flex w-60 shrink-0 flex-col border-r border-zinc-200 bg-white">
    <div class="h-16 flex items-center px-6 border-b border-zinc-200">
      <span class="font-bold text-lg">{Logo}</span>
    </div>
    <nav class="flex-1 p-4 space-y-1">
      <a href="#" class="flex items-center gap-3 rounded-lg px-3 py-2 text-sm font-medium bg-zinc-100">
        <i data-lucide="layout-dashboard" class="w-4 h-4"></i> 대시보드
      </a>
      <a href="#" class="flex items-center gap-3 rounded-lg px-3 py-2 text-sm font-medium text-mute hover:bg-zinc-50">
        <i data-lucide="users" class="w-4 h-4"></i> 사용자
      </a>
      <!-- ... -->
    </nav>
    <div class="p-4 border-t border-zinc-200">
      <!-- 사용자 프로필 카드 -->
    </div>
  </aside>

  <!-- Main -->
  <div class="flex-1 flex flex-col">
    <!-- Top Bar (sticky 64px) -->
    <header class="sticky top-0 z-30 h-16 flex items-center gap-4 px-6 bg-white/80 backdrop-blur-md border-b border-zinc-200">
      <div class="flex-1 max-w-md">
        <div class="relative">
          <i data-lucide="search" class="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-mute"></i>
          <input class="w-full h-9 pl-10 pr-12 rounded-md bg-zinc-100 text-sm placeholder:text-mute focus:outline-none focus:ring-2 focus:ring-accent" placeholder="검색..." />
          <kbd class="absolute right-2 top-1/2 -translate-y-1/2 text-xs text-mute bg-white px-1.5 py-0.5 rounded border border-zinc-200">⌘K</kbd>
        </div>
      </div>
      <button class="p-2 rounded-md hover:bg-zinc-100"><i data-lucide="bell" class="w-5 h-5"></i></button>
    </header>

    <!-- Page Content -->
    <main class="flex-1 p-6 md:p-8">
      <!-- Page Header -->
      <div class="flex items-end justify-between mb-8">
        <div>
          <h1 class="text-3xl font-bold tracking-tight break-keep">대시보드</h1>
          <p class="mt-1 text-sm text-mute">2026년 4월 25일 기준</p>
        </div>
        <button class="rounded-full bg-accent text-white px-5 py-2 text-sm font-semibold">
          <i data-lucide="plus" class="w-4 h-4"></i> 새로 만들기
        </button>
      </div>

      <!-- KPI Bento Grid (비대칭) -->
      <div class="grid grid-cols-1 md:grid-cols-4 gap-4 mb-8">
        <div class="md:col-span-2 bg-white rounded-2xl border border-zinc-200 p-6">
          <p class="text-sm text-mute">월 매출</p>
          <p class="mt-2 text-3xl font-semibold tabular">₩12,847,000</p>
          <p class="mt-1 text-xs text-emerald-600">↑ 12.4% 전월 대비</p>
        </div>
        <div class="bg-white rounded-2xl border border-zinc-200 p-6">
          <p class="text-sm text-mute">활성 사용자</p>
          <p class="mt-2 text-3xl font-semibold tabular">8,431</p>
        </div>
        <div class="bg-white rounded-2xl border border-zinc-200 p-6">
          <p class="text-sm text-mute">전환율</p>
          <p class="mt-2 text-3xl font-semibold tabular">3.2%</p>
        </div>
      </div>

      <!-- Main Chart -->
      <div class="bg-white rounded-2xl border border-zinc-200 p-6">
        <!-- Chart 영역 -->
      </div>
    </main>
  </div>
</div>
```

**대시보드 전용 규칙**:
- 모든 숫자에 `tabular` 클래스
- KPI 카드 4개는 비대칭(2-1-1 또는 1-1-1-1) — 동일 4-column 금지
- 모바일 대응: Sidebar는 `<768px`에서 hamburger drawer로 자동 전환

### 3c. 인증 폼 (로그인·회원가입, 단일 화면)

```html
<div class="min-h-[100dvh] flex items-center justify-center p-4 bg-zinc-50">
  <div class="w-full max-w-md">
    <!-- 로고 -->
    <div class="text-center mb-8">
      <span class="font-bold text-2xl">{Logo}</span>
    </div>

    <!-- Card -->
    <div class="bg-white rounded-2xl border border-zinc-200 p-8 shadow-[0_2px_8px_rgba(0,0,0,0.04)]">
      <h1 class="text-2xl font-bold tracking-tight break-keep">로그인</h1>
      <p class="mt-2 text-sm text-mute break-keep">계정이 없으시면 <a href="#" class="text-accent font-medium hover:underline">회원가입</a></p>

      <form class="mt-6 space-y-4">
        <div>
          <label for="email" class="block text-sm font-medium mb-1.5">이메일</label>
          <input type="email" id="email" class="w-full h-10 px-3 rounded-md border border-zinc-200 focus:outline-none focus:ring-2 focus:ring-accent" placeholder="you@example.com" />
        </div>
        <div>
          <label for="pwd" class="block text-sm font-medium mb-1.5">비밀번호</label>
          <input type="password" id="pwd" class="w-full h-10 px-3 rounded-md border border-zinc-200 focus:outline-none focus:ring-2 focus:ring-accent" />
        </div>
        <button type="submit" class="w-full h-11 rounded-full bg-accent text-white font-semibold hover:scale-[1.01] active:scale-[0.99] transition-transform">
          로그인
        </button>
      </form>

      <div class="mt-6 pt-6 border-t border-zinc-200 text-center text-sm">
        <a href="#" class="text-mute hover:text-ink">비밀번호를 잊으셨나요?</a>
      </div>
    </div>
  </div>
</div>
```

### 3d. 모바일 앱 화면 (세로형, 9:16 가까운 비율 가정)

```html
<div class="min-h-[100dvh] max-w-md mx-auto bg-white flex flex-col">
  <!-- Top Bar (모바일 표준 56px) -->
  <header class="h-14 flex items-center justify-between px-4 border-b border-zinc-200">
    <button class="p-2 -ml-2"><i data-lucide="chevron-left" class="w-6 h-6"></i></button>
    <h1 class="text-base font-semibold">화면 제목</h1>
    <button class="p-2 -mr-2"><i data-lucide="more-vertical" class="w-6 h-6"></i></button>
  </header>

  <!-- Scrollable Content -->
  <main class="flex-1 overflow-y-auto pb-20"> <!-- pb-20: bottom tab 영역 확보 -->
    <!-- 콘텐츠 -->
    <div class="p-4 space-y-4">
      <!-- 카드들 -->
    </div>
  </main>

  <!-- Bottom Tab Bar (4-5개 탭, fixed) -->
  <nav class="fixed bottom-0 inset-x-0 max-w-md mx-auto h-16 grid grid-cols-4 border-t border-zinc-200 bg-white/95 backdrop-blur-md">
    <a href="#" class="flex flex-col items-center justify-center gap-1 text-accent">
      <i data-lucide="home" class="w-5 h-5"></i>
      <span class="text-[10px] font-medium">홈</span>
    </a>
    <a href="#" class="flex flex-col items-center justify-center gap-1 text-mute">
      <i data-lucide="search" class="w-5 h-5"></i>
      <span class="text-[10px] font-medium">검색</span>
    </a>
    <a href="#" class="flex flex-col items-center justify-center gap-1 text-mute">
      <i data-lucide="bell" class="w-5 h-5"></i>
      <span class="text-[10px] font-medium">알림</span>
    </a>
    <a href="#" class="flex flex-col items-center justify-center gap-1 text-mute">
      <i data-lucide="user" class="w-5 h-5"></i>
      <span class="text-[10px] font-medium">마이</span>
    </a>
  </nav>
</div>
```

**모바일 전용 규칙**:
- Touch target ≥ 44x44px (Pre-Flight, iOS HIG)
- `max-w-md mx-auto`로 데스크톱에서도 모바일 비율 유지
- Bottom tab은 `fixed bottom-0` + `pb-20` 본문에 강제

### 3e. 마케팅 콘텐츠/블로그 (장문 본문 중심)

```html
<div class="min-h-[100dvh] bg-white">
  <!-- Minimal Nav -->
  <nav class="h-14 border-b border-zinc-200 flex items-center px-4 md:px-6">
    <span class="font-bold">{Logo}</span>
  </nav>

  <!-- Article Hero -->
  <article class="max-w-3xl mx-auto px-4 md:px-6 py-12 md:py-16">
    <!-- Meta -->
    <div class="text-sm text-mute flex items-center gap-3 mb-4">
      <span>2026년 4월 25일</span>
      <span>·</span>
      <span>김민서</span>
      <span>·</span>
      <span>5분 읽기</span>
    </div>

    <!-- Title -->
    <h1 class="text-4xl md:text-5xl font-bold tracking-tight leading-tight break-keep">
      차분한 디자인이 좋은 디자인이다
    </h1>
    <p class="mt-4 text-lg md:text-xl text-mute leading-relaxed break-keep">
      AI가 만든 디자인의 티를 어떻게 없앨 것인가에 대한 이야기.
    </p>

    <!-- Cover Image -->
    <img src="https://picsum.photos/seed/article-cover/1200/600" alt="..." class="mt-10 rounded-2xl" loading="lazy" />

    <!-- Body (max-w-[65ch] 한국어 가독성) -->
    <div class="mt-12 prose prose-zinc max-w-[65ch] mx-auto">
      <p class="leading-loose break-keep">
        본문 첫 문단. 한국어 본문은 <code>leading-loose</code>로 충분한 호흡감을 준다...
      </p>
      <h2 class="break-keep">중간 제목</h2>
      <p class="leading-loose break-keep">
        본문 두 번째 문단...
      </p>
      <!-- ... -->
    </div>
  </article>

  <!-- Footer Minimal -->
</div>
```

**블로그 전용 규칙**:
- 본문 너비 `max-w-[65ch]` 강제 (한국어 가독성)
- `prose prose-zinc` Tailwind Typography 플러그인 활용 (또는 base 스타일 직접 정의)
- `leading-loose` (2.0) 본문에 사용 — 일반 페이지의 `leading-relaxed` (1.625)보다 더 여유

## 4. 한국어 자동 적용 규칙 (LANGUAGE=ko)

모든 HTML 출력에서 자동 강제:

```html
<!-- ① <html lang="ko"> -->
<html lang="ko">

<!-- ② Pretendard CDN 1번 슬롯 -->

<!-- ③ <body>에 font-sans (Tailwind config에서 Pretendard로 매핑됨) -->
<body class="font-sans">

<!-- ④ 헤드라인·본문 자동 break-keep -->
<h1 class="... break-keep">한국어 헤드라인</h1>
<p class="... leading-relaxed max-w-[65ch]">한국어 본문</p>

<!-- ⑤ 숫자에 tabular -->
<span class="tabular font-medium">12,847</span>
```

## 5. 모션 패턴 (Motion One 활용)

### 5.1 페이드+슬라이드 (가장 흔한 진입 모션)

```html
<div data-motion="fade-up">콘텐츠</div>
```

```javascript
window.motion.inView(el, () => {
  window.motion.animate(el,
    { opacity: [0, 1], transform: ['translateY(20px)', 'translateY(0)'] },
    { duration: 0.6, easing: [0.16, 1, 0.3, 1] }
  );
}, { amount: 0.3 });
```

### 5.2 Stagger (리스트 순차 등장)

```javascript
window.motion.animate('.feature-card',
  { opacity: [0, 1], transform: ['translateY(20px)', 'translateY(0)'] },
  { delay: window.motion.stagger(0.05), easing: [0.16, 1, 0.3, 1] }
);
```

### 5.3 Hover scale (CTA 버튼)

```html
<button class="rounded-full bg-accent text-white px-6 py-3 hover:scale-[1.02] active:scale-[0.98] transition-transform duration-300">
  CTA
</button>
```

→ Tailwind의 `transition-transform`만 사용. `top/left/width/height` 절대 X (`ai-tells-blocklist.md` #26 위반).

## 6. 이미지 처리

| 용도 | URL 패턴 | 이유 |
|---|---|---|
| 풍경·배경 | `https://picsum.photos/seed/{name}/{w}/{h}` | seed 기반 일관성, 안 깨짐 |
| 아바타 | `https://i.pravatar.cc/150?u={name}` | 안정적 |
| 로고 | 인라인 SVG 또는 자체 호스팅 | CDN 의존성 ↓ |
| **금지** | `source.unsplash.com/random/...` | 자주 깨짐, 캐시 안 됨 |

모든 `<img>`에 `loading="lazy" decoding="async"` 자동 추가.

## 7. 상태 처리 (Empty/Error/Loading)

데이터 컴포넌트에 다음 패턴 의무:

```html
<!-- Empty State -->
<div class="text-center py-12">
  <svg class="mx-auto w-16 h-16 text-mute"><!-- 컴포지션 일러스트 --></svg>
  <p class="mt-4 font-medium">{빈 상태 카피}</p>
  <p class="mt-1 text-sm text-mute">{보조 카피}</p>
</div>

<!-- Loading (Skeleton, 실제 레이아웃 매칭) -->
<div class="animate-pulse">
  <div class="h-6 bg-zinc-200 rounded w-3/4"></div>
  <div class="mt-3 h-4 bg-zinc-200 rounded w-1/2"></div>
</div>

<!-- Error -->
<div class="rounded-xl bg-red-50 border border-red-200 p-4">
  <p class="font-medium text-red-900">{에러 제목}</p>
  <p class="mt-1 text-sm text-red-700">{설명}</p>
  <button class="mt-3 text-sm font-semibold text-red-900 hover:underline">다시 시도</button>
</div>
```

## 8. 검증 (Pre-Flight 통합)

HTML 출력 직후 자동 체크:

- [ ] CDN 5개 이하
- [ ] `<html lang="ko">` (LANGUAGE=ko)
- [ ] Pretendard CDN 포함
- [ ] Tailwind config에 fontFamily.sans = Pretendard
- [ ] body에 `font-sans antialiased`
- [ ] 한국어 텍스트 컨테이너에 `break-keep` 또는 inline `word-break:keep-all`
- [ ] `h-screen` 부재 → `min-h-[100dvh]`
- [ ] `grid-cols-3` 동일 카드 3개 부재
- [ ] `<img>`에 `loading="lazy"`, `alt` 속성

위 9개 중 하나라도 실패 → Pre-Flight 차감.
