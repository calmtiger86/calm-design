# Library Policy: json-render (멀티플랫폼 렌더링)

calm-design의 6번째 출력 엔진(`json-render-spec`)이 의존하는 라이브러리. Vercel Labs의 Generative UI Framework. Phase 1.5 점진 채택.

## 0. 정책 한 줄

> JSON Spec 출력 모드 선택 시 `@json-render/core` + `@json-render/shadcn` 채택. 다른 패키지는 Phase 4+에서 사용자 요청 시만.

## 1. 라이선스

- **Apache-2.0** — 상업·재배포·수정 자유
- **NOTICE 파일 의무**: 재배포 시 라이선스 사본 포함 + 변경 사항 표기
- calm-design은 `NOTICE` 파일에 json-render Apache-2.0 표기 자동 추가

## 2. Phase 1.5 채택 패키지 (3개만)

| 패키지 | 역할 | calm-design 사용 위치 |
|---|---|---|
| `@json-render/core` | 핵심 타입(Spec, UIElement) + 카탈로그 + 스트리밍 컴파일러 | 변환 스크립트, 검증 |
| `@json-render/shadcn` | 36개 사전 구성 shadcn 컴포넌트 카탈로그 | React 모드 보강 |
| `@json-render/react` | React 렌더러 | 사용자 측 렌더링 (calm-design은 정의만) |

## 3. 향후 채택 후보 (Phase 4+, 사용자 요청 시)

| 패키지 | 트리거 |
|---|---|
| `@json-render/react-native` | "모바일 앱으로도 줘" |
| `@json-render/react-pdf` | "PDF 다운로드용" |
| `@json-render/react-email` | "이메일 템플릿" |
| `@json-render/remotion` | "비디오로" |
| `@json-render/devtools-react` | "디버깅 강화" |

Phase 4 도입 결정은 사용자 가치 검증 후.

## 4. 설치

```bash
npm install @json-render/core @json-render/shadcn @json-render/react zod
```

shadcn 컴포넌트는 별도 셋업 불필요 — `@json-render/shadcn`이 카탈로그 + 구현 모두 제공.

## 5. 사용 패턴

### 5.1 카탈로그 정의 (calm-design 자체 컴포넌트 + shadcn 합성)

```typescript
// lib/calm-catalog.ts
import { defineCatalog } from "@json-render/core";
import { shadcnCatalog } from "@json-render/shadcn";
import { z } from "zod";

export const calmCatalog = defineCatalog({
  components: {
    ...shadcnCatalog.components,  // shadcn 36개 자동 포함

    // calm-design 자체 컴포넌트 (korean-saas-patterns.md와 동기)
    PageHeader: {
      props: z.object({
        title: z.string(),
        subtitle: z.string().optional(),
      }),
      description: "페이지 제목 + 부제",
    },
    BentoGrid: {
      props: z.object({
        columns: z.number().min(1).max(6).default(4),
      }),
      slots: ["children"],
      description: "비대칭 카드 그리드",
    },
    KPICard: {
      props: z.object({
        label: z.string(),
        value: z.union([z.string(), z.number()]),
        delta: z.number().optional(),
      }),
      description: "KPI 카드 (tabular-nums 자동)",
    },
    TossInput: { /* ... */ },
    TossBottomSheet: { /* ... */ },
    DaangnRecommendCarousel: { /* ... */ },
  },
  actions: {
    setState: { params: z.object({ statePath: z.string(), value: z.any() }) },
  },
});
```

### 5.2 Registry 구현 (실제 컴포넌트 매핑)

```typescript
// lib/calm-registry.ts (web)
import { defineRegistry } from "@json-render/react";
import { calmCatalog } from "./calm-catalog";
import { shadcnRegistry } from "@json-render/shadcn/react";

import { PageHeader } from "@/components/page-header";
import { BentoGrid } from "@/components/bento-grid";
import { KPICard } from "@/components/kpi-card";
import { TossInput } from "@/components/patterns/toss-input";
// ... korean-saas-patterns.md 7개 컴포넌트

export const calmRegistry = defineRegistry(calmCatalog, {
  components: {
    ...shadcnRegistry.components,

    PageHeader: ({ props }) => <PageHeader {...props} />,
    BentoGrid: ({ props, slots }) => <BentoGrid columns={props.columns}>{slots.children}</BentoGrid>,
    KPICard: ({ props }) => <KPICard {...props} />,
    TossInput: ({ props }) => <TossInput {...props} />,
    // ...
  },
});
```

### 5.3 사용자 측 렌더링

```tsx
import { Renderer } from "@json-render/react";
import { calmCatalog, calmRegistry } from "@/lib/calm-catalog";
import spec from "@/calm-design/spec.json";

export default function Page() {
  return (
    <Renderer spec={spec} catalog={calmCatalog} registry={calmRegistry} />
  );
}
```

## 6. 한국어 환경 통합

JSON Spec의 `state.theme.language === "ko"` 시 calm-design registry는 자동으로:

- 모든 텍스트 컴포넌트에 `style={{ wordBreak: "keep-all" }}` 적용
- `font-family` Pretendard 강제
- `font-thin/extralight/light` 차단 (Pre-Flight #13 통과)

이는 registry 구현 시 wrapper로 처리 — 사용자가 별도 신경 X.

## 7. SpecStream 스트리밍 (Phase 2 Mode D 진입 시)

```typescript
import { createSpecStreamCompiler } from "@json-render/core";

const compiler = createSpecStreamCompiler<Spec>();

// LLM이 JSON Patch 라인 단위로 스트리밍
for await (const chunk of llmStream) {
  const { result, newPatches } = compiler.push(chunk);
  // result는 부분 완성 Spec — 즉시 렌더 가능
  setSpec(result);
}

const finalSpec = compiler.getResult();
```

Mode D 3안 동시 생성 시 각 베리언트가 점진 표시 — calm-design "Calm" 정체성과 일치.

## 8. 절대 금지 (정체성 보존)

다음을 채택하지 않음 — calm-design 자체 자산 우선:

- ❌ json-render `DevTools UI` 디자인 색상 차용 (Vercel 톤이 calm-design과 충돌)
- ❌ json-render의 `prompt()` 함수가 calm-design `references/prompt-enhancement.md`를 대체하지 않음 (보강만)
- ❌ json-render `Three Fiber·Remotion` 패키지 자동 채택 (Phase 4+ 사용자 요청 시만)

## 9. NOTICE 파일 추가 의무

`NOTICE` 파일이 calm-design 루트에 추가됨:

```
calm-design — Korean-first AI design skill
Copyright (c) 2026 정민 (@calmtiger_)

This project incorporates components from:

  json-render (vercel-labs/json-render)
  Copyright Vercel Labs
  Licensed under Apache License 2.0
  https://github.com/vercel-labs/json-render
```

## 10. 검증 (Pre-Flight 통합)

JSON Spec 모드에서 자동 체크:

- [ ] `@json-render/core` import 존재 (사용자 코드)
- [ ] `defineCatalog` 호출 시 `@json-render/shadcn`의 `shadcnCatalog` 통합
- [ ] calm-design 한국 SaaS 패턴 7개가 카탈로그에 등록됨
- [ ] Spec 출력 직후 Zod 검증 통과
- [ ] NOTICE 파일이 프로젝트 루트에 존재 (재배포 시)

## 11. 출처·참조

- 공식: https://json-render.dev
- GitHub: https://github.com/vercel-labs/json-render
- 라이선스: Apache-2.0
- 핵심 패키지: `@json-render/core`, `@json-render/shadcn`, `@json-render/react`
