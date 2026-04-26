# calm-design Reference Library

Mode C(Match-Reference)가 사용하는 큐레이션 라이브러리. 사용자가 "토스 처럼", "Linear 스타일로" 등 레퍼런스 키워드로 요청 시 이 라이브러리에서 가장 가까운 브랜드 3개 후보 자동 추천.

## 구조

```
reference-library/
├── _index.json         # 카테고리·브랜드·매칭 알고리즘 메타
├── README.md           # 이 파일
├── global/             # 글로벌 67개 브랜드
│   └── _import_summary.json (Phase 1.5 시범 import 메타)
└── korean/             # 한국 SaaS 자체 작성
    ├── toss/DESIGN.md     ⬆️ Phase 1.5 풀 작성
    ├── kakao/DESIGN.md    ⬆️ Phase 1.5 풀 작성
    ├── daangn/DESIGN.md   ⬆️ Phase 1.5 풀 작성
    └── (12개 추가 예정 — Phase 3.5)
```

## 글로벌 67개 브랜드 — awesome-design-md 기반

[VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) (MIT)의 큐레이션을 참조. **메타데이터(brand 이름·카테고리·한 줄 설명)만 `_index.json`에 인덱스**되어 있으며, 풀 DESIGN.md 본문은 사용자가 다음 방법으로 다운로드:

```bash
# awesome-design-md의 공식 CLI 도구 사용
npx getdesign@latest add {brand}

# 또는 https://getdesign.md/{brand}/design-md 에서 직접 fetch
```

다운로드 후 calm-design은 자동으로 9-섹션 표준으로 변환:
- awesome-design-md Section 7 (Do's/Don'ts) → calm-design Section 7 (Motion) + Section 9 (Anti-Patterns) 분할
- awesome-design-md Section 9 (Agent Prompt Guide) → calm-design Section 9 (Anti-Patterns)에 흡수

변환은 `scripts/awesome-design-md-import.py` 자동 실행.

## 한국 SaaS 15개 — 자체 작성

awesome-design-md에는 한국 SaaS가 부재. calm-design이 자체로 9-섹션 풀 작성:

| Phase 1.5 (3개 시범 완료) | Phase 3.5 (12개 추가 예정) |
|---|---|
| ✅ 토스 (Toss) | 네이버, 라인, 쿠팡, 배민 |
| ✅ 카카오 (Kakao) | 야놀자, 무신사, 29CM, 컬리 |
| ✅ 당근 (Daangn) | 오늘의집, 직방, 클래스101, 스타벅스코리아 |

작성 정책:
- ✅ "Inspired by" 명시 (직접 복제 X, 영감 차용)
- ✅ 공개 디자인 시스템·인터페이스 관찰 기반
- ✅ 시그니처 패턴 명시 (TossBottomSheet, KakaoChatBubble 등)
- ❌ 브랜드 로고·정확한 hex·독점 폰트 사용 X
- ❌ 비공개 디자인 시스템 문서 인용 X

## Mode C 매칭 알고리즘

`_index.json`의 `matching_algorithm` 섹션 참조:

1. 사용자 입력에서 키워드 추출
2. categories[].tags + scenarios와 매칭, 가중치 점수
3. 최고 점수 카테고리에서 브랜드 후보
4. "토스처럼" 직접 명시 시 slug 직접 매칭 우선
5. 최종 3개 후보 사용자 제시 → 선택
6. 매칭 0개 fallback: Linear, Vercel, Stripe, Notion, Apple

자세한 워크플로우는 `modes/match-reference.md` (Phase 3 묶음 M).

## 라이선스 정책

| 영역 | 정책 |
|---|---|
| 글로벌 메타데이터 (`_index.json` global) | MIT (awesome-design-md 출처 명시) |
| 글로벌 풀 DESIGN.md | 사용자가 직접 fetch (npx getdesign 또는 getdesign.md) |
| 한국 자체 작성 | MIT (calm-design 자체 — "Inspired by" 정책) |
| 변환 스크립트 | MIT |

## 기여 환영

`korean/` 디렉토리에 새 브랜드 DESIGN.md 추가 PR 환영. [CONTRIBUTING.md](../CONTRIBUTING.md)의 "reference-library 기여 정책" 참조.
