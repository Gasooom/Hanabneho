import { Report } from "@/types/report";

export const reports: Report[] = [
  {
    id: "REP-001",
    category: "Water Pipeline Failure",
    authority: "Municipal Water and Sewer Department",
    severity: "Critical",
    status: "Pending",
    confidence: 96,
  },
  {
    id: "REP-002",
    category: "Road Surface Collapse",
    authority: "Department of Public Works",
    severity: "High",
    status: "In Progress",
    confidence: 94,
  },
  {
    id: "REP-003",
    category: "Bridge Structural Damage",
    authority: "Bridge Maintenance Authority",
    severity: "Critical",
    status: "Pending",
    confidence: 98,
  },
  {
    id: "REP-004",
    category: "Electrical Pole Fire",
    authority: "Fire Department and Electrical Utility Company",
    severity: "Critical",
    status: "Resolved",
    confidence: 97,
  },
  {
    id: "REP-005",
    category: "Flooded Drainage System",
    authority: "Stormwater Management Department",
    severity: "Medium",
    status: "In Progress",
    confidence: 89,
  },
];