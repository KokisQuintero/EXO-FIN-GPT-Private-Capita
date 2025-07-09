from fastapi import APIRouter, FastAPI
from fastapi.responses import FileResponse
from exo_fin_gpt.core.backtesting import run_backtest
from logs.logging import log_event

router = APIRouter()

app = FastAPI()
app.include_router(router)

@app.get('/health')
def health():
    return {'status': 'ok'}

@app.get('/openapi.yaml', include_in_schema=False)
def serve_openapi():
    return FileResponse('openapi.yaml', media_type='text/yaml')

@app.get('/.well-known/ai-plugin.json', include_in_schema=False)
def serve_manifest():
    return FileResponse('.well-known/ai-plugin.json', media_type='application/json')

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
