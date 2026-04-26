# Mode E: Design Interview — 컨텍스트 수집 후 생성

calm-design의 5가지 모드 중 가장 높은 우선순위. 생성 전 구조화된 질문으로 컨텍스트를 수집해 "깔끔하지만 평범한" 결과 대신 "기억에 남는" 디자인을 만든다.

## 트리거 키워드

다음 키워드 중 하나라도 등장하면 Mode E로 진입:
- "인터뷰 먼저", "컨텍스트부터", "제대로 만들어줘"
- "질문부터", "물어봐줘", "뭘 만들지 같이 정하자"
- "브리핑 받아줘", "요구사항 정리", "디자인 브리프"
- "deep design", "thorough design", "properly"

> Mode E는 **최고 우선순위**. 다른 모드 키워드("토스 스타일", "3가지 안" 등)와 동시 등장해도 Mode E 먼저 실행 → CONTEXT.md 생성 후 해당 모드로 전환.

## Mode E의 가치

| 기존 방식 (Mode A 직행) | Mode E 방식 |
|---|---|
| 컨텍스트 없이 즉시 생성 | 5개 질문으로 핵심 정보 수집 |
| 범용적 "깔끔한" 디자인 | 타겟·감정·차별점 반영된 맞춤 디자인 |
| 체크리스트 기반 검증만 | "기억에 남는가?" 평가 추가 |

## 5개 인터뷰 질문 (필수 순서)

### Q1. 타겟 사용자 (Who)

**질문**: "이 디자인을 사용할 주요 사용자는 누구인가요? (나이대, 직업/역할, 기술 수준)"

**목적**: Persona 추출 → 카피 톤, 정보 밀도, UI 복잡도 결정

**매핑 예시**:
```yaml
# 사용자 응답: "30-40대 스타트업 대표, 바쁜 사람들"
target_persona:
  age_range: "30-40"
  role: "startup_founder"
  tech_level: "intermediate"
  
design_implications:
  copy_tone: "concise"           # 짧고 핵심만
  info_density: "high"           # 한 화면에 많이
  ui_complexity: "medium"        # 너무 단순하지도, 복잡하지도 않게
  number_emphasis: true          # 숫자·데이터 강조
```

### Q2. 원하는 감정 (Feel)

**질문**: "사용자가 이 디자인을 봤을 때 어떤 감정을 느꼈으면 하나요? (예: 신뢰, 설렘, 차분함, 전문성)"

**목적**: 감정 → 색상 심리, 모션 강도, 타이포 무게 매핑

**매핑** (`references/emotion-color-mapping.md` 참조):
```yaml
# 사용자 응답: "신뢰감, 안정감"
desired_emotion: "trust"

design_implications:
  primary_color_family: "blue"      # 신뢰 = 블루 계열
  color_saturation: "<60%"          # 차분한 채도
  motion_intensity: 4               # 절제된 모션
  typography_weight: "medium"       # 안정감 있는 중간 무게
  whitespace: "generous"            # 여유로운 여백
```

### Q3. 기억할 한 가지 (Remember)

**질문**: "사용자가 이 페이지를 보고 1주일 후에도 기억했으면 하는 한 가지는 무엇인가요?"

**목적**: Hero 카피/시각적 시그니처 결정 → 차별화 핵심

**매핑 예시**:
```yaml
# 사용자 응답: "3분 만에 영상 완성"
memorable_point: "3분 만에 영상 완성"

design_implications:
  hero_headline: "숫자 강조형"       # "3분" 크게
  signature_element: "timer_visual" # 시간 관련 시각 요소
  cta_alignment: "speed_focused"    # "지금 바로 시작" 류 CTA
```

### Q4. 경쟁사 차별점 (Differ)

**질문**: "경쟁 서비스와 비교했을 때, 절대 따라하고 싶지 않은 것은 무엇인가요?"

**목적**: 프로젝트 고유 Anti-Patterns 추가 → Section 9 반영

**매핑 예시**:
```yaml
# 사용자 응답: "경쟁사들 다 복잡하고 전문가용처럼 생김"
competitor_avoidance:
  - "complex_ui"
  - "expert_only_vibe"
  - "dark_theme_default"

design_implications:
  anti_patterns:
    - "❌ 다단계 메뉴/네비게이션"
    - "❌ 전문 용어 우선 카피"
    - "❌ 다크 모드 기본값"
  positive_direction:
    - "✅ 단순한 1-depth 네비게이션"
    - "✅ 일상 언어 카피"
    - "✅ 밝고 친근한 톤"
```

### Q5. 비즈니스 목표 (Goal)

**질문**: "이 페이지에서 사용자가 가장 많이 했으면 하는 행동은 무엇인가요? (예: 회원가입, 데모 신청, 결제)"

**목적**: CTA 강조도, 정보 계층 결정

**매핑 예시**:
```yaml
# 사용자 응답: "무료 체험 시작"
primary_goal: "free_trial_signup"

design_implications:
  cta_prominence: "high"           # CTA 크고 눈에 띄게
  cta_repetition: 3                # 페이지 내 3회 노출
  info_hierarchy: "benefit_first"  # 기능보다 혜택 먼저
  friction_reduction: true         # 가입 장벽 최소화 UI
```

## 인터뷰 진행 워크플로우

### Step 1. 인터뷰 시작 안내

```markdown
## 🎨 calm-design 디자인 인터뷰

더 나은 디자인을 위해 5가지 질문을 드릴게요.
각 질문에 간단히 답해주세요. (한 문장이면 충분합니다)

---

**Q1/5. 타겟 사용자**
이 디자인을 사용할 주요 사용자는 누구인가요?
(나이대, 직업/역할, 기술 수준)
```

### Step 2. 질문별 응답 수집

사용자가 답변할 때마다:
1. 응답을 YAML 구조로 파싱
2. Design Implications 자동 추론
3. 다음 질문 제시

**응답 부족 시**: "조금 더 구체적으로 알려주시면 더 좋은 디자인이 나와요. 예를 들어..." + 예시 제공

**스킵 요청 시**: 기본값 적용 후 다음 질문으로 ("기본값으로 진행할게요")

### Step 3. CONTEXT.md 생성

5개 질문 완료 후 `.calm-design/CONTEXT.md` 생성 (`references/context-schema.md` 스키마 준수).

```markdown
## ✅ 인터뷰 완료!

컨텍스트를 정리했어요:

| 항목 | 내용 |
|---|---|
| 타겟 | 30-40대 스타트업 대표 |
| 감정 | 신뢰감, 안정감 |
| 기억점 | "3분 만에 영상 완성" |
| 차별점 | 복잡함 X, 전문가용 X |
| 목표 | 무료 체험 시작 |

`.calm-design/CONTEXT.md`에 저장했습니다.

---

이제 디자인을 시작할까요?
- "진행해줘" → Mode A (Generate)
- "토스 스타일로" → Mode C (Match-Reference)
- "3가지 옵션으로" → Mode D (Multi-Variant)
```

### Step 4. 모드 전환

CONTEXT.md 생성 후 사용자의 다음 지시에 따라 모드 전환:
- 별도 지시 없이 "진행" → Mode A
- "토스 스타일" 등 브랜드 언급 → Mode C
- "여러 옵션" 등 → Mode D

전환된 모드는 **Step 0에서 CONTEXT.md를 자동 로드**해 디자인 결정에 반영.

## 빠른 인터뷰 모드 (선택)

사용자가 "빨리", "간단히" 등을 언급하면 5개 → 3개 핵심 질문만:
- Q2. 원하는 감정 (Feel)
- Q3. 기억할 한 가지 (Remember)
- Q5. 비즈니스 목표 (Goal)

나머지는 기본값 적용.

## 기존 CONTEXT.md 감지

프로젝트에 `.calm-design/CONTEXT.md`가 이미 있으면:

```markdown
기존 컨텍스트가 있네요:
- 타겟: 30-40대 스타트업 대표
- 감정: 신뢰감
- ...

이 컨텍스트를 사용할까요, 아니면 새로 인터뷰할까요?
- "이거 써줘" → 기존 컨텍스트로 진행
- "새로 하자" → 인터뷰 재시작
```

## 실패 처리

| 상황 | 처리 |
|---|---|
| 5개 질문 중 3개 이상 스킵 | 경고 후 기본값 진행 ("컨텍스트가 부족해 기본 스타일로 진행할게요") |
| 응답이 모호함 | 추가 질문 ("혹시 ~라는 뜻인가요?") |
| 사용자가 인터뷰 중단 요청 | 현재까지 수집된 내용으로 CONTEXT.md 생성 후 저장 |

## Mode E 사용 예시

### 예시: AI 영상 편집 SaaS

```
사용자: "랜딩페이지 제대로 만들어줘"

→ Mode E 진입 (트리거: "제대로")

Claude: "Q1. 타겟 사용자는 누구인가요?"
사용자: "유튜버, 인스타 릴스 하는 20-30대"

Claude: "Q2. 어떤 감정을 느꼈으면 하나요?"
사용자: "쉽고 빠르다는 느낌"

Claude: "Q3. 1주일 후에도 기억했으면 하는 한 가지는?"
사용자: "AI가 알아서 편집해준다"

Claude: "Q4. 경쟁사에서 피하고 싶은 것은?"
사용자: "프리미어처럼 복잡한 UI"

Claude: "Q5. 가장 원하는 사용자 행동은?"
사용자: "무료 체험"

→ CONTEXT.md 생성:
  target: 20-30대 콘텐츠 크리에이터
  emotion: ease, speed
  memorable: "AI 자동 편집"
  avoid: complex_pro_ui
  goal: free_trial

→ Design Implications 자동 추론:
  copy_tone: casual, emoji_ok
  color: energetic (coral/yellow)
  motion: 7 (dynamic)
  cta_prominence: high
  anti_patterns: [timeline_ui, layer_panel, pro_terminology]

사용자: "토스 스타일로 진행해줘"

→ Mode C로 전환 (CONTEXT.md 로드됨)
→ 토스 레퍼런스 + CONTEXT.md 결합
→ "쉽고 빠른" 느낌의 토스 스타일 랜딩 생성
```
