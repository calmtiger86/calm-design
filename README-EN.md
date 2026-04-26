# calm-design

> **Premium designs that don't look AI-generated.** Korean-first but Korean-optional. A full-stack design agent skill.

[한국어 README](./README.md)

---

## ☕ What is calm-design?

LLM-based design tools tend to produce a recognizable "AI smell" — purple/blue gradients, Inter font, three equal cards in a row, "Elevate"/"Seamless" copy, pure black, neon glow shadows.

`calm-design` **explicitly blocks** these patterns and outputs **calm, refined designs** instead. In Korean environments, it enforces Pretendard. After generating a design, it inspects its own output and regenerates to fix violations.

### Combines 4 OSS strengths + 3 unique features

| Feature | awesome-design-md | stitch-skills | taste-skill | supanova | **calm-design** |
|---|:-:|:-:|:-:|:-:|:-:|
| 9-section DESIGN.md standard | ✅ | ✅ | ⚠️ | ⚠️ | ✅ |
| Prompt enhancement pipeline | ❌ | ✅ | ⚠️ | ⚠️ | ✅ |
| AI tells block + alternatives | ❌ | ⚠️ | ✅ | ✅ | ✅ (extended) |
| Dial parameters | ❌ | ❌ | 3-dial | 3-dial | **4-dial** |
| Pre-Flight Checklist | ❌ | ❌ | ✅ | ⚠️ | ✅ (21 items) |
| Korean typography standard | ❌ | ❌ | ❌ | ⚠️ | ✅ (deep) |
| **Visual self-critique loop** | ❌ | ❌ | ❌ | ❌ | **✅** |
| **Reference auto-matching** | ❌ | ❌ | ❌ | ❌ | **✅ (Phase 1+)** |
| **Multi-Variant generation** | ❌ | ❌ | ❌ | ❌ | **✅ (Phase 2+)** |

---

## 🚀 Quick Start

### Install

Anthropic Skills standard — works in:
- Claude Cowork (Claude desktop app)
- Claude Code (CLI)
- Cursor, Codex and other SKILL.md-compatible AI coding agents

```bash
# Claude Code
git clone https://github.com/min86k/calm-design .claude/skills/calm-design

# Or via Skills CLI
npx skills add https://github.com/min86k/calm-design
```

### First use

After installing, ask in natural language:

```
"Make me a B2B SaaS dashboard. Calm tone, data-heavy."
```

The skill automatically:
1. **Infers dials**: VARIANCE=4, MOTION=4, DENSITY=7, LANGUAGE=auto→en
2. **Generates 9-section DESIGN.md** → saved to `.calm-design/DESIGN.md`
3. **Outputs HTML + Tailwind CDN** code (lucide, Motion One integrated)
4. **Pre-Flight 21-item validation** + auto-regenerate until pass (max 3 retries)
5. **Returns 4 deliverables**:
   - DESIGN.md
   - Code (HTML or React)
   - Pre-Flight Report (✅/⚠️/❌)
   - Dial summary one-liner

---

## 📐 4-Dial Parameters

| Dial | Range | Default | Meaning |
|---|---|---|---|
| `DESIGN_VARIANCE` | 1–10 | 7 | 1=perfect symmetry, 10=asymmetric/artistic chaos |
| `MOTION_INTENSITY` | 1–10 | 6 | 1=static, 10=cinematic spring physics |
| `VISUAL_DENSITY` | 1–10 | 4 | 1=gallery-airy, 10=cockpit-dense |
| `LANGUAGE` | `ko`/`en`/`auto` | **`ko`** | Korean-first (Pretendard, word-break: keep-all enforced) |

**Natural-language dial control**: "more minimal", "more dynamic", "data-heavy", "trendy" auto-map to dial values.

---

## 🎯 5 Modes

| Mode | Trigger | Output | Status |
|---|---|---|---|
| **A. Generate** | "make me a design", "landing page" | DESIGN.md + code | ✅ |
| **B. Upgrade** | "polish this", "improve" + existing code | Diff + new DESIGN.md | ✅ |
| **C. Match-Reference** | "Toss style", "Linear-like" | Reference analysis + applied code | ✅ |
| **D. Multi-Variant** | "3 options", "varied" | 3 different DESIGN.md + comparison | ✅ |
| **JSON Spec** | "multiplatform", "web+mobile" | json-render format JSON | ✅ |

---

## 🛡️ 50+ Anti-Slop Auto-Block

calm-design auto-validates output and regenerates on detection:

| Category | Blocked (examples) |
|---|---|
| Fonts | Inter, Noto Sans KR, Roboto, font-thin/extralight (Korean) |
| Colors | Pure Black `#000000`, purple/blue AI gradients, saturation 80%+, multiple accents |
| Layout | 3-column equal cards, centered hero (VARIANCE≥5), `h-screen`, missing max-width |
| Copy | "Elevate", "Seamless", "Unleash", "John Doe", "Lorem ipsum", fabricated metrics |
| Motion | linear easing, top/left/width/height animations, useState-based animations |

Full 50+ list: [`references/ai-tells-blocklist.md`](./references/ai-tells-blocklist.md).

---

## 🇰🇷 Korean-First (but Korean-optional)

While `LANGUAGE=ko` is the default, calm-design fully supports English/global:

- Set `LANGUAGE=en` or natural-language English input → switches to Geist/Cabinet Grotesk
- All English mappings, anti-patterns, and references are bilingual
- README, examples, contribution guides exist in both languages

---

## 📦 8 Integrated Libraries

[shadcn/ui](https://ui.shadcn.com) · [lucide](https://lucide.dev) · [zustand](https://github.com/pmndrs/zustand) · [Framer Motion](https://www.framer.com/motion) · [Tailwind CSS](https://tailwindcss.com) · [Pretendard](https://pretendard.dev) · [Radix UI](https://www.radix-ui.com) · [Motion One](https://motion.dev)

Library policies are split per output engine. See [`library-policies/`](./library-policies/).

---

## 🎨 Examples

- [Korean B2B SaaS Dashboard](./examples/01-saas-dashboard-ko/)
- [AI Video Editing SaaS Landing (Toss-style inspired)](./examples/02-landing-toss-style/)
- [JSON Render Spec (Multiplatform)](./examples/03-json-render-spec/)
- [Preview Catalog](./examples/04-preview-catalog/)
- [Figma Export (Design Tokens)](./examples/05-figma-export/)

---

## 🛠️ Roadmap

| Phase | Scope | Status |
|---|---|:-:|
| **Phase 0 — MVP** | Mode A + HTML/React output + 30 anti-slop + self-critique (static analysis) | ✅ Done |
| **Phase 1 — Self-Critique full visual** | Playwright integration, Vision full capture, 30 Pre-Flight items | ✅ Done |
| **Phase 2 — Multi-Variant** | Mode D (3-variant generation) | ✅ Done |
| **Phase 3 — Reference Library** | KR 15 + Global 18 = 33 curated brands + Mode B/C | ✅ Done |
| **Phase 4 — Output Engine expansion** | preview-catalog + figma-export + json-render | ✅ Done |
| Phase 5 — Public Launch | GitHub release, official site, video demo | 🟡 In Progress |

---

## 📜 License

MIT. See [LICENSE](./LICENSE).

Reference library entries (Phase 3+) follow an "Inspired by" policy — no direct brand asset redistribution.

## 🤝 Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md). Korean keyword mappings, new anti-patterns, reference library additions, and translations all welcome.

## 🙏 Credits

Built on top of insights from:

- [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md)
- [google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills)
- [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)
- [uxjoseph/supanova-design-skill](https://github.com/uxjoseph/supanova-design-skill)

And huge thanks to [Pretendard](https://github.com/orioncactus/pretendard) · [shadcn/ui](https://ui.shadcn.com) · [lucide](https://lucide.dev).

---

**Made with ☕ by [@calmtiger_](https://threads.net/@calmtiger_)**
