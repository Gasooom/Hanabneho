export interface AnalysisData {
  summary: string;
  category: string;
  severity: string;
  confidence: number;
  recommended_authority: string;
  reasoning: string;
}

export interface ApiResponse {
  success: boolean;
  message: string;
  data: AnalysisData;
}