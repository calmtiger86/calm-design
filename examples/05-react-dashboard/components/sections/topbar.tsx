"use client";

import { Menu, Search, Bell } from "lucide-react";
import { useAppStore } from "@/lib/stores/use-app-store";

export function Topbar() {
  const { toggleSidebar } = useAppStore();

  return (
    <header className="sticky top-0 z-30 h-16 flex items-center gap-4 px-4 md:px-6 bg-white/80 backdrop-blur-md border-b border-zinc-200">
      <button
        className="md:hidden p-2 -ml-2 hover:bg-zinc-100 rounded-lg"
        onClick={toggleSidebar}
        aria-label="메뉴 열기"
      >
        <Menu className="w-5 h-5" />
      </button>

      <div className="flex-1 max-w-md">
        <label htmlFor="topbar-search" className="sr-only">
          검색
        </label>
        <div className="relative">
          <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-zinc-400" />
          <input
            id="topbar-search"
            type="search"
            className="w-full h-9 pl-10 pr-12 rounded-md bg-zinc-100 text-sm placeholder:text-zinc-400 focus:outline-none focus:bg-white focus:ring-2 focus:ring-emerald-500/20 focus:border focus:border-emerald-500"
            placeholder="검색..."
          />
          <kbd className="hidden md:block absolute right-2 top-1/2 -translate-y-1/2 text-xs text-zinc-400 bg-white px-1.5 py-0.5 rounded border border-zinc-200">
            ⌘K
          </kbd>
        </div>
      </div>

      <button
        className="relative p-2 rounded-md hover:bg-zinc-100"
        aria-label="알림"
      >
        <Bell className="w-5 h-5" />
        <span className="absolute top-1.5 right-1.5 w-2 h-2 rounded-full bg-emerald-500" />
      </button>
    </header>
  );
}
