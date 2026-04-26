# CONTEXT.md 스키마 명세

Mode E (Design Interview)에서 생성되는 `.calm-design/CONTEXT.md` 파일의 YAML 스키마.

## 파일 위치

`.calm-design/CONTEXT.md` — 프로젝트 루트의 `.calm-design/` 폴더 내.

## 전체 스키마

```yaml
---
# CONTEXT.md — calm-design Design Interview 결과
# Generated: 2024-01-15T14:30:00+09:00
# Mode E Version: 1.0
---

# ═══════════════════════════════════════════════════════════
# 1. 인터뷰 원본 응답 (Raw Answers)
# ═══════════════════════════════════════════════════════════

interview:
  q1_target:
    question: "이 디자인을 사용할 주요 사용자는 누구인가요?"
    answer: "30-40대 스타트업 대표, 바쁜 사람들"
    confidence: 0.9  # 응답 명확도 (0-1)
    
  q2_emotion:
    question: "사용자가 어떤 감정을 느꼈으면 하나요?"
    answer: "신뢰감, 안정감"
    confidence: 0.85
    
  q3_remember:
    question: "1주일 후에도 기억했으면 하는 한 가지는?"
    answer: "3분 만에 영상 완성"
    confidence: 0.95
    
  q4_differ:
    question: "경쟁사에서 피하고 싶은 것은?"
    answer: "복잡하고 전문가용처럼 생긴 UI"
    confidence: 0.8
    
  q5_goal:
    question: "가장 원하는 사용자 행동은?"
    answer: "무료 체험 시작"
    confidence: 0.9

# ═══════════════════════════════════════════════════════════
# 2. 파싱된 구조화 데이터 (Parsed Structure)
# ═══════════════════════════════════════════════════════════

parsed:
  target_persona:
    age_range: "30-40"
    role: "startup_founder"
    tech_level: "intermediate"
    time_availability: "limited"      # busy → limited
    decision_style: "data_driven"     # 스타트업 대표 → 데이터 중시
    
  desired_emotion:
    primary: "trust"                  # 신뢰감
    secondary: "stability"            # 안정감
    avoid: ["excitement", "urgency"]  # 피해야 할 감정
    
  memorable_point:
    type: "number_claim"              # 숫자 기반 주장
    value: "3분 만에 영상 완성"
    emphasis: "time_saving"           # 시간 절약 강조
    
  competitor_avoidance:
    patterns:
      - "complex_ui"
      - "expert_only_vibe"
      - "overwhelming_features"
    specific_elements:
      - "multi-level_menus"
      - "technical_jargon"
      - "dense_toolbars"
      
  business_goal:
    primary_action: "free_trial_signup"
    secondary_actions:
      - "demo_video_watch"
      - "pricing_check"
    conversion_priority: "high"

# ═══════════════════════════════════════════════════════════
# 3. 디자인 매핑 (Design Implications)
# ═══════════════════════════════════════════════════════════

design_mappings:
  # Q1 → 카피 톤, UI 복잡도
  copy:
    tone: "concise"                   # 짧고 핵심만
    style: "professional_friendly"    # 전문적이지만 친근
    number_emphasis: true             # 숫자 강조
    jargon_level: "minimal"           # 전문 용어 최소화
    
  # Q2 → 색상, 모션, 타이포
  color:
    primary_family: "blue"            # 신뢰 → 블루
    saturation: "<60%"                # 차분한 채도
    accent_mood: "calm"               # 차분한 액센트
    
  motion:
    intensity: 4                      # 1-10, 절제된 모션
    style: "subtle"                   # 은은한
    spring_config:
      stiffness: 120
      damping: 25
      
  typography:
    weight: "medium"                  # 안정감
    headline_style: "confident"       # 자신감 있는
    
  # Q3 → Hero 섹션
  hero:
    headline_type: "number_focused"   # "3분" 크게
    visual_signature: "timer_element" # 시간 관련 시각 요소
    proof_type: "speed_demo"          # 속도 증명
    
  # Q4 → Anti-Patterns
  anti_patterns:
    project_specific:
      - "❌ 다단계 메뉴/드롭다운 네비게이션"
      - "❌ 전문가용 툴바/패널 레이아웃"
      - "❌ 기술 용어 우선 카피"
      - "❌ 기능 나열식 히어로"
    positive_direction:
      - "✅ 단순 1-depth 네비게이션"
      - "✅ 일상 언어 카피"
      - "✅ 혜택 중심 히어로"
      - "✅ 미니멀 UI"
      
  # Q5 → CTA 설계
  cta:
    prominence: "high"                # 눈에 띄게
    repetition: 3                     # 페이지 내 3회
    style: "friendly"                 # 친근한 톤
    primary_text: "무료로 시작하기"
    friction_reduction:
      - "no_credit_card"
      - "instant_access"
      - "social_login"
      
  # 종합 → 다이얼 값 제안
  suggested_dials:
    variance: 5                       # 중간 (너무 실험적 X)
    motion: 4                         # 절제된
    density: 5                        # 중간 (바쁜 사람 → 밀도 낮게)
    language: "ko"

# ═══════════════════════════════════════════════════════════
# 4. 메타데이터
# ═══════════════════════════════════════════════════════════

metadata:
  created_at: "2024-01-15T14:30:00+09:00"
  interview_duration_seconds: 180
  questions_answered: 5
  questions_skipped: 0
  mode_transition_to: null            # 아직 모드 전환 안 함
  
# ═══════════════════════════════════════════════════════════
# 5. 다음 단계 가이드 (Next Steps)
# ═══════════════════════════════════════════════════════════

next_steps:
  recommended_mode: "A"               # Generate
  alternative_modes:
    - mode: "C"
      trigger: "브랜드 레퍼런스 언급 시"
      example: "토스 스타일로"
    - mode: "D"
      trigger: "복수 옵션 요청 시"
      example: "3가지 안으로"
  ready_for_generation: true
```

## 섹션별 설명

### 1. interview (인터뷰 원본 응답)

사용자의 원본 답변을 그대로 저장. `confidence`는 응답의 명확도(0-1):
- 0.9+ : 명확한 답변
- 0.7-0.9 : 해석 필요
- 0.7 미만 : 추가 질문 권장

### 2. parsed (파싱된 구조화 데이터)

원본 응답을 구조화된 필드로 파싱:

| 필드 | 타입 | 설명 |
|---|---|---|
| `target_persona` | object | 타겟 사용자 프로필 |
| `desired_emotion` | object | 원하는 감정 (primary/secondary/avoid) |
| `memorable_point` | object | 기억할 핵심 포인트 |
| `competitor_avoidance` | object | 경쟁사 회피 패턴 |
| `business_goal` | object | 비즈니스 목표 + 액션 우선순위 |

### 3. design_mappings (디자인 매핑)

인터뷰 결과 → 구체적 디자인 결정으로 변환:

| 매핑 | 소스 질문 | 영향 범위 |
|---|---|---|
| `copy` | Q1 (타겟) | 카피 톤, 전문 용어 수준 |
| `color` | Q2 (감정) | 색상 계열, 채도 |
| `motion` | Q2 (감정) | 모션 강도, 스프링 설정 |
| `typography` | Q2 (감정) | 폰트 무게, 헤드라인 스타일 |
| `hero` | Q3 (기억점) | 히어로 헤드라인, 시각 요소 |
| `anti_patterns` | Q4 (차별점) | Section 9에 추가될 금지 항목 |
| `cta` | Q5 (목표) | CTA 강조도, 반복 횟수, 마찰 감소 |
| `suggested_dials` | 종합 | VARIANCE/MOTION/DENSITY 제안값 |

### 4. metadata (메타데이터)

파일 생성 정보, 인터뷰 통계.

### 5. next_steps (다음 단계)

인터뷰 후 어떤 모드로 진행할지 가이드.

## 감정 → 색상 매핑 (Quick Reference)

| 감정 | Primary Color | Saturation | Motion |
|---|---|---|---|
| 신뢰 (trust) | Blue | <60% | 4 |
| 안정 (stability) | Blue/Green | <50% | 3 |
| 설렘 (excitement) | Coral/Orange | 70-80% | 7 |
| 전문성 (expertise) | Navy/Charcoal | <40% | 4 |
| 친근함 (friendly) | Yellow/Green | 60-70% | 6 |
| 고급감 (premium) | Gold/Black | <30% | 5 |
| 혁신 (innovation) | Purple/Cyan | 70-80% | 7 |
| 편안함 (comfort) | Green/Beige | <50% | 3 |

상세 매핑은 `references/emotion-color-mapping.md` 참조.

## 타겟 → 카피 톤 매핑 (Quick Reference)

| 타겟 특성 | 카피 톤 | 정보 밀도 |
|---|---|---|
| 바쁜 의사결정자 | concise | high |
| 테크 얼리어답터 | trendy, emoji_ok | medium |
| 보수적 B2B | formal | medium |
| Z세대 소비자 | casual, meme_ok | low |
| 전문가/개발자 | technical | high |
| 시니어 | clear, large | low |

상세 매핑은 `references/target-copy-mapping.md` 참조.

## 다른 모드에서 CONTEXT.md 활용

Mode A/B/C/D는 진입 시 Step 0에서 CONTEXT.md 존재 여부를 확인:

```
Step 0. CONTEXT.md 로드 (선택)
  - `.calm-design/CONTEXT.md` 존재하면 로드
  - design_mappings 섹션을 다이얼 초기값으로 사용
  - anti_patterns.project_specific을 Section 9에 추가
  - CONTEXT.md 없으면 기존 흐름대로 진행
```

## 검증 규칙

CONTEXT.md 생성 시 자동 검증:

- [ ] 5개 질문 섹션 모두 존재 (스킵된 것도 `answer: null`로 명시)
- [ ] `confidence` 값이 0-1 범위
- [ ] `design_mappings` 섹션 비어있지 않음
- [ ] `suggested_dials` 값이 1-10 범위
- [ ] `metadata.created_at` ISO 8601 형식
