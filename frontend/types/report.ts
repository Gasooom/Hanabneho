export type Report = {
  id: string;
  category: string;
  authority: string;
  severity: "Critical" | "High" | "Medium" | "Low";
  status: "Pending" | "In Progress" | "Resolved";
  confidence: number;
};