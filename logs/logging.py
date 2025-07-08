import json
import os
from datetime import datetime


def log_decision(event: dict) -> None:
    """Append event with timestamp to narrative trace."""
    event["timestamp"] = datetime.utcnow().isoformat()
    os.makedirs("logs", exist_ok=True)
    with open("logs/narrative_trace.jsonl", "a") as f:
        f.write(json.dumps(event) + "\n")
