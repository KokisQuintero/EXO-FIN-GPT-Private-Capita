import numpy as np


def run_backtest(prices):
    """Calculate ROI and annualized Sharpe ratio for price series."""
    returns = np.diff(prices) / prices[:-1]
    roi = (prices[-1] - prices[0]) / prices[0]
    sharpe = np.mean(returns) / np.std(returns) * np.sqrt(12)
    return {"roi": roi, "sharpe": sharpe}
