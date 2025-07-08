# EXO-FIN-GPT – Private Algorithmic Capital

Sistema de simulación y backtesting financiero con endpoints REST. Calcula ROI y ratio Sharpe y registra eventos en `logs/narrative_trace.jsonl`. El plugin se despliega en Railway para operación 24/7 y es activable desde ChatGPT.

## Instalación
```bash
pip install -r requirements.txt
```

## Ejecutar pruebas
```bash
pytest -q
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

### Crear el proyecto desde ZIP
Descomprimir `EXO-FIN-GPT-Private-Capital.zip` y ejecutar:
```bash
mkdir -p .well-known logs reports tests src/simulator exo_fin_gpt/core
touch logs/narrative_trace.jsonl reports/predictivity_report.md
```
Luego implemente los módulos y archivos descritos en la documentación.
