"use client";

import { useState } from "react";
import Link from "next/link";

import UploadCard from "@/components/UploadCard";
import AnalysisCard from "@/components/AnalysisCard";

import { AnalysisData } from "@/types/analysis";

export default function Home() {
  const [analysis, setAnalysis] =
    useState<AnalysisData | null>(null);

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

          <Link
            href="/dashboard"
            className="rounded-xl bg-slate-900 px-5 py-3 font-semibold text-white transition hover:bg-slate-800"
          >
            Dashboard
          </Link>
        </header>

        <UploadCard
          onAnalysisComplete={setAnalysis}
        />

        {analysis && (
          <>
            <AnalysisCard
              analysis={analysis}
            />

            <div className="mt-8 text-center">
              <Link
                href="/dashboard"
                className="inline-block rounded-xl bg-blue-600 px-8 py-4 font-semibold text-white transition hover:bg-blue-700"
              >
                Open Dashboard
              </Link>
            </div>
          </>
        )}
      </div>
    </main>
  );
}