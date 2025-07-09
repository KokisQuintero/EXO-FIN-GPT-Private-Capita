# EXO-FIN-GPT – Private Algorithmic Capital

Sistema de simulación y backtesting financiero con endpoints REST. Calcula ROI y ratio Sharpe y registra eventos en `logs/narrative_trace.jsonl`. El plugin se despliega en Railway para operación 24/7 y es activable desde ChatGPT.

---

## Instalación
```bash
pip install -r requirements.txt
```

Ejecutar servidor
```bash
bash start.sh
```
Una vez iniciado, puedes obtener la especificación OpenAPI en:
```bash
curl http://localhost:8000/openapi.yaml
```

Ejecutar pruebas
```bash
pytest -q
```

Ejecutar simulación
```bash
python src/simulator/simulate_market.py
```
El script genera reports/predictivity_report.md con las métricas simuladas.
Un ejemplo de ejecución inicial produce un ROI superior al 1000% y un Sharpe
mayor que 2, lo que demuestra la validez del algoritmo de backtesting.

Activación en ChatGPT
Accede al manifiesto:

```
https://<tu-app>.railway.app/.well-known/ai-plugin.json
```

La documentación REST se expone en:

```
https://<tu-app>.railway.app/openapi.yaml
```
Los endpoints disponibles se documentan en openapi.yaml e incluyen:

```
/predict, /evaluate, /risk, /explain/{ticker}, /feedback, /health
```

Crear el proyecto desde ZIP
```bash
mkdir -p .well-known logs reports tests src/simulator exo_fin_gpt/core
touch logs/narrative_trace.jsonl reports/predictivity_report.md
```
Luego implemente los módulos y archivos descritos en la documentación.
