# EXO-FIN-GPT – Private Algorithmic Capital

Sistema de simulación y backtesting financiero con endpoints REST. Calcula ROI y ratio Sharpe y registra eventos en `logs/narrative_trace.jsonl`. El plugin se despliega en Railway y es activable desde ChatGPT.

## Instalación
```bash
pip install -r requirements.txt
```

## Ejecutar simulación
```bash
python src/simulator/simulate_market.py
```
El script genera `reports/predictivity_report.md` con las métricas simuladas.

## Activación en ChatGPT
`https://<tu-app>.railway.app/.well-known/ai-plugin.json`

### API
Los endpoints están documentados en `openapi.yaml` y expuestos vía REST:
`/predict`, `/evaluate`, `/risk`, `/health`.

### Ejecución local
```bash
bash start.sh
```
