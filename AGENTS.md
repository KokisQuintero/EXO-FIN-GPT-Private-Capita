# AGENTS.md

Este archivo documenta los agentes semánticos, funciones deterministas y roles computacionales dentro de EXO-FIN-GPT.

## Agente: exo_fin_gpt.predict()
- Función: Proporciona predicciones financieras razonadas
- Estructura: Input → Análisis → JSON output (ROI, explicación)
- Traza: logs/narrative_trace.jsonl

## Agente: exo_fin_gpt.explain()
- Explica la predicción basada en eventos simulados o reales

## Agente: exo_fin_gpt.evaluate()
- Calcula ROI y Sharpe ratio con base en eventos previos simulados

## Agente: exo_fin_gpt.feedback()
- Registra comentarios del usuario para refinar el comportamiento

## Agente: exo_fin_gpt.risk()
- Analiza la exposición y drawdown esperado del portafolio

## Activación
- Manifest: `.well-known/ai-plugin.json`
- Descripción: `openapi.yaml`
- Hosting: Railway (FastAPI + Uvicorn)
