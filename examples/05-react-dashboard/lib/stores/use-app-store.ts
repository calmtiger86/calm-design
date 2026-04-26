import { create } from "zustand";

interface AppStore {
  isSidebarOpen: boolean;
  toggleSidebar: () => void;
  closeSidebar: () => void;

  activeTab: string;
  setActiveTab: (tab: string) => void;
}

export const useAppStore = create<AppStore>((set) => ({
  isSidebarOpen: false,
  toggleSidebar: () => set((state) => ({ isSidebarOpen: !state.isSidebarOpen })),
  closeSidebar: () => set({ isSidebarOpen: false }),

  activeTab: "dashboard",
  setActiveTab: (tab) => set({ activeTab: tab }),
}));
