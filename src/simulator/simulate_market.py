import os
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

os.makedirs("logs", exist_ok=True)
os.makedirs("reports", exist_ok=True)

import numpy as np
from exo_fin_gpt.core.backtesting import run_backtest
from logs.logging import log_decision


np.random.seed(42)
prices = [100]
for _ in range(12):
    prices.append(prices[-1] * (1 + np.random.normal(0.2, 0.1)))

metrics = run_backtest(np.array(prices))
log_decision({"event": "simulate_market", "metrics": metrics})

with open("reports/predictivity_report.md", "w") as f:
    f.write(f"# Predictivity Report\n- ROI: {metrics['roi']:.2%}\n- Sharpe: {metrics['sharpe']:.2f}\n")
