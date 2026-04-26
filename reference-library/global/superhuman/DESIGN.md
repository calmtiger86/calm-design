# Design System: Inspired by Superhuman

> Source: calm-design 자체 작성 — "Inspired by" 정책. superhuman.com 공개 인터페이스 관찰 기반.
> LANGUAGE: en

## 1. Visual Theme & Atmosphere

Speed-obsessed email client for professionals who treat every second as capital. The interface disappears — a monochrome stage where your inbox is the only actor. Near-white surfaces on light mode, near-black on dark; in both cases the palette shrinks to near-nothing so keyboard shortcuts and message content dominate. No chrome, no decoration, no visual noise. The emotional register is calm confidence: unhurried typography, breathable line-height, and micro-interactions that confirm every keystroke without ceremony.

## 2. Color Palette & Roles

| Canvas  | `#FAFAFA` | Page background (light mode) — off-white, never pure white |
| Surface | `#FFFFFF` | Card and message panel background |
| Ink     | `#111114` | Body text and headlines — near-black, not pure black |
| Mute    | `#6B7280` | Metadata, timestamps, secondary labels |
| Border  | `#E5E7EB` | 1px dividers and separators |
| Accent  | `#EF4B58` | Superhuman red — focus ring, active badge, primary CTA |
| Dark Canvas | `#0E0E10` | Dark mode page background |
| Dark Surface | `#18181B` | Dark mode card and panel background |
| Success | `#16A34A` | Read receipts, sent confirmation |
| Neutral | `#374151` | Secondary interactive elements |

Rules: dual-mode (light default, dark supported), Pure Black `#000000` banned (use `#111114`), single red accent per Superhuman brand identity, saturations kept minimal except accent.

## 3. Typography Rules

- Family: `Cabinet Grotesk, system-ui, sans-serif` (Cabinet Grotesk for premium editorial feel — Inter banned)
- Monospace: `ui-monospace, SFMono-Regular` for keyboard shortcut display
- Display/H1: `text-2xl font-semibold tracking-tight leading-tight`
- Email subject: `text-base font-medium tracking-normal leading-snug`
- Body/Preview: `text-sm leading-relaxed max-w-[68ch]` — optimized for reading comfort
- Label/Meta: `text-xs text-mute tracking-wide`
- Keyboard shortcut: `font-mono text-xs px-1 py-0.5 rounded bg-border`
- Banned: Inter (no brand differentiation), Helvetica, Times/Georgia (inappropriate for email SaaS)

## 4. Component Stylings

### Email Row (Signature Component)
- **Default**: `flex items-start gap-4 px-6 py-3 border-b border-border bg-surface text-ink`
- **Hover**: `bg-[#F5F5F7]` subtle warmth shift — no transform, 100ms ease-out
- **Focus** (keyboard navigation): `ring-2 ring-accent ring-inset` full-row outline, keyboard-first
- **Active** (selected/open): `bg-accent/8 border-l-2 border-l-accent` — left stripe indicator
- **Disabled**: `opacity-50 cursor-not-allowed pointer-events-none`
- **Loading**: line-skeleton matching sender+subject+preview rows, fade shimmer 1.2s loop

### Button (Primary)
- **Default**: `h-9 px-5 rounded-lg bg-accent text-white text-sm font-medium tracking-tight`
- **Hover**: `bg-[#D93F4C]` — darker red, 150ms ease, no scale
- **Focus**: `ring-2 ring-accent/40 ring-offset-2 ring-offset-canvas`
- **Active**: `bg-[#C4384A] scale-[0.98]` — 80ms spring
- **Disabled**: `opacity-40 cursor-not-allowed bg-accent`
- **Loading**: 14px spinner left of label, label text preserved, no width shift

### Compose Input
- **Default**: `w-full bg-surface border-0 border-b border-border text-ink text-sm leading-relaxed outline-none resize-none`
- **Hover**: border-b color `#D1D5DB` — marginal reinforcement
- **Focus**: `border-b-2 border-b-accent` — bottom accent underline only, minimal ring
- **Active**: same as focus
- **Disabled**: `bg-[#F9FAFB] opacity-60 cursor-not-allowed`
- **Loading**: right-aligned spinner in toolbar row, input remains editable

### Command Palette (⌘K)
- **Default**: `max-w-xl bg-surface border border-border rounded-xl shadow-[0_8px_32px_rgba(0,0,0,0.12)]`
- **Hover** (on result row): `bg-[#F5F5F7]` row highlight
- **Focus** (keyboard): `bg-accent/8` row + left `2px` accent stripe
- **Active**: `bg-accent/12`
- **Disabled**: row `opacity-40`
- **Loading**: spinner centered in palette body, backdrop held

## 5. Layout Principles

- **Three-pane layout**: Sidebar `240px` + List `340px` + Detail `flex-1`
- **Full-height shell**: `min-h-[100dvh]` — avoids iOS 100vh overflow
- **Top bar**: `h-14` — thin command bar with search + keyboard hint display
- **Message list**: `divide-y divide-border` — border-only separation, no gap
- **Content max-width**: message body `max-w-3xl mx-auto px-8` for reading comfort
- **Grid**: CSS Grid for three-pane; Flexbox for toolbar and status rows only
- **Banned**: `h-screen` (iOS bug), equal three-column grids, full-bleed hero sections, heavy padding on list rows

## 6. Depth & Elevation

- **Minimal shadow philosophy**: depth expressed through color contrast and border, not shadow
- **Focused panel**: `shadow-[0_1px_4px_rgba(0,0,0,0.06)]` — barely perceptible lift
- **Modal/Command palette**: `shadow-[0_8px_32px_rgba(0,0,0,0.12)] rounded-xl border border-border`
- **Tooltip**: `shadow-[0_2px_8px_rgba(0,0,0,0.10)] rounded-lg bg-ink text-canvas text-xs`
- **Dark mode tint**: `shadow-[0_4px_16px_rgba(0,0,0,0.40)]` on elevated surfaces
- **z-index**: sidebar=30, topbar=40, modal=50, tooltip=60
- **Banned**: colored glow, neon shadow, `shadow-[0_0_20px_#EF4B58]` brand-color glow

## 7. Motion & Interaction

- **Email open**: `opacity 0→1` + `translateX(8px)→0`, 160ms `cubic-bezier(0.16, 1, 0.3, 1)`
- **Row hover**: background color only, 100ms ease-out — zero transform
- **Command palette**: `opacity 0→1` + `scale(0.97)→1`, 180ms spring `stiffness: 110, damping: 22`
- **Keyboard navigation**: zero delay — immediate visual response to ↑↓JK key presses
- **Send confirmation**: brief `translateY(-4px)` toast, 200ms in + 200ms out, 2s hold
- **Stagger entry** (list load): `delay: index * 30ms`, max 240ms total
- **GPU-only**: `transform` and `opacity` exclusively — no layout-triggering animation
- **Reduced-motion**: instant state change, `opacity` fade only at 60ms
- **Spring defaults**: `stiffness: 100, damping: 20` — professional, unhurried

## 8. Responsive Behavior

- **Desktop-first**: Superhuman is desktop email; full experience requires wide viewport
- **Breakpoints**: desktop `≥1280px` three-pane full, tablet `768–1279px` two-pane (list+detail), mobile `<768px` single-pane with back navigation
- **Touch targets**: `44×44px` minimum for all tappable elements
- **Typography**: desktop `text-sm`, tablet same, mobile `text-base` for readability
- **Sidebar**: fixed on desktop, hidden + drawer `<1024px`
- **Command palette**: `max-w-xl` desktop, `max-w-full mx-3` on mobile
- **Toolbar**: horizontal desktop → bottom-fixed row on mobile

## 9. Anti-Patterns (Project-Specific Banned)

- ❌ Decorative gradients or color washes — Superhuman palette is intentionally near-monochrome; color is reserved for accent only
- ❌ Card shadows on list rows — list items use `border-b` only; shadows break the flat document metaphor
- ❌ Animated loading spinners on every interaction — keyboard-first UX assumes instant response; spinners only for actual async operations >300ms
- ❌ Rounded pill buttons `rounded-full` — Superhuman uses `rounded-lg` for control elements; pill shape implies toggles
- ❌ Autoplaying animations in idle state — no perpetual motion; the interface is still when the user is not acting
- ❌ `overflow-hidden` on the message body container — long emails must scroll naturally; clipping breaks reader trust

(Global anti-slop 50+ items are in `references/ai-tells-blocklist.md`)
