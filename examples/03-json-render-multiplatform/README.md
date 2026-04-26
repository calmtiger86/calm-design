# Example 03 — JSON Render 멀티플랫폼

calm-design 6번째 출력 엔진(`json-render-spec`) 데모. **하나의 DESIGN.md → 하나의 JSON Spec → Web/React Native/PDF/Email 4개 플랫폼 동시 출력**.

## 산출물

- [`DESIGN.md`](./DESIGN.md) — 9-섹션 설계 (1차 산출물)
- [`spec.json`](./spec.json) — json-render Spec (자동 변환됨)

## 변환 명령

```bash
python scripts/design-md-to-spec.py \
  --design examples/03-json-render-multiplatform/DESIGN.md \
  --output examples/03-json-render-multiplatform/spec.json
```

→ DESIGN.md 9-섹션 검증(16항목) → 자동 통과 → JSON Spec 생성 완료.

## 4개 플랫폼 사용법

JSON Spec은 동일하지만 registry만 플랫폼별로 다름.

### 1. Web (React + Next.js)

```bash
npm install @json-render/core @json-render/shadcn @json-render/react zod
```

```tsx
// app/login/page.tsx
import { Renderer } from "@json-render/react";
import { calmCatalog, calmWebRegistry } from "@/lib/calm-catalog";
import spec from "@/calm-design/spec.json";

export default function Login() {
  return (
    <main className="min-h-[100dvh] flex items-center justify-center bg-zinc-50">
      <Renderer spec={spec} catalog={calmCatalog} registry={calmWebRegistry} />
    </main>
  );
}
```

### 2. React Native (모바일 앱)

```bash
npm install @json-render/react-native
```

```tsx
// App.tsx
import { Renderer } from "@json-render/react-native";
import { calmCatalog, calmNativeRegistry } from "./lib/calm-catalog";
import spec from "./calm-design/spec.json";

export default function App() {
  return <Renderer spec={spec} catalog={calmCatalog} registry={calmNativeRegistry} />;
}
```

### 3. PDF 다운로드용

```bash
npm install @json-render/react-pdf
```

```tsx
import { renderToBuffer } from "@json-render/react-pdf";
import { calmCatalog, calmPdfRegistry } from "./lib/calm-catalog";

const pdfBuffer = await renderToBuffer(spec, calmCatalog, calmPdfRegistry);
fs.writeFileSync("signup-form.pdf", pdfBuffer);
```

### 4. 이메일 템플릿 (HTML)

```bash
npm install @json-render/react-email
```

```tsx
import { renderToHtml } from "@json-render/react-email";
import { calmCatalog, calmEmailRegistry } from "./lib/calm-catalog";

const html = await renderToHtml(spec, calmCatalog, calmEmailRegistry);
// 이메일 발송 라이브러리(Resend 등)로 전송
```

## 동일한 결과, 다른 플랫폼

| 플랫폼 | TossInput 렌더 | TossPrimaryButton 렌더 | 한국어 처리 |
|---|---|---|---|
| Web | `<input>` + floating label CSS | `<button>` + Framer Motion scale | `word-break: keep-all` 자동 |
| Native | `<TextInput>` + Animated.View | `<TouchableOpacity>` + spring | NativeBase 또는 자체 한국어 폰트 |
| PDF | `<Text>` + `<TextField>` | `<Button>` (정적) | Pretendard 폰트 임베드 |
| Email | `<table>` 기반 input | inline-styled button | 웹폰트 fallback (Pretendard X일 시 system) |

## 핵심 가치

- **DESIGN.md 1번 작성 → 4개 플랫폼 동시 지원** (calm-design 단독으로는 불가능)
- 한국어 처리(Pretendard, word-break) 모든 플랫폼 자동 적용
- 안티-슬롭 50개 + Pre-Flight 30개 모든 플랫폼 동일하게 통과
- json-render의 Zod 카탈로그가 LLM hallucination 컴포넌트 차단

## 한계 (정직한 명시)

- React Native registry는 사용자가 직접 구현 필요 (calm-design Phase 4에서 풀 지원 예정)
- PDF·Email은 인터랙션 없는 정적 출력 — Spring 모션·hover 효과 무시
- Phase 1.5 채택 범위: `@json-render/core` + `@json-render/shadcn` + `@json-render/react`만. 나머지(native, pdf, email)는 사용자가 옵셔널로 추가.

## 다음 단계 (Phase 4+)

- calm-design이 React Native registry를 자체 제공 (Phase 4)
- PDF·Email registry도 자체 제공 (Phase 4)
- 4개 플랫폼 자동 검증 스크립트 (Phase 4)

지금은 Phase 1.5 — Web만 풀 지원. 나머지는 사용자가 선택적으로 확장 가능.
