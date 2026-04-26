# 한국어 타이포그래피 표준 (Typography KO)

> **Inspired by**: [uxjoseph/supanova-design-skill](https://github.com/uxjoseph/supanova-design-skill) — 한국어 정책(Pretendard 강제, `word-break: keep-all`) 원조
>
> **calm-design 확장**: 9개 항목 깊이 — 폰트, 줄바꿈, 줄높이, 자간, 너비, weight, 숫자, 검증 체크리스트, 자주 등장하는 실수 Quick Reference. 한국 SaaS 관찰 기반 가이드라인 + Phase 1+ 정밀 측정 약속.

`LANGUAGE=ko`인 모든 출력에 강제 적용한다.

## 0. 핵심 원칙 한 줄

**한국어는 라틴 문자가 아니다.** 자체 자간·줄높이·줄바꿈 규칙이 필요하며, 이걸 지키지 않으면 아무리 디자인이 좋아도 "AI가 만든 한국어 사이트" 티가 난다.

## 1. 폰트 (NON-NEGOTIABLE)

### 1.1 강제 채택: Pretendard

```css
font-family: Pretendard, "Pretendard Variable", system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
```

- **모든 한국어 텍스트**에 Pretendard 강제. 본문·헤드라인·UI 텍스트 차별 없음.
- Variable 폰트(weight 100-900) 우선 사용 — `font-weight` 자유롭게 조정 가능.
- 라이선스: SIL Open Font License (상업·재배포 자유)

### 1.2 절대 금지 폰트 (한국어 환경)

| 금지 폰트 | 이유 |
|---|---|
| **Inter** | 라틴 환경 표준 → 한국어 변별력 없음, AI 슬롭의 대표 지문 |
| **Noto Sans KR** | Google 기본값 → AI 템플릿 99%가 사용, 무성격 |
| **Roboto** | 한국어 글꼴 미포함 또는 시스템 폴백 발생 |
| **Malgun Gothic** | 윈도우 의존, 다른 OS에서 깨짐, 디자인 톤 보수적 |
| **Apple SD Gothic Neo** | macOS/iOS 의존, 다른 환경에서 fallback |
| **Nanum Gothic** | 자간·줄높이 보정 부재, 디자인 톤 학생 보고서 |

### 1.3 영문 혼용 시 폰트 페어링

한국어와 영문이 함께 등장할 때:

```css
/* 옵션 1: Pretendard만 (단일성, 권장 기본) */
font-family: Pretendard, system-ui, sans-serif;

/* 옵션 2: 한·영 분리 (영문에 별도 디자인 의도가 있을 때) */
font-family: "Cabinet Grotesk", Pretendard, system-ui, sans-serif;
/* → 라틴 문자는 Cabinet Grotesk, 한글은 Pretendard로 자동 분기 */
```

영문에 Geist / Cabinet Grotesk / Outfit / Satoshi 중 하나를 페어링하면 프리미엄 톤 ↑.

## 2. 줄바꿈 — `word-break: keep-all` 강제

### 2.1 왜 필수인가

라틴 문자는 단어 사이 공백이 자연 줄바꿈 지점이지만, **한국어는 단어 사이 공백이 없거나 적다.** 기본 `word-break: normal`은 한국어에서 단어 중간을 끊는다:

```
❌ 잘못된 예 (word-break: normal)
   "디자인을 업그레이드하
   는 스킬"

✅ 올바른 예 (word-break: keep-all)
   "디자인을
   업그레이드하는 스킬"
```

### 2.2 적용 범위

**모든 한국어 헤드라인·본문 컨테이너에 적용**:

```css
.korean-text, h1, h2, h3, h4, p {
  word-break: keep-all;
  overflow-wrap: break-word; /* 단일 단어가 컨테이너 초과 시만 끊기 */
}
```

Tailwind 환경:

```html
<h1 class="text-5xl tracking-tight leading-tight" style="word-break: keep-all">
  디자인을 업그레이드하는 차분한 스킬
</h1>
```

또는 `tailwind.config.js`에 커스텀 유틸리티 추가:

```js
theme: { extend: { wordBreak: { keep: 'keep-all' } } }
// → class="break-keep" 사용 가능
```

## 3. 줄높이 (line-height)

한국어는 라틴 문자보다 **글자 높이가 크고**, 자형이 정사각형에 가까워 줄 사이 공기를 더 줘야 한다.

| 용도 | 라틴 환경 | 한국어 환경 (Pretendard) |
|---|---|---|
| 디스플레이/H1 | `leading-none` (1.0) | `leading-tight` (1.25) |
| H2/H3 | `leading-tight` (1.25) | `leading-snug` (1.375) |
| 본문 | `leading-normal` (1.5) | `leading-relaxed` (1.625) |
| 긴 본문 (블로그/아티클) | `leading-relaxed` (1.625) | `leading-loose` (2.0) |

## 4. 자간 (letter-spacing / tracking)

한국어는 자간을 **거의 좁히지 않는다**. 라틴의 `tracking-tighter` (-0.05em)는 한국어에서 글자가 겹쳐 보임.

| 용도 | 라틴 | 한국어 |
|---|---|---|
| 디스플레이 | `tracking-tighter` (-0.05em) | `tracking-tight` (-0.025em) |
| 헤드라인 | `tracking-tight` (-0.025em) | `tracking-normal` (0) |
| 본문 | `tracking-normal` (0) | `tracking-normal` (0) |
| 메타·캡션 | `tracking-wide` (+0.025em) | `tracking-wide` (+0.025em) |

## 5. 본문 너비 (max-width)

영문 가독성 표준은 "한 줄 60–75자" (typography 기본 원칙).

한국어는 한 줄에 **45–65자**가 가독성 최적이라는 것이 한국 디자인 커뮤니티의 경험적 합의다 (정확한 환산 비율은 글꼴·콘텍스트·독자 연령에 따라 달라지므로, 이는 실측값이 아니라 **가이드라인**으로 다룬다).

CSS의 `ch` 단위는 "0(zero) 글자 너비" 기반이라 한국어와 라틴 문자에서 실제 줄 길이가 다르게 측정될 수 있다. 다만 Tailwind `max-w-[65ch]`는 한국어 본문에 충분히 적합한 시작점으로 검증돼 있다.

```html
<p class="max-w-[65ch] mx-auto">한국어 본문...</p>
```

또는 명시적 `rem` 단위 (가이드라인):

```css
.body-text-ko       { max-width: 32rem; } /* 약 한국어 45자 가이드 */
.body-text-ko-wide  { max-width: 38rem; } /* 약 한국어 55자 가이드 */
```

**근거 요약 (실측 데이터 아닌 관찰 기반)**:
- 한국어 한 글자가 차지하는 시각적 공간이 라틴 문자 평균보다 넓음 (정사각형 자형)
- 한 줄에 너무 많은 글자가 있으면 안구 추적 부담 증가, 줄바꿈 후 다음 줄 찾기 곤란
- 토스·당근·라인·노션 한국어 페이지 관찰 시 본문 너비가 대체로 32–38rem 범위
- 정밀 측정 데이터는 Phase 1+에서 보강 예정

## 6. 폰트 굵기 (font-weight)

Pretendard는 100~900 가변. 한국어는 글자 획이 많아 **얇은 weight가 가독성 떨어짐**.

| 용도 | 권장 weight |
|---|---|
| 디스플레이 (큰 글자) | 600~800 |
| 헤드라인 | 600~700 |
| 본문 | 400~500 |
| 메타·라벨 | 500 |
| **금지** | 100~200 (`font-thin`, `font-extralight`) — 한국어에서 눈에 띄지 않음 |

## 7. 숫자 처리

한국어 본문 안의 숫자는 **고정폭 숫자(tabular-nums)** 권장. 표·통계·시간 정렬에 필수.

```css
.numeric { font-variant-numeric: tabular-nums; }
```

또는 본문은 Pretendard로 두고, **숫자만 별도 모노스페이스**로 분기:

```css
.dashboard-metric {
  font-family: "Geist Mono", "JetBrains Mono", Pretendard, monospace;
  font-variant-numeric: tabular-nums;
}
```

## 8. 검증 체크리스트 (스킬이 자동 적용)

출력 직전 자동 검증:

- [ ] 한국어 텍스트 컨테이너에 `word-break: keep-all` 적용됨
- [ ] `font-family`에 Pretendard 명시 (Inter / Noto Sans KR / Roboto 등 미포함)
- [ ] 헤드라인 줄높이 ≥ 1.25 (`leading-tight` 이상)
- [ ] 본문 줄높이 ≥ 1.625 (`leading-relaxed` 이상)
- [ ] 본문 max-width가 65ch 이하
- [ ] `font-thin` (100), `font-extralight` (200) 한국어에 미사용
- [ ] 데이터·숫자에 `tabular-nums` 적용 (있을 경우)

하나라도 실패 시 typography-ko 위반으로 Pre-Flight 차감.

## 9. 자주 등장하는 실수 (Quick Reference)

| 잘못된 코드 | 올바른 코드 |
|---|---|
| `font-family: Inter, sans-serif` | `font-family: Pretendard, system-ui, sans-serif` |
| `<h1 class="text-6xl tracking-tighter">` | `<h1 class="text-6xl tracking-tight" style="word-break: keep-all">` |
| `<p class="leading-normal">한국어 긴 본문...</p>` | `<p class="leading-relaxed break-keep">한국어 긴 본문...</p>` |
| `<p class="max-w-prose">` (~75자) | `<p class="max-w-[65ch]">` (~한국어 65자) |
| `<span class="font-thin">2026</span>` | `<span class="font-medium tabular-nums">2026</span>` |
