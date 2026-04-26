# calm-design

> **AI가 만든 티 안 나는 차분한 프리미엄 디자인.** 한국어 1순위. 풀스택 디자인 에이전트 스킬.

[English README](./README-EN.md)

---

## ☕ calm-design이 뭔가요?

LLM 기반 디자인 도구가 만드는 결과물에는 **AI가 만든 티**가 강하게 납니다 — 보라/파란 그래디언트, Inter 폰트, 3-칸 동일 카드, "Elevate"·"Seamless" 카피, Pure Black, 자주색 글로우 그림자.

`calm-design`은 이 패턴을 **명시적으로 차단**하고, 대신 **차분하고 정제된 디자인**을 출력합니다. 한국어 환경에서는 Pretendard를 강제하고, 만든 결과를 다시 보고 검증까지 합니다.

### 4개 OSS의 강점을 통합 + 3가지 차별점

| 기능 | awesome-design-md | stitch-skills | taste-skill | supanova | **calm-design** |
|---|:-:|:-:|:-:|:-:|:-:|
| 9-섹션 DESIGN.md 표준 | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| 프롬프트 강화 파이프라인 | ❌ | ✅ | ⚠️ | ⚠️ | ✅ |
| AI Tells 금지+대체안 | ❌ | ⚠️ | ✅ | ✅ | ✅ (확장) |
| 다이얼 파라미터 | ❌ | ❌ | 3-다이얼 | 3-다이얼 | **4-다이얼** |
| Pre-Flight Checklist | ❌ | ❌ | ✅ | ⚠️ | ✅ (21항목) |
| 한국어 타이포 표준 | ❌ | ❌ | ❌ | ⚠️ | ✅ (깊이) |
| **시각적 셀프-크리틱 루프** | ❌ | ❌ | ❌ | ❌ | **✅** |
| **레퍼런스 자동 매칭** | ❌ | ❌ | ❌ | ❌ | **✅ (Phase 1+)** |
| **Multi-Variant 3안 생성** | ❌ | ❌ | ❌ | ❌ | **✅ (Phase 2+)** |

---

## 🚀 빠른 시작

### 설치

Anthropic Skills 표준을 따르므로 다음 환경에서 동작합니다:
- Claude Cowork (Claude 데스크톱 앱)
- Claude Code (CLI)
- Cursor, Codex 등 SKILL.md 호환 AI 코딩 에이전트

#### Cowork

플러그인 마켓플레이스에서 `calm-design` 검색 후 설치 (Phase 5 출시 예정).

또는 수동: 이 저장소를 클론해 Cowork의 skills 디렉토리에 복사.

#### Claude Code

```bash
# 프로젝트 루트에서
git clone https://github.com/min86k/calm-design .claude/skills/calm-design
```

또는 Anthropic Skills CLI:

```bash
npx skills add https://github.com/min86k/calm-design
```

### 첫 사용

스킬 설치 후 AI에게 자연어로 요청:

```
"한국 B2B SaaS 대시보드 디자인 만들어줘. 차분하고 데이터 많은 톤으로."
```

스킬은 자동으로:
1. **다이얼 추론**: VARIANCE=4, MOTION=4, DENSITY=7, LANGUAGE=ko
2. **9-섹션 DESIGN.md** 생성 → `.calm-design/DESIGN.md`로 저장
3. **HTML + Tailwind CDN** 코드 출력 (Pretendard·lucide·Motion One 통합)
4. **Pre-Flight 21항목 검증** + 통과까지 자동 재생성 (최대 3회)
5. **결과 4가지 산출물** 전달:
   - DESIGN.md
   - 코드 (HTML 또는 React)
   - Pre-Flight Report (✅/⚠️/❌)
   - 다이얼 한 줄 요약

---

## 📐 4-다이얼 파라미터

| 다이얼 | 범위 | 기본값 | 의미 |
|---|---|---|---|
| `DESIGN_VARIANCE` | 1–10 | 7 | 1=완벽 대칭, 10=비대칭·예술적 혼돈 |
| `MOTION_INTENSITY` | 1–10 | 6 | 1=정적, 10=영화적 스프링 |
| `VISUAL_DENSITY` | 1–10 | 4 | 1=갤러리, 10=조종석 |
| `LANGUAGE` | `ko`/`en`/`auto` | **`ko`** | 한국어 1순위 (Pretendard 강제, word-break: keep-all) |

**자연어로 다이얼 조정**: "더 미니멀하게", "더 차분하게", "데이터 많은", "트렌디하게" 등 자연어가 자동으로 다이얼 값에 매핑됩니다.

---

## 🎯 5가지 모드

| 모드 | 트리거 | 산출물 | 상태 |
|---|---|---|---|
| **A. Generate** | "디자인 만들어줘", "랜딩페이지" | DESIGN.md + 코드 | ✅ |
| **B. Upgrade** | "다듬어줘", "업그레이드" + 기존 코드 첨부 | 개선 diff + 새 DESIGN.md | ✅ |
| **C. Match-Reference** | "토스 스타일", "Linear 처럼" | 레퍼런스 분석 + 적용 코드 | ✅ |
| **D. Multi-Variant** | "3가지 안", "다양하게" | 3개 다른 DESIGN.md + 비교 | ✅ |
| **JSON Spec** | "멀티플랫폼", "웹+모바일" | json-render 포맷 JSON | ✅ |

---

## 🛡️ 50+ 안티-슬롭 자동 차단

calm-design은 다음 패턴을 **출력 직후 자동 검증**해 발견 시 자동 재생성:

| 카테고리 | 차단 항목 (예시) |
|---|---|
| 폰트 | Inter, Noto Sans KR, Roboto, font-thin/extralight (한국어) |
| 색상 | Pure Black `#000000`, 보라/파란 AI 그래디언트, 채도 80%+, 다중 액센트 |
| 레이아웃 | 3-column equal cards, centered hero (VARIANCE≥5), `h-screen`, max-width 부재 |
| 카피 | "Elevate", "Seamless", "Unleash", "John Doe", "Lorem ipsum", fabricated metrics |
| 모션 | linear easing, top/left/width/height 애니메이션, useState 기반 애니메이션 |

전체 50+ 항목은 [`references/ai-tells-blocklist.md`](./references/ai-tells-blocklist.md) 참조.

---

## 🇰🇷 한국어 1순위

`LANGUAGE=ko`(기본값) 환경에서 자동 강제:

- **Pretendard 폰트** 강제 (Inter·Noto Sans KR 차단)
- `word-break: keep-all` 자동 적용 (한국어 단어 중간 줄바꿈 방지)
- 한국어 줄높이 (`leading-relaxed` 1.625 이상)
- 한국어 본문 너비 가이드 (45–65자)
- 한국어 weight 정책 (`font-thin`/`extralight` 금지)
- Generic placeholder 한국화 (김민서·박지호·주식회사 정민)

자세한 내용: [`references/typography-ko.md`](./references/typography-ko.md)

---

## 📦 통합된 8개 라이브러리

| 라이브러리 | 역할 | 출력 엔진 |
|---|---|---|
| [shadcn/ui](https://ui.shadcn.com) | React 기본 컴포넌트 | React 모드 |
| [lucide](https://lucide.dev) | 표준 아이콘 | 모든 모드 |
| [zustand](https://github.com/pmndrs/zustand) | 상태 관리 (조건부) | React 모드 |
| [Framer Motion](https://www.framer.com/motion) | React 애니메이션 | React 모드 |
| [Tailwind CSS](https://tailwindcss.com) | 스타일링 | 모든 모드 |
| [Pretendard](https://pretendard.dev) | 한국어 폰트 | LANGUAGE=ko 강제 |
| [Radix UI](https://www.radix-ui.com) | 헤드리스 (shadcn 자동) | React 모드 |
| [Motion One](https://motion.dev) | HTML 경량 애니메이션 (4KB) | HTML 모드 |

---

## 📂 디렉토리 구조

```
calm-design/
├── SKILL.md                          # 진입점·라우터 (~6KB)
├── README.md                         # 이 파일
├── README-EN.md                      # English
├── LICENSE                           # MIT
├── CONTRIBUTING.md
├── references/                       # 의도별 sparse load
│   ├── design-md-spec.md             # 9-섹션 DESIGN.md 표준
│   ├── prompt-enhancement.md         # 프롬프트 강화 4기법 + 한국어 매핑
│   ├── pre-flight-checklist.md       # 21항목 검증 게이트
│   ├── ai-tells-blocklist.md         # 30+ 글로벌 금지 패턴
│   ├── typography-ko.md              # 한국어 타이포 표준
│   └── self-critique-loop.md         # 시각적 셀프-크리틱 5단계
├── modes/
│   └── generate.md                   # Mode A: 제로 생성 (Phase 0)
├── output-engines/
│   ├── html-tailwind.md              # HTML + Tailwind CDN (5가지 페이지 타입)
│   └── react-shadcn.md               # React + shadcn (Next.js/Vite/Remix)
├── library-policies/
│   ├── pretendard.md                 # 한국어 폰트 강제
│   ├── lucide.md                     # 표준 아이콘
│   └── shadcn-ui.md                  # React 컴포넌트
└── examples/
    ├── 01-saas-dashboard-ko/         # 한국 B2B SaaS 대시보드
    ├── 02-landing-toss-style/        # 토스 스타일 영감 랜딩페이지
    ├── 03-json-render-spec/          # JSON Render Spec 출력
    ├── 04-preview-catalog/           # 디자인 시스템 카탈로그
    └── 05-figma-export/              # Figma 토큰 JSON 출력
```

---

## 🎨 예시 결과물

### [예시 1: 한국 B2B SaaS 대시보드](./examples/01-saas-dashboard-ko/)
- VARIANCE=4 / MOTION=4 / DENSITY=7
- Sidebar + KPI Bento (비대칭 2-1-1) + 차트 + 활동 피드
- 검색 ⌘K, Pretendard, lucide, Motion One

### [예시 2: AI 영상 편집 SaaS 랜딩 (Toss 스타일 영감)](./examples/02-landing-toss-style/)
- VARIANCE=7 / MOTION=6 / DENSITY=4
- Hero Split → Social Proof → Bento Features → CTA → Footer
- Toss Blue 단일 액센트, 충분한 호흡감

### [예시 3: JSON Render Spec (멀티플랫폼)](./examples/03-json-render-spec/)
- json-render 포맷 JSON 출력
- 웹/모바일/PDF 동시 지원 가능한 플랫폼 독립 명세

### [예시 4: Preview Catalog](./examples/04-preview-catalog/)
- 디자인 시스템 시각적 카탈로그 (색상, 타이포, 컴포넌트)
- HTML 독립 실행 가능

### [예시 5: Figma Export](./examples/05-figma-export/)
- W3C Design Tokens (DTCG) 포맷 JSON 출력
- Figma Variables / Tokens Studio 호환

---

## 🛠️ 출시 로드맵

| Phase | 범위 | 상태 |
|---|---|:-:|
| **Phase 0 — MVP** | Mode A + HTML/React 출력 + 30 anti-slop + 셀프-크리틱(정적 분석) | ✅ 완료 |
| **Phase 1 — Self-Critique 풀 시각** | Playwright 통합, Vision 풀 캡처, 30 Pre-Flight 항목 | ✅ 완료 |
| **Phase 2 — Multi-Variant** | Mode D (3안 동시 생성) | ✅ 완료 |
| **Phase 3 — Reference Library** | 한국 15 + 글로벌 18 = 33개 큐레이션 + Mode B/C | ✅ 완료 |
| **Phase 4 — Output Engine 확장** | preview-catalog + figma-export + json-render | ✅ 완료 |
| Phase 5 — Public Launch | GitHub 공개, 공식 사이트, 영상 데모 | 🟡 진행중 |

---

## 📜 라이선스

MIT — 상업적 사용·재배포·수정 모두 자유. [LICENSE](./LICENSE) 참조.

레퍼런스 라이브러리(Phase 3+)의 브랜드 디자인 시스템 분석은 **"Inspired by"** 정책으로 라이선스 안전 — 직접 복제 아닌 영감 표시.

## 🤝 기여

[CONTRIBUTING.md](./CONTRIBUTING.md) 참조. 한국어 매핑 보강·새로운 안티-패턴 제안·레퍼런스 라이브러리 추가 등 환영합니다.

## 🙏 감사

이 스킬은 다음 OSS 프로젝트의 분석·차용 위에 만들어졌습니다:

- [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) — 9-섹션 DESIGN.md 표준의 원조
- [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills) — 프롬프트 강화 + 워크플로우 라우팅
- [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) — Anti-slop 철학 + 다이얼 파라미터
- [uxjoseph/supanova-design-skill](https://github.com/uxjoseph/supanova-design-skill) — 한국어 환경 특화 + Pretendard 통합

그리고 [Pretendard](https://github.com/orioncactus/pretendard)·[shadcn/ui](https://ui.shadcn.com)·[lucide](https://lucide.dev)에 감사를.

---

**Made with ☕ by [@calmtiger_](https://threads.net/@calmtiger_)**
