from fastapi import FastAPI
from exo_fin_gpt.core.backtesting import run_backtest

app = FastAPI()


@app.get('/health')
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
