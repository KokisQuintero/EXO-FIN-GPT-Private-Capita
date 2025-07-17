# EXO-FIN-GPT – Private Algorithmic Capital

Sistema de simulación y backtesting financiero con endpoints REST. Calcula ROI y ratio Sharpe y registra eventos en `logs/narrative_trace.jsonl`. El plugin se despliega en Railway para operación 24/7 y es activable desde ChatGPT.
La especificacion OpenAPI esta disponible en `/openapi.yaml` para registrar el plugin.

---

## Instalación
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
Nota: el archivo `requirements.txt` instala todas las dependencias, incluido `httpx`, necesario para que las pruebas con `TestClient` funcionen correctamente.

Ejecutar servidor
```bash
bash start.sh
```
Una vez iniciado, verifica que la API responda:
```bash
curl http://localhost:8000/health
curl http://localhost:8000/openapi.yaml
curl http://localhost:8000/.well-known/ai-plugin.json
```
El archivo `openapi.yaml` también debe estar disponible en producción para poder registrar el plugin en ChatGPT.

Ejecutar pruebas
```bash
pytest -q
```
Si las pruebas indican "ModuleNotFoundError: httpx", ejecuta `pip install httpx`.

Ejecutar simulación
```bash
python src/simulator/simulate_market.py
```
El script genera `reports/predictivity_report.md` con las métricas simuladas.
Por ejemplo, una ejecución típica arroja un ROI cercano al 1071% con un Sharpe
de aproximadamente 11.16, validando así el algoritmo de backtesting.

Activación en ChatGPT
Accede al manifiesto:

```
https://<tu-app>.railway.app/.well-known/ai-plugin.json
```
Durante el desarrollo puedes verificarlo localmente con:

```
curl http://localhost:8000/.well-known/ai-plugin.json
```
Este archivo permite registrar el plugin en ChatGPT y debe estar disponible también en producción.
Para completar el registro abre la URL del manifiesto en tu navegador y sigue las instrucciones de ChatGPT.

La documentación REST se expone en:

```
https://<tu-app>.railway.app/openapi.yaml
```
Los endpoints disponibles se documentan en `openapi.yaml` e incluyen:

Tambien puedes consultarlo localmente en http://localhost:8000/openapi.yaml.
- `/predict` – Calcula ROI y Sharpe para una serie de precios
- `/evaluate` – Devuelve el informe de la última simulación
- `/risk` – Estima de forma sencilla el riesgo del portafolio
- `/health` – Comprueba que el servidor esté activo
- `/explain/{ticker}` – Ofrece una explicación narrativa
- `/feedback` – Registra comentarios para ajustar la estrategia

Verifica también que el manifiesto del plugin esté disponible en:

```bash
curl http://localhost:8000/.well-known/ai-plugin.json
```

Crear el proyecto desde ZIP
```bash
mkdir -p .well-known logs reports tests src/simulator exo_fin_gpt/core
touch logs/narrative_trace.jsonl reports/predictivity_report.md
```
Luego implemente los módulos y archivos descritos en la documentación.

En Railway configura la variable de entorno `PORT` (por ejemplo `8080`) para que
`start.sh` pueda exponer la API correctamente las 24 horas.

Para verificar el correcto funcionamiento de todos los endpoints puedes ejecutar:
```bash
pytest -q
```

Requisitos para validación GPT Plugin
✔️ `openapi.yaml` accesible
✔️ `ai-plugin.json` estructurado correctamente
✔️ `pytest -q` sin errores
✔️ `logs/narrative_trace.jsonl` generado por el simulador
✔️ Plugin registrado desde ChatGPT
