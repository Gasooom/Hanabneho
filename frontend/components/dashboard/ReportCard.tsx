import { DashboardReport } from "@/services/reports";

type Props = {
  report: DashboardReport;
};

function formatConfidence(confidence: number): string {
  const percentage = confidence <= 1 ? confidence * 100 : confidence;

  return `${Math.round(percentage)}%`;
}

export default function ReportCard({
  report,
}: Props) {
  return (
    <div className="rounded-2xl border bg-white p-6 shadow-sm">
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-2xl font-semibold">
            {report.category}
          </h2>
        </div>

        <span className="rounded-full bg-red-100 px-4 py-2 font-semibold text-red-700">
          {report.severity}
        </span>
      </div>

      <div className="mt-6 grid gap-4 md:grid-cols-3">
        <Info
          label="Authority"
          value={report.recommended_authority}
        />

        <Info
          label="Status"
          value={report.status}
        />

        <Info
          label="AI Confidence"
          value={formatConfidence(report.confidence)}
        />
      </div>

      <div className="mt-6 flex justify-end">
        <button className="rounded-xl bg-blue-600 px-5 py-2 font-semibold text-white hover:bg-blue-700">
          Open Report
        </button>
      </div>
    </div>
  );
}

function Info({
  label,
  value,
}: {
  label: string;
  value: string | number;
}) {
  return (
    <div>
      <p className="text-sm text-slate-500">
        {label}
      </p>

      <p className="font-medium">{value}</p>
    </div>
  );
}