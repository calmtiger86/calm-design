# 예시 05: Figma Export

calm-design의 **figma-export 출력 엔진** 데모.

DESIGN.md를 입력으로 받아 Figma Variables JSON (W3C Design Tokens 표준)을 자동 생성합니다.

## 파일 구조

```
05-figma-export/
├── DESIGN.md           # 입력: calm-design 기본 톤 (9섹션 표준)
├── figma-tokens.json   # 출력: W3C Design Tokens (DTCG) 포맷
└── README.md           # 이 문서
```

## 사용법

### 자동 생성

```bash
cd ~/.claude/skills/calm-design

python scripts/design-md-to-figma.py \
  --design examples/05-figma-export/DESIGN.md \
  --output examples/05-figma-export/figma-tokens.json
```

### 옵션

| 옵션 | 설명 |
|------|------|
| `--design` | 입력 DESIGN.md 경로 (필수) |
| `--output` | 출력 JSON 경로 (필수) |
| `--format dtcg\|tokens-studio` | 포맷 (기본: dtcg) |
| `--include-descriptions` | $description 필드 포함 |

## Figma 임포트 방법

### 방법 1: Tokens Studio 플러그인 (권장)

1. Figma에서 [Tokens Studio](https://tokens.studio/) 플러그인 설치
2. 플러그인 열기 → Import → JSON 파일 선택
3. `figma-tokens.json` 업로드
4. 토큰이 자동으로 Figma Variables로 변환됨

### 방법 2: Figma Variables 직접 임포트

1. Figma에서 Variables 패널 열기
2. 우측 상단 메뉴 → Import variables from JSON
3. `figma-tokens.json` 선택

## 생성되는 토큰

| 카테고리 | 토큰 예시 |
|----------|----------|
| `color` | canvas, surface, ink, mute, border, accent, success, danger |
| `typography` | fontFamily.sans, fontSize.*, lineHeight.* |
| `spacing` | 1 (4px), 2 (8px), 4 (16px), 8 (32px), ... |
| `borderRadius` | sm, md, lg, xl, 2xl, full |
| `shadow` | sm, md, lg |

## 자신의 DESIGN.md로 생성

```bash
python scripts/design-md-to-figma.py \
  --design .calm-design/DESIGN.md \
  --output figma-tokens.json \
  --include-descriptions
```
