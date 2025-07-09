from fastapi import APIRouter
from exo_fin_gpt.core.backtesting import run_backtest
from logs.logging import log_event

router = APIRouter()

@router.post('/predict')
def predict(prices: list[float]):
    """Return ROI and Sharpe metrics for a list of prices."""
    metrics = run_backtest(prices)
    log_event({"event": "predict", "prices": prices, "metrics": metrics})
    return metrics

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
    log_event({"event": "explain", "ticker": ticker})
    return {"explanation": explanation}


@router.post('/feedback')
def feedback(note: dict):
    """Accept user feedback and log it."""
    log_event({"event": "feedback", "note": note})
    return {"status": "received"}
