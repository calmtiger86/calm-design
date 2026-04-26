# Korean SaaS Patterns — 한국 SaaS 시그니처 패턴 코드 카탈로그

`creative-arsenal.md`와 `motion-system.md`에서 추상적으로 묘사한 한국 SaaS 패턴의 **실제 구현 코드**. Mode C(Match-Reference)에서 "토스 스타일", "당근 처럼" 등의 요청 시 직접 참조.

> Phase 1 활성화 (잠재 이슈 #3 처리). Phase 3 reference-library/ 풀 구축 시 각 브랜드 폴더로 분리 예정.

## 0. 라이선스·관찰 정책

- 모든 코드는 calm-design **자체 작성** — 브랜드 자산 직접 복제 X
- "Inspired by" 정책 엄격 — 시그니처 인상만 추출
- 브랜드 로고·정확한 hex·독점 폰트 사용 X

---

## 1. 토스 (Toss) — 핀테크 신뢰 톤

### 1.1 Bottom Sheet (모바일 결제 흐름)

```tsx
// components/patterns/toss-bottom-sheet.tsx
"use client";
import { motion, AnimatePresence } from "motion/react";
import { useState } from "react";

export function TossBottomSheet({ open, onClose, title, children }: Props) {
  return (
    <AnimatePresence>
      {open && (
        <>
          <motion.div
            initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}
            onClick={onClose}
            className="fixed inset-0 bg-black/40 z-40"
            aria-hidden="true"
          />
          <motion.div
            role="dialog"
            aria-labelledby="sheet-title"
            initial={{ y: "100%" }}
            animate={{ y: 0 }}
            exit={{ y: "100%" }}
            transition={{ type: "spring", stiffness: 300, damping: 35 }}
            drag="y"
            dragConstraints={{ top: 0, bottom: 0 }}
            dragElastic={0.15}
            onDragEnd={(_, info) => { if (info.offset.y > 150) onClose(); }}
            className="fixed inset-x-0 bottom-0 z-50 max-w-md mx-auto
                       bg-white rounded-t-[28px] pb-8 shadow-[0_-8px_40px_rgba(0,0,0,0.08)]"
          >
            <div className="w-12 h-1 bg-zinc-300 rounded-full mx-auto mt-3 mb-4" aria-hidden="true" />
            <h2 id="sheet-title" className="text-xl font-bold tracking-tight px-6 break-keep">
              {title}
            </h2>
            <div className="px-6 mt-4">{children}</div>
          </motion.div>
        </>
      )}
    </AnimatePresence>
  );
}
```

**시그니처 포인트**:
- 모서리 radius `28px` (토스 특유, 일반 24px보다 큼)
- Spring stiffness 300/damping 35 (꽉 찬 느낌)
- 드래그 핸들 `w-12 h-1` (얇음·차분)

### 1.2 Floating Label Input (한국어 친화)

```tsx
export function TossInput({ id, label, error, ...props }: Props) {
  return (
    <div className="space-y-1.5">
      <div className="relative">
        <input
          id={id}
          placeholder=" "
          className={`peer w-full h-14 px-4 pt-6 pb-1 rounded-xl border bg-zinc-50
                     text-base font-medium
                     focus:outline-none focus:bg-white focus:ring-2 focus:ring-accent/20
                     ${error ? "border-red-500" : "border-zinc-200 focus:border-accent"}`}
          {...props}
        />
        <label htmlFor={id}
               className="absolute left-4 top-4 text-mute text-base
                          peer-focus:top-2 peer-focus:text-xs peer-focus:text-accent
                          peer-[:not(:placeholder-shown)]:top-2 peer-[:not(:placeholder-shown)]:text-xs
                          pointer-events-none transition-all break-keep">
          {label}
        </label>
      </div>
      {error && (
        <p role="alert" className="text-xs text-red-600 font-medium break-keep flex items-center gap-1">
          <span aria-hidden="true">⚠</span> {error}
        </p>
      )}
    </div>
  );
}
```

### 1.3 Primary CTA Button (토스 시그니처)

```tsx
export function TossPrimaryButton({ children, loading, ...props }: Props) {
  return (
    <button
      disabled={loading}
      className="w-full h-14 rounded-2xl bg-accent text-white font-bold text-base
                 hover:scale-[1.01] active:scale-[0.99]
                 transition-transform duration-200 ease-[cubic-bezier(0.16,1,0.3,1)]
                 disabled:opacity-60 disabled:cursor-not-allowed
                 break-keep flex items-center justify-center gap-2"
      {...props}
    >
      {loading && <span className="w-4 h-4 border-2 border-white/30 border-t-white rounded-full animate-spin" />}
      {children}
    </button>
  );
}
```

---

## 2. 당근 (Daangn) — 친근·로컬 톤

### 2.1 Recommend Card (가로 스크롤)

```tsx
export function DaangnRecommendCarousel({ items }: { items: Item[] }) {
  return (
    <section className="py-6">
      <div className="flex items-end justify-between px-4 mb-4">
        <h2 className="text-xl font-bold tracking-tight break-keep">
          오늘 추천드려요
        </h2>
        <a href="#" className="text-sm text-mute hover:text-ink">
          전체 보기 →
        </a>
      </div>
      <div className="flex gap-3 px-4 overflow-x-auto snap-x snap-mandatory scrollbar-hide pb-2">
        {items.map((item) => (
          <article
            key={item.id}
            className="snap-start shrink-0 w-44 bg-white rounded-2xl border border-zinc-100 overflow-hidden"
          >
            <img src={item.image} alt={item.title}
                 className="w-full aspect-square object-cover" loading="lazy" />
            <div className="p-3">
              <h3 className="text-sm font-semibold break-keep line-clamp-2">{item.title}</h3>
              <p className="mt-1 text-base font-bold tabular-nums">{item.price.toLocaleString("ko-KR")}원</p>
              <p className="mt-0.5 text-xs text-mute">{item.location}</p>
            </div>
          </article>
        ))}
      </div>
    </section>
  );
}
```

**시그니처 포인트**:
- 가로 스크롤 + snap (모바일 친화)
- `aspect-square` 이미지 (정사각, 시각 일관성)
- 가격 `tabular-nums` 강제 (단위 정렬)
- "오늘 추천드려요" 같은 친근한 한국어 톤

---

## 3. 카카오톡 — 채팅 메시지 패턴

### 3.1 Bubble Chat (대화형 FAQ·인터뷰 콘텐츠)

```tsx
export function KakaoChatBubble({ message, sender, time }: Props) {
  const isMe = sender === "me";
  return (
    <div className={`flex ${isMe ? "justify-end" : "justify-start"} gap-2 my-1`}>
      {!isMe && (
        <div className="w-9 h-9 rounded-full bg-zinc-200 shrink-0" aria-hidden="true" />
      )}
      <div className={`flex flex-col ${isMe ? "items-end" : "items-start"} max-w-[70%]`}>
        {!isMe && <span className="text-xs text-mute mb-1 break-keep">{message.senderName}</span>}
        <div className="flex items-end gap-1.5">
          {isMe && <span className="text-[10px] text-mute tabular-nums">{time}</span>}
          <div className={`px-3 py-2 rounded-2xl break-keep
            ${isMe
              ? "bg-[#FEE500] text-ink rounded-br-sm"
              : "bg-white text-ink border border-zinc-200 rounded-bl-sm"}`}>
            <p className="text-sm leading-relaxed">{message.text}</p>
          </div>
          {!isMe && <span className="text-[10px] text-mute tabular-nums">{time}</span>}
        </div>
      </div>
    </div>
  );
}
```

**시그니처 포인트**:
- 카카오 노란색은 약간 비슷한 톤(`#FEE500`)으로만, 정확 복제 X
- 한쪽 모서리만 sharp (`rounded-bl-sm`/`rounded-br-sm`) — 말풍선 꼬리 인상

---

## 4. 네이버 — 검색 자동완성

### 4.1 Search Suggestion Dropdown

```tsx
export function NaverSearchSuggest({ query, suggestions, popular }: Props) {
  return (
    <div className="absolute top-full left-0 right-0 mt-2 bg-white rounded-xl
                    border border-zinc-200 shadow-[0_4px_20px_rgba(0,0,0,0.06)]
                    overflow-hidden z-30">
      {query && suggestions.length > 0 && (
        <div className="py-2">
          {suggestions.map((s, i) => (
            <button key={i}
                    className="w-full text-left px-4 py-2 hover:bg-zinc-50 flex items-center gap-3 break-keep">
              <span className="text-mute" aria-hidden="true">🔍</span>
              <span className="text-sm">
                {s.split(query).map((part, j, arr) => (
                  <span key={j}>
                    {part}
                    {j < arr.length - 1 && <strong className="text-accent">{query}</strong>}
                  </span>
                ))}
              </span>
            </button>
          ))}
        </div>
      )}
      {!query && popular && (
        <div className="border-t border-zinc-100">
          <div className="px-4 py-2 text-xs font-semibold text-mute">실시간 인기 검색어</div>
          {popular.map((item, i) => (
            <button key={i} className="w-full text-left px-4 py-2 hover:bg-zinc-50 flex items-center gap-3 break-keep">
              <span className="text-xs font-bold text-accent tabular-nums w-5">{i + 1}</span>
              <span className="text-sm flex-1">{item.title}</span>
              {item.delta && <span className="text-xs text-red-500 tabular-nums">↑{item.delta}</span>}
            </button>
          ))}
        </div>
      )}
    </div>
  );
}
```

**시그니처 포인트**:
- 실시간 인기 검색어 1, 2, 3... `tabular-nums` 정렬
- 매칭 키워드 강조 (`<strong>` 액센트 색상)
- 변동(`↑/↓`) 표시 — 데이터 밀도

---

## 5. 라인 (LINE) — 메시지 반응

### 5.1 Sticker Reactions (액션 버튼들)

```tsx
const REACTIONS = ["👍", "❤️", "😄", "🎉", "🔥"];

export function LineReactionPicker({ onPick }: { onPick: (r: string) => void }) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 10, scale: 0.9 }}
      animate={{ opacity: 1, y: 0, scale: 1 }}
      transition={{ type: "spring", stiffness: 400, damping: 25 }}
      className="inline-flex gap-1 bg-white rounded-full px-2 py-1.5
                 border border-zinc-200 shadow-[0_2px_12px_rgba(0,0,0,0.08)]"
    >
      {REACTIONS.map((r) => (
        <motion.button
          key={r}
          whileHover={{ scale: 1.3, y: -4 }}
          whileTap={{ scale: 1.1 }}
          onClick={() => onPick(r)}
          className="text-xl w-8 h-8 flex items-center justify-center rounded-full hover:bg-zinc-100"
          aria-label={`${r} 반응`}
        >
          {r}
        </motion.button>
      ))}
    </motion.div>
  );
}
```

**시그니처 포인트**:
- hover scale + y 이동 (mac dock 스타일)
- bouncy spring (stiffness 400, damping 25)

---

## 6. 무신사 — Filter Sidebar

### 6.1 Filter Panel (이커머스·카탈로그)

```tsx
export function MusinsaFilterSidebar({ filters, onChange }: Props) {
  return (
    <aside className="w-60 shrink-0 border-r border-zinc-200 bg-white">
      <div className="sticky top-0 bg-white border-b border-zinc-200 p-4">
        <h2 className="font-bold tracking-tight">필터</h2>
      </div>
      <div className="p-4 space-y-6">
        {filters.map((group) => (
          <FilterGroup key={group.id} {...group} onChange={onChange} />
        ))}
      </div>
    </aside>
  );
}

function FilterGroup({ id, label, options, onChange }: GroupProps) {
  return (
    <fieldset>
      <legend className="text-sm font-semibold mb-2 break-keep">{label}</legend>
      <ul className="space-y-1">
        {options.map((opt) => (
          <li key={opt.value}>
            <label className="flex items-center justify-between py-1.5 cursor-pointer
                              text-sm hover:text-ink text-mute">
              <span className="flex items-center gap-2 break-keep">
                <input type="checkbox" name={id} value={opt.value}
                       onChange={(e) => onChange(id, opt.value, e.target.checked)}
                       className="w-4 h-4 rounded text-accent focus:ring-accent/30" />
                {opt.label}
              </span>
              <span className="text-xs text-mute tabular-nums">({opt.count})</span>
            </label>
          </li>
        ))}
      </ul>
    </fieldset>
  );
}
```

**시그니처 포인트**:
- `<fieldset>`+`<legend>` (접근성 의무 — Pre-Flight #23·#26 통과)
- 카운트 `tabular-nums` 정렬

---

## 7. Mode C 사용 매핑 (Phase 3 진입 시)

| 사용자 의도 | 적용 패턴 |
|---|---|
| "토스 스타일" + 모바일 결제 | TossBottomSheet + TossInput + TossPrimaryButton |
| "토스 스타일" + 일반 폼 | TossInput + TossPrimaryButton |
| "당근 처럼" + 추천 섹션 | DaangnRecommendCarousel |
| "카카오톡 같은 채팅 UI" | KakaoChatBubble |
| "네이버처럼 검색 자동완성" | NaverSearchSuggest |
| "라인 메시지 반응" | LineReactionPicker |
| "무신사 카탈로그" | MusinsaFilterSidebar |

이 매핑은 Phase 3 `reference-library/_index.json`에 통합 예정.
