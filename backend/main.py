from fastapi import FastAPI
from typing import List
from pydantic import BaseModel

from detectors import score_transactions
from explainer import generate_explanation


app = FastAPI(
    title="Invoice / Transaction Anomaly Detection API",
    description="Scores invoices using anomaly detection models and generates LLM-style explanations.",
    version="1.0.0"
)


class Transaction(BaseModel):
    invoice_id: str
    vendor: str
    amount: float
    department: str
    date: str


class ScoredRecord(BaseModel):
    invoice_id: str
    anomaly_score: float
    is_anomalous: bool
    explanation: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/score_and_explain", response_model=List[ScoredRecord])
def score_and_explain(records: List[Transaction]):
    """
    Main endpoint for anomaly detection + explanation generation.
    """
    scores = score_transactions(records)
    results = []

    for record, score in zip(records, scores):
        is_anomalous = score > 0.95  # Example threshold
        explanation = generate_explanation(record, score, is_anomalous)

        results.append(
            ScoredRecord(
                invoice_id=record.invoice_id,
                anomaly_score=score,
                is_anomalous=is_anomalous,
                explanation=explanation
            )
        )

    return results
