"use client";

import { useEffect, useRef, useState } from "react";

import { analyzeReport } from "@/services/api";
import { AnalysisData } from "@/types/analysis";

type Props = {
  onAnalysisComplete: (analysis: AnalysisData) => void;
};

const steps = [
  {
    title: "Analyzing image",
    text: "Understanding infrastructure damage...",
  },
  {
    title: "Assessing severity",
    text: "Estimating impact and urgency...",
  },
  {
    title: "Selecting authority",
    text: "Finding the responsible organization...",
  },
  {
    title: "Generating report",
    text: "Preparing the AI assessment...",
  },
];

export default function UploadCard({
  onAnalysisComplete,
}: Props) {
  const inputRef = useRef<HTMLInputElement>(null);

  const [image, setImage] = useState<File | null>(null);
  const [imagePreview, setImagePreview] = useState<string | null>(null);
  const imageLabel = image?.name ?? "Selected image";
  const [description, setDescription] = useState("");
  const [loading, setLoading] = useState(false);
  const [step, setStep] = useState(0);

  useEffect(() => {
    if (!image) {
      setImagePreview(null);
      return;
    }

    const previewUrl = URL.createObjectURL(image);

    setImagePreview(previewUrl);

    return () => URL.revokeObjectURL(previewUrl);
  }, [image]);

  useEffect(() => {
    if (!loading) return;

    const interval = setInterval(() => {
      setStep((prev) =>
        prev < steps.length - 1 ? prev + 1 : prev
      );
    }, 900);

    return () => clearInterval(interval);
  }, [loading]);

  function handleFileChange(
    e: React.ChangeEvent<HTMLInputElement>
  ) {
    const file = e.target.files?.[0];

    if (file) {
      setImage(file);
    }

    e.target.value = "";
  }

  async function handleAnalyze() {
    if (!image) return;

    setStep(0);
    setLoading(true);

    try {
      const result = await analyzeReport(
        image,
        description
      );

      onAnalysisComplete(result.data);
    } catch (err: any) {
      console.error(err);

      if (err.response) {
        alert(
          err.response.data?.message ??
            JSON.stringify(err.response.data)
        );
      } else if (err.request) {
        alert(
          "Cannot connect to the backend. Make sure FastAPI is running."
        );
      } else {
        alert(err.message);
      }
    } finally {
      setLoading(false);
    }
  }

  return (
    <section className="mx-auto max-w-3xl">
      <div
        onClick={() => inputRef.current?.click()}
        className="cursor-pointer rounded-2xl border-2 border-dashed border-slate-300 bg-white p-10 text-center transition hover:border-blue-600"
      >
        {imagePreview ? (
          <div className="space-y-4">
            <div className="overflow-hidden rounded-2xl border border-slate-200 bg-slate-50">
              <img
                src={imagePreview}
                alt={imageLabel}
                className="h-72 w-full object-cover"
              />
            </div>

            <div>
              <h2 className="text-2xl font-bold">
                Upload Infrastructure Image
              </h2>

              <p className="mt-2 text-slate-500">
                {imageLabel}
              </p>
            </div>
          </div>
        ) : (
          <>
            <h2 className="text-2xl font-bold">
              Upload Infrastructure Image
            </h2>

            <p className="mt-2 text-slate-500">
              Click to choose an image
            </p>
          </>
        )}

        <input
          ref={inputRef}
          type="file"
          accept="image/*"
          className="hidden"
          onChange={handleFileChange}
        />
      </div>

      <textarea
        rows={4}
        value={description}
        onChange={(e) =>
          setDescription(e.target.value)
        }
        placeholder="Describe the damage..."
        className="mt-6 w-full rounded-xl border p-4"
      />

      <button
        onClick={handleAnalyze}
        disabled={!image || loading}
        className="mt-6 w-full rounded-xl bg-blue-600 py-3 font-semibold text-white transition hover:bg-blue-700 disabled:bg-slate-400"
      >
        {loading
          ? "Analyzing..."
          : "Analyze"}
      </button>

      {loading && (
        <div className="mt-8 rounded-2xl border bg-white p-6 shadow">
          <h3 className="mb-6 text-xl font-semibold">
            AI Analysis
          </h3>

          <div className="space-y-4">
            {steps.map((item, index) => (
              <div
                key={item.title}
                className={`rounded-xl border p-4 ${
                  index <= step
                    ? "border-blue-600 bg-blue-50"
                    : "border-slate-200"
                }`}
              >
                <h4 className="font-semibold">
                  {item.title}
                </h4>

                <p className="text-sm text-slate-600">
                  {item.text}
                </p>
              </div>
            ))}
          </div>
        </div>
      )}
    </section>
  );
}