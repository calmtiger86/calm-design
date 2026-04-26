# 예시 04: Preview Catalog

calm-design의 **preview-catalog 출력 엔진** 데모.

DESIGN.md를 입력으로 받아 디자인 시스템 시각 카탈로그 HTML을 자동 생성합니다.

## 파일 구조

```
04-preview-catalog/
├── DESIGN.md      # 입력: calm-design 기본 톤 (9섹션 표준)
├── index.html     # 출력: 자동 생성된 시각 카탈로그
└── README.md      # 이 문서
```

## 사용법

### 자동 생성

```bash
cd ~/.claude/skills/calm-design

python scripts/build-preview-catalog.py \
  --design examples/04-preview-catalog/DESIGN.md \
  --output examples/04-preview-catalog/index.html
```

### 옵션

| 옵션 | 설명 |
|------|------|
| `--design` | 입력 DESIGN.md 경로 (필수) |
| `--output` | 출력 HTML 경로 (필수) |
| `--language ko\|en` | 언어 강제 (기본: 자동 감지) |
| `--no-contrast` | WCAG contrast 계산 스킵 |

## 카탈로그 섹션

생성된 `index.html`은 5개 섹션을 포함합니다:

1. **Color Palette** — 색상 견본 + WCAG contrast 표시
2. **Typography Scale** — 타입 스케일 (한국어 샘플)
3. **Component States** — 컴포넌트별 6상태 그리드
4. **Spacing System** — 4/8/16/24/32/48/64 px 시각화
5. **Shadow Tokens** — 그림자 견본

## 브라우저에서 보기

```bash
open examples/04-preview-catalog/index.html
```

## 자신의 DESIGN.md로 생성

```bash
python scripts/build-preview-catalog.py \
  --design .calm-design/DESIGN.md \
  --output preview-catalog.html
```
