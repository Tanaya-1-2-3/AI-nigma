"use client";

export function ClassificationResult({ result }) {
  if (!result) return null;

  const confidencePct = (result.confidence * 100).toFixed(1);

  return (
    <div className="border border-border rounded-md p-4 bg-card">
      <h3 className="text-sm font-semibold mb-2">Classification Result</h3>
      <p><strong>Description:</strong> {result.description}</p>
      <p><strong>Category:</strong> {result.predicted_category || "Unknown"}</p>
      <p><strong>Amount:</strong> ₹{result.amount.toFixed(2)}</p>
      <p><strong>Confidence:</strong> {confidencePct}%</p>
      {confidencePct < 80 ? (
        <p className="text-xs text-destructive">Reasonably confident - verify if unsure</p>
      ) : (
        <p className="text-xs text-muted-foreground">High confidence</p>
      )}
    </div>
  );
}
