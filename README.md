# EXO-FIN-GPT – Private Algorithmic Capital

Sistema de simulación y backtesting financiero con endpoints REST. Calcula ROI y ratio Sharpe y registra eventos en `logs/narrative_trace.jsonl`. El plugin se despliega en Railway para operación 24/7 y es consumible desde ChatGPT.

## Instalación
```bash
pip install -r requirements.txt
```

### Ejecutar servidor
```bash
bash start.sh
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

La documentación REST se expone en:
```
https://<tu-app>.railway.app/openapi.yaml
```

Los endpoints disponibles se documentan en `openapi.yaml` e incluyen `/predict`, `/evaluate`, `/risk` y `/health`.

## Crear el proyecto desde el ZIP
1. Descomprimir el archivo `EXO-FIN-GPT-Private-Capital.zip` y entrar al directorio.
2. Crear la estructura base:
   ```bash
   mkdir -p .well-known logs reports tests src/simulator exo_fin_gpt/core
   touch logs/narrative_trace.jsonl reports/predictivity_report.md
   ```
3. Añadir el manifiesto `.well-known/ai-plugin.json` y `openapi.yaml` según este repositorio.
4. Implementar el módulo de backtesting en `exo_fin_gpt/core/backtesting.py` y el simulador en `src/simulator/simulate_market.py`.
5. Añadir el logger en `logs/logging.py` y los tests en `tests/test_endpoints.py`.
6. Configurar `start.sh`, `Procfile` y `requirements.txt` para despliegue en Railway.
7. Ejecutar `pytest` y `python src/simulator/simulate_market.py` para verificar que todo funciona.
