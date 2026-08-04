"use client";

import { useEffect, useMemo, useState } from "react";

import DashboardHeader from "@/components/dashboard/DashboardHeader";
import StatsGrid from "@/components/dashboard/StatsGrid";
import AuthorityFilter from "@/components/dashboard/AuthorityFilter";
import ReportsList from "@/components/dashboard/ReportsList";

import {
  getDashboardReports,
  DashboardReport,
} from "@/services/reports";

const authorities = [
  "All Authorities",
  "Municipal Water and Sewer Department",
  "Department of Public Works",
  "Bridge Maintenance Authority",
  "Fire Department and Electrical Utility Company",
  "Stormwater Management Department",
];

export default function DashboardPage() {
  const [reports, setReports] = useState<DashboardReport[]>([]);
  const [loading, setLoading] = useState(true);

  const [selectedAuthority, setSelectedAuthority] =
    useState("All Authorities");

  useEffect(() => {
    async function loadReports() {
      try {
        const data = await getDashboardReports();
        setReports(data);
      } catch (error) {
        console.error(error);
      } finally {
        setLoading(false);
      }
    }

    loadReports();
  }, []);

  const filteredReports = useMemo(() => {
    if (selectedAuthority === "All Authorities") {
      return reports;
    }

    return reports.filter(
      (report) =>
        report.recommended_authority === selectedAuthority
    );
  }, [reports, selectedAuthority]);

  if (loading) {
    return (
      <main className="flex min-h-screen items-center justify-center">
        <h1 className="text-2xl font-semibold">
          Loading reports...
        </h1>
      </main>
    );
  }

  return (
    <main className="min-h-screen bg-slate-100">
      <div className="mx-auto max-w-7xl px-8 py-10">
        <DashboardHeader />

        <StatsGrid
          total={filteredReports.length}
          pending={
            filteredReports.filter(
              (r) => r.status === "Pending"
            ).length
          }
          critical={
            filteredReports.filter(
              (r) => r.severity === "Critical"
            ).length
          }
          resolved={filteredReports.filter(
            (r) => r.status === "Resolved"
          ).length}
        />

        <AuthorityFilter
          authorities={authorities}
          selected={selectedAuthority}
          onChange={setSelectedAuthority}
        />

        <ReportsList reports={filteredReports as any} />
      </div>
    </main>
  );
}