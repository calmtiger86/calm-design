# Self-Critique Loop — 시각적 셀프-크리틱 5단계 알고리즘

calm-design의 핵심 차별점. 4개 분석 OSS(awesome-design-md, stitch-skills, taste-skill, supanova) 어디에도 없는 메커니즘. **만든 디자인을 자기가 다시 보고 고친다.**

> 트리거: 모든 출력 생성 직후 자동. 사용자 `--no-critique` 또는 "검증 건너뛰어" 명시 시만 비활성.

## 🚨 단계별 실제 동작 수준 (Phase 0 → Phase 1+ 진화)

| 능력 | Phase 0 | **Phase 1 (현재 진행 중)** | Phase 2+ |
|---|:-:|:-:|:-:|
| **정적 분석** (21항목 중 17개) | ✅ 풀 동작 | ✅ 30+ 항목으로 확장 | ✅ |
| **코드 텍스트 기반 Vision** (의미 추론) | ✅ 동작 | ✅ | ✅ |
| **시각 캡처** (`scripts/render-preview.js`) | ❌ | ✅ **활성화** (Playwright + 데스크톱·모바일 듀얼) | ✅ |
| **픽셀 단위 Vision** (`scripts/self-critique.py`) | ❌ | ✅ **활성화** (Anthropic Vision API + 5질문) | ✅ |
| **데스크톱+모바일 듀얼 캡처** | ❌ | ✅ **활성화** (1440x900 + 390x844) | ✅ |
| **인터랙션 상태 캡처** (hover, focus) | ❌ | ⚠️ 부분 (Playwright `hover()` 가능, 자동 트리거는 Phase 2+) | ✅ |

**Phase 1 결론**: 시각적 셀프-크리틱이 **풀 동작**. `scripts/render-preview.js`로 캡처 → `scripts/self-critique.py`로 Vision + 정적 분석 결합 → 핀포인트 재생성 프롬프트 자동 생성. 21→30+ 항목 확장은 묶음 F에서.

**4개 OSS 어디에도 없는 차별점이 Phase 1에서 100% 가동.**

## 0. 5단계 한 눈에

```
[1] Generate    →  코드/HTML 출력 생성 완료
   ↓
[2] Render+Capture  →  실제 렌더링하여 스크린샷 PNG 캡처
   ↓
[3] Vision Self-Analysis  →  Claude Vision으로 자기 결과 평가
   ↓
[4] Pre-Flight Scoring   →  21항목 채점 (정규식 + AST + Vision 결합)
   ↓
[5] Pinpoint Regenerate  →  실패 항목만 표적 재생성 (최대 3회)
   ↓
[Final]  →  통과 결과 + Pre-Flight Report 사용자에게 전달
```

---

## [1] Generate — 코드 생성

이 단계는 SKILL.md의 진입 4단계(다이얼 추론 → 모드 결정 → 출력 엔진 결정 → 9-섹션 DESIGN.md → 코드 변환)에서 이미 끝남. self-critique은 그 직후 자동 시작.

**출력 종류**:
- HTML 모드: 단일 `.html` 파일
- React 모드: 다수 `.tsx` 파일 + `tailwind.config.ts` + `app/layout.tsx`
- DESIGN.md만: 텍스트 (이 경우 [2] 단계 스킵)

---

## [2] Render + Capture — 렌더링 후 스크린샷

생성한 코드를 실제로 화면에 띄우고 PNG로 캡처. 환경별 분기:

### 2.0 환경 자동 감지

스킬은 진입 시 다음 시그널로 환경 자동 분류:

| 시그널 | 분류 | 기본 캡처 경로 |
|---|---|---|
| `mcp__visualize__*` 도구 사용 가능 | **Cowork** | 2.1 인-스킬 경로 (외부 API 키·스크립트 불필요) |
| `mcp__workspace__bash` + `Read/Write` 가능 + visualize 부재 | **Claude Code** | 2.2 외부 스크립트 경로 (Playwright) |
| 둘 다 불가 (다른 SKILL 호환 에이전트 — Cursor·Codex 등) | **Fallback** | 2.3 정적 분석만 |

→ 사용자는 명시 없이 자동 동작. 강제 경로는 `--capture-mode=cowork|playwright|none` 플래그.

### 2.1 Cowork 경로 — 인-스킬 Vision (외부 API 키 불필요)

핵심 통찰: **Cowork에서 calm-design 스킬을 호출하는 Claude 모델 자체가 Vision 가능 모델이다.** 따라서 외부 API 키 없이 Claude 자체가 캡처 + 코드를 함께 보고 5질문 답한다.

```
[1] mcp__visualize__show_widget으로 HTML 인라인 렌더 → 사용자에게 즉시 표시
[2] 스킬은 코드 텍스트 + 시각 결과를 동시에 인지 (사용자 디바이스에서 렌더된 모습은 사용자 눈에)
[3] Claude 자체가 SCRIPT 호출 없이 5질문 자기 답변 (인-스킬 Vision)
[4] 정적 분석 결과와 결합 → Pre-Flight 채점
```

**왜 외부 API 키가 필요 없는가**: 스킬 호출자(Claude)가 이미 Vision 가능. 자기가 만든 코드를 자기가 다시 읽고 평가하는 것이라 제3자 API 호출이 불필요.

**한계**: Cowork visualize MCP는 사용자에게 인라인 렌더하지만, 자동 PNG 캡처를 Claude에게 되돌리는 직접 경로는 현재 제한적. 따라서 Cowork 경로는 **"코드 텍스트 + 사용자 화면 인상 + 정적 분석"** 결합으로 동작 (시각 픽셀 분석은 부분적). 이 한계는 Phase 2+ visualize MCP 캡처 API 추가 시 해소.

### 2.2 Claude Code 경로 — Playwright 외부 스크립트 (Phase 1 — 활성화됨)

`scripts/render-preview.js` 사용 (Playwright 기반, 풀 구현 완료):

```bash
# 사전 설치
npm install playwright
npx playwright install chromium

# 실행
node scripts/render-preview.js \
  examples/01-saas-dashboard-ko/index.html \
  .calm-design/critique-shots
```

산출물 (`.calm-design/critique-shots/`):
- `desktop.png` — 1440×900 viewport, 풀 페이지 캡처
- `desktop-fold.png` — 1440×900 first-fold만 (히어로·첫인상 검증용)
- `mobile.png` — 390×844 (iPhone 14), 풀 페이지 캡처
- `meta.json` — 페이지 제목·언어·viewport 메타

→ 이 4개 파일이 [3] Vision 호출 입력.

### 2.3 Fallback (환경 미지원)

[2]단계 캡처 불가 시: **정적 분석만으로 [4] Pre-Flight 채점**. Vision 검증은 스킵하되, 정규식·AST·DOM 추론으로 90% 항목 검증 가능.

---

## [3] Vision Self-Analysis — 자기 결과 평가

### 3.0 환경별 Vision 호출 경로

| 환경 | 호출 방식 | API 키 필요? |
|---|---|:-:|
| **Cowork (인-스킬)** | Claude 자체가 직접 5질문 자기 답변 (스킬 호출자 = Vision 가능 모델) | ❌ 불필요 |
| **Claude Code (인-스킬)** | 동일 — Claude 자체가 직접 답변 | ❌ 불필요 |
| **Claude Code (외부 자동화·CI)** | `scripts/self-critique.py` + `ANTHROPIC_API_KEY` 환경변수 | ✅ 필요 |
| **다른 SKILL 호환 에이전트** | 호스팅 모델이 Vision 가능하면 인-스킬, 아니면 정적 분석만 | 모델별 |

**일반 사용자는 외부 스크립트나 API 키 없이도 인-스킬 경로로 풀 동작.** scripts/self-critique.py는 CI·자동 검증·배치 처리 등 사용자 개입 없이 돌아가야 하는 시나리오 전용.

### 3.1 5가지 시각적 자기 점검 질문 (모든 경로 공통)

캡처한 PNG(또는 코드 텍스트)를 입력으로 5가지 자기 점검 질문 답변:

```
Q1. 이 화면은 "AI가 만든 티"가 나는가?
    구체 시그널: 보라/네온 그래디언트, Inter 폰트, 3-column equal cards, centered hero, 
    fabricated 통계, 이모지 UI 라벨

Q2. 한국어 가독성이 적절한가? (LANGUAGE=ko일 때만)
    구체 시그널: 단어 중간 줄바꿈, 줄높이 부족, 본문 너무 김, 얇은 weight

Q3. 시각 위계가 명확한가?
    구체 시그널: 가장 중요한 액션이 즉시 식별되는가? CTA가 1개로 명확한가?

Q4. 화이트스페이스가 충분한가?
    구체 시그널: 섹션 패딩 ≥ py-24, 카드 안 패딩 충분, 텍스트 줄 사이 호흡

Q5. 다이얼 값(VARIANCE/MOTION/DENSITY)이 시각적으로 반영됐는가?
    구체 시그널: VARIANCE=7인데 모두 centered면 실패, DENSITY=4인데 데이터 가득이면 실패
```

### 3.2 Vision 응답 포맷 (JSON 강제)

```json
{
  "ai_tells_detected": ["centered hero", "3-column features"],
  "ko_typography_issues": [],
  "hierarchy_score": 8,
  "whitespace_score": 7,
  "dial_match": {
    "variance_actual": 4,
    "variance_target": 7,
    "delta": -3,
    "needs_correction": true
  },
  "overall_assessment": "VARIANCE 미달, AI tells 2개 검출"
}
```

이 JSON이 [4]단계로 전달.

---

## [4] Pre-Flight Scoring — 21항목 채점

`references/pre-flight-checklist.md`의 21항목을 자동 스캔:

### 4.1 항목별 검증 방법 (정적 분석 vs Vision 분리)

| 항목 | 검증 방법 | Phase 0 동작 |
|---|---|:-:|
| 1 (모바일 붕괴 가드) | 정규식: `md:grid-cols-` + `grid-cols-1` 패턴 | ✅ |
| 2 (`min-h-[100dvh]`) | 정규식: `h-screen` 부재 | ✅ |
| 3 (max-width) | 정규식: `max-w-7xl mx-auto` 또는 `max-w-[65ch]` | ✅ |
| 4 (섹션 다양화) | **Vision 보완** (정적 분석 부분 가능) | ⚠️ 부분 |
| 5 (3-column equal) | 정규식: `grid-cols-3` + 동일 카드 카운트 | ✅ |
| 6 (Pure Black) | 정규식: `#000000`, `#000`, `bg-black` | ✅ |
| 7 (LILA BAN) | 정규식: `from-purple-` `to-blue-`, 자주 글로우 | ✅ |
| 8 (액센트 1개) | hex 색상 빈도 분석 | ✅ |
| 9 (Inter 부재) | 문자열 매칭: `Inter` | ✅ |
| 10 (Pretendard 강제) | 문자열 매칭: `Pretendard` 1순위 | ✅ |
| 11 (`word-break: keep-all`) | 정규식: `word-break: keep-all` 또는 `break-keep` | ✅ |
| 12 (한국어 줄높이) | Tailwind 클래스 매칭: `leading-relaxed`+ | ✅ |
| 13 (한국어 weight) | Tailwind 클래스 매칭: `font-thin/extralight` 부재 | ✅ |
| 14 (한국어 본문 너비) | Tailwind 클래스 매칭: `max-w-[65ch]` | ✅ |
| 15 (GPU 친화) | CSS 속성 검출: `top/left/width/height` 애니메이션 | ✅ |
| 16 (Spring physics) | `cubic-bezier(0.16, 1, 0.3, 1)` 또는 `spring` | ✅ |
| 17 (컴포넌트 6상태) | AST 분석: Button/Input 6 props 검증 | ✅ |
| 18 (AI 카피 클리셰) | 사전 매칭: Elevate/Seamless/Unleash 등 | ✅ |
| 19 (Generic placeholder) | 사전 매칭: John Doe/Acme/Lorem ipsum | ✅ |
| 20 (Filler UI 텍스트) | 사전 매칭: Scroll to explore 등 | ✅ |
| 21 (Empty/Error/Loading) | AST 분석: 컴포넌트별 상태 정의 | ✅ |

**Vision 보완 필요 항목 (Phase 0 부분 동작 → Phase 1+ 풀 동작)**:
- 항목 4 (섹션 다양화의 시각적 균형)
- + 추가로 캐치 (정적 분석 누락): 시각 위계 명확성, 화이트스페이스 충분성, 색온도 충돌, 모바일 시각 깨짐

→ **17/21 항목은 Phase 0에서 즉시 풀 동작**. 4개 항목만 Phase 1+ 캡처 통합 시 풀 검증.

### 4.2 채점 결과 종합

```yaml
total_score:
  passed: 19  # ✅
  warnings: 1  # ⚠️
  failed: 1   # ❌

failed_items:
  - id: 21
    title: "Empty/Error/Loading 상태"
    location: "src/components/KPICard.tsx:24"
    issue: "데이터 0건 시 빈 컨테이너만 출력"
    suggested_fix: "Empty 상태 일러스트 + '아직 데이터가 없어요' 카피 추가"

warnings:
  - id: 17
    title: "Button Loading 상태"
    location: "src/components/Button.tsx"
    issue: "Loading 상태 누락 (Default/Hover/Focus/Active/Disabled만 정의됨)"

vision_findings:
  ai_tells: ["centered hero detected"]
  dial_mismatch: "VARIANCE actual 4 vs target 7"
```

---

## [5] Pinpoint Regenerate — 표적 재생성

실패한 항목만 핀포인트로 수정. 전체 코드를 다시 생성하지 않음 (시간·토큰 낭비).

### 5.1 핀포인트 수정 프롬프트 자동 생성

```
다음 항목만 수정해서 코드를 다시 출력해줘:

❌ 항목 21 (Empty State 누락)
- 위치: src/components/KPICard.tsx
- 문제: 데이터 0건 시 빈 컨테이너만 출력
- 수정 지시: KPI 값이 null 또는 0건일 때 다음 패턴으로 Empty 상태 추가
  - 컴포지션된 SVG 일러스트 (chart-empty.svg)
  - 카피: "아직 측정된 값이 없어요"
  - 보조 카피: "데이터가 누적되면 여기에 표시됩니다"

⚠️ 항목 17 (Button Loading 상태 누락)
- 위치: src/components/Button.tsx
- 수정 지시: Loading 상태 추가
  - prop: `loading?: boolean`
  - UI: spinner inline + 텍스트 유지 + disabled
  - 패턴: <Loader2 className="animate-spin" /> + 기존 children

🔧 Vision 발견: Centered Hero 감지 → VARIANCE=7 달성 위해 Split Screen 60/40으로 재구성
- 위치: app/page.tsx:Hero
- 수정 지시: 텍스트 60% 좌측, 비주얼 40% 우측. text-left 강제. CTA 좌측 정렬.

다른 부분은 절대 수정하지 마. 위 3가지만 핀포인트로 수정해.
```

### 5.2 재생성 후 [4]단계 재실행

수정된 코드에 대해 Pre-Flight 다시 채점. 21개 모두 ✅이거나 3회 시도 도달까지 반복.

### 5.3 3회 시도 후 처리

3회 시도 후에도 ❌ 잔존 시:
- **부분 통과 결과** 그대로 사용자에게 전달
- **미통과 리포트** 동봉 (어떤 항목이 왜 실패했는지, 사용자가 직접 수정해야 할 부분)
- 재생성 무한 루프 방지

---

## 비용·성능 고려

### 토큰 비용
- Vision 호출: 1회당 약 1500-3000 토큰 (이미지 + 응답)
- 3회 재생성 시 최대 ~10K 토큰 추가
- 사용자가 비용 우려 시 `--no-critique` 옵션으로 완전 비활성

### 시간
- Render + Capture: 1-3초 (Playwright)
- Vision 분석: 2-5초
- Pre-Flight 채점: <1초 (정적 분석)
- 총 1회 루프: 약 5-10초
- 3회 재생성 최대: 30초

### 사용자 통제 옵션

| 옵션 | 효과 |
|---|---|
| 기본 (옵션 없음) | 셀프-크리틱 자동 실행 (3회 재생성까지) |
| `--no-critique` | 셀프-크리틱 완전 스킵 (가장 빠름, 위험도 ↑) |
| `--critique-once` | 1회만 검증, 재생성 안 함 (리포트만) |
| `--critique-strict` | 5회까지 재생성 (시간 ↑, 품질 ↑) |
| `--no-vision` | Vision 호출만 스킵, 정적 분석만 |

기본값은 `자동 + 3회 재생성 한도`로 설정.

---

## 환경별 동작 매트릭스

| 환경 | Render | Capture | Vision | Static Analysis |
|---|:-:|:-:|:-:|:-:|
| Cowork (Phase 0) | ✅ visualize MCP | ⚠️ 제한적 (사용자만 보는 것이 1차) | ✅ Vision (코드 직접 읽기 보완) | ✅ |
| Cowork (Phase 1+) | ✅ visualize MCP | ✅ 캡처 기능 추가 | ✅ | ✅ |
| Claude Code (Phase 1+) | ✅ Playwright | ✅ Full screenshot | ✅ | ✅ |
| 환경 미지원 fallback | ❌ | ❌ | ❌ | ✅ (정적 분석만) |

Phase 0에서는 정적 분석 + 코드 텍스트 기반 Vision으로 시작. Phase 1에서 풀 시각 캡처 추가.
