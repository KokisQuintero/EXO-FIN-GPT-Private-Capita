from fastapi import APIRouter
from exo_fin_gpt.core.backtesting import run_backtest

router = APIRouter()

@router.post('/predict')
def predict(prices: list[float]):
    """Return ROI and Sharpe metrics for a list of prices."""
    metrics = run_backtest(prices)
    return metrics

@router.get('/risk')
def risk():
    """Return a placeholder risk metric."""
    return {'risk': 'low'}

@router.get('/evaluate')
def evaluate():
    """Return contents of the latest report if available."""
    try:
        with open('reports/predictivity_report.md') as f:
            content = f.read()
    except FileNotFoundError:
        content = 'No report available'
    return {'report': content}
