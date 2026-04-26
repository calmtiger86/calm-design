# Mode B: Upgrade — 기존 디자인 업그레이드

calm-design의 4가지 모드 중 두 번째. 사용자가 이미 가지고 있는 디자인(코드·스크린샷·DESIGN.md)을 받아서 calm-design 표준으로 업그레이드.

> Mode A(Generate)와의 차이: A는 제로에서 생성, B는 **기존 자산 보존하면서 개선**. 사용자의 브랜드 톤·핵심 카피·구조는 가능한 한 유지하고, 안티-슬롭·접근성·한국어 친화 영역만 표적 수정.

## 트리거 키워드

다음 키워드 + 기존 코드/디자인 첨부 시 Mode B 진입:
- "업그레이드해줘", "다듬어줘", "개선해줘", "고쳐줘"
- "이거 calm-design 스타일로 바꿔줘"
- "기존 코드 리팩토링", "디자인 리뉴얼"
- "안티-슬롭 적용해줘", "AI 티 빼줘"

> 기존 코드 첨부 부재면 Mode A로 자동 폴백 (생성 모드)
>
> "토스 스타일로 바꿔줘" 같이 레퍼런스 키워드 동시 등장 시 → Mode C(Match-Reference) 우선

## 9-단계 워크플로우

### Step 1. 기존 자산 수집

사용자 입력에서 다음 자산 추출:

| 자산 | 처리 |
|---|---|
| HTML/JSX 코드 (전체 또는 일부) | 정적 분석 입력 |
| 스크린샷 PNG/JPG | Vision 분석 입력 |
| 기존 DESIGN.md | 9-섹션 비교 기준 |
| URL (배포된 사이트) | Playwright로 캡처 후 분석 (Phase 1+) |
| Figma 링크 | 참고용 (직접 import는 Phase 4+) |

자산이 부재하면 **AskUserQuestion** 트리거: "기존 코드/스크린샷/DESIGN.md 중 어떤 형식으로 공유하시겠어요?"

### Step 2. 현재 상태 진단 (Pre-Flight 자기 점검)

`scripts/self-critique.py` 또는 인-스킬 정적 분석으로 기존 자산을 **34항목**(Pre-Flight 30 + AI Tells 자동 검증 4)으로 채점:

```yaml
diagnosis:
  total: 34
  passed: 12
  warnings: 15
  failed: 7
  critical_issues:
    - id: 6
      title: "Pure Black 부재"
      detail: "#000000 사용 — Off-Black로 교체"
    - id: 7
      title: "LILA BAN"
      detail: "from-purple-500 to-blue-500 그래디언트 발견"
    - id: 9
      title: "Inter 폰트 부재"
      detail: "font-family: Inter, sans-serif 발견"
    # ... (7개 critical)
```

### Step 3. 진단 리포트 사용자 공유 + 우선순위 결정

사용자에게 진단 결과 공유 후 다음 4단계 우선순위 옵션 제시:

```markdown
## 🩺 진단 리포트

현재 디자인 점수: **35/100** (passed 12, warnings 15, **failed 7**)

### 즉시 수정 권장 (Critical, 7개)
- [P0] Inter 폰트 → Pretendard 교체 (한국어 환경)
- [P0] Pure Black → Off-Black 교체
- [P0] LILA BAN: 보라/파란 그래디언트 → Neutral + 단일 액센트
- [P1] 3-column equal cards → Bento Grid
- [P1] h-screen → min-h-[100dvh]
- [P2] AI 카피 클리셰 ("Elevate", "Seamless")
- [P2] aria-label 누락 (검색 input)

### 어떤 단계로 진행하시겠어요?
1. **모두 자동 수정** (24항목 한 번에 — 가장 빠르지만 변경 폭 큼)
2. **Critical만 (7개)** 수정 → 검토 후 다음 단계 (안전한 점진 개선)
3. **카테고리별** 선택 (폰트만 / 색상만 / 접근성만)
4. **사용자 명시 항목만** (정민님이 직접 항목 골라서)
```

→ AskUserQuestion 트리거. Step 4부터 사용자 선택에 따라 분기.

### Step 4. 보존 계약 (Preservation Contract)

#### 4.0 자연어에서 자동 추출 (LLM 기반 contract extractor)

사용자 입력에서 다음 시그널을 자동 인식하여 보존 계약 초안을 생성. 사용자에게 확인받은 후 확정.

**한국어 보존 시그널 패턴**:

| 사용자 발화 패턴 | 추출되는 보존 항목 |
|---|---|
| "Hero 카피는 그대로", "헤드라인 유지" | `preserve.hero_copy = true` |
| "로고는 건드리지 마", "로고 그대로" | `preserve.logo = true` |
| "토스 블루는 유지해줘", "이 색상은 그대로" | `preserve.accent_hex = "#3182F6"` (특정 hex 추출) |
| "구조는 바꾸지 마", "페이지 그대로" | `preserve.site_structure = true` |
| "zustand 쓰고 있어 빼지 마" | `preserve.libraries = ["zustand"]` |
| "한국어 카피는 손대지 마" | `preserve.korean_copy = true` |
| "핵심 기능 설명만 그대로" | `preserve.core_features_copy = true` |

**영문 보존 시그널 패턴**:

| Pattern | Extracted |
|---|---|
| "keep the hero copy", "don't touch headline" | `preserve.hero_copy = true` |
| "preserve the logo", "keep our logo" | `preserve.logo = true` |
| "keep our brand color", "the accent stays" | `preserve.accent_hex = <auto-detected>` |
| "keep the structure", "don't change pages" | `preserve.site_structure = true` |

**충돌 시 우선순위**: 사용자 명시 보존 > 자동 추출 보존 > calm-design 기본 동작.

**자동 추출 결과 사용자 확인 양식**:

```markdown
## 🤝 보존 계약 초안 (자동 추출)

다음 항목을 절대 변경하지 않겠습니다. 맞나요?

✅ Hero 헤드라인 카피: "영상 편집을 10배 빠르게"
✅ 로고: 좌측 상단 "cutter" 텍스트 마크
✅ 액센트 색상: #3182F6 (Toss Blue) — 채도·명도 보정만 가능, hex 변경 X
✅ 페이지 구조: Nav → Hero → Social Proof → Features → CTA → Footer (6 섹션)
✅ 사용 라이브러리: Tailwind, Pretendard, lucide, Motion One

수정할 항목이 있나요? (없으면 "그대로 진행" 답변)
```

#### 4.1 명시 계약 (사용자가 추가하는 항목)

자연어 추출이 놓친 부분을 사용자가 직접 추가. 카테고리별 명시:

```yaml
preservation_contract:
  - 브랜드 액센트 색상 (사용자가 명시한 #3182F6 토스 블루 → 채도 보정만 가능, 색상 변경 X)
  - Hero 섹션의 핵심 카피 ("영상 편집을 10배 빠르게")
  - Logo 디자인·위치
  - 사이트 정보 구조 (페이지 종류·개수·순서)
  - 사용자 명시 라이브러리 (이미 zustand 쓰고 있으면 유지)

  # 단, 다음은 보정 가능:
  modifiable:
  - 색상 hex 값 (브랜드 색상 유지하되 채도·명도 보정)
  - 폰트 (한국어 환경이면 Pretendard 강제 OK)
  - 레이아웃 패턴 (centered → split, 3-column → Bento)
  - 모션·애니메이션
  - 마이크로카피·placeholder
  - 접근성 속성 (aria-label, htmlFor 추가)
```

이 계약은 **Step 5 핀포인트 수정 시 절대 위반 금지**. 위반 시 Step 7에서 사용자 거부 가능.

### Step 5. 핀포인트 표적 수정

`scripts/self-critique.py`의 `regen_prompt` 자동 생성 활용. 모든 ❌ 항목과 사용자가 선택한 ⚠️ 항목만 수정:

**핀포인트 원칙**:
- 같은 파일 안에서도 **수정 영역 외 코드는 1바이트도 변경 X**
- diff 형식으로 산출 (Before / After 명시)
- 보존 계약 위반 검출 시 자동 롤백

**수정 패턴 표**:

| Critical 항목 | 표적 수정 |
|---|---|
| Inter 폰트 | `font-family: Inter` → `font-family: 'Pretendard Variable', Pretendard, system-ui, sans-serif` + Pretendard CDN/`next/font` 추가 |
| Pure Black | `#000000` `bg-black` `text-black` → `#0A0A0A` `bg-zinc-950` `text-ink` |
| LILA BAN | `from-purple-500 to-blue-500` → 단일 액센트 (`bg-emerald-500` 또는 `bg-[#3182F6]`) |
| 3-column equal | `grid-cols-3` 동일 카드 → Bento `md:col-span-2 md:row-span-2` 큰 카드 + 작은 카드 4 |
| h-screen | `h-screen` → `min-h-[100dvh]` |
| AI 카피 클리셰 | "Elevate" "Seamless" "Unleash" → 구체 동사 ("줄이세요" "연결합니다" "보세요") |
| aria-label 누락 | 아이콘만 있는 버튼·input에 `aria-label="검색"` 또는 `<label htmlFor=...>` 추가 |
| word-break 미적용 | 한국어 헤드라인에 `style="word-break: keep-all"` 또는 `class="break-keep"` |

### Step 6. 새 DESIGN.md 생성 (업그레이드 후 상태 문서화)

기존 DESIGN.md가 있으면 그 위에 diff로, 없으면 새로 생성. 9-섹션 표준(`references/design-md-spec.md`) 준수.

DESIGN.md 헤더에 업그레이드 메타 명시:

```markdown
> Generated by calm-design · LANGUAGE: ko · VARIANCE: 5 · MOTION: 4 · DENSITY: 7 · Mode: B
> Upgraded from: 기존 디자인 (점수 35/100 → 92/100)
> Upgrade date: 2026-04-25
> Critical fixes: 7 (Inter, Pure Black, LILA BAN, 3-col, h-screen, AI 카피, aria)
```

### Step 7. 보존 계약 자동 검증

업그레이드된 코드와 원본을 비교해 보존 계약 위반 자동 검출:

- 사용자 명시 액센트 색상이 변경됐는지 (hex 단위 비교)
- Hero 핵심 카피가 보존됐는지 (문자열 매칭)
- 사이트 구조(페이지 수·순서)가 동일한지
- 사용자 명시 라이브러리가 빠지지 않았는지 (`package.json` diff)

위반 발견 시 **자동 롤백** + 사용자에게 보고: "보존 계약 위반 발견 — 어떻게 처리할까요?"

### Step 8. 셀프-크리틱 루프 자동 트리거

업그레이드 결과에 대해 `references/self-critique-loop.md` 5단계 적용:

- 정적 분석 34항목 → 80%+ 통과 목표
- Vision 분석 (Cowork 인-스킬 또는 Claude Code Playwright)
- 실패 항목만 핀포인트 재생성 (최대 3회)

### Step 9. 산출물 5가지 사용자 전달

```markdown
## ✅ calm-design Mode B 업그레이드 완료

[ Before/After 진단 ]      35/100 → 92/100 (Critical 7개 모두 해결)
[ 업그레이드 코드 ]        기존 파일 핀포인트 수정 또는 새 파일
[ 새 DESIGN.md ]            .calm-design/DESIGN.md (Upgrade 메타 포함)
[ Diff 리포트 ]             변경 위치·전후 비교 + 변경 사유
[ Pre-Flight Report ]      34항목 ✅/⚠️/❌ + 보존 계약 통과 여부
```

## 보존 계약 위반 시 처리 매트릭스

| 위반 유형 | 자동 처리 |
|---|:-:|
| 사용자 명시 색상 hex 변경 | 자동 롤백 → 사용자 확인 |
| Hero 핵심 카피 변경 | 자동 롤백 |
| 페이지 수 변경 | 자동 롤백 |
| 사용자 라이브러리 제거 | 자동 롤백 |
| Logo 위치/디자인 변경 | 사용자 확인 후 진행 |

## Mode B 사용 예시

### 예시 1: 한국 SaaS 랜딩 — 35/100 → 92/100

```
사용자: "이 코드 calm-design 스타일로 업그레이드해줘. Hero 카피랑 로고는 그대로 둬."
[기존 index.html 첨부]

→ Step 1: 코드 추출
→ Step 2: 진단 — 35/100 (failed 7, warnings 15)
→ Step 3: 사용자 선택 → "Critical 7개만 먼저"
→ Step 4: 보존 계약 — Hero 카피·Logo·페이지 구조 보존
→ Step 5: 핀포인트 수정
   - font-family: Inter → Pretendard
   - Pure Black → Off-Black
   - LILA BAN → 토스 블루 단일 액센트 (브랜드 색 유지)
   - 3-column equal → Bento
   - h-screen → min-h-[100dvh]
   - "Elevate" → "줄이세요"
   - 검색 input aria-label 추가
→ Step 6: 새 DESIGN.md (Mode: B 메타 포함)
→ Step 7: 보존 계약 자동 검증 통과
→ Step 8: 셀프-크리틱 → 92/100 통과
→ Step 9: 5가지 산출물 전달
```

### 예시 2: 다른 모드로 자동 전환

```
사용자: "이거 토스 스타일로 업그레이드해줘"
[코드 첨부]

→ Mode B 트리거 감지 + "토스 스타일" 키워드 → Mode C 우선
→ Mode B 진단(Step 2)까지는 진행 후 Mode C로 인계 (보존 계약 + 진단 리포트 그대로 전달)
```

## 다른 모드와의 분기

Mode B 진행 중 다음 시그널 발견 시 자동 전환:
- "여러 가지 안 보여줘" → Mode D (Multi-Variant)
- "토스/Linear/Vercel처럼" → Mode C (Match-Reference) 우선
- 기존 코드 부재 → Mode A 폴백
