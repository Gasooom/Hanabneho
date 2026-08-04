import axios from "axios";
import { ApiResponse } from "@/types/analysis";

const client = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_URL,
});

export async function analyzeReport(
  image: File,
  description: string
): Promise<ApiResponse> {
  const formData = new FormData();

  formData.append("image", image);
  formData.append("description", description);

  const response = await client.post(
    "/reports/analyze",
    formData
  );

  return response.data;
}

export async function createReport(
  title: string,
  description: string
) {
  const response = await client.post("/reports", {
    title,
    description,
  });

  return response.data;
}