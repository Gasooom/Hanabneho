import { DashboardReport } from "@/services/reports";
import ReportCard from "./ReportCard";

type Props = {
  reports: DashboardReport[];
};

export default function ReportsList({
  reports,
}: Props) {
  if (reports.length === 0) {
    return (
      <div className="mt-10 rounded-2xl bg-white p-10 text-center shadow-sm">
        <h2 className="text-xl font-semibold">
          No reports found
        </h2>

        <p className="mt-2 text-slate-500">
          There are no incidents for the selected authority.
        </p>
      </div>
    );
  }

  return (
    <div className="mt-10 grid gap-6">
      {reports.map((report) => (
        <ReportCard
          key={report.report_id}
          report={report}
        />
      ))}
    </div>
  );
}