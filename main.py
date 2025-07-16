from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel

from exo_fin_gpt.core.backtesting import run_backtest
from logs.logging import log_decision

app = FastAPI()


class PriceSeries(BaseModel):
    prices: list[float]


@app.get("/health")
def health():
    return {'status': 'ok'}


@app.post('/predict')
def predict(data: PriceSeries):
    metrics = run_backtest(data.prices)
    log_decision({"event": "predict", "prices": data.prices, "metrics": metrics})
    return metrics


@app.get('/risk')
def risk():
    # Placeholder risk metric
    return {'risk': 'low'}


@app.get('/evaluate')
def evaluate():
    # Return last metrics from report if available
    try:
        with open('reports/predictivity_report.md') as f:
            content = f.read()
    except FileNotFoundError:
        content = 'No report available'
    return {'report': content}


@app.get("/openapi.yaml", include_in_schema=False)
def openapi_spec():
    return FileResponse("openapi.yaml", media_type="text/yaml")


@app.get("/.well-known/ai-plugin.json", include_in_schema=False)
def plugin_manifest():
    return FileResponse(".well-known/ai-plugin.json", media_type="application/json")
