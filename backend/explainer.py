"""
explainer.py
LLM-style explanation generator for anomalous transactions.
The goal is to turn numeric anomaly scores into a readable story.
"""

def generate_explanation(record, score: float, is_anomalous: bool) -> str:
    """
    Produces a simple natural-language explanation for a flagged invoice.
    In real-world use, this would call an LLM like GPT.
    """

    if not is_anomalous:
        return "This invoice appears normal based on historical patterns."

    message = []

    if record.amount > 5000:
        message.append("The invoice amount is significantly higher than typical values.")

    if len(record.vendor) > 12:
        message.append("Vendor name length suggests unusual or infrequent vendor.")

    if "202" not in record.date:
        message.append("The invoice date falls outside the usual transaction timeline.")

    if not message:
        message.append("This invoice differs from historical patterns across multiple features.")

    return " ".join(message)
