# 감정 → 색상 매핑 (Emotion-Color Mapping)

Mode E 인터뷰의 Q2 (원하는 감정) 응답을 색상·모션·타이포그래피로 변환하는 매핑 테이블.

## 핵심 감정 12가지 매핑

### 1. 신뢰 (Trust)

> "믿을 수 있는", "안심되는", "검증된"

```yaml
emotion: trust
color:
  primary: "blue"
  palette:
    - { name: "Trust Blue", hex: "#3182F6", role: "accent" }      # 토스 블루
    - { name: "Deep Navy", hex: "#1E3A5F", role: "headline" }
    - { name: "Soft Sky", hex: "#E8F4FD", role: "surface" }
  saturation: "<60%"
  temperature: "cool"
  
motion:
  intensity: 4
  style: "subtle"
  spring: { stiffness: 120, damping: 25 }
  transitions: "400-600ms"
  
typography:
  weight: "medium"
  headline_style: "confident"
  spacing: "relaxed"
  
whitespace: "generous"
```

### 2. 안정 (Stability)

> "든든한", "변함없는", "꾸준한"

```yaml
emotion: stability
color:
  primary: "blue-green"
  palette:
    - { name: "Stable Teal", hex: "#0D9488", role: "accent" }
    - { name: "Deep Forest", hex: "#134E4A", role: "headline" }
    - { name: "Calm Mint", hex: "#F0FDFA", role: "surface" }
  saturation: "<50%"
  temperature: "neutral-cool"
  
motion:
  intensity: 3
  style: "minimal"
  spring: { stiffness: 100, damping: 30 }
  transitions: "500-700ms"
  
typography:
  weight: "medium-bold"
  headline_style: "grounded"
  spacing: "comfortable"
  
whitespace: "generous"
```

### 3. 설렘 (Excitement)

> "기대되는", "흥분되는", "두근두근"

```yaml
emotion: excitement
color:
  primary: "coral-orange"
  palette:
    - { name: "Energetic Coral", hex: "#FF6B6B", role: "accent" }
    - { name: "Warm Orange", hex: "#FF8C42", role: "secondary" }
    - { name: "Soft Peach", hex: "#FFF5F0", role: "surface" }
  saturation: "70-80%"
  temperature: "warm"
  
motion:
  intensity: 7
  style: "dynamic"
  spring: { stiffness: 200, damping: 15 }
  transitions: "200-400ms"
  perpetual: ["pulse", "bounce"]
  
typography:
  weight: "bold"
  headline_style: "playful"
  spacing: "tight"
  
whitespace: "moderate"
```

### 4. 전문성 (Expertise)

> "프로페셔널한", "전문가다운", "깊이 있는"

```yaml
emotion: expertise
color:
  primary: "navy-charcoal"
  palette:
    - { name: "Expert Navy", hex: "#1E293B", role: "primary" }
    - { name: "Muted Gold", hex: "#B8860B", role: "accent" }
    - { name: "Warm Gray", hex: "#F8FAFC", role: "surface" }
  saturation: "<40%"
  temperature: "neutral"
  
motion:
  intensity: 4
  style: "precise"
  spring: { stiffness: 150, damping: 20 }
  transitions: "300-500ms"
  
typography:
  weight: "medium"
  headline_style: "authoritative"
  spacing: "structured"
  
whitespace: "moderate"
```

### 5. 친근함 (Friendly)

> "편안한", "가까운", "부담 없는"

```yaml
emotion: friendly
color:
  primary: "yellow-green"
  palette:
    - { name: "Friendly Green", hex: "#22C55E", role: "accent" }    # 당근 그린 계열
    - { name: "Warm Yellow", hex: "#FBBF24", role: "secondary" }
    - { name: "Soft Cream", hex: "#FEFCE8", role: "surface" }
  saturation: "60-70%"
  temperature: "warm"
  
motion:
  intensity: 6
  style: "bouncy"
  spring: { stiffness: 180, damping: 18 }
  transitions: "250-400ms"
  
typography:
  weight: "regular-medium"
  headline_style: "warm"
  spacing: "relaxed"
  emoji_ok: true
  
whitespace: "generous"
```

### 6. 고급감 (Premium)

> "럭셔리한", "프리미엄", "특별한"

```yaml
emotion: premium
color:
  primary: "gold-black"
  palette:
    - { name: "Luxury Gold", hex: "#D4AF37", role: "accent" }
    - { name: "Rich Black", hex: "#0A0A0A", role: "primary" }
    - { name: "Champagne", hex: "#F7F3E9", role: "surface" }
  saturation: "<30%"
  temperature: "warm-neutral"
  
motion:
  intensity: 5
  style: "elegant"
  spring: { stiffness: 80, damping: 25 }
  transitions: "500-800ms"
  
typography:
  weight: "light-medium"
  headline_style: "refined"
  spacing: "generous"
  
whitespace: "very_generous"
```

### 7. 혁신 (Innovation)

> "새로운", "앞서가는", "미래지향적"

```yaml
emotion: innovation
color:
  primary: "purple-cyan"
  palette:
    - { name: "Innovation Purple", hex: "#8B5CF6", role: "accent" }  # 주의: 채도 제한
    - { name: "Tech Cyan", hex: "#06B6D4", role: "secondary" }
    - { name: "Future Gray", hex: "#F1F5F9", role: "surface" }
  saturation: "60-75%"   # LILA BAN 회피를 위해 80% 미만 유지
  temperature: "cool"
  
motion:
  intensity: 7
  style: "futuristic"
  spring: { stiffness: 200, damping: 12 }
  transitions: "200-350ms"
  perpetual: ["shimmer", "glow"]
  
typography:
  weight: "medium-bold"
  headline_style: "forward"
  spacing: "tight"
  
whitespace: "moderate"
```

### 8. 편안함 (Comfort)

> "쉬는 느낌", "힐링", "부드러운"

```yaml
emotion: comfort
color:
  primary: "green-beige"
  palette:
    - { name: "Comfort Sage", hex: "#84CC16", role: "accent" }
    - { name: "Warm Beige", hex: "#D4C4B0", role: "secondary" }
    - { name: "Soft Linen", hex: "#FAF9F6", role: "surface" }
  saturation: "<50%"
  temperature: "warm"
  
motion:
  intensity: 3
  style: "gentle"
  spring: { stiffness: 60, damping: 30 }
  transitions: "600-900ms"
  
typography:
  weight: "regular"
  headline_style: "soft"
  spacing: "generous"
  
whitespace: "very_generous"
```

### 9. 활력 (Energetic)

> "에너지 넘치는", "활동적인", "생기 있는"

```yaml
emotion: energetic
color:
  primary: "orange-yellow"
  palette:
    - { name: "Energy Orange", hex: "#F97316", role: "accent" }
    - { name: "Bright Yellow", hex: "#EAB308", role: "secondary" }
    - { name: "Light Cream", hex: "#FFFBEB", role: "surface" }
  saturation: "70-85%"
  temperature: "warm"
  
motion:
  intensity: 8
  style: "lively"
  spring: { stiffness: 250, damping: 12 }
  transitions: "150-300ms"
  perpetual: ["bounce", "pulse"]
  
typography:
  weight: "bold"
  headline_style: "impactful"
  spacing: "tight"
  
whitespace: "moderate"
```

### 10. 차분함 (Calm)

> "고요한", "평온한", "조용한"

```yaml
emotion: calm
color:
  primary: "stone-slate"
  palette:
    - { name: "Calm Stone", hex: "#78716C", role: "accent" }
    - { name: "Quiet Slate", hex: "#475569", role: "headline" }
    - { name: "Whisper Gray", hex: "#FAFAF9", role: "surface" }
  saturation: "<40%"
  temperature: "neutral"
  
motion:
  intensity: 2
  style: "serene"
  spring: { stiffness: 50, damping: 35 }
  transitions: "700-1000ms"
  
typography:
  weight: "regular"
  headline_style: "understated"
  spacing: "generous"
  
whitespace: "very_generous"
```

### 11. 재미 (Fun)

> "즐거운", "유쾌한", "놀이 같은"

```yaml
emotion: fun
color:
  primary: "multicolor"
  palette:
    - { name: "Fun Pink", hex: "#EC4899", role: "accent" }
    - { name: "Playful Blue", hex: "#3B82F6", role: "secondary" }
    - { name: "Happy Yellow", hex: "#FEF9C3", role: "surface" }
  saturation: "70-80%"
  temperature: "warm-cool mix"
  
motion:
  intensity: 8
  style: "playful"
  spring: { stiffness: 220, damping: 10 }
  transitions: "150-250ms"
  perpetual: ["wiggle", "bounce", "confetti"]
  
typography:
  weight: "bold"
  headline_style: "quirky"
  spacing: "varied"
  emoji_ok: true
  
whitespace: "moderate"
```

### 12. 신비 (Mystery)

> "궁금한", "호기심 자극", "비밀스러운"

```yaml
emotion: mystery
color:
  primary: "deep-purple-dark"
  palette:
    - { name: "Mystery Purple", hex: "#581C87", role: "accent" }   # 어두운 보라 (LILA BAN 회피)
    - { name: "Deep Indigo", hex: "#312E81", role: "primary" }
    - { name: "Midnight", hex: "#0F0F23", role: "surface" }
  saturation: "40-60%"   # LILA BAN 회피: 밝은 보라 네온 금지
  temperature: "cool"
  
motion:
  intensity: 5
  style: "mysterious"
  spring: { stiffness: 100, damping: 25 }
  transitions: "500-700ms"
  perpetual: ["fade", "reveal"]
  
typography:
  weight: "light-medium"
  headline_style: "intriguing"
  spacing: "generous"
  
whitespace: "generous"
```

## 복합 감정 처리

사용자가 여러 감정을 언급할 때:

### 예시: "신뢰 + 친근"

```yaml
combined_emotions: ["trust", "friendly"]
resolution:
  color:
    primary: "trust.blue"           # 1순위 감정에서
    secondary: "friendly.green"     # 2순위 감정에서
    saturation: "average(60%, 65%)" # 중간값
  motion:
    intensity: 5                    # 평균
  typography:
    weight: "medium"                # 1순위 기준
    emoji_ok: true                  # 2순위에서 허용되면 OK
```

### 예시: "전문성 + 혁신"

```yaml
combined_emotions: ["expertise", "innovation"]
resolution:
  color:
    primary: "expertise.navy"
    secondary: "innovation.cyan"
    saturation: "<55%"              # 전문성 쪽으로 절제
  motion:
    intensity: 5                    # 중간
  typography:
    weight: "medium"
    headline_style: "authoritative" # 전문성 우선
```

## 감정 → DESIGN.md 섹션 매핑

| 감정 속성 | DESIGN.md 영향 섹션 |
|---|---|
| `color.palette` | Section 2. Color Palette |
| `motion.*` | Section 7. Motion & Interaction |
| `typography.*` | Section 3. Typography Rules |
| `whitespace` | Section 5. Layout Principles |

## LILA BAN 회피 규칙

혁신(innovation), 신비(mystery) 등 보라색 계열 감정 매핑 시:

1. **채도 제한**: 절대 80% 이상 금지
2. **네온 금지**: `#7C3AED`, `#A855F7` 같은 밝은 보라 금지
3. **그래디언트 금지**: 보라→파랑 그래디언트 절대 금지
4. **대안**: 어두운 indigo (`#312E81`) 또는 desaturated purple (`#6B21A8`) 사용
