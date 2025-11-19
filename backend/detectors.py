"""
detectors.py
Placeholder anomaly detection models for invoice/transaction data.
Simulates scoring using IsolationForest / LOF-style logic.
"""

from typing import List
import random


def score_transactions(records: List[object]) -> List[float]:
    """
    This function simulates anomaly detection scoring.
    
    In a real implementation:
    - You would preprocess features (amount, vendor frequency, timing)
    - Train models like IsolationForest or Local Outlier Factor
    - Return anomaly scores between 0 and 1

    Here we simply return random scores for demonstration.
    """
    scores = []

    for r in records:
        # Fake anomaly scoring logic:
        base = len(r.vendor) / 100.0
        random_component = random.uniform(0, 1)

        score = (base + random_component) / 2
        scores.append(score)

    return scores
