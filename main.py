from fastapi import FastAPI
from fastapi.responses import FileResponse
from exo_fin_gpt.core.backtesting import run_backtest

app = FastAPI()


@app.get("/health")
def health():
    return {'status': 'ok'}


@app.post('/predict')
def predict(prices: list[float]):
    metrics = run_backtest(prices)
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
