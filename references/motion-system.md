# Motion System — 모션 철학·스프링 피직스·다이얼별 변형

calm-design의 모션 결정 알고리즘 + Mode D Multi-Variant 모션 베리언트 생성용 자산.

> Phase 1 활성화. SKILL.md ALWAYS 로드 X. Mode D 또는 사용자가 "다른 모션", "더 다이내믹하게" 요청 시 sparse load.

## 0. 절대 원칙 5개

1. **GPU 친화 속성만** — `transform`, `opacity` (top/left/width/height 절대 X)
2. **Spring physics 기본** — linear easing 금지
3. **MOTION_INTENSITY=1일 때도 hover transition은 유지** (인터랙션 피드백)
4. **Reduced-motion 미디어 쿼리 지원 의무** (전정 장애 보호)
5. **모바일에서 모션 강도 ↓** — 대형 모션은 데스크톱만

## 1. 다이얼별 모션 강도

| MOTION_INTENSITY | 의미 | 대표 패턴 |
|---|---|---|
| 1-2 | 거의 없음 | Hover transition만 (300ms color/opacity) |
| 3-4 | 미세 보강 | Fade-in, 짧은 transform (200-400ms) |
| 5-6 | 균형 (기본) | Stagger cascade, Spring bounce, Scroll-triggered fade-up |
| 7-8 | 다이내믹 | Magnetic button, Counter up, Staggered orchestration |
| 9-10 | 영화적 | Scroll storytelling, Page transitions, Particle systems |

## 2. Spring 피직스 표준값

| 톤 | Stiffness | Damping | 사용처 |
|---|---:|---:|---|
| **Calm Premium** (기본) | 100 | 20 | 일반 transition (페이드·스케일) |
| **Bouncy Playful** | 300 | 15 | CTA active, 알림 도착 |
| **Heavy Slow** | 50 | 30 | 큰 요소 (Hero 비주얼, Modal) |
| **Quick Snappy** | 400 | 25 | 마이크로 인터랙션 (toggle, switch) |
| **Anti-bounce** | 200 | 40 | bounce 없는 부드러움 (레이아웃 변경) |

CSS cubic-bezier 근사:

```css
/* Calm Premium 근사 */
transition-timing-function: cubic-bezier(0.16, 1, 0.3, 1);

/* Bouncy 근사 */
transition-timing-function: cubic-bezier(0.34, 1.56, 0.64, 1);

/* Anti-bounce 근사 */
transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
```

## 3. 표준 모션 패턴 (10개)

### 3.1 Fade-Up (가장 흔한 진입)

```jsx
<motion.div
  initial={{ opacity: 0, y: 20 }}
  whileInView={{ opacity: 1, y: 0 }}
  viewport={{ amount: 0.3, once: true }}
  transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] }}
/>
```

### 3.2 Stagger Cascade (리스트 순차)

```jsx
{items.map((item, i) => (
  <motion.div
    initial={{ opacity: 0, y: 20 }}
    whileInView={{ opacity: 1, y: 0 }}
    transition={{ delay: i * 0.05, ease: [0.16, 1, 0.3, 1] }}
  />
))}
```

### 3.3 Hover Scale (CTA)

```jsx
<motion.button
  whileHover={{ scale: 1.02 }}
  whileTap={{ scale: 0.98 }}
  transition={{ type: "spring", stiffness: 300, damping: 15 }}
/>
```

### 3.4 Counter Up (KPI)

```jsx
const count = useMotionValue(0);
const rounded = useTransform(count, latest => Math.round(latest));

useEffect(() => {
  const animation = animate(count, targetValue, { duration: 1.5, ease: [0.16, 1, 0.3, 1] });
  return animation.stop;
}, [targetValue]);
```

### 3.5 Pulse (영구 마이크로)

```jsx
<motion.div
  animate={{ scale: [1, 1.05, 1] }}
  transition={{ duration: 2, repeat: Infinity, ease: "easeInOut" }}
/>
```

VARIANCE ≥ 7 + MOTION ≥ 6에서만 사용. 활성 요소에만 (CTA·신규 항목·실시간 데이터).

### 3.6 Float (떠다니는 효과)

```jsx
<motion.div
  animate={{ y: [-4, 4, -4] }}
  transition={{ duration: 3, repeat: Infinity, ease: "easeInOut" }}
/>
```

### 3.7 Shimmer (Skeleton)

```css
@keyframes shimmer {
  0% { background-position: -200% 0; }
  100% { background-position: 200% 0; }
}
.skeleton {
  background: linear-gradient(90deg, #f4f4f5 0%, #e4e4e7 50%, #f4f4f5 100%);
  background-size: 200% 100%;
  animation: shimmer 1.5s linear infinite;
}
```

### 3.8 Magnetic Button (VARIANCE ≥ 7)

```jsx
const x = useMotionValue(0);
const y = useMotionValue(0);

const handleMouse = (e) => {
  const rect = e.currentTarget.getBoundingClientRect();
  x.set((e.clientX - rect.left - rect.width / 2) * 0.3);
  y.set((e.clientY - rect.top - rect.height / 2) * 0.3);
};

<motion.button onMouseMove={handleMouse} style={{ x, y }} />
```

### 3.9 Page Transition (View Transitions API)

```css
::view-transition-old(root) { animation: fade-out 0.3s; }
::view-transition-new(root) { animation: fade-in 0.3s; }
```

Phase 4에서 풀 통합.

### 3.10 Scroll-triggered Reveal Sections

스크롤 진입 시 각 섹션이 차례로 등장. `whileInView` + `viewport={ once: true }`.

## 4. Reduced-motion 자동 적용

모든 calm-design 출력은 다음 패턴 의무:

### React (Framer Motion)

```jsx
import { useReducedMotion } from "framer-motion";

function FadeUp({ children }) {
  const reduced = useReducedMotion();
  return (
    <motion.div
      initial={{ opacity: 0, y: reduced ? 0 : 20 }}
      whileInView={{ opacity: 1, y: 0 }}
      transition={{ duration: reduced ? 0 : 0.6 }}
    >
      {children}
    </motion.div>
  );
}
```

### CSS

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

## 5. Mode D 모션 베리언트 매트릭스

| Variant | 모션 톤 | MOTION 권장 |
|---|---|---|
| **Variant 1 (미니멀 차분)** | Hover만, Fade-up | 3-4 |
| **Variant 2 (트렌디 다이내믹)** | Stagger + Magnetic + Counter Up | 7-8 |
| **Variant 3 (도메인 매칭)** | 사용자 의도 기반 | 5-6 |

## 6. 한국 SaaS 모션 시그니처 (Match-Reference, Phase 3)

| 브랜드 | 시그니처 모션 |
|---|---|
| Toss | Bottom Sheet 슬라이드 + Floating label + Spring bounce |
| 당근 | 카드 horizontal scroll + 페이드 |
| 카카오 | 채팅 말풍선 등장 (scale + opacity) |
| 라인 | 스티커 반응 spring bounce |
| 네이버 | 검색 자동완성 instant fade |

상세는 `reference-library/{brand}/DESIGN.md` Section 7 (Phase 3).
