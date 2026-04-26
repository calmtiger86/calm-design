# Library Policy: shadcn/ui (React 모드 기본 컴포넌트)

calm-design React 출력 엔진의 **기본 컴포넌트 라이브러리**. 가장 널리 쓰이는 React 디자인 시스템 OSS의 살아있는 표준이며, 우리는 그 위에 한국어 환경 + 차분 톤을 얹는다.

## 0. 정책 한 줄

> shadcn은 npm 의존이 아닌 **컴포넌트 직접 복사 방식**. 우리는 shadcn 컴포넌트를 추가한 뒤 한국어 환경(Pretendard, word-break, tabular-nums)과 calm-design 톤(Spring physics, 단일 액센트, Loading 상태)으로 **수정해서 사용**한다.

## 1. 라이선스

- **MIT** — 상업·재배포·수정 자유
- 컴포넌트 코드를 프로젝트로 복사하므로 **버전 잠금 없음** — 우리 마음대로 수정 가능

## 2. 초기 설정

```bash
npx shadcn@latest init
```

대화형 프롬프트 응답 (calm-design 권장값):

```
✓ Which style would you like to use? → new-york
  (default보다 정제된 톤. 차분한 calm-design 철학과 부합)
✓ Which color would you like to use as base color? → zinc
  (Slate/Gray보다 미세하게 차가운 톤. neutral 베이스로 가장 보편)
✓ Where is your global CSS file? → app/globals.css
✓ Do you want to use CSS variables for colors? → yes
✓ Where is your tailwind.config.ts? → tailwind.config.ts
✓ Configure import alias? → @/*
✓ Are you using React Server Components? → yes
```

생성되는 `components.json`:

```json
{
  "$schema": "https://ui.shadcn.com/schema.json",
  "style": "new-york",
  "rsc": true,
  "tsx": true,
  "tailwind": {
    "config": "tailwind.config.ts",
    "css": "app/globals.css",
    "baseColor": "zinc",
    "cssVariables": true
  },
  "aliases": {
    "components": "@/components",
    "utils": "@/lib/utils",
    "ui": "@/components/ui"
  }
}
```

## 3. Phase 0 권장 컴포넌트 세트

랜딩페이지·대시보드 양쪽 커버하는 최소 8개:

```bash
npx shadcn@latest add button
npx shadcn@latest add card
npx shadcn@latest add input
npx shadcn@latest add label
npx shadcn@latest add dialog
npx shadcn@latest add dropdown-menu
npx shadcn@latest add separator
npx shadcn@latest add skeleton
```

추가로 데이터 UI일 때:

```bash
npx shadcn@latest add table
npx shadcn@latest add tabs
npx shadcn@latest add badge
```

## 4. 한국어 환경 자동 수정

shadcn이 생성한 컴포넌트는 영문 환경 가정. calm-design은 추가로 다음을 자동 적용:

### 4.1 Button — `loading` prop 추가 (Pre-Flight #17)

shadcn 기본 Button에는 Loading 상태가 없음. 추가:

```tsx
// components/ui/button.tsx (shadcn 기본 + loading prop)
import { Loader2 } from "lucide-react";

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement>,
                              VariantProps<typeof buttonVariants> {
  asChild?: boolean;
  loading?: boolean; // 한국어 환경 + Pre-Flight #17 충족
}

// ... forwardRef 안에서
{loading && <Loader2 className="animate-spin" />}
{children}
```

### 4.2 Card — Empty/Error 변형 추가 (Pre-Flight #21)

```tsx
// components/ui/card.tsx 추가 변형
export function CardEmpty({ icon: Icon, title, description }: {
  icon?: React.ComponentType<{ className?: string }>;
  title: string;
  description?: string;
}) {
  return (
    <div className="text-center py-12">
      {Icon && <Icon className="mx-auto w-16 h-16 text-mute" />}
      <p className="mt-4 font-medium break-keep">{title}</p>
      {description && (
        <p className="mt-1 text-sm text-mute break-keep max-w-sm mx-auto">
          {description}
        </p>
      )}
    </div>
  );
}
```

### 4.3 Input — 한국어 친화 base

```tsx
// components/ui/input.tsx
const Input = React.forwardRef<HTMLInputElement, ...>(
  ({ className, type, ...props }, ref) => (
    <input
      type={type}
      ref={ref}
      className={cn(
        "flex h-10 w-full rounded-md border border-zinc-200 bg-white px-3 py-2 text-sm",
        "ring-offset-background placeholder:text-mute",
        "focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-accent focus-visible:ring-offset-2",
        "disabled:cursor-not-allowed disabled:opacity-50",
        "break-keep", // 한국어 placeholder 줄바꿈
        className
      )}
      {...props}
    />
  )
);
```

## 5. CSS 변수 매핑 (`app/globals.css`)

shadcn이 자동 생성하는 CSS 변수에 calm-design 컬러 추가:

```css
@layer base {
  :root {
    /* shadcn 기본 (zinc base) */
    --background: 0 0% 100%;
    --foreground: 240 10% 3.9%;
    --card: 0 0% 100%;
    --card-foreground: 240 10% 3.9%;
    --primary: 240 5.9% 10%;
    --primary-foreground: 0 0% 98%;
    /* ... */

    /* calm-design 추가 */
    --ink: 0 0% 4%;             /* #0A0A0A — Pure Black 대체 */
    --mute: 240 4% 46%;         /* #71717A */
    --accent: 158 64% 40%;      /* Emerald — 단일 액센트 (DESIGN.md Section 2와 동기화) */
    --border-subtle: 240 6% 90%;
  }

  .dark {
    /* 다크모드 — Off-Black 베이스 */
    --background: 0 0% 4%;     /* #0A0A0A */
    --foreground: 0 0% 98%;
    --card: 240 4% 8%;
    /* ... */
  }
}
```

## 6. 차단 정책 (shadcn 사용 시 절대 금지)

### 6.1 Inter 폰트 차단

shadcn 기본 템플릿이 Inter를 자동 import하는 경우가 있음. **반드시 제거**하고 Pretendard로 교체:

```tsx
// ❌ shadcn create-next-app 기본 layout.tsx
import { Inter } from "next/font/google";
const inter = Inter({ subsets: ["latin"] });

// ✅ calm-design 교체
import localFont from "next/font/local";
const pretendard = localFont({
  src: "../public/fonts/PretendardVariable.woff2",
  display: "swap",
  weight: "45 920",
  variable: "--font-pretendard",
});
```

### 6.2 Radix UI 직접 import 금지

shadcn은 내부적으로 Radix UI에 의존. **사용자는 shadcn 인터페이스로만 사용** — Radix 직접 import 금지.

```tsx
// ❌ 금지
import * as DialogPrimitive from "@radix-ui/react-dialog";

// ✅ shadcn 통해서만
import { Dialog, DialogContent, DialogHeader } from "@/components/ui/dialog";
```

이유: Radix 직접 사용은 shadcn의 모든 스타일링·접근성·트랜지션을 잃음.

### 6.3 다른 React UI 라이브러리 동시 사용 금지

```tsx
// ❌ 금지 — 다중 디자인 시스템 충돌
import { Button as MuiButton } from "@mui/material";
import { Button as AntButton } from "antd";
import { Button } from "@/components/ui/button"; // shadcn

// ✅ shadcn만
import { Button } from "@/components/ui/button";
```

## 7. shadcn Block 활용 (선택)

shadcn은 컴포넌트뿐 아니라 **완성된 UI 블록**도 제공 (https://ui.shadcn.com/blocks):

```bash
npx shadcn@latest add login-01
npx shadcn@latest add dashboard-01
npx shadcn@latest add sidebar-07
```

calm-design 권장 블록:
- `dashboard-01` — SaaS 대시보드 시작점
- `sidebar-07` — Linear 스타일 사이드바
- `login-01` — 인증 폼

**주의**: 블록도 그대로 쓰지 말고, **한국어 환경 + 안티-슬롭 적용 후** 사용. AI Tells 검증 통과 필수.

## 8. 검증 (Pre-Flight 통합)

```
[검사 항목]
✅ components.json 존재
✅ components/ui/ 폴더에 shadcn 컴포넌트들 (직접 복사된 것)
✅ Inter 폰트 미import (Pretendard 교체됨)
✅ Button에 loading prop (또는 동등한 6상태)
✅ @radix-ui/* 직접 import 부재 (shadcn 자동 의존만)
✅ 다른 React UI 라이브러리(MUI, Antd, Chakra) 부재

[자동 매칭]
- 파일 트리에 components/ui/button.tsx 존재 → ✅
- "from \"next/font/google\"" + "Inter" → ❌
- "@radix-ui/" 직접 import (단, components/ui/ 안의 사용은 OK) → ❌
- "@mui/", "antd/", "@chakra-ui/" → ❌
```

## 9. 출처·참조

- 공식 사이트: https://ui.shadcn.com
- GitHub: https://github.com/shadcn-ui/ui
- 라이선스: MIT
- Blocks: https://ui.shadcn.com/blocks
- Themes: https://ui.shadcn.com/themes (DESIGN.md Section 2 변환에 활용 가능)

React 디자인 시스템의 살아있는 표준. 우리는 이 위에 한국어 + 차분 톤을 얹는다.
