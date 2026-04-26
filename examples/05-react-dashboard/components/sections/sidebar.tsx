"use client";

import {
  LayoutDashboard,
  Users,
  BarChart3,
  CreditCard,
  Settings,
  X,
} from "lucide-react";
import { useAppStore } from "@/lib/stores/use-app-store";
import { cn } from "@/lib/utils";

const navItems = [
  { id: "dashboard", label: "대시보드", icon: LayoutDashboard },
  { id: "users", label: "사용자", icon: Users },
  { id: "analytics", label: "분석", icon: BarChart3 },
  { id: "billing", label: "결제", icon: CreditCard },
  { id: "settings", label: "설정", icon: Settings },
];

export function Sidebar() {
  const { isSidebarOpen, closeSidebar, activeTab, setActiveTab } = useAppStore();

  return (
    <>
      {/* Mobile Overlay */}
      {isSidebarOpen && (
        <div
          className="fixed inset-0 bg-black/20 backdrop-blur-sm z-40 md:hidden"
          onClick={closeSidebar}
        />
      )}

      {/* Sidebar */}
      <aside
        className={cn(
          "fixed md:static inset-y-0 left-0 z-50 w-60 shrink-0 flex flex-col border-r border-zinc-200 bg-white transition-transform duration-300 md:translate-x-0",
          isSidebarOpen ? "translate-x-0" : "-translate-x-full"
        )}
      >
        {/* Header */}
        <div className="h-16 flex items-center justify-between px-6 border-b border-zinc-200">
          <span className="font-bold text-lg">calm.io</span>
          <button
            className="md:hidden p-2 -mr-2 hover:bg-zinc-100 rounded-lg"
            onClick={closeSidebar}
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Navigation */}
        <nav className="flex-1 p-4 space-y-1">
          {navItems.map((item) => {
            const Icon = item.icon;
            const isActive = activeTab === item.id;

            return (
              <button
                key={item.id}
                onClick={() => {
                  setActiveTab(item.id);
                  closeSidebar();
                }}
                className={cn(
                  "w-full flex items-center gap-3 rounded-lg px-3 py-2 text-sm font-medium transition-colors",
                  isActive
                    ? "bg-zinc-100 text-zinc-900"
                    : "text-zinc-500 hover:bg-zinc-50 hover:text-zinc-900"
                )}
              >
                <Icon className="w-4 h-4" />
                {item.label}
              </button>
            );
          })}
        </nav>

        {/* User Profile */}
        <div className="p-4 border-t border-zinc-200">
          <div className="flex items-center gap-3">
            <img
              src="https://i.pravatar.cc/40?u=minseo"
              alt="김민서 프로필"
              className="w-8 h-8 rounded-full"
            />
            <div className="flex-1 min-w-0">
              <p className="text-sm font-medium truncate">김민서</p>
              <p className="text-xs text-zinc-500 truncate">관리자</p>
            </div>
          </div>
        </div>
      </aside>
    </>
  );
}
