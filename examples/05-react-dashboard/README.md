# React 모드 예시: SaaS 대시보드

calm-design의 **React 출력 엔진**을 활용한 예시입니다.

## 사용 라이브러리

| 라이브러리 | 용도 | 버전 |
|-----------|------|-----|
| **shadcn/ui** | UI 컴포넌트 | - |
| **lucide-react** | 아이콘 | ^0.400 |
| **framer-motion** | 애니메이션 | ^11.0 |
| **zustand** | 상태 관리 | ^4.5 |
| Tailwind CSS | 스타일링 | ^3.4 |
| Next.js | 프레임워크 | ^14.2 |

## 주요 특징

### 1. shadcn/ui 컴포넌트

```tsx
// components/ui/button.tsx
// loading prop 추가 — Pre-Flight #17 충족
<Button loading={isSubmitting}>제출</Button>
```

### 2. zustand 상태 관리

```tsx
// lib/stores/use-app-store.ts
// 사이드바 상태를 여러 컴포넌트에서 공유
const { isSidebarOpen, toggleSidebar } = useAppStore();
```

### 3. Framer Motion 애니메이션

```tsx
// components/motion/fade-up.tsx
// Spring physics 기반 진입 애니메이션
<FadeUp delay={0.1}>
  <Card>...</Card>
</FadeUp>
```

### 4. lucide-react 아이콘

```tsx
import { Plus, TrendingUp, Users } from "lucide-react";
<Plus className="w-4 h-4" />
```

## 실행 방법

```bash
# 1. 의존성 설치
npm install

# 2. Pretendard 폰트 다운로드 (public/fonts/)
# https://github.com/orioncactus/pretendard/releases

# 3. 개발 서버 실행
npm run dev
```

## 파일 구조

```
05-react-dashboard/
├── app/
│   ├── layout.tsx      # Pretendard 폰트 등록
│   ├── globals.css     # Tailwind + CSS 변수
│   └── page.tsx        # 대시보드 페이지
├── components/
│   ├── ui/             # shadcn 컴포넌트
│   │   ├── button.tsx  # loading prop 추가
│   │   └── card.tsx    # Empty 상태 추가
│   ├── sections/       # 페이지 섹션
│   │   ├── sidebar.tsx # zustand 사용
│   │   └── topbar.tsx
│   └── motion/         # 애니메이션 래퍼
│       └── fade-up.tsx
├── lib/
│   ├── utils.ts        # cn() 헬퍼
│   └── stores/         # zustand 스토어
│       └── use-app-store.ts
└── package.json
```

## calm-design 적용 사항

- ✅ Pretendard 폰트 (한국어 1순위)
- ✅ Off-Black (#0A0A0A) 사용 (Pure Black 금지)
- ✅ 에메랄드 단일 액센트 (보라/파랑 그래디언트 금지)
- ✅ 비대칭 벤토 그리드 (동일 카드 3개 금지)
- ✅ min-h-[100dvh] (h-screen 금지)
- ✅ word-break: keep-all (한국어 줄바꿈)
- ✅ Button loading 상태 (6상태 충족)
- ✅ Spring physics 애니메이션
