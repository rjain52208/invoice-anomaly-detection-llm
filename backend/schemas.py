"""
schemas.py
Shared Pydantic models for transactional data and responses.
"""

from pydantic import BaseModel
from typing import Optional


class TransactionModel(BaseModel):
    invoice_id: str
    vendor: str
    amount: float
    department: str
    date: str


class AnomalyResult(BaseModel):
    invoice_id: str
    anomaly_score: float
    is_anomalous: bool
    explanation: Optional[str]
