# Design System: Inspired by Mintlify

> Source: calm-design 자체 작성 — "Inspired by" 정책. mintlify.com 공개 인터페이스 관찰 기반.
> LANGUAGE: en

## 1. Visual Theme & Atmosphere

Developer documentation platform built around clarity, speed, and extensibility. Mintlify leans into a dark-mode-first aesthetic with cool gray surfaces and a mint-green accent that signals modernity without being harsh. The interface is dense with information — code blocks, navigation trees, API reference tables — yet never cluttered, thanks to precise spacing and a rigorous typographic hierarchy. The overall tone is "docs that feel as good to read as the product feels to use."

## 2. Color Palette & Roles

| Canvas  | `#0F1117` | Page background — deep cool near-black (Off-Black) |
| Surface | `#1A1D27` | Sidebar, cards, code block backgrounds |
| Raised  | `#21242F` | Elevated surfaces: dropdowns, tooltips |
| Ink     | `#F1F5F9` | Primary text — Slate-100, not Pure White |
| Mute    | `#94A3B8` | Secondary text, breadcrumbs, metadata |
| Border  | `#2D3149` | 1px dividers, sidebar item outlines |
| Accent  | `#3ECF8E` | Mint-green primary — CTAs, active nav, inline links |
| AccentDim | `#1E6B4E` | Accent hover backgrounds, subtle fills |
| Warning | `#F59E0B` | Deprecation notices, caution callouts |
| Danger  | `#F87171` | Error callouts, breaking-change badges |

Rules: Single mint-green accent. Pure Black `#000000` 금지 — Off-Black Canvas `#0F1117` 사용. Accent kept below 75% saturation to avoid neon glare. Dark mode is the primary mode; light mode is secondary.

## 3. Typography Rules

- Family: `Satoshi, system-ui, sans-serif` for UI chrome and prose; `Geist Mono` for all code (Inter is banned — generic, no docs personality)
- Display / H1: `text-3xl md:text-4xl`, `tracking-tight`, `font-semibold`, `leading-snug`
- H2: `text-xl md:text-2xl`, `font-semibold`, `tracking-tight`, border-bottom `border-border` for section delineation
- H3: `text-lg`, `font-medium`, used as component / parameter headings
- Body prose: `text-base`, `leading-relaxed`, `max-w-[68ch]`, `text-ink`
- Code inline: `font-mono text-sm bg-raised rounded px-1.5 py-0.5 text-accent`
- Code block: `font-mono text-sm leading-relaxed` with line numbers in `text-mute`
- Banned: Inter (too common for docs products), serif fonts, system-stack-only definitions

## 4. Component Stylings

### Button (Primary / CTA)
- **Default**: `bg-accent text-[#0F1117] rounded-lg px-4 py-2 text-sm font-semibold`
- **Hover**: `bg-[#4FDEA0]` (lighter mint), transition 150ms ease-out
- **Focus**: `outline-none ring-2 ring-accent ring-offset-2 ring-offset-[#0F1117]`
- **Active**: `bg-[#35B97A] scale-[0.97]`
- **Disabled**: `opacity-40 cursor-not-allowed`
- **Loading**: spinner SVG (12px accent-colored) left of label, label remains visible

### Navigation Sidebar Item
- **Default**: `text-mute text-sm px-3 py-1.5 rounded-md`
- **Hover**: `bg-surface text-ink`
- **Focus**: `ring-1 ring-accent/60 outline-none`
- **Active** (current page): `bg-AccentDim text-accent font-medium border-l-2 border-accent`
- **Disabled** (coming soon): `opacity-40 cursor-default`
- **Loading**: skeleton line `animate-pulse bg-raised rounded h-4`

### Code Block
- **Default**: `bg-surface border border-border rounded-xl p-4 font-mono text-sm overflow-x-auto`
- **Hover**: no visual change (static display element)
- **Focus**: copy button appears (`opacity-0 → opacity-100`) on keyboard focus
- **Active**: copy button pressed — icon switches from Copy to Check for 1.5s
- **Disabled**: not applicable
- **Loading**: skeleton three-line placeholder with shimmer `animate-pulse`

### Callout / Alert Card
- **Default**: `rounded-lg border-l-4 px-4 py-3` with color variant per type (info=accent, warning=Warning, danger=Danger)
- **Hover**: no change (static)
- **Focus**: focusable if contains links — `ring-1 ring-accent/40`
- **Active**: not applicable
- **Disabled**: not applicable
- **Loading**: skeleton with left-bar placeholder

## 5. Layout Principles

- **Three-zone layout**: `w-64 left-sidebar` (nav tree) + `flex-1 main content` + `w-56 right-sidebar` (on-page ToC) on desktop
- **Content max-width**: `max-w-3xl` for prose; API reference allows `max-w-5xl`
- **Section padding**: `py-10 md:py-14` — tighter than marketing pages since docs are read linearly
- **min-h-[100dvh]** on root layout — `h-screen` banned (iOS 100vh bug)
- **Grid**: CSS Grid `grid-cols-[256px_1fr_224px]` on desktop collapses to `grid-cols-1` on mobile
- **Banned**: full-bleed hero sections in doc pages, 3-column equal cards, decorative divider graphics

## 6. Depth & Elevation

- **Default surfaces**: 1px `border-border` provides depth — shadow avoided on primary content areas
- **Raised elements** (dropdowns, tooltips): `shadow-lg shadow-black/60` — dark tinted shadow for dark canvas
- **Modals**: `bg-raised border border-border rounded-2xl shadow-2xl shadow-black/80` + `backdrop-blur-sm bg-black/60` overlay
- **Code blocks**: no shadow — `border border-border` creates containment without elevation drama
- **Sticky header**: `border-b border-border backdrop-blur-md bg-canvas/80` — glass effect for scroll continuity
- **z-index**: nav=40, sticky-header=30, dropdown=45, modal=50, toast=60
- **Banned**: neon/colored glows, outer glow on mint accent, `shadow-[0_0_*_#3ECF8E]` patterns

## 7. Motion & Interaction

- **Easing**: `cubic-bezier(0.16, 1, 0.3, 1)` for panel entrances; `ease-out` 120ms for micro-interactions
- **GPU-only**: `transform` and `opacity` exclusively — `width`, `height`, `top`, `left` never animated
- **Sidebar collapse**: `translateX(-100%)` → `translateX(0)` 200ms with spring easing
- **Code copy confirmation**: icon crossfade `opacity` 150ms — no scale or position shift
- **Search modal**: fade + scale `scale-95 → scale-100` 180ms on open; reverse on close
- **Staggered nav items**: `delay: index * 30ms` on initial sidebar render
- **Reduced-motion**: `@media (prefers-reduced-motion: reduce)` — all transitions `duration-0`, no stagger

## 8. Responsive Behavior

- **Breakpoints**: mobile `<768px`, tablet `768–1024px`, desktop `≥1024px`
- **Mobile**: both sidebars hidden; left nav behind hamburger drawer (bottom sheet or left slide-in); right ToC hidden entirely
- **Tablet**: left sidebar collapses to icon-only rail (32px), right ToC hidden
- **Desktop**: full three-zone layout
- **Touch targets**: `44×44px` minimum on all nav items and buttons (iOS HIG)
- **Code blocks**: horizontal scroll on overflow — no text-wrap on code
- **Typography**: `clamp(0.875rem, 1vw + 0.5rem, 1rem)` for body; headings clamped separately

## 9. Anti-Patterns (Project-Specific Banned)

- ❌ Light-mode-only designs — Mintlify is dark-mode-first; forcing light breaks brand identity
- ❌ Auto-collapsing code blocks with "show more" — docs readers need full code visibility at rest; truncation destroys copy-paste workflow
- ❌ Marketing hero sections inside doc pages — docs are task-oriented, not promotional; hero imagery distracts from content
- ❌ Colored text other than accent for inline code — using random colors for syntax token override confuses the single-accent rule
- ❌ Breadcrumb trails exceeding 3 levels displayed simultaneously — deep nesting should be collapsed with `…` ellipsis pattern
- ❌ Full-page loading spinners on navigation — docs pages should stream content; blocking spinners feel like page refreshes

(글로벌 안티-슬롭 50개는 `references/ai-tells-blocklist.md` 자동 적용)
