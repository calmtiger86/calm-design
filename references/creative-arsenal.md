# Creative Arsenal — 50+ 고급 UI 패턴 카탈로그

> **Inspired by**: [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) — Creative Arsenal 40+ 패턴 원조
>
> **calm-design 확장**: 50+ 패턴으로 확장. **카테고리 7 (한국 SaaS 시그니처 6개)** 신설 — 토스 Bottom Sheet, 당근 Recommend Card, 카카오 Bubble Chat, 네이버 Search Suggestion, 라인 Sticker Reactions, 무신사 Filter Sidebar. 핵심 7개 패턴에 즉시 복사 가능 코드 스니펫 추가.

calm-design이 Multi-Variant(Mode D)·Match-Reference(Mode C)에서 변형 생성 시 참조하는 고급 패턴 풀.

> Phase 1 활성화. Phase 0에서는 SKILL.md의 핵심 5개 안티-슬롭만 자동 적용, Mode D 진입 시 이 카탈로그 sparse load.

## 사용 정책

- **Mode A**: 일반적으로 미사용. 사용자가 "트렌디하게", "역동적으로" 명시 시만 sparse load.
- **Mode D (Multi-Variant)**: 3안 생성 시 각 베리언트마다 다른 카테고리 패턴 채택.
- **Mode C (Match-Reference)**: 레퍼런스 브랜드의 시그니처 패턴과 매칭.
- **다이얼 매핑**: VARIANCE ≥ 7일 때 적극 활용, ≤ 4면 보수적 사용.

---

## 카테고리 1: Navigation & Menus (8개)

### 1.1 Mac OS Dock Magnification
- 마우스 hover 시 인접 아이템들이 멀리갈수록 작아지는 자석 효과
- 사용처: Hero 데모, Showcase 페이지
- 구현: Framer Motion `useMotionValue` + `useTransform` 거리 기반 스케일

### 1.2 Magnetic Button
- 마우스가 버튼 근처에 오면 버튼이 마우스 쪽으로 끌려옴 (자석)
- 사용처: Primary CTA 강조
- 구현: `mousemove` 이벤트 + transform translate

### 1.3 Gooey Menu (액체 변형 메뉴)
- 메뉴 열릴 때 액체처럼 분리되는 SVG filter 효과
- 사용처: FAB (Floating Action Button) 확장
- 주의: SVG `feGaussianBlur` + `feColorMatrix` — 모바일 성능 부담 ⚠️

### 1.4 Dynamic Island (Apple 스타일)
- 상단 알림 영역이 콘텐츠에 따라 모양 변형
- 사용처: 모바일 앱 알림, 진행 상태
- 구현: Framer Motion `layout` prop + spring

### 1.5 Contextual Radial Menu
- 우클릭 시 원형으로 펼쳐지는 컨텍스트 메뉴
- 사용처: 디자인 도구·에디터

### 1.6 Floating Speed Dial (FAB 확장)
- 메인 FAB 클릭 시 보조 액션들이 호 형태로 펼쳐짐
- 사용처: 모바일 앱 다중 액션

### 1.7 Mega Menu Reveal
- Nav hover 시 풀-너비 드롭다운 (이미지·카테고리 다층)
- 사용처: 이커머스, 콘텐츠 사이트

### 1.8 Bottom Sheet (한국 모바일 표준)
- 하단에서 올라오는 시트, 스와이프로 높이 조절
- 사용처: 토스·당근 표준. 모바일 네이티브 톤
- 구현: `transform: translateY()` + drag gesture

---

## 카테고리 2: Layout & Grids (8개)

### 2.1 Bento Grid (Apple Control Center 스타일)
- 비대칭 카드 그리드, `col-span-2 row-span-2` 큰 카드 + 작은 카드 혼합
- 사용처: Features 섹션, 대시보드 KPI
- 한국 사례: 토스 메인 메뉴

### 2.2 Masonry Layout
- Pinterest 스타일 — 카드 높이 다른 다중 컬럼
- 사용처: Testimonials, 갤러리

### 2.3 Chroma Grid
- 카드마다 다른 색상 액센트, 그러나 통일된 톤
- 사용처: 카테고리 분류, 태그 그리드

### 2.4 Split Screen Scroll
- 좌우 50/50 분할, 한쪽 고정·한쪽 스크롤
- 사용처: Feature 비교, Before/After

### 2.5 Curtain Reveal
- 스크롤 시 위 섹션이 커튼처럼 올라가며 다음 섹션 등장
- 사용처: 스토리텔링 랜딩

### 2.6 Sticky Stack
- 카드들이 스크롤 시 차례로 쌓이며 정착
- 사용처: 단계 설명, 워크플로우

### 2.7 Asymmetric Whitespace
- 의도적 비대칭 여백 (예: 텍스트 좌측 정렬, 우측 거대 여백)
- 사용처: 에디토리얼 톤

### 2.8 Inline Image Typography (시그니처)
- 헤드라인의 단어 사이에 이미지 인라인 삽입
- 사용처: Hero 섹션 차별화 (반드시 Mode D variant 1개에 활용)
- 모바일: 이미지가 헤드라인 아래로 떨어짐

---

## 카테고리 3: Cards & Containers (8개)

### 3.1 Parallax Tilt Card
- hover 시 마우스 위치에 따라 3D 기울기
- 구현: `transform: rotateX/rotateY()` + `perspective`

### 3.2 Spotlight Border Card
- 마우스 hover 시 마우스 주변에서만 보더가 빛남
- 구현: CSS `radial-gradient` + `mouse-position` CSS 변수

### 3.3 Glassmorphism Panel
- 반투명 + backdrop-blur + 미세 보더
- 주의: 배경 이미지·그래디언트 위에서만 효과 확실. 무지 배경에선 의미 없음.

### 3.4 Holographic Foil Card
- 카드 표면에 무지개 홀로그램 효과
- 사용처: 프리미엄 멤버십, 한정판

### 3.5 Morphing Modal
- 클릭한 카드가 모달로 모핑 (FLIP 애니메이션)
- 구현: Framer Motion `layoutId` prop

### 3.6 Double-Bezel Card (supanova 차용)
- 외부 셸 + 내부 코어 분리 — 하드웨어 톤
- 외부: `bg-white/5 ring-1 ring-white/10 p-1.5 rounded-[2rem]`
- 내부: `rounded-[calc(2rem-0.375rem)] shadow-[inset_0_1px_1px_rgba(255,255,255,0.15)]`

### 3.7 Tabbed Card
- 한 카드 안에서 탭 전환으로 콘텐츠 변경
- 사용처: 가격 플랜 비교

### 3.8 Expanding Card (아코디언)
- 클릭 시 카드가 풀 너비로 확장
- 한국 사례: 노션, 라인 사이트

---

## 카테고리 4: Forms & Inputs (6개)

### 4.1 Floating Label Input
- 라벨이 입력 시 위로 떠오름 (Material Design 표준)
- 한국 사례: 토스, 카카오

### 4.2 Inline Validation (실시간)
- 입력 중 실시간 검증 표시 (이메일·비밀번호 강도)

### 4.3 Stepper Form
- 긴 폼을 단계별로 분할 + 진행 표시줄

### 4.4 Magic Input (Iconify 자동)
- 입력 컨텍스트에 따라 아이콘 자동 변경 (URL → 글로브, 이메일 → @)

### 4.5 Slot OTP Input
- 6자리 코드 입력, 자동 포커스 이동
- 한국 사례: 토스 인증

### 4.6 Drag-to-reorder List
- 드래그로 항목 순서 변경
- 사용처: Trello·Notion 톤

---

## 카테고리 5: Motion Patterns (8개)

### 5.1 Stagger Cascade
- 리스트가 0.05s 간격으로 순차 등장
- 모든 calm-design 출력의 기본

### 5.2 Spring Bounce
- 클릭 시 살짝 튀는 스프링 (`stiffness: 300, damping: 15`)
- CTA 버튼 active 상태

### 5.3 Pulse Highlight
- 새로 등장한 항목이 미세 펄스 (1-2초)
- 사용처: 알림 도착, 신규 기능

### 5.4 Counter Up
- 숫자가 0에서 목표값까지 카운트업
- 사용처: KPI 카드, Social Proof

### 5.5 Typewriter
- 텍스트가 한 글자씩 타이핑되듯 등장
- 한국어: 한 글자씩, 영문: 단어 단위

### 5.6 Float (영구 마이크로)
- 활성 요소가 무한히 미세하게 떠다님 (3-5초 사이클)
- VARIANCE ≥ 7에서만 사용

### 5.7 Shimmer (Skeleton)
- 로딩 중 좌→우로 빛이 지나가는 효과

### 5.8 Page Transition (View Transitions API)
- 페이지 전환 시 공유 요소가 부드럽게 이동
- 차세대 브라우저 표준

---

## 카테고리 6: Data Visualization (6개)

### 6.1 Sparkline
- 셀 안에 들어가는 미니 라인 차트
- 사용처: 테이블, KPI 카드

### 6.2 Animated Number Reveal
- 큰 숫자가 카드 클릭 시 사이즈·색상 변경

### 6.3 Live Gauge (실시간 게이지)
- 원형/막대 게이지가 실시간 데이터로 변동

### 6.4 Heatmap
- 색상 그라디언트로 밀도 표시
- 한국 사례: GitHub 컨트리뷰션 그리드 톤

### 6.5 Sankey Flow
- 데이터 흐름 시각화 (입력 → 처리 → 출력)

### 6.6 Constellation Chart
- 데이터 포인트들이 별자리처럼 연결

---

## 카테고리 7: Korean SaaS 시그니처 (6개)

### 7.1 토스 Bottom Sheet
- 하단 시트 + 스와이프 핸들 + 단계별 결제
- 채택: 결제·인증 흐름

### 7.2 당근 Recommend Card
- 가로 스크롤 카드 + 큰 이미지 + 짧은 카피
- 채택: 추천 콘텐츠 섹션

### 7.3 카카오톡 Bubble Chat
- 말풍선 형태 채팅 UI
- 채택: 콘텐츠 형 인터뷰, 대화형 FAQ

### 7.4 네이버 Search Suggestion
- 검색창 아래 자동완성 + 인기 검색어
- 채택: 검색 중심 SaaS

### 7.5 라인 Sticker Reactions
- 메시지에 이모지·스티커 반응
- 채택: 협업 도구

### 7.6 무신사 Filter Sidebar
- 좌측 다중 필터 + 우측 결과 그리드
- 채택: 이커머스, 카탈로그

---

## 🛠️ 핵심 패턴 코드 스니펫 (Phase 1 추가)

자주 사용되는 7개 패턴의 즉시 복사 가능 구현. 나머지 패턴은 이 7개를 변형해서 도출.

### Snippet 1: Bento Grid (비대칭 카드)

```html
<!-- HTML + Tailwind -->
<div class="grid grid-cols-1 md:grid-cols-3 gap-4 md:gap-6 auto-rows-fr">
  <div class="md:col-span-2 md:row-span-2 bg-white rounded-3xl border border-zinc-200 p-8 md:p-10">
    <!-- 큰 카드 (강조) -->
  </div>
  <div class="bg-white rounded-2xl border border-zinc-200 p-6"><!-- 작은 1 --></div>
  <div class="bg-white rounded-2xl border border-zinc-200 p-6"><!-- 작은 2 --></div>
  <div class="bg-white rounded-2xl border border-zinc-200 p-6"><!-- 작은 3 --></div>
  <div class="bg-white rounded-2xl border border-zinc-200 p-6"><!-- 작은 4 --></div>
</div>
```

### Snippet 2: Magnetic Button (Framer Motion)

```tsx
"use client";
import { motion, useMotionValue, useTransform, animate } from "motion/react";

export function MagneticButton({ children }: { children: React.ReactNode }) {
  const x = useMotionValue(0);
  const y = useMotionValue(0);

  const handleMove = (e: React.MouseEvent<HTMLButtonElement>) => {
    const rect = e.currentTarget.getBoundingClientRect();
    x.set((e.clientX - rect.left - rect.width / 2) * 0.3);
    y.set((e.clientY - rect.top - rect.height / 2) * 0.3);
  };

  const handleLeave = () => {
    animate(x, 0, { type: "spring", stiffness: 200, damping: 20 });
    animate(y, 0, { type: "spring", stiffness: 200, damping: 20 });
  };

  return (
    <motion.button
      onMouseMove={handleMove}
      onMouseLeave={handleLeave}
      style={{ x, y }}
      className="rounded-full bg-accent text-white px-7 py-3.5 font-semibold"
    >
      {children}
    </motion.button>
  );
}
```

### Snippet 3: Floating Label Input (한국어 친화)

```tsx
export function FloatingLabelInput({ id, label, ...props }: Props) {
  return (
    <div className="relative">
      <input
        id={id}
        placeholder=" "
        className="peer w-full h-12 px-3 pt-5 pb-1 rounded-md border border-zinc-200
                   focus:outline-none focus:ring-2 focus:ring-accent/20 focus:border-accent
                   bg-white transition-all"
        {...props}
      />
      <label
        htmlFor={id}
        className="absolute left-3 top-3.5 text-mute text-base
                   peer-focus:top-1.5 peer-focus:text-xs peer-focus:text-accent
                   peer-[:not(:placeholder-shown)]:top-1.5 peer-[:not(:placeholder-shown)]:text-xs
                   pointer-events-none transition-all break-keep"
      >
        {label}
      </label>
    </div>
  );
}
```

### Snippet 4: Counter Up (KPI 숫자 카운트업)

```tsx
"use client";
import { motion, useMotionValue, useTransform, animate, useReducedMotion, useInView } from "motion/react";
import { useEffect, useRef } from "react";

export function CounterUp({ to, duration = 1.5 }: { to: number; duration?: number }) {
  const ref = useRef<HTMLSpanElement>(null);
  const inView = useInView(ref, { once: true });
  const reduced = useReducedMotion();
  const count = useMotionValue(reduced ? to : 0);
  const display = useTransform(count, (n) => Math.round(n).toLocaleString("ko-KR"));

  useEffect(() => {
    if (!inView || reduced) return;
    const ctrl = animate(count, to, { duration, ease: [0.16, 1, 0.3, 1] });
    return () => ctrl.stop();
  }, [inView, to, duration, reduced]);

  return <motion.span ref={ref} className="tabular-nums">{display}</motion.span>;
}
```

### Snippet 5: Spotlight Border Card (마우스 추적 빛)

```tsx
export function SpotlightCard({ children }: { children: React.ReactNode }) {
  const handleMove = (e: React.MouseEvent<HTMLDivElement>) => {
    const rect = e.currentTarget.getBoundingClientRect();
    e.currentTarget.style.setProperty("--mx", `${e.clientX - rect.left}px`);
    e.currentTarget.style.setProperty("--my", `${e.clientY - rect.top}px`);
  };

  return (
    <div
      onMouseMove={handleMove}
      className="group relative rounded-2xl border border-zinc-200 bg-white p-6
                 before:absolute before:inset-0 before:rounded-2xl before:opacity-0
                 before:[background:radial-gradient(circle_at_var(--mx)_var(--my),theme(colors.accent/20),transparent_40%)]
                 before:transition-opacity hover:before:opacity-100"
    >
      <div className="relative z-10">{children}</div>
    </div>
  );
}
```

### Snippet 6: 토스 스타일 Bottom Sheet (모바일)

```tsx
"use client";
import { motion, AnimatePresence } from "motion/react";

export function BottomSheet({ open, onClose, children }: Props) {
  return (
    <AnimatePresence>
      {open && (
        <>
          <motion.div
            initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}
            onClick={onClose}
            className="fixed inset-0 bg-black/40 backdrop-blur-sm z-40"
          />
          <motion.div
            initial={{ y: "100%" }} animate={{ y: 0 }} exit={{ y: "100%" }}
            transition={{ type: "spring", stiffness: 100, damping: 20 }}
            drag="y"
            dragConstraints={{ top: 0, bottom: 0 }}
            dragElastic={0.2}
            onDragEnd={(_, info) => { if (info.offset.y > 100) onClose(); }}
            className="fixed inset-x-0 bottom-0 z-50 bg-white rounded-t-3xl pb-8
                       max-w-md mx-auto shadow-[0_-4px_24px_rgba(0,0,0,0.08)]"
          >
            <div className="w-12 h-1.5 bg-zinc-300 rounded-full mx-auto my-3" />
            <div className="px-6">{children}</div>
          </motion.div>
        </>
      )}
    </AnimatePresence>
  );
}
```

### Snippet 7: Inline Image Typography (Hero 시그니처)

```html
<h1 class="text-5xl md:text-7xl font-bold tracking-tight leading-tight break-keep">
  영상을
  <span class="inline-flex items-baseline align-middle mx-2">
    <img src="https://picsum.photos/seed/hero/120/80"
         class="inline-block h-[0.85em] aspect-[3/2] rounded-xl object-cover translate-y-[0.1em]" alt=""/>
  </span>
  10배 빠르게 편집하세요
</h1>
<style>
  /* 모바일에서는 인라인 이미지를 헤드라인 아래로 떨어뜨림 */
  @media (max-width: 767px) {
    h1 img { display: block; height: 6rem; margin: 0.5rem auto; }
  }
</style>
```

---

## Mode D Multi-Variant 사용 매트릭스

3안 생성 시 각 베리언트가 **서로 다른 패턴 카테고리**를 채택하도록 강제:

| Variant | 추천 패턴 |
|---|---|
| **Variant 1: 미니멀 차분** | Asymmetric Whitespace + Stagger Cascade + Floating Label Input |
| **Variant 2: 트렌디 다이내믹** | Bento Grid + Magnetic Button + Inline Image Typography |
| **Variant 3: 한국 SaaS 시그니처** | 토스 Bottom Sheet + 당근 Recommend + Pretendard 강조 |

이 매트릭스는 `modes/multi-variant.md`(Phase 2)에서 자동 적용.

## Mode C Match-Reference 매핑 (Phase 3)

레퍼런스 브랜드별 시그니처 패턴 사전 매핑:

| 브랜드 | 시그니처 패턴 |
|---|---|
| Linear | Asymmetric Whitespace + Sparkline + Stagger Cascade |
| Vercel | Inline Image Typography + Bento Grid |
| Stripe | Spotlight Border + Counter Up + Smooth Page Transition |
| Toss | Bottom Sheet + Floating Label + Spring Bounce |
| 당근 | Recommend Card + 큰 이미지 + 한국어 자연 카피 |

상세 매핑은 `reference-library/_index.json`(Phase 3)에서 자동 로드.
