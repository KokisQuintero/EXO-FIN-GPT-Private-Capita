import json
from datetime import datetime, timezone
from pathlib import Path

LOG_DIR = Path(__file__).resolve().parent


def log_event(event: dict) -> None:
    """Append an event with timestamp to the JSONL trace."""
    event["timestamp"] = datetime.now(timezone.utc).isoformat()
    with open(LOG_DIR / "narrative_trace.jsonl", "a") as f:
        f.write(json.dumps(event) + "\n")
