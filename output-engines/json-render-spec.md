# Output Engine: JSON Render Spec (멀티플랫폼 동시 출력)

calm-design의 6번째 출력 엔진. DESIGN.md를 [vercel-labs/json-render](https://github.com/vercel-labs/json-render)의 JSON Spec으로 변환하여 React/React Native/PDF/Email/Video/3D 등 멀티플랫폼에 동일 산출물로 렌더링.

> Phase 1.5 활성화 (json-render 점진 채택). 기존 출력 엔진(html-tailwind, react-shadcn) 보완 — 대체 X.

## 1. 트리거 시그널

다음 키워드 등장 시 이 엔진 사용:
- "JSON 스펙으로", "json-render로"
- "멀티플랫폼으로 한 번에", "웹+모바일 동시"
- "React Native·PDF·Email 동시 생성"
- "Spec 파일만 줘"

> 이 엔진은 다른 출력 엔진과 **공존** 가능. 사용자가 "HTML도 함께 뽑아줘" 하면 html-tailwind와 동시 실행.

## 2. JSON Spec 구조 (json-render `Spec` 타입 준수)

```typescript
interface Spec {
  root: string;                          // 시작 요소 키
  elements: Record<string, UIElement>;   // 평탄 맵
  state?: Record<string, unknown>;       // 초기 상태 (테마·데이터)
}

interface UIElement {
  type: string;                          // 카탈로그의 컴포넌트명
  props: Record<string, unknown>;
  children?: string[];                   // 자식 요소 키
  visible?: VisibilityCondition;         // 조건부 표시
  on?: Record<string, ActionBinding>;    // 이벤트 바인딩
  repeat?: { statePath: string };        // 배열 반복
}
```

## 3. DESIGN.md → JSON Spec 변환 매핑 (9-섹션 → Spec)

| DESIGN.md 섹션 | JSON Spec 위치 | 변환 규칙 |
|---|---|---|
| 1. Visual Theme & Atmosphere | `state.theme.atmosphere` | 자유 텍스트 그대로 |
| 2. Color Palette & Roles | `state.theme.colors` | 표 → `{ canvas, surface, ink, mute, border, accent, ... }` 객체 |
| 3. Typography Rules | `state.theme.typography` | `{ fontFamily, headingClasses, bodyClasses, breakKeep: true }` |
| 4. Component Stylings | `elements[*].props` | 각 컴포넌트 정의 → 카탈로그 등록 |
| 5. Layout Principles | `elements.root.children[]` | 페이지 섹션 순서 → root의 children 배열 |
| 6. Depth & Elevation | `state.theme.elevation` | shadow·z-index 정책 |
| 7. Motion & Interaction | `state.theme.motion` + `elements[*].on` | spring 표준값 + 이벤트 바인딩 |
| 8. Responsive Behavior | (json-render의 responsive props) | breakpoint 분기 |
| 9. Anti-Patterns | (변환 시 차단 검증) | 위반 시 변환 거부 |

## 4. 변환 예시 (한국 SaaS 대시보드)

### 입력: DESIGN.md (요약)

```markdown
## 2. Color Palette & Roles
| Canvas | #FAFAFA | 페이지 배경 |
| Surface | #FFFFFF | 카드 배경 |
| Ink | #0A0A0A | 본문 |
| Accent | #10B981 | CTA |

## 5. Layout Principles
- 구조: Sidebar 240px + Main flex-1
- 페이지 섹션: PageHeader → KPICards → MainChart → ActivityFeed
```

### 출력: spec.json

```json
{
  "root": "dashboard",
  "elements": {
    "dashboard": {
      "type": "DashboardLayout",
      "props": { "sidebarWidth": 240 },
      "children": ["sidebar", "main"]
    },
    "sidebar": {
      "type": "Sidebar",
      "props": { "logo": "calm.io" },
      "children": ["nav-items"]
    },
    "main": {
      "type": "MainArea",
      "children": ["page-header", "kpi-grid", "main-chart", "activity"]
    },
    "page-header": {
      "type": "PageHeader",
      "props": {
        "title": "대시보드",
        "subtitle": { "$state": "/today_label" }
      }
    },
    "kpi-grid": {
      "type": "BentoGrid",
      "props": { "columns": 4, "gap": 16 },
      "children": ["kpi-revenue", "kpi-users", "kpi-conversion"]
    },
    "kpi-revenue": {
      "type": "KPICard",
      "props": {
        "label": "월 매출",
        "value": { "$state": "/metrics/revenue" },
        "delta": { "$state": "/metrics/revenue_delta" },
        "span": 2
      }
    }
  },
  "state": {
    "theme": {
      "language": "ko",
      "colors": {
        "canvas": "#FAFAFA",
        "surface": "#FFFFFF",
        "ink": "#0A0A0A",
        "mute": "#71717A",
        "border": "#E4E4E7",
        "accent": "#10B981"
      },
      "typography": {
        "fontFamily": "'Pretendard Variable', Pretendard, system-ui, sans-serif",
        "breakKeep": true
      },
      "motion": {
        "ease": [0.16, 1, 0.3, 1],
        "duration": 0.6,
        "respectsReducedMotion": true
      }
    },
    "today_label": "2026년 4월 26일 기준",
    "metrics": {
      "revenue": 12847000,
      "revenue_delta": 12.4,
      "users": 8431,
      "conversion": 3.2
    }
  }
}
```

## 5. 카탈로그 정의 (json-render `defineCatalog`)

calm-design은 자체 카탈로그 + json-render/shadcn 카탈로그를 합쳐 사용:

```typescript
// lib/calm-catalog.ts
import { defineCatalog } from "@json-render/core";
import { z } from "zod";
import { shadcnCatalog } from "@json-render/shadcn/catalog";

export const calmCatalog = defineCatalog({
  components: {
    ...shadcnCatalog.components,  // shadcn 36개 사전구성

    // calm-design 자체 컴포넌트
    DashboardLayout: {
      props: z.object({ sidebarWidth: z.number().default(240) }),
      slots: ["sidebar", "main"],
      description: "한국 SaaS 대시보드 표준 레이아웃 (Sidebar + Main)",
    },
    PageHeader: {
      props: z.object({
        title: z.string(),
        subtitle: z.string().optional(),
        action: z.any().optional(),
      }),
      description: "페이지 제목 + 서브타이틀 + 우측 Primary Action",
    },
    BentoGrid: {
      props: z.object({
        columns: z.number().min(1).max(6).default(4),
        gap: z.number().default(16),
      }),
      slots: ["children"],
      description: "비대칭 카드 그리드 (3-column equal 회피)",
    },
    KPICard: {
      props: z.object({
        label: z.string(),
        value: z.union([z.string(), z.number()]),
        delta: z.number().optional(),
        span: z.number().min(1).max(4).default(1),
        format: z.enum(["currency", "number", "percent"]).optional(),
      }),
      description: "대시보드 KPI 카드. value는 자동 tabular-nums.",
    },
    // 한국 SaaS 시그니처 (korean-saas-patterns.md 동기)
    TossInput: {
      props: z.object({
        label: z.string(),
        error: z.string().optional(),
        type: z.enum(["text", "email", "password", "tel"]).default("text"),
      }),
      description: "토스 스타일 floating label input. 한국어 친화 (break-keep).",
    },
    TossBottomSheet: {
      props: z.object({ open: z.boolean(), title: z.string() }),
      slots: ["children"],
      description: "모바일 결제 흐름 — 하단 시트 + 드래그 핸들.",
    },
    DaangnRecommendCarousel: {
      props: z.object({
        title: z.string().default("오늘 추천드려요"),
        items: z.array(z.object({
          id: z.string(),
          title: z.string(),
          price: z.number(),
          location: z.string(),
          image: z.string().url(),
        })),
      }),
      description: "당근 스타일 가로 스크롤 추천 카드.",
    },
  },
  actions: {
    setState: { params: z.object({ statePath: z.string(), value: z.any() }) },
    pushState: { params: z.object({ statePath: z.string(), value: z.any() }) },
  },
});
```

## 6. 변환 스크립트 — `scripts/design-md-to-spec.py`

```bash
python scripts/design-md-to-spec.py \
  --design examples/01-saas-dashboard-ko/DESIGN.md \
  --output examples/01-saas-dashboard-ko/spec.json
```

스크립트는:
1. DESIGN.md 9-섹션 파싱
2. `validate-design-md.py` 통과 검증 (변환 전 게이트)
3. 각 섹션 → JSON Spec 위치로 매핑
4. `calm-catalog`의 컴포넌트 스키마(Zod)로 props 검증
5. 출력: `spec.json` (들여쓰기 2)

## 7. 멀티플랫폼 렌더링 (사용자가 직접 실행)

JSON Spec이 있으면 사용자는 다음 4개 플랫폼에 동일 Spec으로 렌더:

```tsx
// 1. Web (React)
import { Renderer } from "@json-render/react";
import { calmCatalog } from "@/lib/calm-catalog";
import { calmRegistry } from "@/lib/calm-registry";

<Renderer spec={spec} catalog={calmCatalog} registry={calmRegistry.web} />

// 2. React Native
import { Renderer as NativeRenderer } from "@json-render/react-native";
<NativeRenderer spec={spec} catalog={calmCatalog} registry={calmRegistry.native} />

// 3. PDF
import { renderToBuffer } from "@json-render/react-pdf";
const pdf = await renderToBuffer(spec, calmCatalog, calmRegistry.pdf);

// 4. Email (HTML)
import { renderToHtml } from "@json-render/react-email";
const html = await renderToHtml(spec, calmCatalog, calmRegistry.email);
```

각 registry는 같은 카탈로그 컴포넌트를 플랫폼별로 구현. calm-design은 web·native registry를 기본 제공, pdf·email은 Phase 4에서 추가.

## 8. 한국어 환경 자동 적용

JSON Spec 변환 시 LANGUAGE=ko면 자동으로:

- `state.theme.typography.fontFamily` = Pretendard 우선 체인
- `state.theme.typography.breakKeep = true` → registry의 React 컴포넌트가 `word-break: keep-all` 자동 적용
- 한국어 placeholder·라벨 자동 매핑

## 9. 검증 (Pre-Flight 통합)

JSON Spec 출력 직후 자동 체크:

- [ ] `root` 키가 `elements`에 존재
- [ ] 모든 `children` 참조가 유효한 키
- [ ] 각 element의 `type`이 `calmCatalog.components`에 등록됨
- [ ] `props`가 Zod 스키마 통과 (LLM hallucination 차단)
- [ ] `state.theme.colors`에 Pure Black 부재
- [ ] LANGUAGE=ko면 `breakKeep: true` 강제
- [ ] visibility/repeat 표현식이 유효한 statePath

7개 중 1개라도 실패 → 자동 재생성 (최대 3회).

## 10. 안티-슬롭 자동 차단 (json-render 통합 후)

기존 `references/ai-tells-blocklist.md`의 50+ 패턴을 JSON Spec 검증에 통합:

- `state.theme.colors.ink === "#000000"` → ❌ Pre-Flight #6 (Pure Black 차단)
- `props.font` 안에 `Inter` 문자열 → ❌ Pre-Flight #9
- `BentoGrid.props.columns === 3` + 동일 카드 3개 children → ⚠️ Pre-Flight #5

## 11. 라이선스

- json-render: Apache-2.0
- calm-design: MIT
- 결합: 양방향 호환. NOTICE 파일에 Apache-2.0 표기 (LICENSE 옆에 추가됨)
