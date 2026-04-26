"use client";

import { Plus, TrendingUp, TrendingDown, UserPlus, CreditCard, MessageSquare } from "lucide-react";
import { Sidebar } from "@/components/sections/sidebar";
import { Topbar } from "@/components/sections/topbar";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { FadeUp } from "@/components/motion/fade-up";

const kpiData = [
  {
    label: "월 매출",
    value: "₩12,847,000",
    change: "+12.4%",
    trend: "up",
    span: 2,
  },
  {
    label: "활성 사용자",
    value: "8,431",
    subtext: "주간 평균",
    span: 1,
  },
  {
    label: "전환율",
    value: "3.2%",
    change: "-0.4%p",
    trend: "down",
    span: 1,
  },
];

const activities = [
  {
    icon: UserPlus,
    iconBg: "bg-emerald-50",
    iconColor: "text-emerald-600",
    text: "박지호님이 가입했습니다",
    time: "5분 전",
  },
  {
    icon: CreditCard,
    iconBg: "bg-zinc-100",
    iconColor: "text-zinc-600",
    text: "결제 완료 — Pro 플랜",
    time: "1시간 전",
  },
  {
    icon: MessageSquare,
    iconBg: "bg-zinc-100",
    iconColor: "text-zinc-600",
    text: "새 문의 접수",
    time: "2시간 전",
  },
];

export default function DashboardPage() {
  return (
    <div className="min-h-[100dvh] flex">
      <Sidebar />

      <div className="flex-1 flex flex-col min-w-0">
        <Topbar />

        <main className="flex-1 p-4 md:p-6 lg:p-8">
          {/* Page Header */}
          <FadeUp>
            <div className="flex items-end justify-between mb-8">
              <div>
                <h1 className="text-3xl font-bold tracking-tight">대시보드</h1>
                <p className="mt-1 text-sm text-zinc-500">2026년 4월 25일 기준</p>
              </div>
              <Button>
                <Plus className="w-4 h-4" />
                새로 만들기
              </Button>
            </div>
          </FadeUp>

          {/* KPI Bento Grid (비대칭 2-1-1) */}
          <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-8">
            {kpiData.map((kpi, index) => (
              <FadeUp key={kpi.label} delay={index * 0.05}>
                <Card className={kpi.span === 2 ? "md:col-span-2" : ""}>
                  <CardContent className="p-6">
                    <p className="text-xs font-medium tracking-wide text-zinc-500 uppercase">
                      {kpi.label}
                    </p>
                    <p className="mt-3 text-3xl font-semibold tabular">
                      {kpi.value}
                    </p>
                    {kpi.change && (
                      <p
                        className={`mt-2 text-xs flex items-center gap-1 ${
                          kpi.trend === "up" ? "text-emerald-600" : "text-red-600"
                        }`}
                      >
                        {kpi.trend === "up" ? (
                          <TrendingUp className="w-3.5 h-3.5" />
                        ) : (
                          <TrendingDown className="w-3.5 h-3.5" />
                        )}
                        <span className="tabular">{kpi.change}</span>
                        {kpi.trend === "up" && (
                          <span className="text-zinc-500">전월 대비</span>
                        )}
                      </p>
                    )}
                    {kpi.subtext && (
                      <p className="mt-2 text-xs text-zinc-500">{kpi.subtext}</p>
                    )}
                  </CardContent>
                </Card>
              </FadeUp>
            ))}
          </div>

          {/* Main Section: Chart + Recent Activity */}
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
            {/* Chart */}
            <FadeUp delay={0.15} className="lg:col-span-2">
              <Card>
                <CardContent className="p-6">
                  <div className="flex items-center justify-between mb-6">
                    <div>
                      <h2 className="text-base font-semibold tracking-tight">
                        매출 추이
                      </h2>
                      <p className="mt-1 text-xs text-zinc-500">최근 30일</p>
                    </div>
                    <div className="flex gap-1 text-xs">
                      <button className="px-3 py-1 rounded-md bg-zinc-100 font-medium">
                        30일
                      </button>
                      <button className="px-3 py-1 rounded-md text-zinc-500 hover:bg-zinc-50">
                        90일
                      </button>
                      <button className="px-3 py-1 rounded-md text-zinc-500 hover:bg-zinc-50">
                        1년
                      </button>
                    </div>
                  </div>

                  {/* Chart placeholder */}
                  <div className="h-64 flex items-end gap-1 border-b border-zinc-100">
                    {[40, 55, 50, 70, 85, 75, 95].map((height, i) => (
                      <div
                        key={i}
                        className="flex-1 bg-emerald-500 rounded-t transition-all duration-500"
                        style={{ height: `${height}%`, opacity: 0.3 + i * 0.1 }}
                      />
                    ))}
                  </div>
                  <div className="flex justify-between mt-2 text-xs text-zinc-500 tabular">
                    <span>4/19</span>
                    <span>4/21</span>
                    <span>4/23</span>
                    <span>4/25</span>
                  </div>
                </CardContent>
              </Card>
            </FadeUp>

            {/* Recent Activity */}
            <FadeUp delay={0.2}>
              <Card>
                <CardContent className="p-6">
                  <h2 className="text-base font-semibold tracking-tight mb-4">
                    최근 활동
                  </h2>
                  <ul className="space-y-4">
                    {activities.map((activity, index) => {
                      const Icon = activity.icon;
                      return (
                        <li key={index} className="flex gap-3">
                          <div
                            className={`w-8 h-8 rounded-full ${activity.iconBg} flex items-center justify-center shrink-0`}
                          >
                            <Icon className={`w-4 h-4 ${activity.iconColor}`} />
                          </div>
                          <div className="flex-1 min-w-0">
                            <p className="text-sm">{activity.text}</p>
                            <p className="text-xs text-zinc-500 mt-0.5">
                              {activity.time}
                            </p>
                          </div>
                        </li>
                      );
                    })}
                  </ul>
                </CardContent>
              </Card>
            </FadeUp>
          </div>
        </main>
      </div>
    </div>
  );
}
