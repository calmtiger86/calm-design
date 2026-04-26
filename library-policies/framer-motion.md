# Library Policy: Framer Motion (React 모드 표준 애니메이션)

calm-design React 출력의 **표준 애니메이션 라이브러리**. taste-skill의 강제 정책(`useMotionValue`/`useTransform` 강제, `useState` 애니메이션 금지) 그대로 채택 + 한국어 환경 보강.

## 0. 정책 한 줄

> Framer Motion은 React 모드의 기본 애니메이션. `useMotionValue` + `useTransform` 강제. `useState` 기반 애니메이션 절대 금지. 모든 활성 컴포넌트에 `useReducedMotion` 보호 의무.

## 1. 라이선스

- **MIT** — 상업·재배포·수정 자유
- 의존성: `motion` 패키지 (Framer Motion v11+). 이전 버전은 `framer-motion`로 import.

## 2. 설치

```bash
npm install framer-motion
# 또는 v11+ 짧은 이름
npm install motion
```

```tsx
// v10 이하
import { motion, useMotionValue, useTransform, useReducedMotion } from "framer-motion";

// v11+
import { motion, useMotionValue, useTransform, useReducedMotion } from "motion/react";
```

calm-design 권장: `motion@11+` (가벼움, 트리쉐이킹 개선).

## 3. 강제 패턴 (이걸 지키지 않으면 Pre-Flight #15·#16·#27 fail)

### 3.1 `useMotionValue` + `useTransform` 강제

```tsx
// ✅ 권장 — Spring physics, 60fps 보장
import { useMotionValue, useTransform, animate } from "framer-motion";

function Counter({ target }: { target: number }) {
  const count = useMotionValue(0);
  const rounded = useTransform(count, (latest) => Math.round(latest));

  useEffect(() => {
    const controls = animate(count, target, {
      duration: 1.5,
      ease: [0.16, 1, 0.3, 1],
    });
    return controls.stop;
  }, [target]);

  return <motion.span>{rounded}</motion.span>;
}
```

### 3.2 `useState` 기반 애니메이션 금지

```tsx
// ❌ 금지 — 매 프레임 re-render → 60fps 깨짐
function BadCounter({ target }: { target: number }) {
  const [count, setCount] = useState(0);
  useEffect(() => {
    const interval = setInterval(() => {
      setCount((c) => c + 1);  // ❌ 모든 step마다 React re-render
      if (count >= target) clearInterval(interval);
    }, 16);
    return () => clearInterval(interval);
  }, [target]);
  return <span>{count}</span>;
}
```

이 패턴을 보면 `ai-tells-blocklist.md` #27이 자동 fail.

### 3.3 `useReducedMotion` 보호 의무

모든 시각적 모션이 있는 컴포넌트는 `useReducedMotion` 분기 강제:

```tsx
import { motion, useReducedMotion } from "motion/react";

function FadeUp({ children, delay = 0 }: Props) {
  const reduced = useReducedMotion();

  return (
    <motion.div
      initial={{ opacity: 0, y: reduced ? 0 : 20 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ amount: 0.3, once: true }}
      transition={{
        duration: reduced ? 0 : 0.6,
        delay: reduced ? 0 : delay,
        ease: [0.16, 1, 0.3, 1],
      }}
    >
      {children}
    </motion.div>
  );
}
```

이걸 빠뜨리면 Pre-Flight #30 fail.

### 3.4 GPU 친화 속성만 사용

```tsx
// ✅ 권장
<motion.div animate={{ x: 100, opacity: 0.5, scale: 1.1 }} />

// ❌ 금지 — top/left/width/height
<motion.div animate={{ left: "100px", width: "200px" }} />
```

이걸 어기면 Pre-Flight #15 fail.

## 4. 표준 모션 컴포넌트 라이브러리 (calm-design 권장)

`components/motion/` 디렉토리에 다음 5개 표준 래퍼:

### 4.1 `<FadeUp>` (가장 흔함)

```tsx
// components/motion/fade-up.tsx
"use client";
import { motion, useReducedMotion } from "motion/react";

export function FadeUp({
  children,
  delay = 0,
  amount = 0.3,
  className,
}: {
  children: React.ReactNode;
  delay?: number;
  amount?: number;
  className?: string;
}) {
  const reduced = useReducedMotion();
  return (
    <motion.div
      className={className}
      initial={{ opacity: 0, y: reduced ? 0 : 20 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ amount, once: true }}
      transition={{
        duration: reduced ? 0 : 0.6,
        delay: reduced ? 0 : delay,
        ease: [0.16, 1, 0.3, 1],
      }}
    >
      {children}
    </motion.div>
  );
}
```

### 4.2 `<StaggerList>` (리스트 순차)

```tsx
export function StaggerList({ items, render }: Props) {
  const reduced = useReducedMotion();
  return (
    <>
      {items.map((item, i) => (
        <motion.div
          key={i}
          initial={{ opacity: 0, y: reduced ? 0 : 16 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ amount: 0.3, once: true }}
          transition={{
            duration: reduced ? 0 : 0.5,
            delay: reduced ? 0 : i * 0.05,
            ease: [0.16, 1, 0.3, 1],
          }}
        >
          {render(item)}
        </motion.div>
      ))}
    </>
  );
}
```

### 4.3 `<HoverScale>` (CTA)

```tsx
export function HoverScale({ children, factor = 1.02 }: Props) {
  return (
    <motion.div
      whileHover={{ scale: factor }}
      whileTap={{ scale: 1 - (factor - 1) }}
      transition={{ type: "spring", stiffness: 300, damping: 15 }}
    >
      {children}
    </motion.div>
  );
}
```

### 4.4 `<CounterUp>` (KPI 숫자)

```tsx
export function CounterUp({ to, duration = 1.5, format }: Props) {
  const reduced = useReducedMotion();
  const count = useMotionValue(reduced ? to : 0);
  const display = useTransform(count, (latest) =>
    format ? format(latest) : Math.round(latest).toLocaleString("ko-KR")
  );
  useEffect(() => {
    if (reduced) return;
    const ctrl = animate(count, to, {
      duration,
      ease: [0.16, 1, 0.3, 1],
    });
    return ctrl.stop;
  }, [to]);
  return <motion.span className="tabular-nums">{display}</motion.span>;
}
```

### 4.5 `<ScrollProgress>` (스크롤 진행률)

```tsx
export function ScrollProgress() {
  const { scrollYProgress } = useScroll();
  const scaleX = useSpring(scrollYProgress, { stiffness: 100, damping: 30 });
  return (
    <motion.div
      style={{ scaleX, transformOrigin: "0%" }}
      className="fixed top-0 left-0 right-0 h-0.5 bg-accent z-50"
    />
  );
}
```

## 5. GSAP·anime.js 동시 사용 금지

```tsx
// ❌ 금지 — 라이브러리 충돌, 번들 크기 폭증
import gsap from "gsap";
import { motion } from "motion/react";
import anime from "animejs";
```

calm-design React 모드는 **Framer Motion 1개만** 허용.

예외: 사용자가 `--motion=gsap` 명시 요청 시. 이때도 Framer Motion과 혼용 금지 — 둘 중 하나만.

## 6. Tailwind animate 클래스와의 관계

Tailwind의 `animate-pulse`, `animate-spin`, `animate-bounce` 등은 **단순 무한 루프 애니메이션에만** 사용:

```tsx
// ✅ Skeleton, Spinner — Tailwind animate 클래스
<div className="animate-pulse bg-zinc-200 h-6 rounded" />
<Loader2 className="animate-spin" />

// ✅ 컴포넌트 진입·hover·복잡한 spring — Framer Motion
<motion.div whileInView={{ opacity: 1 }} />
```

기준: **상태 의존**(in-view, hover) → Framer Motion / **무한 단순 루프** → Tailwind animate.

## 7. 검증 (Pre-Flight 통합)

React 출력 직후 자동 체크:

```
✅ framer-motion 또는 motion 패키지 import 존재
✅ 모션 컴포넌트에 useMotionValue 또는 motion.X 사용
✅ useState 기반 setInterval 애니메이션 부재 (#27 fail)
✅ top/left/width/height 애니메이션 부재 (#15 fail)
✅ useReducedMotion 호출 또는 prefers-reduced-motion 미디어 쿼리 (#30)
✅ ease: [0.16, 1, 0.3, 1] 또는 type: "spring" 명시 (#16)
✅ GSAP·anime.js 동시 사용 부재
```

7개 중 1개라도 실패 → Pre-Flight 차감.

## 8. 출처·참조

- 공식: https://motion.dev (구 Framer Motion)
- GitHub: https://github.com/framer/motion
- 라이선스: MIT
- v11+ 패키지명: `motion`
- v10 이하: `framer-motion`

calm-design은 `motion@11+` 권장 — 더 가볍고 SSR 안정성 개선.
