# Awesome List 등록 가이드

calm-design을 Claude Code 커뮤니티에 공개하기 위한 등록 가이드입니다.

## 등록 대상 리스트

### 1. rohitg00/awesome-claude-code-toolkit (추천)

가장 활발한 Claude Code 리소스 모음 (135 agents, 35+ skills)

**Skills 섹션에 추가할 내용:**

```markdown
| [calm-design](https://github.com/calmtiger86/calm-design) | AI가 만든 티 안 나는 프리미엄 디자인. 50+ 안티-슬롭 자동 차단, 33개 브랜드 레퍼런스, 한국어 1순위. |
```

**PR 제출:**
```bash
# 1. Fork
gh repo fork rohitg00/awesome-claude-code-toolkit

# 2. Clone
git clone https://github.com/YOUR_USERNAME/awesome-claude-code-toolkit
cd awesome-claude-code-toolkit

# 3. README.md의 Skills 섹션에 calm-design 추가

# 4. Commit & Push
git add README.md
git commit -m "Add calm-design skill"
git push origin main

# 5. PR 생성
gh pr create --title "Add calm-design skill" --body "Add calm-design: Premium designs that don't look AI-generated. 50+ anti-slop patterns, 33 brand references, Korean-first."
```

---

### 2. hesreallyhim/awesome-claude-code

Skills, hooks, slash-commands 전문 리스트

**추가할 내용:**

```markdown
### Design & UI

- [calm-design](https://github.com/calmtiger86/calm-design) - Premium designs that don't look AI-generated. 50+ anti-slop patterns blocked, 33 brand references, Korean-first with Pretendard.
```

---

### 3. ccplugins/awesome-claude-code-plugins

플러그인/스킬 전문 리스트

---

## Anthropic 공식 마켓플레이스

### 등록 방법

1. **plugin.json 확인** (이미 생성됨)
   - `calm-design/plugin.json`

2. **제출 요청**
   - Anthropic Discord에서 문의
   - 또는 공식 플러그인 제출 양식 사용 (출시 시)

### 커뮤니티 마켓플레이스 생성 (선택)

자체 마켓플레이스를 만들어 다른 사용자가 쉽게 설치할 수 있게 할 수 있습니다:

```json
// marketplaces.json
{
  "name": "calmtiger's Skills",
  "plugins": [
    {
      "name": "calm-design",
      "source": "github:calmtiger86/calm-design"
    }
  ]
}
```

사용자 설치:
```bash
claude plugin marketplace add https://github.com/calmtiger86/calm-design/marketplaces.json
```

---

## 홍보 채널

### 추천 순서

1. **GitHub** - 이미 공개됨 ✅
2. **Awesome Lists** - PR 제출 (위 가이드)
3. **Threads/Twitter** - 출시 포스트
4. **Discord** - Anthropic 공식 디스코드
5. **Reddit** - r/ClaudeAI, r/LocalLLaMA

### 출시 포스트 예시

```
🎨 calm-design 출시

AI가 만든 디자인인데 AI 티가 안 나요.

✅ 50+ "AI 냄새" 자동 차단
✅ 토스, 당근 등 33개 브랜드 레퍼런스
✅ 한국어 최적화 (Pretendard)
✅ 셀프-크리틱 자동 검증

GitHub: https://github.com/calmtiger86/calm-design

#ClaudeCode #AI #Design #한국어
```

---

## 체크리스트

- [x] GitHub 저장소 공개
- [x] plugin.json 생성
- [x] Issue/PR 템플릿 설정
- [x] Discussions 활성화
- [ ] awesome-claude-code-toolkit PR 제출
- [ ] awesome-claude-code PR 제출
- [ ] 출시 포스트 작성
- [ ] Anthropic Discord 공유
