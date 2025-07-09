import json
from datetime import datetime, timezone


def log_decision(event: dict) -> None:
    """Append event with timestamp to narrative trace."""
    event["timestamp"] = datetime.now(timezone.utc).isoformat()
    with open("logs/narrative_trace.jsonl", "a") as f:
        f.write(json.dumps(event) + "\n")
