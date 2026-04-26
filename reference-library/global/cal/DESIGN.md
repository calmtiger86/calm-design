# Design System: Inspired by Cal.com

> Source: calm-design 자체 작성 — "Inspired by" 정책. cal.com 공개 인터페이스 관찰 기반.
> LANGUAGE: en

## 1. Visual Theme & Atmosphere

Open-source scheduling infrastructure with a clean, trustworthy aesthetic. Cal.com favors generous white space on a bright canvas, letting content breathe without decorative noise. A restrained violet-purple accent anchors CTAs and interactive elements against an otherwise neutral palette. The tone is professional yet approachable — sophisticated enough for enterprise buyers, legible enough for individual creators who just want to share a booking link.

## 2. Color Palette & Roles

| Canvas  | `#FFFFFF` | Page background — pure white canvas |
| Surface | `#F9FAFB` | Card and sheet backgrounds |
| Ink     | `#111827` | Headlines and body text (Off-Black, not Pure Black) |
| Mute    | `#6B7280` | Secondary text, meta, placeholders |
| Border  | `#E5E7EB` | 1px dividers, input outlines |
| Accent  | `#6D28D9` | Primary CTA, active states, focus rings (Violet-700) |
| Subtle  | `#EDE9FE` | Accent tint — hover backgrounds, tag fills |
| Danger  | `#DC2626` | Error states, destructive actions |
| Success | `#16A34A` | Confirmation, availability indicators |

Rules: Single violet accent only. Pure Black `#000000` 금지 — Off-Black Ink `#111827` 사용. Accent saturation kept below 80%. Subtle tint used for non-disruptive highlight areas.

## 3. Typography Rules

- Family: `Geist, system-ui, sans-serif` (Geist is Cal.com's primary typeface; Inter is banned — overused, no differentiation)
- Display / H1: `text-4xl md:text-5xl lg:text-6xl`, `tracking-tight`, `leading-tight`, `font-semibold`
- H2–H3: `text-2xl md:text-3xl`, `tracking-tight`, `font-medium`
- Body: `text-base md:text-lg`, `leading-relaxed`, `max-w-[72ch]`
- Label / Meta: `text-xs tracking-wide uppercase text-mute font-medium`
- Numeric / Time: `tabular-nums font-mono` (Geist Mono) — critical for scheduling time slots
- Banned: Inter (too generic), Helvetica, Times New Roman, system-reliant stacks without Geist

## 4. Component Stylings

### Button (Primary)
- **Default**: `bg-accent text-white rounded-md px-4 py-2 text-sm font-medium`
- **Hover**: `bg-violet-800` (one shade darker), transition 150ms ease-out
- **Focus**: `outline-none ring-2 ring-accent ring-offset-2`
- **Active**: `bg-violet-900 scale-[0.98]`
- **Disabled**: `opacity-50 cursor-not-allowed pointer-events-none`
- **Loading**: inline spinner SVG (12px) left of label text, label unchanged

### Button (Secondary / Ghost)
- **Default**: `bg-transparent border border-border text-ink rounded-md px-4 py-2 text-sm`
- **Hover**: `bg-surface border-gray-300`
- **Focus**: `ring-2 ring-accent ring-offset-2`
- **Active**: `bg-gray-100`
- **Disabled**: `opacity-50 cursor-not-allowed`
- **Loading**: inline spinner, border color shifts to `border-accent/40`

### Booking Card
- **Default**: `bg-white border border-border rounded-xl p-5 shadow-sm`
- **Hover**: `border-accent/40 shadow-md` transition 150ms
- **Focus**: `ring-2 ring-accent ring-offset-2` (keyboard nav)
- **Active** (selected slot): `bg-subtle border-accent`
- **Disabled** (unavailable): `opacity-40 cursor-not-allowed bg-surface`
- **Loading**: skeleton shimmer replacing time text — `animate-pulse bg-gray-200 rounded`

### Input / Form Field
- **Default**: `border border-border rounded-md px-3 py-2 text-sm bg-white`
- **Hover**: `border-gray-400`
- **Focus**: `border-accent ring-2 ring-accent/20 outline-none`
- **Active**: same as Focus while typing
- **Disabled**: `bg-surface opacity-60 cursor-not-allowed`
- **Loading**: skeleton block matching field height, `animate-pulse`

## 5. Layout Principles

- **Max-width**: `max-w-5xl mx-auto px-4 md:px-6` for content; booking widget max-w-md centered
- **Macro spacing**: section padding `py-20 md:py-28` — generous but not excessive
- **Grid**: CSS Grid `grid-cols-12` base; booking UI uses `grid-cols-1 md:grid-cols-2` (calendar + time slots)
- **Sidebar pattern**: settings pages use `w-56 sidebar + flex-1 main` layout
- **min-h-[100dvh]** on full-page route wrappers — `h-screen` banned (iOS 100vh bug)
- **Banned**: 3-column equal-width card grids, full-bleed hero images, ornamental section dividers

## 6. Depth & Elevation

- **Cards**: `shadow-sm` (subtle lift) as default; `shadow-md` on hover for interactive cards only
- **Modals / Dialogs**: `shadow-xl` + `backdrop-blur-sm bg-black/40` overlay
- **Dropdowns**: `shadow-lg border border-border rounded-lg` — no tinted shadows
- **Tinted shadow**: not used — Cal.com stays neutral; colored glows are banned
- **z-index layers**: nav=40, dropdown=45, modal=50, toast=60
- **Inset highlight**: not used (light-mode first, inset highlights are dark-mode patterns)

## 7. Motion & Interaction

- **Easing**: `cubic-bezier(0.16, 1, 0.3, 1)` spring-like for entrances; `ease-out` 150ms for micro-interactions
- **GPU-only properties**: `transform` and `opacity` only — never animate `top`, `left`, `width`, `height`
- **Page transitions**: fade + slight upward translate (`translateY(4px)` → `translateY(0)`) 200ms
- **Calendar date selection**: scale pulse `scale-95 → scale-100` 120ms on selection confirm
- **Staggered lists**: `delay: index * 40ms` for time slot grid appearance
- **Reduced-motion**: `@media (prefers-reduced-motion: reduce)` — all transitions set to `duration-0`
- **Perpetual animations**: banned except skeleton shimmer during loading states

## 8. Responsive Behavior

- **Breakpoints**: mobile `<768px`, tablet `768–1024px`, desktop `≥1024px`
- **Booking widget**: stacked single-column on mobile (calendar above, time slots below); side-by-side on tablet+
- **Navigation**: horizontal nav on desktop → hamburger sheet on mobile (`bottom-sheet` pattern preferred over top drawer)
- **Touch targets**: minimum `44×44px` on all interactive elements (iOS HIG)
- **Typography scaling**: `clamp(1rem, 1.5vw + 0.75rem, 1.25rem)` for body text
- **Time slot grid**: 3-column on desktop, 2-column on tablet, 1-column on mobile

## 9. Anti-Patterns (Project-Specific Banned)

- ❌ Playful / whimsical illustration in the booking flow — trust and clarity are paramount; cartoons undermine the scheduling context
- ❌ Dark-mode-only designs — Cal.com is light-mode primary; dark mode is opt-in, not the brand default
- ❌ Neon or vivid gradient accents — the violet accent must stay muted (Violet-700, not electric purple)
- ❌ Auto-advancing calendar interactions without explicit user confirmation — scheduling errors are high-stakes
- ❌ Hiding availability status behind hover — always surface unavailable slots visually at rest state
- ❌ Dense data tables without zebra striping or row hover — scheduling admin UIs need clear row separation

(글로벌 안티-슬롭 50개는 `references/ai-tells-blocklist.md` 자동 적용)
