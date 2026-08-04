"use client";

import { useState } from "react";

import AnalysisCard from "@/components/AnalysisCard";
import UploadCard from "@/components/UploadCard";
import { AnalysisData } from "@/types/analysis";

export default function ReportPage() {
  const [analysis, setAnalysis] = useState<AnalysisData | null>(null);

  return (
    <main className="min-h-screen bg-slate-100">
      <div className="mx-auto max-w-5xl px-6 py-10">
        <header className="mb-10 flex items-center justify-between">
          <div>
            <h1 className="text-4xl font-bold text-slate-900">
              Hanabneho
            </h1>

            <p className="mt-2 text-slate-600">
              Rebuilding Communities with Artificial Intelligence
            </p>
          </div>
        </header>

        <UploadCard onAnalysisComplete={setAnalysis} />

        {analysis && <AnalysisCard analysis={analysis} />}
      </div>
    </main>
  );
}