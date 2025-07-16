import numpy as np


def run_backtest(prices):
    """Calculate ROI and annualized Sharpe ratio for a price series."""
    returns = np.diff(prices) / prices[:-1]
    roi = float((prices[-1] - prices[0]) / prices[0])
    # Verify ROI is a valid positive float
    assert isinstance(roi, float) and roi > 0, "Error: ROI inválido o nulo"
    sharpe = np.mean(returns) / np.std(returns) * np.sqrt(12)
    return {"roi": roi, "sharpe": sharpe}
