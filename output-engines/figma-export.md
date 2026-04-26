# Output Engine: Figma Export (디자인 토큰 → Figma 임포트)

> Phase 4 산출물. DESIGN.md → Figma Variables JSON 또는 Tokens Studio 호환 포맷으로 변환.

calm-design이 생성한 DESIGN.md의 색상, 타이포그래피, 스페이싱, 그림자 토큰을 **Figma에서 즉시 사용 가능한 JSON**으로 변환. 디자이너가 Figma에서 calm-design 출력을 편집하고 확장할 수 있게 합니다.

## 1. 트리거 시그널

다음 키워드 감지 시 이 출력 엔진 활성화:
- "Figma 명세", "Figma로 보내줘"
- "Figma 토큰", "Figma Variables"
- "Tokens Studio", "디자인 토큰 JSON"
- "Figma에서 쓸 수 있게"

## 2. 입력 / 출력

| 구분 | 명세 |
|------|------|
| **입력** | DESIGN.md (calm-design 9-섹션 표준) |
| **출력** | `figma-tokens.json` (W3C Design Tokens 표준 호환) |
| **자동화** | `python scripts/design-md-to-figma.py --design <path> --output <path>` |

## 3. 출력 포맷: W3C Design Tokens (DTCG)

[W3C Design Tokens Community Group](https://design-tokens.github.io/community-group/format/) 표준을 따릅니다. Figma의 Variables 기능 및 Tokens Studio 플러그인과 호환.

### 3.1 기본 구조

```json
{
  "$schema": "https://design-tokens.github.io/community-group/format/",
  "color": {
    "canvas": { "$value": "#FAFAFA", "$type": "color" },
    "surface": { "$value": "#FFFFFF", "$type": "color" },
    "ink": { "$value": "#0A0A0A", "$type": "color" },
    "mute": { "$value": "#71717A", "$type": "color" },
    "border": { "$value": "#E4E4E7", "$type": "color" },
    "accent": { "$value": "#10B981", "$type": "color" },
    "success": { "$value": "#22C55E", "$type": "color" },
    "danger": { "$value": "#EF4444", "$type": "color" }
  },
  "typography": {
    "fontFamily": {
      "sans": { "$value": "Pretendard Variable, Pretendard, system-ui, sans-serif", "$type": "fontFamily" }
    },
    "fontSize": {
      "xs": { "$value": "12px", "$type": "dimension" },
      "sm": { "$value": "14px", "$type": "dimension" },
      "base": { "$value": "16px", "$type": "dimension" },
      "lg": { "$value": "18px", "$type": "dimension" },
      "xl": { "$value": "20px", "$type": "dimension" },
      "2xl": { "$value": "24px", "$type": "dimension" },
      "3xl": { "$value": "30px", "$type": "dimension" },
      "4xl": { "$value": "36px", "$type": "dimension" },
      "5xl": { "$value": "48px", "$type": "dimension" }
    },
    "lineHeight": {
      "tight": { "$value": "1.1", "$type": "number" },
      "snug": { "$value": "1.25", "$type": "number" },
      "normal": { "$value": "1.5", "$type": "number" },
      "relaxed": { "$value": "1.625", "$type": "number" }
    }
  },
  "spacing": {
    "1": { "$value": "4px", "$type": "dimension" },
    "2": { "$value": "8px", "$type": "dimension" },
    "3": { "$value": "12px", "$type": "dimension" },
    "4": { "$value": "16px", "$type": "dimension" },
    "6": { "$value": "24px", "$type": "dimension" },
    "8": { "$value": "32px", "$type": "dimension" },
    "12": { "$value": "48px", "$type": "dimension" },
    "16": { "$value": "64px", "$type": "dimension" }
  },
  "borderRadius": {
    "sm": { "$value": "4px", "$type": "dimension" },
    "md": { "$value": "8px", "$type": "dimension" },
    "lg": { "$value": "12px", "$type": "dimension" },
    "xl": { "$value": "16px", "$type": "dimension" },
    "2xl": { "$value": "24px", "$type": "dimension" },
    "full": { "$value": "9999px", "$type": "dimension" }
  },
  "shadow": {
    "sm": {
      "$value": { "offsetX": "0", "offsetY": "1px", "blur": "2px", "spread": "0", "color": "rgba(0,0,0,0.05)" },
      "$type": "shadow"
    },
    "md": {
      "$value": { "offsetX": "0", "offsetY": "4px", "blur": "6px", "spread": "-1px", "color": "rgba(0,0,0,0.1)" },
      "$type": "shadow"
    },
    "lg": {
      "$value": { "offsetX": "0", "offsetY": "10px", "blur": "15px", "spread": "-3px", "color": "rgba(0,0,0,0.1)" },
      "$type": "shadow"
    }
  }
}
```

## 4. DESIGN.md → Figma Tokens 변환 매핑

| DESIGN.md 섹션 | Figma Tokens 키 | 변환 규칙 |
|---|---|---|
| 2. Color Palette | `color.*` | 표의 각 행 → `{ "$value": hex, "$type": "color" }` |
| 3. Typography | `typography.*` | fontFamily, fontSize, lineHeight 추출 |
| 5. Layout | `spacing.*` | 패딩/마진 값 → spacing 스케일 |
| 6. Depth | `shadow.*`, `borderRadius.*` | shadow 값 파싱 + radius 추출 |

### 4.1 색상 변환 규칙

```
DESIGN.md:
| Canvas | `#FAFAFA` | 페이지 배경 |

→ Figma Tokens:
"color": {
  "canvas": { "$value": "#FAFAFA", "$type": "color", "$description": "페이지 배경" }
}
```

### 4.2 타이포그래피 변환 규칙

```
DESIGN.md:
- Family: `'Pretendard Variable', Pretendard, system-ui, sans-serif`
- 디스플레이/H1: `text-4xl tracking-tight leading-tight`

→ Figma Tokens:
"typography": {
  "fontFamily": { "sans": { "$value": "Pretendard Variable", "$type": "fontFamily" } },
  "fontSize": { "4xl": { "$value": "36px", "$type": "dimension" } }
}
```

### 4.3 그림자 변환 규칙

```
DESIGN.md:
- 카드 그림자: `shadow-[0_2px_8px_rgba(0,0,0,0.04)]`

→ Figma Tokens:
"shadow": {
  "card": {
    "$value": { "offsetX": "0", "offsetY": "2px", "blur": "8px", "spread": "0", "color": "rgba(0,0,0,0.04)" },
    "$type": "shadow"
  }
}
```

## 5. Figma 임포트 방법

### 5.1 Tokens Studio 플러그인 (권장)

1. Figma에서 [Tokens Studio](https://tokens.studio/) 플러그인 설치
2. 플러그인 열기 → Import → JSON 파일 선택
3. `figma-tokens.json` 업로드
4. 토큰이 자동으로 Figma Variables로 변환됨

### 5.2 Figma Variables 직접 임포트

1. Figma에서 Variables 패널 열기
2. 우측 상단 메뉴 → Import variables from JSON
3. `figma-tokens.json` 선택
4. 매핑 확인 후 Import

### 5.3 CLI 자동화

```bash
# Tokens Studio CLI 사용 (선택)
npx token-transformer figma-tokens.json figma-variables.json

# Figma REST API로 직접 푸시 (고급)
# https://www.figma.com/developers/api#variables
```

## 6. 자동화 스크립트

```bash
# DESIGN.md → figma-tokens.json 변환
python scripts/design-md-to-figma.py \
  --design .calm-design/DESIGN.md \
  --output figma-tokens.json

# 옵션
#   --format dtcg|tokens-studio  포맷 (기본: dtcg)
#   --include-descriptions       $description 필드 포함
```

## 7. 한국어 환경 특수 처리

LANGUAGE=ko 감지 시:
- `typography.fontFamily.sans` → `"Pretendard Variable, Pretendard, system-ui, sans-serif"`
- `typography.fontFamily.mono` → `"JetBrains Mono, Menlo, monospace"`
- 한국어 설명 유지 (`$description` 필드)

## 8. Pre-Flight 연동

변환 전 DESIGN.md가 다음 Pre-Flight 항목을 통과하는지 자동 검증:

- [C1] Pure Black 미사용
- [C2] 단일 액센트
- [T1] Pretendard 명시 (LANGUAGE=ko)
- [A1] 유효한 hex 코드

위반 시 변환 거부 + 위반 항목 리포트.

## 9. 한계 및 Phase 4.1 예정

| 현재 (Phase 4) | Phase 4.1 예정 |
|----------------|----------------|
| DTCG 포맷 | + Tokens Studio 네이티브 포맷 |
| 색상/타이포/스페이싱/그림자 | + 컴포넌트 토큰 (Button, Input 등) |
| JSON 파일 출력 | + Figma REST API 직접 푸시 |
| 단일 테마 | + 라이트/다크 모드 분리 |

## 10. 참고 자료

- [W3C Design Tokens Format](https://design-tokens.github.io/community-group/format/)
- [Tokens Studio Documentation](https://docs.tokens.studio/)
- [Figma Variables API](https://www.figma.com/developers/api#variables)
