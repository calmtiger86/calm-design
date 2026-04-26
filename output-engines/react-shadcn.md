# Output Engine: React + shadcn/ui (개발자용)

calm-design의 두 번째 출력 엔진. React + Next.js 14+ App Router + shadcn/ui + Tailwind v4 + Framer Motion + Pretendard 통합. 프로덕션 코드 그대로 사용 가능.

## 1. 트리거 시그널

다음 중 하나라도 등장 시 이 엔진 사용:
- "React로", "Next.js로", "컴포넌트로"
- "TSX 파일로", "프로덕션 코드"
- "이 코드를 우리 React 프로젝트에 붙일거야"

## 2. 디렉토리 구조 (Next.js 14+ App Router 기준)

```
app/
├── layout.tsx                # Pretendard 등록, Tailwind v4 설정
├── page.tsx                  # 페이지 콘텐츠 (composition)
├── globals.css               # Tailwind base + 한국어 word-break
├── components/
│   ├── ui/                   # shadcn/ui 컴포넌트 (직접 복사)
│   │   ├── button.tsx
│   │   ├── card.tsx
│   │   └── ...
│   ├── sections/             # 페이지 섹션 (Hero, Features 등)
│   │   ├── nav.tsx
│   │   ├── hero.tsx
│   │   ├── features.tsx
│   │   └── ...
│   └── motion/               # Framer Motion 래퍼
│       └── fade-up.tsx
├── lib/
│   └── utils.ts              # cn() 헬퍼 (shadcn 표준)
└── public/
    └── fonts/
        └── PretendardVariable.woff2
```

## 3. 필수 파일 템플릿

### 3.1 `app/layout.tsx` (한국어 환경 통합)

```tsx
import type { Metadata } from "next";
import localFont from "next/font/local";
import "./globals.css";

const pretendard = localFont({
  src: "../public/fonts/PretendardVariable.woff2",
  display: "swap",
  weight: "45 920",
  variable: "--font-pretendard",
});

export const metadata: Metadata = {
  title: "{프로젝트 제목}",
  description: "{설명}",
};

export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="ko" className={pretendard.variable}>
      <body className="font-pretendard antialiased bg-zinc-50 text-ink">
        {children}
      </body>
    </html>
  );
}
```

### 3.2 `app/globals.css`

```css
@import "tailwindcss";

/* 한국어 줄바꿈 강제 */
@layer base {
  h1, h2, h3, h4, h5, h6, p, li, dt, dd {
    word-break: keep-all;
    overflow-wrap: break-word;
  }
}

/* 숫자 정렬 유틸 */
@layer utilities {
  .tabular { font-variant-numeric: tabular-nums; }
  .break-keep { word-break: keep-all; }
}

/* CSS 변수 (DESIGN.md Section 2 컬러 매핑) */
@theme {
  --color-ink: #0A0A0A;
  --color-mute: #71717A;
  --color-accent: #10B981;
  --font-pretendard: var(--font-pretendard), "system-ui", "sans-serif";
}
```

### 3.3 `lib/utils.ts` (shadcn 필수)

```ts
import { clsx, type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}
```

## 4. shadcn/ui 통합 (자세한 정책은 `library-policies/shadcn-ui.md`)

### 4.1 초기 설정

```bash
npx shadcn@latest init
# style: new-york (권장 — 더 정제된 톤)
# baseColor: zinc
# cssVariables: yes
```

### 4.2 컴포넌트 추가 (필요한 것만)

```bash
npx shadcn@latest add button card input label dialog
```

→ `components/ui/`에 직접 복사됨. 우리가 한국어 환경에 맞게 **수정 가능**.

### 4.3 한국어 환경 추가 수정 (Button 예시)

shadcn Button을 그대로 쓰지 않고, 한국어 친화 prop 추가:

```tsx
// components/ui/button.tsx (shadcn 기본 + 한국어 환경 보강)
import * as React from "react";
import { Slot } from "@radix-ui/react-slot";
import { cva, type VariantProps } from "class-variance-authority";
import { cn } from "@/lib/utils";
import { Loader2 } from "lucide-react";

const buttonVariants = cva(
  "inline-flex items-center justify-center gap-2 whitespace-nowrap rounded-full text-sm font-semibold transition-all duration-300 ease-[cubic-bezier(0.16,1,0.3,1)] focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent focus-visible:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed [&_svg]:size-4 break-keep",
  {
    variants: {
      variant: {
        default: "bg-accent text-white hover:scale-[1.02] active:scale-[0.98]",
        outline: "border border-zinc-300 bg-white hover:bg-zinc-50",
        ghost: "hover:bg-zinc-100",
      },
      size: {
        default: "h-10 px-6 py-2",
        sm: "h-9 px-4",
        lg: "h-12 px-8 text-base",
      },
    },
    defaultVariants: { variant: "default", size: "default" },
  }
);

interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement>,
    VariantProps<typeof buttonVariants> {
  asChild?: boolean;
  loading?: boolean; // 한국어 환경 추가 prop — Pre-Flight 항목 17 충족
}

const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant, size, asChild = false, loading, children, ...props }, ref) => {
    const Comp = asChild ? Slot : "button";
    return (
      <Comp
        className={cn(buttonVariants({ variant, size }), className)}
        ref={ref}
        disabled={loading || props.disabled}
        {...props}
      >
        {loading && <Loader2 className="animate-spin" />}
        {children}
      </Comp>
    );
  }
);
Button.displayName = "Button";

export { Button, buttonVariants };
```

→ shadcn 기본에 **`loading` prop 추가**. 이것이 Pre-Flight 항목 17 (컴포넌트 6상태) 통과 핵심.

## 5. Framer Motion 통합

### 5.1 Fade-Up 래퍼 (가장 자주 사용)

```tsx
// components/motion/fade-up.tsx
"use client";
import { motion, useMotionValue, useTransform, useInView } from "framer-motion";
import { useRef } from "react";

interface FadeUpProps {
  children: React.ReactNode;
  delay?: number;
  className?: string;
}

export function FadeUp({ children, delay = 0, className }: FadeUpProps) {
  const ref = useRef(null);
  const isInView = useInView(ref, { amount: 0.3, once: true });

  return (
    <motion.div
      ref={ref}
      initial={{ opacity: 0, y: 20 }}
      animate={isInView ? { opacity: 1, y: 0 } : {}}
      transition={{
        duration: 0.6,
        delay,
        ease: [0.16, 1, 0.3, 1], // Spring 흉내내는 cubic-bezier
      }}
      className={className}
    >
      {children}
    </motion.div>
  );
}
```

### 5.2 사용 패턴

```tsx
import { FadeUp } from "@/components/motion/fade-up";

export default function Hero() {
  return (
    <section className="py-24 md:py-32 lg:py-40 bg-zinc-50">
      <div className="max-w-7xl mx-auto px-4 md:px-6 grid md:grid-cols-12 gap-8 items-center">
        <FadeUp className="md:col-span-7">
          <h1 className="text-5xl md:text-6xl lg:text-7xl font-bold tracking-tight leading-tight break-keep">
            {한국어 헤드라인}
          </h1>
          <p className="mt-6 text-lg md:text-xl text-mute leading-relaxed max-w-[65ch]">
            {부제}
          </p>
          <div className="mt-10 flex gap-3">
            <Button size="lg">{Primary CTA}</Button>
            <Button size="lg" variant="outline">{Secondary CTA}</Button>
          </div>
        </FadeUp>
        <FadeUp className="md:col-span-5" delay={0.2}>
          {/* 비주얼 */}
        </FadeUp>
      </div>
    </section>
  );
}
```

### 5.3 Framer Motion 강제 규칙

- ✅ `useMotionValue`, `useTransform`, `useInView` 사용
- ❌ `useState` 기반 애니메이션 (`ai-tells-blocklist.md` #27)
- ✅ `transform`, `opacity`만
- ❌ `top/left/width/height` 애니메이션 (#26)

## 6. zustand 통합 (조건부 — 다중 컴포넌트 상태 공유 시만)

```tsx
// lib/stores/use-app-store.ts
import { create } from "zustand";

interface AppStore {
  isMobileMenuOpen: boolean;
  toggleMobileMenu: () => void;
}

export const useAppStore = create<AppStore>((set) => ({
  isMobileMenuOpen: false,
  toggleMobileMenu: () => set((s) => ({ isMobileMenuOpen: !s.isMobileMenuOpen })),
}));
```

**zustand 사용 조건**:
- ✅ 2개 이상 컴포넌트가 같은 상태를 공유 (예: Nav 햄버거 ↔ Drawer)
- ❌ 단일 컴포넌트 내부 상태 → `useState`로 충분
- ❌ 폼 상태 → React Hook Form 권장 (별도)

## 7. 페이지 합성 예시 (`app/page.tsx`)

```tsx
import { Nav } from "@/components/sections/nav";
import { Hero } from "@/components/sections/hero";
import { SocialProof } from "@/components/sections/social-proof";
import { Features } from "@/components/sections/features";
import { Testimonials } from "@/components/sections/testimonials";
import { CTABanner } from "@/components/sections/cta-banner";
import { Footer } from "@/components/sections/footer";

export default function Home() {
  return (
    <main className="min-h-[100dvh]">
      <Nav />
      <Hero />
      <SocialProof />
      <Features />
      <Testimonials />
      <CTABanner />
      <Footer />
    </main>
  );
}
```

→ `<main className="min-h-[100dvh]">` 강제. `h-screen` 절대 금지 (Pre-Flight #2).

## 8. `tailwind.config.ts` (v4 기준)

Tailwind v4는 `@theme` 디렉티브로 설정하므로 별도 config 파일이 거의 불필요. 단, IDE 자동완성을 위해 최소 설정:

```ts
import type { Config } from "tailwindcss";

export default {
  content: [
    "./app/**/*.{ts,tsx}",
    "./components/**/*.{ts,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        pretendard: ["var(--font-pretendard)"],
      },
    },
  },
} satisfies Config;
```

## 9. 검증 (Pre-Flight 통합)

React 출력 직후 자동 체크:

- [ ] `app/layout.tsx`에 Pretendard `next/font` 등록
- [ ] `<html lang="ko">` (LANGUAGE=ko)
- [ ] `globals.css`에 `word-break: keep-all` base 스타일
- [ ] Tailwind config에 Pretendard 폰트 변수
- [ ] shadcn Button에 `loading` prop (또는 동등 6상태)
- [ ] Framer Motion 사용 시 `useMotionValue`/`useTransform` (또는 `motion.div`의 `initial`/`animate`)
- [ ] `useState` 기반 애니메이션 부재
- [ ] `top/left/width/height` 애니메이션 부재
- [ ] 모든 페이지 main 컨테이너에 `min-h-[100dvh]`
- [ ] 데이터 컴포넌트에 Empty/Error/Loading 상태 정의

10개 중 하나라도 실패 → 자동 재생성.

## 10. 패키지 의존성 (package.json 추가)

```json
{
  "dependencies": {
    "next": "^14.0.0",
    "react": "^18.0.0",
    "react-dom": "^18.0.0",
    "lucide-react": "^0.400.0",
    "framer-motion": "^11.0.0",
    "@radix-ui/react-slot": "^1.0.0",
    "class-variance-authority": "^0.7.0",
    "clsx": "^2.0.0",
    "tailwind-merge": "^2.0.0",
    "tailwindcss": "^4.0.0"
  },
  "devDependencies": {
    "typescript": "^5.0.0",
    "@types/react": "^18.0.0",
    "@types/node": "^20.0.0"
  },
  "optionalDependencies": {
    "zustand": "^4.5.0"
  }
}
```

`zustand`는 optional — 다중 컴포넌트 상태 공유 시에만 추가.

---

## 11. 다중 환경 지원 매트릭스 (Next.js App Router 외)

위 Section 1-10은 Next.js 14+ App Router 기준이다. 다른 환경에서도 calm-design을 적용할 수 있도록 환경별 통합 가이드를 추가:

### 11.1 환경별 핵심 차이 표

| 환경 | 폰트 통합 | shadcn init | RSC 지원 | 권장도 |
|---|---|---|:-:|:-:|
| **Next.js App Router 14+** | `next/font/local` | `rsc: true` | ✅ | ⭐⭐⭐ (기본) |
| **Next.js Pages Router** | `next/font/local` (`_app.tsx`) | `rsc: false` | ❌ | ⭐⭐ |
| **Vite + React** | `@import` in CSS | `rsc: false` | ❌ | ⭐⭐ |
| **Remix** | `links()` export | `rsc: false` (Remix는 자체 RSC 모델) | ⚠️ | ⭐ |

### 11.2 Next.js Pages Router

```tsx
// pages/_app.tsx
import "@/styles/globals.css";
import type { AppProps } from "next/app";
import localFont from "next/font/local";

const pretendard = localFont({
  src: "../public/fonts/PretendardVariable.woff2",
  display: "swap",
  weight: "45 920",
  variable: "--font-pretendard",
});

export default function App({ Component, pageProps }: AppProps) {
  return (
    <main className={`${pretendard.variable} font-pretendard antialiased`}>
      <Component {...pageProps} />
    </main>
  );
}
```

`components.json` 차이: `"rsc": false`로 변경. 나머지는 동일.

### 11.3 Vite + React

```bash
npm create vite@latest my-app -- --template react-ts
cd my-app
npm install lucide-react framer-motion clsx tailwind-merge class-variance-authority
npx shadcn@latest init  # rsc: false 선택
```

`src/index.css`:

```css
@import "tailwindcss";

/* Pretendard CDN 또는 npm */
@import "https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable.min.css";
/* 또는: @import "pretendard/dist/web/variable/pretendardvariable.css"; */

:root {
  --font-pretendard: "Pretendard Variable", Pretendard, system-ui, sans-serif;
}

@layer base {
  body {
    font-family: var(--font-pretendard);
    @apply antialiased bg-zinc-50 text-zinc-950;
  }
  h1, h2, h3, h4, h5, h6, p, li, dt, dd {
    word-break: keep-all;
    overflow-wrap: break-word;
  }
}
```

```tsx
// src/main.tsx (lang 속성을 HTML 루트에 반드시)
// → public/index.html 또는 root html에 <html lang="ko"> 강제
```

### 11.4 Remix

```tsx
// app/root.tsx
import type { LinksFunction } from "@remix-run/node";
import { Links, Meta, Outlet, Scripts } from "@remix-run/react";

export const links: LinksFunction = () => [
  {
    rel: "stylesheet",
    href: "https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable.min.css",
  },
];

export default function App() {
  return (
    <html lang="ko">
      <head>
        <Meta />
        <Links />
      </head>
      <body className="font-pretendard antialiased">
        <Outlet />
        <Scripts />
      </body>
    </html>
  );
}
```

### 11.5 환경별 검증 차이

Pre-Flight #10 (Pretendard 강제) 검증 시 환경별로 다른 패턴 매칭:

| 환경 | 검증 패턴 |
|---|---|
| App Router | `localFont({ src: ".../PretendardVariable.woff2"` |
| Pages Router | `_app.tsx`에 `localFont` import |
| Vite | `@import "...pretendard..."` in CSS |
| Remix | `links()` 함수에 pretendard CDN URL |

스킬은 `package.json`의 dependencies로 환경 자동 감지 후 해당 패턴 검증:
- `next` 있고 `app/layout.tsx` → Next.js App Router
- `next` 있고 `pages/_app.tsx` → Next.js Pages Router
- `vite` → Vite
- `@remix-run/*` → Remix

Phase 0은 App Router 기본. 다른 환경은 Phase 1+에서 풀 동작 검증 추가.
