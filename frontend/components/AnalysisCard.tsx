import { AnalysisData } from "@/types/analysis";
import Link from "next/link";

type Props = {
  analysis: AnalysisData;
};

export default function AnalysisCard({
  analysis,
}: Props) {
  const confidence = Math.round(
    analysis.confidence * 100
  );

  const severityColor = {
    Critical: "bg-red-100 text-red-700",
    High: "bg-orange-100 text-orange-700",
    Medium: "bg-yellow-100 text-yellow-700",
    Low: "bg-green-100 text-green-700",
  }[analysis.severity] || "bg-slate-100 text-slate-700";

  return (
    <section className="mx-auto mt-10 max-w-4xl rounded-3xl bg-white p-8 shadow-xl">
      <div className="mb-8 border-b pb-6">
        <div className="flex items-center gap-3">
          <div className="flex h-12 w-12 items-center justify-center rounded-full bg-green-100 text-2xl">
            ✅
          </div>

          <div>
            <h2 className="text-3xl font-bold text-slate-900">
              Analysis Complete
            </h2>

            <p className="text-slate-500">
              Hanabneho AI has finished assessing the
              infrastructure damage.
            </p>
          </div>
        </div>
      </div>

      <div className="grid gap-6 md:grid-cols-2">
        <Card
          title="Category"
          value={analysis.category}
        />

        <div className="rounded-2xl border p-5">
          <h3 className="text-sm font-semibold uppercase text-slate-500">
            Severity
          </h3>

          <div
            className={`mt-4 inline-flex rounded-full px-4 py-2 font-semibold ${severityColor}`}
          >
            {analysis.severity}
          </div>
        </div>

        <div className="rounded-2xl border p-5">
          <h3 className="text-sm font-semibold uppercase text-slate-500">
            AI Confidence
          </h3>

          <p className="mt-4 text-4xl font-bold text-slate-900">
            {confidence}%
          </p>

          <div className="mt-4 h-3 overflow-hidden rounded-full bg-slate-200">
            <div
              className="h-full rounded-full bg-blue-600 transition-all"
              style={{
                width: `${confidence}%`,
              }}
            />
          </div>
        </div>

        <Card
          title="Recommended Authority"
          value={analysis.recommended_authority}
        />
      </div>

      <div className="mt-8 rounded-2xl border p-6">
        <h3 className="text-sm font-semibold uppercase text-slate-500">
          Summary
        </h3>

        <p className="mt-4 leading-8 text-slate-700">
          {analysis.summary}
        </p>
      </div>

      <div className="mt-6 rounded-2xl border p-6">
        <h3 className="text-sm font-semibold uppercase text-slate-500">
          AI Reasoning
        </h3>

        <p className="mt-4 leading-8 text-slate-700">
          {analysis.reasoning}
        </p>
      </div>

      <div className="mt-10 flex justify-end">
        <Link
          href="/dashboard"
          className="rounded-xl bg-blue-600 px-6 py-3 font-semibold text-white transition hover:bg-blue-700"
        >
          Open Dashboard →
        </Link>
      </div>
    </section>
  );
}

function Card({
  title,
  value,
}: {
  title: string;
  value: string;
}) {
  return (
    <div className="rounded-2xl border p-5">
      <h3 className="text-sm font-semibold uppercase text-slate-500">
        {title}
      </h3>

      <p className="mt-4 text-lg font-semibold text-slate-900">
        {value}
      </p>
    </div>
  );
}