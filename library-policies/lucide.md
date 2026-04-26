# Library Policy: Lucide (표준 아이콘)

calm-design의 모든 출력에서 **기본 아이콘 라이브러리**. supanova의 Iconify Solar 강제 정책을 폐기하고 lucide로 통일 (shadcn 공식 채택, 더 보편적).

## 0. 정책 한 줄

> 모든 calm-design 출력의 아이콘은 lucide. 다른 세트(Material, Font Awesome, Heroicons)와 혼용 금지. Iconify Solar는 사용자가 명시적으로 `--icons=iconify` 요청 시만 사용.

## 1. 라이선스

- **ISC License** (Feather Icons fork)
- 상업적 사용·재배포·수정 자유
- 라이선스 표기 의무 없음 (표기하면 좋음)

## 2. 출력 엔진별 통합

### 2.1 HTML 모드 (CDN, SVG inline)

CDN 슬롯 #3 사용:

```html
<script src="https://unpkg.com/lucide@latest"></script>
```

마크업에서 `data-lucide` 속성으로 호출:

```html
<i data-lucide="zap"></i>
<i data-lucide="arrow-right" class="w-5 h-5"></i>
<i data-lucide="check-circle" class="w-6 h-6 text-accent"></i>
```

페이지 끝 `<script>`에서 한 번만 렌더:

```html
<script>
  lucide.createIcons();
</script>
```

→ `<i>` 태그가 자동으로 `<svg>`로 치환됨. SVG 인라인이라 외부 요청 추가 0개.

### 2.2 React 모드 (lucide-react)

```bash
npm install lucide-react
```

```tsx
import { Zap, ArrowRight, CheckCircle, Loader2 } from "lucide-react";

<Zap className="w-5 h-5 text-accent" />
<Button>
  시작하기 <ArrowRight className="w-4 h-4" />
</Button>
```

**Tree-shaking 자동**: 사용한 아이콘만 번들에 포함.

## 3. 아이콘 일관성 규칙

### 3.1 Stroke 두께

lucide는 모든 아이콘이 동일 stroke 두께 (기본 2). **혼용 금지 사례**:

```tsx
// ❌ 다른 stroke 두께 혼용
<Zap strokeWidth={2} /><ArrowRight strokeWidth={1.5} />

// ✅ 한 페이지 일관 stroke
<Zap strokeWidth={2} /><ArrowRight strokeWidth={2} />
```

### 3.2 사이즈 표준

| 용도 | 권장 사이즈 |
|---|---|
| Inline text 옆 (버튼 안) | `w-4 h-4` (16px) |
| 작은 아이콘 (메뉴) | `w-5 h-5` (20px) |
| 일반 (카드 헤더) | `w-6 h-6` (24px) |
| Hero 강조 | `w-8 h-8` (32px) |
| 큰 일러스트성 | `w-12 h-12` ~ `w-16 h-16` |

### 3.3 색상

```tsx
<Zap className="text-accent" />     {/* 액센트 색상 */}
<Info className="text-mute" />      {/* 보조 정보 */}
<AlertCircle className="text-red-500" /> {/* 경고/에러 */}
```

→ `currentColor` 자동 활용. `fill` 속성 직접 설정 금지 (stroke 기반 아이콘이라 어색해짐).

## 4. 절대 금지

### 4.1 다른 아이콘 세트와 혼용 금지

```tsx
// ❌ 금지
import { Zap } from "lucide-react";
import { CheckCircle } from "@heroicons/react/24/outline";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";

// ✅ 한 세트만
import { Zap, CheckCircle, Star } from "lucide-react";
```

이유: 세트마다 stroke 두께·corner radius·optical size 다름 → 디자인 일관성 파괴 (`ai-tells-blocklist.md` #29).

### 4.2 Emoji를 UI 라벨에 금지

```tsx
// ❌ 금지
<button>🚀 시작하기</button>
<div>📊 대시보드</div>

// ✅ lucide
<Button>
  <Rocket className="w-4 h-4" />
  시작하기
</Button>
<div className="flex items-center gap-2">
  <BarChart3 className="w-5 h-5" />
  대시보드
</div>
```

이유: Emoji는 OS·브라우저마다 렌더링 다름. 디자인 컨트롤 불가. AI 슬롭 인상 (`ai-tells-blocklist.md` #30).

## 5. Iconify Solar 사용 조건 (예외)

사용자가 명시적으로 `--icons=iconify` 또는 "Iconify로", "Solar 아이콘" 요청 시만:

```html
<!-- HTML 모드 -->
<script src="https://code.iconify.design/iconify-icon/2.3.0/iconify-icon.min.js"></script>
<iconify-icon icon="solar:arrow-right-linear"></iconify-icon>
```

이 경우 lucide와 **혼용 금지** — 한 페이지에 한 세트만.

## 6. 자주 사용하는 lucide 아이콘 (Quick Reference)

| 용도 | 아이콘 이름 |
|---|---|
| 액션·CTA | `arrow-right`, `arrow-up-right`, `external-link`, `chevron-right` |
| 상태 | `check`, `check-circle`, `alert-circle`, `x`, `x-circle`, `info` |
| 로딩 | `loader-2` (animate-spin과 함께) |
| 메뉴 | `menu`, `x` (햄버거 ↔ 닫기 토글) |
| 검색 | `search`, `command` (⌘K UI) |
| 사용자 | `user`, `user-circle`, `users`, `log-in`, `log-out` |
| 데이터 | `bar-chart-3`, `line-chart`, `pie-chart`, `trending-up`, `database` |
| 파일 | `file`, `file-text`, `folder`, `download`, `upload` |
| 미디어 | `image`, `play`, `pause`, `volume-2`, `mic` |
| 통신 | `mail`, `phone`, `message-circle`, `bell` |
| 전자상거래 | `shopping-cart`, `credit-card`, `tag`, `package` |

전체 1500+ 아이콘은 https://lucide.dev 검색.

## 7. 검증 (Pre-Flight 통합)

```
[검사 항목]
✅ 아이콘 세트가 lucide 1개로 통일 (shadcn 자동 포함)
✅ Emoji가 UI 라벨/버튼/네비게이션에 미사용
✅ stroke 두께 일관 (한 페이지 안)
✅ 아이콘 사이즈 표준 (w-4/5/6/8 중 하나, 임의 사이즈 X)

[자동 매칭]
- "@heroicons/" 또는 "@fontawesome/" 또는 "react-icons/" import → ❌
- 텍스트에 emoji 정규식 (`\p{Emoji}`) → ❌ (단, 본문 콘텐츠 emoji는 허용)
- `<i data-lucide="...">` 또는 `<X />` (lucide-react 컴포넌트) 검출 → ✅
```

## 8. 출처·참조

- 공식 사이트: https://lucide.dev
- GitHub: https://github.com/lucide-icons/lucide
- React 패키지: https://www.npmjs.com/package/lucide-react
- 라이선스: ISC

shadcn/ui 공식 채택 아이콘으로, 가장 널리 쓰이는 React 아이콘 라이브러리 중 하나.
