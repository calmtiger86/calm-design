# 타겟 → 카피 톤 매핑 (Target-Copy Mapping)

Mode E 인터뷰의 Q1 (타겟 사용자) 응답을 카피 톤, 정보 밀도, UI 복잡도로 변환하는 매핑 테이블.

## 타겟 축 3가지

### 축 1: 연령대 (Age Range)

| 연령대 | 카피 톤 | 정보 밀도 | 특수 고려 |
|---|---|---|---|
| 10-20대 (Z세대) | casual, meme_ok | low-medium | 짧은 문장, 이모지 OK, 트렌드 용어 |
| 20-30대 (밀레니얼) | friendly, trendy | medium | 밸런스, 적절한 전문 용어 |
| 30-40대 (의사결정자) | concise, professional | high | 숫자 강조, 핵심만, 시간 절약 |
| 40-50대 (시니어 리더) | formal, respectful | medium | 명확한 가치 제안, 신뢰 강조 |
| 50대+ | clear, large | low | 큰 글씨, 단순한 구조, 명시적 안내 |

### 축 2: 역할/직업 (Role)

| 역할 | 카피 톤 | UI 복잡도 | 특수 고려 |
|---|---|---|---|
| 개발자/엔지니어 | technical, direct | high | 코드 예시 OK, API 언급, 기술 스펙 |
| 디자이너/크리에이터 | aesthetic, inspiring | medium | 비주얼 중심, 영감 제공 |
| 마케터/PM | benefit_focused | medium | ROI, 지표, 성과 강조 |
| 경영진/대표 | executive, roi_focused | low | 핵심 가치만, 숫자로 증명 |
| 스타트업 창업자 | direct, growth_focused | medium-high | 성장 지표, 확장성, 빠른 실행 |
| 일반 소비자 | simple, friendly | low | 쉬운 말, 혜택 중심, 신뢰 요소 |
| 학생/취준생 | encouraging, accessible | low | 비용 강조, 쉬운 시작, 성장 스토리 |

### 축 3: 기술 수준 (Tech Level)

| 기술 수준 | 용어 수준 | UI 힌트 | 온보딩 |
|---|---|---|---|
| beginner | 일상 언어만 | 툴팁 많이, 단계별 가이드 | 필수, 상세 |
| intermediate | 기본 용어 OK | 적절한 힌트 | 선택적 |
| advanced | 전문 용어 OK | 최소 힌트, 단축키 강조 | 스킵 가능 |
| expert | 업계 용어, 약어 OK | 힌트 없음, 커스텀 강조 | 불필요 |

## 복합 타겟 매핑 예시

### 예시 1: "30-40대 스타트업 대표"

```yaml
target_input: "30-40대 스타트업 대표"

parsed:
  age_range: "30-40"
  role: "startup_founder"
  tech_level: "intermediate"  # 스타트업 대표 → 어느 정도 알음

copy_mapping:
  tone: "concise"                    # 30-40대 → 핵심만
  style: "direct"                    # 스타트업 → 직접적
  formality: "professional_friendly" # 바쁘지만 차갑진 않게
  
  rules:
    - "한 문장 15자 이내 권장"
    - "숫자로 시작하는 헤드라인 우선"
    - "ROI, 시간 절약 강조"
    - "전문 용어 최소화 but 비즈니스 용어 OK"
    
  examples:
    good:
      - "3분 만에 영상 완성"
      - "팀 생산성 40% 향상"
      - "지금 바로 시작하기"
    bad:
      - "혁신적인 AI 기반 차세대 영상 편집 솔루션"
      - "당신의 크리에이티브 여정을 함께합니다"
      
info_density: "high"
ui_complexity: "medium"
number_emphasis: true
```

### 예시 2: "20-30대 콘텐츠 크리에이터"

```yaml
target_input: "20-30대 유튜버, 인스타 릴스 하는 사람들"

parsed:
  age_range: "20-30"
  role: "creator"
  tech_level: "intermediate"
  platform_context: ["youtube", "instagram"]

copy_mapping:
  tone: "casual"
  style: "trendy"
  formality: "friendly"
  emoji_ok: true
  
  rules:
    - "짧고 펀치 있게"
    - "플랫폼 언어 사용 OK (릴스, 쇼츠, 알고리즘)"
    - "이모지 헤드라인 가능"
    - "before/after 강조"
    
  examples:
    good:
      - "편집 노가다, 이제 끝 ✨"
      - "AI가 알아서 컷 편집"
      - "릴스 30초면 완성"
    bad:
      - "전문 영상 편집 도구"
      - "엔터프라이즈급 워크플로우"
      
info_density: "medium"
ui_complexity: "low"
visual_emphasis: true
```

### 예시 3: "개발자 대상 DevTool"

```yaml
target_input: "개발자, 시니어 엔지니어"

parsed:
  age_range: null  # 개발자는 나이보다 역할이 중요
  role: "developer"
  tech_level: "advanced"

copy_mapping:
  tone: "technical"
  style: "direct"
  formality: "peer_to_peer"  # 동료처럼
  code_snippets: true
  
  rules:
    - "기술 용어 그대로 사용"
    - "코드 예시 최상단 배치"
    - "설치 명령어 바로 보이게"
    - "마케팅 수식어 금지"
    
  examples:
    good:
      - "npm install calm-cli"
      - "타입 안전한 API 클라이언트"
      - "빌드 시간 50% 단축"
    bad:
      - "혁신적인 개발자 경험"
      - "차세대 개발 도구"
      
info_density: "high"
ui_complexity: "high"
terminal_style_ok: true
```

### 예시 4: "50대 이상 시니어"

```yaml
target_input: "50-60대, 컴퓨터 잘 못하는"

parsed:
  age_range: "50-60"
  role: "general_consumer"
  tech_level: "beginner"

copy_mapping:
  tone: "clear"
  style: "respectful"
  formality: "polite"
  
  rules:
    - "큰 글씨 (text-lg 이상)"
    - "한 화면에 하나의 행동만"
    - "버튼 텍스트 명시적으로 (예: '다음으로 넘어가기')"
    - "영어/전문 용어 금지"
    - "단계별 진행 표시"
    
  examples:
    good:
      - "여기를 누르면 시작됩니다"
      - "1단계: 이름을 입력하세요"
      - "완료되었습니다. 수고하셨습니다."
    bad:
      - "Get Started"
      - "로그인"만 덩그러니
      
info_density: "low"
ui_complexity: "minimal"
step_indicator: true
large_touch_targets: true
```

## DESIGN.md 섹션 매핑

| 타겟 속성 | DESIGN.md 영향 |
|---|---|
| `copy_mapping.tone` | Section 1. Visual Theme 톤 설명 |
| `copy_mapping.examples` | Hero 카피, CTA 텍스트 |
| `info_density` | Section 5. Layout (VISUAL_DENSITY 다이얼) |
| `ui_complexity` | Section 4. Component 복잡도 |
| `number_emphasis` | Hero 헤드라인 스타일 |
| `emoji_ok` | 전체 카피에 이모지 허용 여부 |

## 특수 조합 규칙

### 바쁜 의사결정자 패턴

```yaml
trigger: 
  - role in ["executive", "startup_founder", "manager"]
  - OR "바쁜", "시간 없는" 언급

apply:
  - 첫 화면에 핵심 가치 + CTA
  - 스크롤 없이 이해 가능하게
  - "30초 데모" 같은 시간 약속
  - 상세 설명은 접기/펼치기
```

### 감성 구매자 패턴

```yaml
trigger:
  - role in ["creator", "designer"]
  - OR "예쁜", "감성적인" 언급

apply:
  - 비주얼 우선 (텍스트 최소화)
  - 갤러리/포트폴리오 형태
  - 인스타그램 같은 그리드
  - 무드보드 스타일 히어로
```

### 분석적 구매자 패턴

```yaml
trigger:
  - role in ["developer", "engineer", "analyst"]
  - tech_level in ["advanced", "expert"]

apply:
  - 스펙/기능 표 제공
  - 비교 차트
  - 문서 링크 눈에 띄게
  - "어떻게 작동하는가" 섹션
```

## 다이얼 자동 제안

타겟 분석 결과 → CONTEXT.md의 `suggested_dials` 자동 설정:

| 타겟 패턴 | VARIANCE | MOTION | DENSITY |
|---|---|---|---|
| Z세대 소비자 | 7 | 7 | 4 |
| 밀레니얼 전문직 | 5 | 5 | 6 |
| 시니어 의사결정자 | 4 | 3 | 5 |
| 개발자 | 3 | 3 | 8 |
| 크리에이터 | 7 | 7 | 4 |
| 시니어 (50+) | 3 | 2 | 3 |
