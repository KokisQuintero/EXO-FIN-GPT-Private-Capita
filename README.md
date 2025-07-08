# EXO-FIN-GPT – Private Algorithmic Capital

Sistema de simulación y backtesting financiero con endpoints REST. Calcula ROI y ratio Sharpe y registra eventos en `logs/narrative_trace.jsonl`. El plugin se despliega en Railway para operación 24/7 y es consumible desde ChatGPT.

## Instalación
```bash
pip install -r requirements.txt
```

### Ejecutar pruebas
```bash
pytest -q
```

## Ejecutar simulación
```bash
python src/simulator/simulate_market.py
```

## Activación desde ChatGPT
Accede al manifiesto:
```
https://<tu-app>.railway.app/.well-known/ai-plugin.json
```

Los endpoints disponibles se documentan en `openapi.yaml` e incluyen `/predict`, `/evaluate`, `/risk` y `/health`.
