"use client";

import { useState } from "react";
import { Bar, Pie } from "react-chartjs-2";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  ArcElement,
  Tooltip,
  Legend,
} from "chart.js";

ChartJS.register(CategoryScale, LinearScale, BarElement, ArcElement, Tooltip, Legend);

export default function Page() {
  const [latestResult, setLatestResult] = useState(null);
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleClassify = async (formData) => {
    setLoading(true);
    try {
      const response = await fetch("/api/classify", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          description: formData.description,
          amount: formData.amount,
        }),
      });
      const data = await response.json();
      const classificationData = {
        ...data,
        description: formData.description,
        amount: formData.amount,
        confidence: Number(data.confidence) || 0,
      };
      setLatestResult(classificationData);
      setResults([classificationData, ...results]);
    } catch (err) {
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  // Bar chart
  const barData = latestResult
    ? {
        labels: Object.keys(latestResult.probabilities),
        datasets: [
          {
            label: "Probability",
            data: Object.values(latestResult.probabilities),
            backgroundColor: Object.keys(latestResult.probabilities).map((cat) =>
              cat === latestResult.predicted_category ? "#2563eb" : "#94a3b8"
            ),
          },
        ],
      }
    : null;

  const barOptions = {
    responsive: true,
    plugins: { legend: { display: false } },
    scales: { y: { beginAtZero: true, max: 1 } },
  };

  // Pie chart
  const pieData = results.length
    ? (() => {
        const categoryMap = {};
        results.forEach((r) => {
          categoryMap[r.predicted_category] = (categoryMap[r.predicted_category] || 0) + r.amount;
        });
        const labels = Object.keys(categoryMap);
        const data = Object.values(categoryMap);
        const colors = [
          "#2563eb", "#10b981", "#f59e0b", "#ef4444", "#8b5cf6",
          "#ec4899", "#14b8a6", "#f43f5e", "#22c55e", "#eab308"
        ];
        return {
          labels,
          datasets: [
            {
              data,
              backgroundColor: labels.map((_, i) => colors[i % colors.length]),
            },
          ],
        };
      })()
    : null;

  const pieOptions = {
    responsive: true,
    plugins: {
      legend: { position: "bottom" },
      tooltip: {
        callbacks: {
          label: function (ctx) {
            const total = ctx.dataset.data.reduce((a, b) => a + b, 0);
            const percent = ((ctx.raw / total) * 100).toFixed(1);
            return `${ctx.label}: ₹${ctx.raw.toFixed(2)} (${percent}%)`;
          },
        },
      },
    },
  };

  const confidenceColor = (confidence) => {
    if (confidence >= 0.8) return "bg-green-100 text-green-800";
    if (confidence >= 0.5) return "bg-yellow-100 text-yellow-800";
    return "bg-red-100 text-red-800";
  };

  return (
    <main className="min-h-screen bg-background p-6 flex flex-col items-center space-y-6">
      {/* Header */}
      <header className="w-full max-w-3xl text-center">
        <h1 className="text-3xl font-bold mb-2">💰 Smart Transaction Categorizer</h1>
        <p className="text-muted-foreground text-sm">
          Automatically classify your transactions and analyze spending patterns.
        </p>
      </header>

      {/* Form */}
      <form
        className="w-full max-w-md bg-card border border-border rounded-lg p-6 shadow-lg space-y-4"
        onSubmit={(e) => {
          e.preventDefault();
          const formData = {
            description: e.target.description.value,
            amount: parseFloat(e.target.amount.value),
          };
          handleClassify(formData);
        }}
      >
        <input
          type="text"
          name="description"
          placeholder="Transaction description"
          className="w-full border rounded p-2 focus:ring-2 focus:ring-primary focus:outline-none"
          required
        />
        <input
          type="number"
          name="amount"
          placeholder="Amount (₹)"
          className="w-full border rounded p-2 focus:ring-2 focus:ring-primary focus:outline-none"
          required
        />
        <button
          type="submit"
          className="w-full bg-primary text-white py-2 rounded font-semibold hover:bg-primary/90 transition"
        >
          {loading ? "Classifying..." : "Classify Transaction"}
        </button>
      </form>

      {/* Latest Result */}
      {latestResult && (
        <div className="w-full max-w-md bg-card border border-border rounded-lg shadow-lg p-6 space-y-4 animate-fade-in">
          <h3 className="text-xl font-bold">📊 Classification Result</h3>
          <p>
            <strong>Description:</strong> {latestResult.description}
          </p>
          <p>
            <strong>Category:</strong>{" "}
            <span className="text-primary font-semibold">{latestResult.predicted_category}</span>
          </p>
          <p>
            <strong>Amount:</strong> ₹{latestResult.amount.toFixed(2)}
          </p>
          <p>
            <strong>Confidence:</strong>{" "}
            <span className={`px-2 py-1 rounded ${confidenceColor(latestResult.confidence)}`}>
              {(latestResult.confidence * 100).toFixed(1)}%
            </span>
          </p>
          {latestResult.confidence < 0.8 && (
            <p className="text-xs text-red-500">⚠️ Low confidence - verify category!</p>
          )}

          {/* Bar chart */}
          {barData && (
            <div className="mt-4">
              <h4 className="text-sm font-semibold mb-1">Category Probabilities</h4>
              <Bar data={barData} options={barOptions} />
            </div>
          )}

          {/* Tip */}
          <div className="mt-3 p-3 bg-blue-50 border border-blue-200 rounded text-sm text-blue-800">
            💡 Tip: Regularly review low-confidence predictions to improve financial awareness.
          </div>
        </div>
      )}

      {/* Pie chart */}
      {pieData && results.length > 0 && (
        <div className="w-full max-w-md bg-card border border-border rounded-lg shadow-lg p-6">
          <h3 className="text-xl font-bold mb-2">💹 Spending Summary</h3>
          <Pie data={pieData} options={pieOptions} />
        </div>
      )}

      {/* Educational Section */}
      <div className="w-full max-w-3xl bg-gradient-to-r from-primary/20 to-accent/20 border border-border rounded-lg p-6 text-center text-sm space-y-2">
        <p>🎓 Did you know?</p>
        <p>Consistent categorization helps you budget better and detect overspending habits.</p>
        <p>Use the probability bars and pie chart to understand trends and prioritize savings.</p>
      </div>
    </main>
  );
}
