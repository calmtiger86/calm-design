# Library Policy: Pretendard (한국어 폰트 강제)

`LANGUAGE=ko`인 모든 출력에서 **반드시** 채택. 다른 한국어 폰트 사용 금지.

## 0. 정책 한 줄 요약

> 한국어 텍스트가 있는 모든 페이지는 Pretendard를 로드해야 한다. 누락 시 Pre-Flight 자동 실패.

## 1. 라이선스

- **SIL Open Font License 1.1** (orioncactus/pretendard)
- 상업적 사용·재배포·임베딩 모두 자유. 라이선스 표기 의무 없음(파일에 포함만).
- 단, 폰트 자체 판매·라이선스 매매 금지 (당연한 조항)

## 2. 출력 엔진별 통합 방식

### 2.1 HTML 모드 (Tailwind CDN)

`<head>`에 다음 CDN 링크를 **첫 번째 폰트 슬롯**으로 추가:

```html
<link rel="stylesheet" as="style" crossorigin
  href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css" />
```

**Variable 폰트** (가변 weight 100-900) 권장:

```html
<link rel="stylesheet" as="style" crossorigin
  href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable.min.css" />
```

이후 Tailwind config 주입:

```html
<script>
  tailwind.config = {
    theme: {
      extend: {
        fontFamily: {
          sans: ['Pretendard Variable', 'Pretendard', 'system-ui', 'sans-serif'],
        },
      },
    },
  };
</script>
```

→ 이후 모든 텍스트가 자동으로 Pretendard 사용 (Tailwind `font-sans`가 기본).

### 2.2 React + Next.js 모드 (`next/font`)

```bash
npm install pretendard
```

```tsx
// app/layout.tsx (Next.js 13+ App Router)
import localFont from "next/font/local";

const pretendard = localFont({
  src: "../public/fonts/PretendardVariable.woff2",
  display: "swap",
  weight: "45 920",
  variable: "--font-pretendard",
});

export default function RootLayout({ children }) {
  return (
    <html lang="ko" className={pretendard.variable}>
      <body className="font-pretendard">{children}</body>
    </html>
  );
}
```

`tailwind.config.ts`:

```ts
fontFamily: {
  sans: ["var(--font-pretendard)", "system-ui", "sans-serif"],
  pretendard: ["var(--font-pretendard)", "system-ui", "sans-serif"],
},
```

### 2.3 일반 React (Vite 등) — npm 패키지

```bash
npm install pretendard
```

```tsx
// main.tsx
import "pretendard/dist/web/variable/pretendardvariable.css";
```

`tailwind.config.js`:

```js
fontFamily: {
  sans: ['"Pretendard Variable"', "Pretendard", "system-ui", "sans-serif"],
},
```

## 3. 필수 동반 CSS (모든 환경 공통)

Pretendard 로드 후 다음 base 스타일을 **반드시** 함께 적용:

```css
html {
  font-family: "Pretendard Variable", Pretendard, system-ui, -apple-system,
               BlinkMacSystemFont, "Segoe UI", sans-serif;
}

/* 한국어 줄바꿈 */
h1, h2, h3, h4, h5, h6, p, li, dt, dd {
  word-break: keep-all;
  overflow-wrap: break-word;
}

/* 숫자 정렬 (선택, 데이터 UI에 권장) */
.tabular { font-variant-numeric: tabular-nums; }
```

## 4. weight 사용 정책

Pretendard Variable은 weight 45-920 가변. 권장 사용 범위:

| 클래스 (Tailwind) | weight | 용도 |
|---|---|---|
| `font-medium` | 500 | 본문, 메타 |
| `font-semibold` | 600 | 헤드라인 H2-H4, 라벨 강조 |
| `font-bold` | 700 | 헤드라인 H1-H2 |
| `font-extrabold` | 800 | 디스플레이 (히어로 큰 글자) |

**금지**:
- `font-thin` (100), `font-extralight` (200), `font-light` (300) — 한국어 가독성 저하
- `font-black` (900) — 광고 톤이라 SaaS·서비스에 부적합 (광고/헤드 카피용은 예외 허용)

## 5. 검증 (Pre-Flight 통합)

스킬은 출력 전 다음을 자동 체크:

```
✅ HTML 모드: <link>에 pretendard CDN URL 포함
✅ React 모드: pretendard 패키지 import 또는 next/font 설정
✅ tailwind.config의 fontFamily.sans에 Pretendard 첫번째 위치
✅ html/body에 font-family 설정 (또는 Tailwind 기본 sans 사용)
✅ 한국어 텍스트 컨테이너에 word-break: keep-all (또는 .break-keep 유틸)
✅ font-thin/extralight/light 한국어 텍스트에 미사용
```

위 6개 중 하나라도 실패 시 → Pre-Flight 차감 → 자동 재생성.

## 6. 폴백 정책

Pretendard CDN이 차단된 환경(중국·일부 기업 방화벽)을 대비해 fallback 명시:

```css
font-family:
  "Pretendard Variable", Pretendard,        /* 1순위: 가변 */
  -apple-system, BlinkMacSystemFont,        /* 2순위: macOS/iOS */
  "Apple SD Gothic Neo",                    /* 3순위: macOS 한글 */
  "Malgun Gothic",                          /* 4순위: Windows */
  system-ui, sans-serif;                     /* 5순위: 보편 */
```

이 폴백 체인은 **Pretendard가 로드된 환경에서는 절대 활성화되지 않음** (1순위가 항상 우선). 단순히 안전망.

## 7. 출처·참조

- 공식 저장소: https://github.com/orioncactus/pretendard
- 공식 사이트: https://pretendard.dev
- npm: https://www.npmjs.com/package/pretendard
- 디자이너: 길형진 (@orioncactus)

한국 디자인 커뮤니티의 사실상 표준이며, 토스·당근·라인 등 주요 한국 SaaS가 모두 채택.
