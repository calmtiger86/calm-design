# calm-design — Product Requirements Document (PRD)

> **버전**: v1.0
> **작성일**: 2026-04-26
> **상태**: Phase 0–3.6 완료, Phase 4-5 정의

---

## 1. 제품 비전

> AI가 만든 티 안 나는 차분한 프리미엄 디자인을 한국어 1순위로 출력하고, 자기 결과를 자기가 검증하는 풀스택 디자인 에이전트.

calm-design은 단순한 코드 생성 도구가 아니라 **DESIGN.md(설계 의도)를 1차 산출물로 두는 디자인 에이전트**다. 코드는 DESIGN.md에서 파생되며, 모든 출력은 30 Pre-Flight + 50 Anti-Slop + 시각적 셀프-크리틱으로 검증된다.

---

## 2. 대상 사용자

### 2.1 1차 사용자 (Primary)

- **한국 SaaS·스타트업 개발자·디자이너**
  - 한국어 환경 친화 (Pretendard·word-break 자동)
  - 토스·당근·네이버 등 한국 SaaS 시그니처 패턴 즉시 사용 가능
  - 짧은 시간 안에 프로덕션급 코드 필요

### 2.2 2차 사용자 (Secondary)

- **글로벌 인디 해커·디자이너**
  - 한국어 의존이 아닌 LANGUAGE=en도 정통 지원
  - Linear·Vercel·Stripe 등 글로벌 SaaS 패턴 매칭

### 2.3 환경

- **Claude Cowork**: 데스크톱 앱 (visualize MCP)
- **Claude Code CLI**: 터미널 (Playwright 통합 자동화)
- **Cursor / Codex**: SKILL.md 호환 AI 코딩 에이전트

---

## 3. 핵심 가치 제안 (Value Proposition)

| 사용자 페인 포인트 | calm-design 해결 |
|---|---|
| LLM 디자인은 보라/파란 그래디언트·Inter·3-칸 카드 — "AI 티" | 50개 안티-슬롭 자동 차단 + 출처 기반 영감 |
| 한국어 환경에서 word-break·Pretendard 일일이 처리 | LANGUAGE=ko 자동 감지 + 9 항목 한국어 표준 |
| 디자인 이론 모르는 개발자가 "프리미엄" 표현 어려움 | 4-다이얼 자연어 매핑 ("더 차분하게" → 자동 다이얼 조정) |
| AI가 만든 결과를 사람이 일일이 검증해야 함 | 30 Pre-Flight + 시각적 셀프-크리틱 자동 |
| 토스·Linear 같은 특정 톤 재현 어려움 | 27 풀 큐레이션 + Mode C 자동 매칭 |
| 변형 디자인 비교 어려움 | Mode D 3안 동시 생성 + 비교 리포트 |

---

## 4. 기능 요구사항 (Functional Requirements)

### 4.1 완료 기능 (Phase 0–3.6)

#### F1. 9-섹션 DESIGN.md 표준 [✅ 완료]
- Visual Theme / Color Palette / Typography / Component Stylings / Layout / Depth / Motion / Responsive / Anti-Patterns
- 자동 검증 16항목 (`scripts/validate-design-md.py`)
- 컨텍스트 인식 (Pure Black 정체성·Inter 금지 컨텍스트 OK)

#### F2. 4-다이얼 파라미터 [✅ 완료]
- DESIGN_VARIANCE / MOTION_INTENSITY / VISUAL_DENSITY / **LANGUAGE**
- 자연어 매핑 ("더 미니멀하게" → VARIANCE −2)

#### F3. 5 모드 라우팅 [✅ 완료]
- Mode A: Generate (제로 생성, 9단계)
- Mode B: Upgrade (보존 계약 + 진단 + 자동 수정 4종)
- Mode C: Match-Reference (27 풀 큐레이션 매칭)
- Mode D: Multi-Variant (3안 매트릭스 + Quick 모드)
- (Mode 충돌 우선순위: D > C > B > A)

#### F4. 50 Anti-Slop 자동 차단 [✅ 완료]
- 7 카테고리 (폰트/색상/레이아웃/타이포/모션/카피/이미지)
- 자동 검증 정규식 + 한국어 환경 5 항목

#### F5. 30 Pre-Flight 검증 [✅ 완료]
- 7 카테고리 (레이아웃/색상·타이포/한국어/모션/콘텐츠/상태/접근성)
- WCAG 2.0 luminance 정밀 계산 (`scripts/color-utils.py`)
- ⚠️ 부분 통과 단계

#### F6. 시각적 셀프-크리틱 루프 [✅ 완료]
- 5단계 (생성 → 렌더+캡처 → Vision → Pre-Flight 채점 → 핀포인트 재생성)
- 환경 자동 감지 (Cowork visualize / Claude Code Playwright / Fallback 정적)

#### F7. 출력 엔진 3종 [✅ 완료]
- HTML + Tailwind CDN (5 페이지 타입)
- React + shadcn (4 환경 — Next App/Pages/Vite/Remix)
- JSON Spec (json-render 호환, 멀티플랫폼)

#### F8. 한국어 1순위 [✅ 완료]
- LANGUAGE=ko 기본값
- Pretendard 강제 + 9 항목 타이포 표준
- 15 한국 SaaS 풀 작성 (100% 커버리지)

#### F9. Reference Library [✅ 완료]
- _index.json: 10 카테고리, 59 글로벌 + 15 한국 메타, 매칭 알고리즘
- 27 풀 큐레이션 (글로벌 12 + 한국 15)
- "Inspired by" 정책 (라이선스 안전)

#### F10. 보존 계약 시스템 [✅ 완료] (Mode B 고유)
- 자연어 시그널 자동 추출 ("로고는 그대로", "Toss Blue 유지")
- 위반 시 자동 롤백
- 4 OSS 어디에도 없는 차별점

### 4.2 미완성 기능 (Phase 4-5)

#### F11. preview-catalog 출력 엔진 [❌ Phase 4]
- DESIGN.md → 디자인 시스템 시각 카탈로그 HTML 자동 생성
- 색상 견본 / 타입 스케일 / 컴포넌트 모든 상태 / 스페이싱·섀도우 시스템
- awesome-design-md의 preview.html 패턴 활용

#### F12. figma-export 출력 엔진 [❌ Phase 4]
- DESIGN.md → Figma 임포트용 명세 (JSON 또는 Figma plugin spec)
- 디자이너가 Figma에서 calm-design 출력을 즉시 편집

#### F13. 글로벌 풀 큐레이션 확장 [❌ Phase 4+]
- 현재 12/59 → 30/59 목표
- Cal.com / Mintlify / Raycast / Superhuman / Replicate / Runwayml 등

#### F14. Public Launch [❌ Phase 5]
- GitHub 공개 (`min86k/calm-design`)
- 공식 사이트 (calm-design.dev 또는 유사)
- 영상 데모 (사용 시나리오 3-5개)
- 마케팅 (Threads, Twitter, Hacker News 등)

---

## 5. 비기능 요구사항 (Non-Functional Requirements)

### 5.1 성능

- SKILL.md 진입 시 자동 로드: **6KB 미만** 강제 (현재 5,870 bytes)
- 각 references/는 의도별 sparse load (Mode A 5개, Mode B/C/D는 +1-3개)
- 셀프-크리틱 루프 1회 ≤ 10초 (Playwright 캡처 + Vision)
- 정적 분석만 ≤ 1초

### 5.2 호환성

- Anthropic Skills 표준 (Claude Cowork·Claude Code 모두)
- Cursor / Codex / Gemini CLI 호환 (SKILL.md 표준)
- Python 3.10+ (스크립트), Node 18+ (Playwright)

### 5.3 라이선스 안전

- MIT (calm-design 자체)
- 영감원 4 OSS 출처 NOTICE 명시 (awesome-design-md / taste-skill / stitch-skills / supanova)
- 5 라이브러리 출처 NOTICE 명시 (Pretendard / shadcn / Lucide / Framer Motion / Tailwind)
- json-render Apache 2.0 호환 (NOTICE 추가)
- 브랜드 디자인 직접 복제 X — "Inspired by" 정책

### 5.4 graceful degradation

- Playwright 미설치 → 정적 분석만으로 80% 동작
- anthropic 미설치 → 인-스킬 Vision (Claude 자체) 또는 코드 텍스트 추론
- ANTHROPIC_API_KEY 미설정 → 자동 스킵 + 정적 분석

---

## 6. 사용 시나리오 (User Stories)

### 시나리오 1: 한국 SaaS 대시보드 (Mode A)
> "한국 B2B SaaS 대시보드 디자인 만들어줘. 차분하고 데이터 많은 톤으로."

→ 다이얼: VARIANCE=4, MOTION=4, DENSITY=7, LANGUAGE=ko
→ 페이지 타입: dashboard
→ DESIGN.md 9섹션 + HTML/React 출력 + Pre-Flight 30/30 ✅
→ 산출물 4가지 전달 (DESIGN.md / 코드 / 리포트 / 다이얼 요약)

### 시나리오 2: 토스 스타일 인증 폼 (Mode C)
> "토스처럼 인증 폼 만들어줘. 로고는 우리 거 그대로 둬."

→ Mode C 자동 감지 + 매칭 점수: toss=110
→ 보존 계약: 로고 유지
→ korean/toss/DESIGN.md 로드 + auth 페이지 구조 합성
→ TossInput·TossPrimaryButton 시그니처 컴포넌트 사용
→ 출력 + 보존 계약 자동 검증 통과

### 시나리오 3: 기존 코드 업그레이드 (Mode B)
> "이 코드 calm-design 스타일로 업그레이드해줘. Hero 카피랑 로고는 그대로."

→ Mode B 자동 감지 + 진단: 35/100 (P0 7개·P1 7개·P2 8개)
→ 사용자 선택: P0 Critical만 수정
→ 자동 수정 4종 (Inter→Pretendard / Pure Black→Off-Black / h-screen→100dvh / 한국어 thin weight)
→ 보존 계약 통과 + 재진단: 92/100
→ Diff 리포트 + 새 DESIGN.md

### 시나리오 4: 3안 비교 (Mode D)
> "한국 SaaS 랜딩페이지 3가지 안 보여줘. Toss Blue는 유지."

→ Mode D + 보존 조건: accent=Toss Blue
→ V1 (미니멀 Stone) / V2 (트렌디 Zinc + Inline Image Typography) / V3 (도메인 매칭)
→ 모든 베리언트 Toss Blue 강제 (Warm Amber → Toss Blue 자동 교체)
→ 3 DESIGN.md + 3 HTML + comparison.md

### 시나리오 5: 멀티플랫폼 (json-render)
> "JSON Spec으로 만들어줘. 웹 + React Native + PDF 동시 렌더링."

→ json-render-spec 출력 엔진 활성화
→ DESIGN.md → JSON Spec 자동 변환 (`design-md-to-spec.py`)
→ Web (React) + React Native + PDF + Email registry 가이드
→ Zod 카탈로그로 LLM hallucination 차단

---

## 7. 성공 지표 (KPI)

### 7.1 품질 KPI (정량)

| 지표 | 목표 | 현재 |
|---|---|---|
| SKILL.md 한도 준수 | < 6,144 bytes | ✅ 5,870 bytes |
| 27 풀 큐레이션 검증 통과율 | 100% | ✅ 100% (15-16/15-16) |
| 자동 회귀 검증 통과 | 100% | ✅ 100% |
| Anti-Slop 자동 차단 항목 | 50+ | ✅ 50 |
| Pre-Flight 항목 | 30+ | ✅ 30 |
| 한국 SaaS 풀 커버리지 | 100% (15/15) | ✅ 100% |

### 7.2 사용자 KPI (Phase 5 후 측정)

- GitHub Stars / Forks / Issues
- 사용자 시나리오 1-5 성공률 (수동 테스트)
- 한국어 환경에서 자동 적용 정확도 (Pretendard 강제 등)
- 외부 사용자 피드백 (Threads / Twitter)

---

## 8. 제약사항

### 8.1 기술적 제약

- SKILL.md 6KB 한도 (Anthropic Skills 표준)
- Playwright는 데스크톱 환경만 (CI/CD 가능)
- Cowork visualize MCP의 PNG 회수 제한 (Phase 1+ API 추가 시 해소)

### 8.2 라이선스 제약

- 브랜드 로고·정확한 폰트(Sodo Sans, Circular 등) 직접 사용 X
- 풀 본문은 awesome-design-md에서 자동 fetch 불가능 (사용자 직접 fetch)

### 8.3 정민님 의도 (절대 변경 금지)

- 한국어 1순위
- "calm" 정체성 (절제·차분·신뢰)
- 4 OSS 출처 명시 의무
- 풀 모듈화 (메인 SKILL.md 6KB 한도)

---

## 9. 출시 마일스톤

| 단계 | 시점 | 산출물 |
|---|---|---|
| **Phase 3.6 — 글로벌 풀 6개 추가** | ✅ 2026-04-26 | 27 풀 큐레이션 |
| Phase 4 — preview-catalog + figma-export | +4주 | 5 출력 엔진 |
| Phase 5 — Public Launch | +2주 | GitHub 공개 + 영상 데모 |
| Phase 6 — 외부 피드백 반영 | +4주 | 사용자 피드백 기반 보강 |

---

## 10. 위험·완화 (Risk & Mitigation)

| 위험 | 영향 | 완화 |
|---|:-:|---|
| Phase 4·5 출시 전 외부 베타 시 사용자 혼란 | 🟠 보통 | 명확한 README + HANDOVER 문서 + 5 모드 동작 검증 |
| 한국어 typo 가이드의 경험치 기반 한계 | 🟢 낮음 | Phase 1+에서 KDS·정부24 정밀 검증 약속 명시 |
| Cowork visualize 캡처 제한 | 🟡 중간 | 정적 분석 80% 동작 + Phase 1+ visualize API 대기 |
| 글로벌 47/59 메타만 — Mode C에서 한 줄 톤만으로 합성 | 🟠 보통 | "Inspired by 메타" 라벨로 한계 명시 + Phase 4+ 보강 |
| Apache 2.0(json-render) NOTICE 의무 | 🟢 낮음 | NOTICE 파일에 명시 완료 |

---

## 11. 비전 — 다음 1년

calm-design이 도달할 수 있는 미래:
- **한국 SaaS 디자인 OSS의 사실상 표준** (toss·당근 같은 한국 SaaS도 calm-design을 사용)
- **Multi-platform 디자인 에이전트** (json-render 풀 통합으로 Web/Native/PDF/Email/Video 동시 출력)
- **2,000+ 풀 큐레이션** (사용자 기여 + Phase 4 자동 import)
- **Anthropic Skills 마켓플레이스 톱 5** (Anthropic 공식 추천)

이 PRD는 **품질에 집중**하며 마케팅·확산은 Phase 5에서 별도 다룬다.
