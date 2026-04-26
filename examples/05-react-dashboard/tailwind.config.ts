import type { Config } from "tailwindcss";

export default {
  content: [
    "./app/**/*.{ts,tsx}",
    "./components/**/*.{ts,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ["var(--font-pretendard)", "system-ui", "sans-serif"],
      },
      colors: {
        ink: "hsl(var(--ink))",
        mute: "hsl(var(--mute))",
      },
    },
  },
  plugins: [],
} satisfies Config;
