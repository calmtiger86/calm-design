# Design System: Inspired by Raycast

> Source: calm-design 자체 작성 — "Inspired by" 정책. raycast.com 공개 인터페이스 관찰 기반.
> LANGUAGE: en

## 1. Visual Theme & Atmosphere

Keyboard-first productivity launcher for macOS power users. Deep dark canvas with razor-sharp command interfaces — zero decoration, maximum signal. The aesthetic is calm obsidian: near-black surfaces, restrained warm-gray hierarchy, and a single cool accent that guides without shouting. Every pixel earns its place by reducing friction between thought and action. Speed is the primary sensory cue: instant feedback, instant results, instant context.

## 2. Color Palette & Roles

| Canvas  | `#0D0D0F` | Page background — deep off-black, not pure black |
| Surface | `#161618` | Panel, card, and sheet background |
| Elevated | `#1F1F23` | Popover, hover row, and secondary surface |
| Ink     | `#F2F2F3` | Primary text and headlines |
| Mute    | `#8C8C99` | Secondary text, metadata, placeholder |
| Border  | `#2A2A30` | 1px separator lines |
| Accent  | `#5B7CF6` | Calm indigo — active state, CTA, selection indicator |
| Positive | `#3DAB76` | Success, completion, positive feedback |
| Caution | `#E8A035` | Warning, pending, in-progress |
| Danger  | `#D95F5F` | Error, destructive action |

Rules: dark-mode only, Pure Black `#000000` avoided (use off-black `#0D0D0F`), single indigo accent (LILA BAN applied — vivid purple/neon gradients replaced with calm indigo), saturation capped at 65%.

## 3. Typography Rules

- Family: `Geist, system-ui, sans-serif` (Geist preferred — Inter banned)
- Monospace: `Geist Mono, ui-monospace` for command text, shortcuts, paths
- Display/H1: `text-3xl font-semibold tracking-tight leading-tight`
- Body: `text-sm leading-normal` — dense information layout
- Label/Meta: `text-xs tracking-wide uppercase text-mute`
- Command text: `font-mono text-sm` with `tabular-nums`
- Banned: Inter, Helvetica, system default sans (no brand differentiation)

## 4. Component Stylings

### Command Row (Signature Component)
- **Default**: `flex items-center gap-3 px-3 py-2 rounded-lg text-ink bg-transparent`
- **Hover**: `bg-elevated` — subtle lift, no scale transform, 120ms ease-out
- **Focus** (keyboard): `bg-accent/15 text-accent ring-0` — full-row highlight, keyboard-driven
- **Active** (pressed): `bg-accent/25 scale-[0.99]` — 80ms spring
- **Disabled**: `opacity-40 cursor-not-allowed pointer-events-none`
- **Loading**: shimmer skeleton matching row height, no spinner flash

### Button (Primary)
- **Default**: `h-8 px-4 rounded-lg bg-accent text-white text-sm font-medium`
- **Hover**: `bg-accent brightness-110` — 150ms ease, no scale
- **Focus**: `ring-2 ring-accent/50 ring-offset-2 ring-offset-canvas`
- **Active**: `bg-accent/85 scale-[0.98]` — 80ms spring physics
- **Disabled**: `opacity-40 cursor-not-allowed`
- **Loading**: inline spinner (16px) left of label, label text preserved

### Search Input
- **Default**: `w-full bg-elevated border border-border rounded-lg px-4 py-2.5 text-sm text-ink placeholder:text-mute`
- **Hover**: `border-border/80` — marginal change
- **Focus**: `border-accent/60 ring-2 ring-accent/20 outline-none`
- **Active**: same as focus
- **Disabled**: `opacity-50 pointer-events-none`
- **Loading**: right-side spinner, input remains interactive

### Keyboard Shortcut Badge
- **Default**: `inline-flex items-center gap-0.5 px-1.5 py-0.5 rounded bg-elevated border border-border text-xs font-mono text-mute`
- **Hover**: `border-accent/40 text-ink`
- **Focus**: `ring-1 ring-accent`
- **Active**: `bg-accent/10`
- **Disabled**: `opacity-30`
- **Loading**: not applicable — static badge

## 5. Layout Principles

- **Command panel**: `max-w-2xl mx-auto` centered in viewport — fixed command interface pattern
- **Full-height container**: `min-h-[100dvh]` for root shell, avoiding iOS 100vh overflow bug
- **Result list**: `flex flex-col gap-px` — 1px gap between rows, no card borders
- **Sidebar** (extensions): fixed `240px` left, main content `flex-1`
- **Top bar**: `h-12` — compact header with breadcrumb navigation
- **Content padding**: `px-3 py-2` for list items, `px-6 py-4` for detail panels
- **Banned**: multi-column equal grids, decorative spacing, `h-screen`, hero sections

## 6. Depth & Elevation

- **Primary depth**: 1px border `border-border` replaces shadows — flat elevation model
- **Elevated surfaces**: `bg-elevated` color shift with `border border-border/60`
- **Modal/overlay**: `bg-surface backdrop-blur-xl border border-border rounded-2xl shadow-[0_24px_48px_rgba(0,0,0,0.5)]`
- **Inset highlight**: `shadow-[inset_0_1px_0_rgba(255,255,255,0.06)]` on panel tops
- **z-index**: sidebar=30, nav=40, command overlay=50, tooltip=60
- **Banned**: neon glow, colored shadow, `shadow-[0_0_30px_#5B7CF6]` outer glow (LILA BAN)

## 7. Motion & Interaction

- **Command palette entry**: `opacity 0→1` + `translateY(4px)→0`, 180ms `cubic-bezier(0.16, 1, 0.3, 1)`
- **Row selection**: background color only, 120ms ease-out — no layout shift
- **Panel slide**: `translateX` 200ms spring `stiffness: 120, damping: 22`
- **Keyboard feedback**: immediate (0ms delay) visual confirmation on focus move
- **Result stagger**: `delay: index * 20ms` for list mount, max 200ms total
- **GPU-only properties**: `transform`, `opacity` exclusively — no top/left animation
- **Reduced-motion**: all transitions collapse to `opacity` only, 80ms
- **Spring defaults**: `stiffness: 100, damping: 20` — snappy but not jarring

## 8. Responsive Behavior

- **Desktop-first**: Raycast is a macOS-native experience; web companion follows suit
- **Breakpoints**: desktop `≥1024px` primary, tablet `768–1023px` secondary, mobile `<768px` degraded
- **Command palette**: `max-w-2xl` on desktop, `max-w-full mx-2` on mobile
- **Touch targets**: minimum `44×44px` (iOS HIG) for all interactive elements on mobile
- **Typography scaling**: desktop `text-sm`, mobile stays `text-sm` (density preserved)
- **Sidebar**: hidden `<768px`, collapsible `768–1023px`, fixed `≥1024px`
- **Navigation**: desktop horizontal nav → mobile bottom sheet or hamburger drawer

## 9. Anti-Patterns (Project-Specific Banned)

- ❌ Bright purple/violet gradients — LILA BAN applied; calm indigo `#5B7CF6` replaces Raycast's vivid brand purple
- ❌ Light mode surfaces — Raycast is dark-only; forced light backgrounds break brand identity
- ❌ Decorative imagery, illustrations, or emoji as UI labels — launcher UI is text+icon only
- ❌ Scale-up hover transforms on list rows — Raycast uses color-only hover; scale breaks density
- ❌ Rounded pill buttons `rounded-full` — Raycast uses `rounded-lg` consistently
- ❌ Marketing hero sections — this system is for product UI, not landing pages

(Global anti-slop 50+ items are in `references/ai-tells-blocklist.md`)
