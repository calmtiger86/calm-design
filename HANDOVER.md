# calm-design — Claude Code CLI 인수인계서

> **작성일**: 2026-04-26
> **From**: Cowork 환경 (Claude Sonnet 4.6)
> **To**: Claude Code CLI 환경 (정민님 + Claude Code의 Claude)
> **목적**: Cowork에서 진행한 calm-design 프로젝트를 Claude Code CLI에서 이어 작업할 수 있도록 전체 컨텍스트 인계

---

## 0. 한 페이지 요약 (TL;DR)

- **무엇을 만들었나**: `calm-design` — AI가 만든 티 안 나는 차분한 프리미엄 디자인을 DESIGN.md(9-섹션 마크다운)로 출력하고, Pre-Flight 30항목 검증 + 시각적 셀프-크리틱 + 50개 안티-슬롭 자동 차단까지 수행하는 Anthropic Skills 표준 호환 풀스택 디자인 에이전트.
- **현 진척도**: Phase 0–3.6 완료. **75+ 파일, ~700KB, 5 모드 동작, 27 브랜드 풀 큐레이션** 보유.
- **남은 작업**: Phase 4 (preview-catalog + figma-export, ~4주) → Phase 5 (Public Launch, ~2주).
- **즉시 사용 가능**: `~/.claude/skills/calm-design/`에 복사 후 Claude Code에서 자연어 요청.
- **외부 의존성**: 모두 graceful degradation (Playwright·anthropic 미설치 시 자동 fallback).

---

## 1. 프로젝트 정체성

### 1.1 비전
> "AI가 만든 티 안 나는 차분한 프리미엄 디자인을, 한국어 1순위로, DESIGN.md로 출력하고, 자기 결과를 자기가 검증하는 풀스택 디자인 에이전트."

### 1.2 4개 OSS 분석 → 우리만의 차별점

| 차원 | 4개 OSS (awesome-design-md / stitch-skills / taste-skill / supanova) | calm-design |
|---|---|---|
| 9-섹션 DESIGN.md | ✅ 표준 (awesome-design-md 원조) | ✅ 한국어 분기 + Section 7 Motion / 9 Anti-Patterns 변형 |
| Anti-Slop 카탈로그 | 40+ (taste-skill) | **50** (한국어 + 접근성 추가) |
| Pre-Flight | 17-21 (taste-skill) | **30** (WCAG luminance 정밀 계산 통합) |
| 다이얼 | 3 (taste-skill) | **4** (LANGUAGE 추가) |
| 한국어 친화 | 일부 (supanova) | **9개 항목 깊이** + 15개 한국 SaaS 풀 작성 |
| **시각적 셀프-크리틱 루프** | ❌ | **✅ (4 OSS 어디에도 없음)** |
| **레퍼런스 자동 매칭** | ❌ (정적 카탈로그만) | **✅ (Mode C, 27 풀 큐레이션)** |
| **Multi-Variant 3안 생성** | ❌ | **✅ (Mode D)** |
| **보존 계약 시스템** | ❌ | **✅ (Mode B Upgrade)** |

### 1.3 핵심 정책

1. **풀 모듈화** — 진입 SKILL.md ≤ 6KB, references/ sparse load (정민님이 우려한 "분산 함정" 회피용으로 메인은 라우팅 표 + 핵심 안티-슬롭 5개를 의무 포함)
2. **한국어 1순위** — LANGUAGE 다이얼 기본값 `ko`, Pretendard 강제, `word-break: keep-all`
3. **Inspired by 정책** — 브랜드 디자인 직접 복제 X, 영감만 차용. 4 OSS 출처는 NOTICE에 명시
4. **Graceful Degradation** — Playwright·anthropic·Vision API 미설치 시 자동 fallback (정적 분석 80%로 동작)

---

## 2. 현재 상태 (2026-04-26 기준)

### 2.1 Phase 진척도

| Phase | 상태 | 산출물 |
|---|:-:|---|
| Phase 0 — MVP | 🟢 완료 | SKILL.md + 핵심 references 7 + 기본 출력 엔진 2 + 예시 2 |
| Phase 1 — 셀프-크리틱 풀 + 30 Pre-Flight + 50 Anti-Slop + Mode B + Phase 2-3 준비 | 🟢 완료 | Playwright/Vision 통합 + 보존 계약 시스템 + creative-arsenal/color-system/motion-system/framer-motion 정책 |
| Phase 1.5 — json-render 점진 채택 | 🟢 완료 | output-engines/json-render-spec + library-policies/json-render + design-md-to-spec.py + examples/03 |
| Phase 2 — Mode D Multi-Variant | 🟢 완료 | modes/multi-variant.md + scripts/multi-variant.py (3안 매트릭스 + 보존 조건) |
| Phase 3 — Reference Library + Mode C | 🟢 완료 | _index.json (10 카테고리·59 글로벌·15 한국) + Mode C 풀 구현 + 한국 시범 3개 |
| Phase 3.5 — 한국 SaaS 12개 추가 | 🟢 완료 | naver/line/musinsa/kurly/baemin/coupang/yanolja/29cm/ohou/zigbang/class101/starbucks_kr |
| **Phase 3.6 — 글로벌 풀 6개** | 🟢 **완료** | cursor/supabase/figma/framer/spotify/airbnb |
| Phase 4 — Output Engine 확장 | 🟡 대기 | preview-catalog.md + figma-export.md (~4주) |
| Phase 5 — Public Launch | 🟡 대기 | 공식 사이트 + 영상 데모 + GitHub 공개 (~2주) |

### 2.2 동작 가능한 5 모드 + 4 출력 엔진

| 모드 | 트리거 | 동작 |
|---|---|:-:|
| **A. Generate** | "디자인 만들어줘" | ✅ 풀 동작 |
| **B. Upgrade** | "다듬어줘" + 코드 첨부 | ✅ 진단 + 자동 수정 4종 + 보존 계약 |
| **C. Match-Reference** | "토스처럼", "Linear 풍" | ✅ 27 풀 큐레이션 매칭 |
| **D. Multi-Variant** | "3가지 안" | ✅ 3안 매트릭스 + 보존 조건 |
| **HTML 출력** | 기본 | ✅ |
| **React+shadcn 출력** | "React로", "Next.js" | ✅ Next.js / Vite / Pages Router / Remix 4 환경 |
| **JSON Spec (json-render)** | "json-render", "멀티플랫폼" | ✅ 6개 플랫폼 동시 출력 가능 |
| **preview-catalog** | "preview" | ❌ Phase 4 미구현 |
| **figma-export** | "Figma 명세" | ❌ Phase 4 미구현 |

### 2.3 Reference Library 풀 커버리지 (27/74)

```
글로벌 풀 작성 (12/59):
  Linear · Vercel · Stripe · Notion · Apple · Tesla
  Cursor · Supabase · Figma · Framer · Spotify · Airbnb (Phase 3.6 추가)
  → 나머지 47개는 메타데이터만, 풀은 사용자가 npx getdesign add 또는 직접 fetch

한국 SaaS 풀 작성 (15/15) — 100% 커버리지:
  Toss · Kakao · Daangn · Naver · LINE · Musinsa · Kurly · Baemin
  Coupang · Yanolja · 29CM · Ohou · Zigbang · Class101 · Starbucks Korea
```

---

## 3. 디렉토리 구조 (75+ 파일)

```
calm-design/
├── SKILL.md                              5.9KB ✅ 6KB 한도 안전 (Anthropic Skills 진입점)
├── README.md / README-EN.md
├── LICENSE (MIT) / NOTICE (4 OSS 영감원 + 6 라이브러리 출처)
├── CONTRIBUTING.md
├── .gitignore                            ⬆️ Phase 6 추가
├── HANDOVER.md                           ⬆️ 이 문서
├── PRD.md                                ⬆️ 제품 요구사항
├── TASK_HANDOFF.md                       ⬆️ 작업지시서
│
├── references/ (10개)
│   ├── design-md-spec.md                 9-섹션 표준 + Inspired by awesome-design-md
│   ├── typography-ko.md                  한국어 9 항목 + Inspired by supanova
│   ├── ai-tells-blocklist.md             50개 + Inspired by taste-skill+supanova
│   ├── prompt-enhancement.md             4기법 + Inspired by stitch-skills
│   ├── pre-flight-checklist.md           30항목 + Inspired by taste-skill
│   ├── self-critique-loop.md             5단계 + 환경 자동 감지
│   ├── creative-arsenal.md               50+ 패턴 + 7 코드 스니펫
│   ├── color-system.md                   4-다이얼 컬러 베리언트
│   ├── motion-system.md                  Spring 표준 5종 + 10 패턴
│   └── korean-saas-patterns.md           7 한국 SaaS 시그니처 컴포넌트 코드
│
├── library-policies/ (5개)
│   ├── pretendard.md / lucide.md / shadcn-ui.md / framer-motion.md
│   └── json-render.md                    Phase 1.5 추가
│
├── modes/ (4개)
│   ├── generate.md (Mode A)              5축 분류기 + 9단계
│   ├── upgrade.md (Mode B)               보존 계약 + 자동 수정 4종
│   ├── multi-variant.md (Mode D)         3-베리언트 매트릭스
│   └── match-reference.md (Mode C)       매칭 알고리즘 + 27 풀 큐레이션
│
├── output-engines/ (3개)
│   ├── html-tailwind.md                  5 페이지 타입 골격 (랜딩/대시보드/인증/모바일/콘텐츠)
│   ├── react-shadcn.md                   4 환경 (Next App/Pages/Vite/Remix)
│   └── json-render-spec.md               멀티플랫폼 (Phase 1.5)
│
├── scripts/ (9개)
│   ├── render-preview.js                 Playwright HTML→PNG 듀얼 캡처
│   ├── self-critique.py                  30항목 정적 + WCAG luminance + 영어 환경 + Vision (graceful)
│   ├── validate-design-md.py             16항목 + 컨텍스트 인식 검증 (Pure Black/Inter 정체성 OK)
│   ├── upgrade-diagnose.py               P0/P1/P2 가중치 점수
│   ├── apply-upgrade.py                  자동 수정 4종 + 보존 계약 검증
│   ├── color-utils.py                    WCAG contrast CLI (contrast/validate-design-md/suggest-accent)
│   ├── design-md-to-spec.py              DESIGN.md → JSON Spec 변환 (페이지 타입 다중 시그널 가중치)
│   ├── multi-variant.py                  3-베리언트 골격 + --quick 모드
│   └── awesome-design-md-import.py       (메타 인덱스 — 풀 본문은 사용자가 fetch)
│
├── examples/ (3개)
│   ├── 01-saas-dashboard-ko/             DESIGN.md + index.html
│   ├── 02-landing-toss-style/            DESIGN.md + index.html
│   └── 03-json-render-multiplatform/     DESIGN.md + spec.json + README
│
├── reference-library/                    Phase 3+ 풀 커버리지
│   ├── _index.json                       10 카테고리 + 59 글로벌 메타 + 15 한국 메타 + 매칭 알고리즘
│   ├── README.md
│   ├── global/ (12 풀 + 5 stub + _import_summary.json)
│   └── korean/ (15 풀)
│
└── research/ (1개)
    └── json-render-evaluation.md         결합 가치 8.5/10 평가
```

---

## 4. Claude Code CLI에서 즉시 시작하는 법

### 4.1 설치

```bash
# 옵션 1: 폴더 복사
cp -r ~/Downloads/Claude\ Cowork/calm-design ~/.claude/skills/calm-design

# 옵션 2: GitHub 공개 후 (Phase 5)
git clone https://github.com/min86k/calm-design ~/.claude/skills/calm-design
# 또는
npx skills add https://github.com/min86k/calm-design
```

### 4.2 (선택) 외부 의존성 — 풀 동작 원할 때만

```bash
# 시각 셀프-크리틱 풀 동작용 (Cowork에선 불필요, Claude Code 자동화 시만)
cd ~/.claude/skills/calm-design
npm install playwright && npx playwright install chromium

# 외부 자동화 Vision API용 (인-스킬 Vision은 불필요)
pip install anthropic
export ANTHROPIC_API_KEY=...
```

### 4.3 사용 — 자연어로 요청

```
> 한국 SaaS 대시보드 디자인 만들어줘. 차분하고 데이터 많은 톤으로.
> 토스처럼 인증 폼 만들어줘. 한국어로.
> 이 코드 calm-design 스타일로 업그레이드해줘. Hero 카피랑 로고는 그대로 둬. [코드 첨부]
> 한국 SaaS 랜딩페이지 3가지 안 보여줘. Toss Blue는 유지.
> JSON Spec으로 만들어줘. 웹+모바일 동시 렌더링.
```

Claude Code의 Claude가 자동으로 SKILL.md를 읽고, 의도 분류 → 모드 라우팅 → references sparse load → 9-섹션 DESIGN.md 생성 → 출력 변환 → Pre-Flight 검증.

---

## 5. 외부 자산 결합

| 자산 | 결합 위치 | 라이선스 |
|---|---|---|
| awesome-design-md (VoltAgent) | reference-library/ 메타 인덱스 + design-md-spec 9섹션 표준 | MIT |
| taste-skill (Leonxlnx) | ai-tells-blocklist + pre-flight-checklist + creative-arsenal + 다이얼 | 공개 사용 |
| stitch-skills (Google Labs) | prompt-enhancement 4기법 + 워크플로우 라우팅 | Apache 2.0 |
| supanova-design-skill (uxjoseph) | typography-ko + Pretendard 정책 + ABSOLUTE ZERO DIRECTIVE | 공개 사용 |
| json-render (Vercel Labs) | output-engines/json-render-spec + library-policies/json-render | Apache 2.0 |

상세 출처는 NOTICE 파일 + 각 references/*.md 헤더의 "Inspired by" 명시.

---

## 6. 미해결 이슈 / 잠재 위험 (정직 명시)

### 6.1 의도된 결손 (Phase 4+ 예정, 차단 사항 아님)

- ❌ `output-engines/preview-catalog.md` (Phase 4)
- ❌ `output-engines/figma-export.md` (Phase 4)
- ❌ `scripts/match-reference.py` (LLM이 _index.json 직접 처리, 의도)
- ❌ 글로벌 47개 메타만 (풀은 사용자가 npx getdesign 또는 직접 fetch)

### 6.2 사용자 환경 정리 권장 (권한 제약으로 미처리)

- 빈 `reference-library/ko/` 디렉토리 (의도와 무관, `rmdir reference-library/ko`)
- `scripts/__pycache__/` (이미 .gitignore에 포함, 다음 git add 시 제외)

### 6.3 알려진 한계

| 한계 | 대응 |
|---|---|
| Cowork visualize MCP의 PNG 캡처 자동 회수가 제한적 | 인-스킬 Vision으로 80% 동작, Phase 1+의 visualize 캡처 API 추가 시 100% |
| LLM이 _index.json 직접 매칭 (스크립트 부재) | 단순한 알고리즘이라 LLM이 충분히 처리. Phase 3.7+에서 match-reference.py 자동화 가능 |
| Phase 4·5 미완성 | 외부 베타 가능 시점이지만 풀 출시는 아님 |

---

## 7. 다음 작업 우선순위 (정민님 + Claude Code의 Claude)

`TASK_HANDOFF.md` 참조 — 구체 액션 항목 + Phase 4 실행 순서 + Phase 5 출시 체크리스트.

---

## 8. Cowork → Claude Code 전환 시 차이점

| 영역 | Cowork (지금까지) | Claude Code (이후) |
|---|---|---|
| 환경 | 데스크톱 앱 (visualize MCP) | 터미널 CLI (파일 시스템 직접 접근) |
| 셀프-크리틱 | visualize MCP로 즉시 렌더 | Playwright 스크립트 권장 |
| Vision API | 인-스킬 (Claude 자체) | 인-스킬 또는 외부 API |
| 파일 작업 | Cowork 마운트 폴더 | 일반 파일 시스템 |
| Git 통합 | 수동 | 자연스러운 git 통합 |

→ Claude Code에서는 **git 통합·Playwright·자동 검증 파이프라인**이 더 자연스럽습니다.

---

## 9. 회귀 검증 명령 (인계 후 첫 실행 권장)

```bash
cd ~/.claude/skills/calm-design

# 1. SKILL.md 6KB 한도 확인
wc -c SKILL.md  # 5870 미만이어야

# 2. 모든 Python 스크립트 syntax
for f in scripts/*.py; do python3 -c "import ast; ast.parse(open('$f').read())"; done

# 3. JSON 검증
python3 -c "import json; json.load(open('reference-library/_index.json'))"

# 4. DESIGN.md 27개 풀 큐레이션 검증
for f in reference-library/global/*/DESIGN.md reference-library/korean/*/DESIGN.md; do
  python3 scripts/validate-design-md.py "$f" 2>&1 | grep "총"
done

# 5. 변환기 동작 — 예시 03
python3 scripts/design-md-to-spec.py \
  --design examples/03-json-render-multiplatform/DESIGN.md \
  --output /tmp/test-spec.json
```

모두 통과해야 인계 완료.

---

## 10. 연락·기여

- 원작자: 정민 ([@calmtiger_](https://threads.net/@calmtiger_))
- 라이선스: MIT
- 영감원 출처: NOTICE 파일

**감사합니다 — 이제 Claude Code에서 좋은 작업 이어가세요!** ☕
