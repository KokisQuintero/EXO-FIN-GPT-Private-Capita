# AGENTS.md — Agentes Cognitivos de EXO-FIN-GPT

## /predict
- Acción central de predicción.
- Devuelve: JSON con decisión, ROI esperado, confianza.

## /evaluate
- Calcula métricas ROI y Sharpe Ratio usando backtesting.

## /explain/{ticker}
- Explicación semántica del razonamiento de inversión.

## /feedback
- Procesa retroalimentación del usuario y mejora decisiones.

## /risk
- Estimación del drawdown y perfil de riesgo del activo.

## /health
- Verifica la salud del sistema y del servidor.

Cada agente se activa mediante un endpoint REST expuesto en OpenAPI y disponible en el manifiesto `.well-known/ai-plugin.json`.
