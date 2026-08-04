import client from "./client";

export type DashboardReport = {
  report_id: string;
  title: string;
  description: string;
  category: string;
  severity: "Critical" | "High" | "Medium" | "Low";
  confidence: number;
  recommended_authority: string;
  status: string;
  created_at: string;
};

export async function getDashboardReports(): Promise<DashboardReport[]> {
  const response = await client.get("/reports/dashboard");

  return response.data.data;
}