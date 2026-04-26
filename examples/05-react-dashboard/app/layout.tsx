import type { Metadata } from "next";
import localFont from "next/font/local";
import "./globals.css";

const pretendard = localFont({
  src: "../public/fonts/PretendardVariable.woff2",
  display: "swap",
  weight: "45 920",
  variable: "--font-pretendard",
});

export const metadata: Metadata = {
  title: "calm-design React 예시 — SaaS 대시보드",
  description: "shadcn/ui + zustand + lucide-react를 활용한 React 모드 예시",
};

export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="ko" className={pretendard.variable}>
      <body className="font-sans antialiased bg-zinc-50 text-zinc-950">
        {children}
      </body>
    </html>
  );
}
