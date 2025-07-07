import numpy as np
from exo_fin_gpt.core.backtesting import run_backtest
from logs.logging import log_decision


np.random.seed(42)
prices = [100]
for _ in range(12):
    prices.append(prices[-1] * (1 + np.random.normal(0.2, 0.1)))

metrics = run_backtest(np.array(prices))
log_decision({"event": "simulate_market", "prices": prices, "metrics": metrics})

with open("reports/predictivity_report.md", "w") as f:
    f.write(f"# Predictivity Report\n- ROI: {metrics['roi']:.2%}\n- Sharpe: {metrics['sharpe']:.2f}\n")
