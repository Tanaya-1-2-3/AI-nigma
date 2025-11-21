import { NextResponse } from "next/server";

export async function POST(request) {
  try {
    const body = await request.json();
    const { description, amount } = body;

    if (!description || typeof description !== "string") {
      return NextResponse.json({ error: "Invalid description" }, { status: 400 });
    }
    if (amount === undefined || typeof amount !== "number") {
      return NextResponse.json({ error: "Invalid amount" }, { status: 400 });
    }

    const res = await fetch("http://127.0.0.1:8000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ description, amount }),
    });

    if (!res.ok) {
      const errText = await res.text();
      console.error("FastAPI error:", errText);
      return NextResponse.json({ error: "Failed to classify transaction" }, { status: 500 });
    }

    const data = await res.json();

    // Directly use the category returned by FastAPI
    const predicted_category = data.predicted_category || "Unknown";

    // Confidence is the probability of that category
    let confidence = 0;
    if (data.probabilities && predicted_category in data.probabilities) {
      confidence = data.probabilities[predicted_category];
    }

    return NextResponse.json({
      predicted_category,
      confidence,
      probabilities: data.probabilities || {},
    });

  } catch (error) {
    console.error("[route.js] Classification error:", error);
    return NextResponse.json({ error: "Failed to classify transaction" }, { status: 500 });
  }
}
