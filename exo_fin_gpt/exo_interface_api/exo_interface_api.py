from fastapi import APIRouter
from exo_fin_gpt.core.backtesting import run_backtest
from logs.logging import log_decision

router = APIRouter()

@router.post('/predict')
def predict(prices: list[float]):
    """Return ROI and Sharpe metrics for a list of prices."""
    metrics = run_backtest(prices)
    log_decision({"event": "predict", "prices": prices, "metrics": metrics})
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


@router.get('/explain/{ticker}')
def explain(ticker: str):
    """Return a placeholder explanation for a given ticker."""
    explanation = f"Analysis of {ticker}: strategy based on simulated data."
    log_decision({"event": "explain", "ticker": ticker})
    return {"explanation": explanation}


@router.post('/feedback')
def feedback(note: dict):
    """Accept user feedback and log it."""
    log_decision({"event": "feedback", "note": note})
    return {"status": "received"}
