from fastapi import FastAPI
from fastapi.responses import FileResponse
from exo_fin_gpt.exo_interface_api.exo_interface_api import router

app = FastAPI()
app.include_router(router)


@app.get('/health')
def health():
    return {'status': 'ok'}


@app.get('/openapi.yaml', include_in_schema=False)
def serve_openapi():
    """Serve the static OpenAPI specification for plugin use."""
    return FileResponse('openapi.yaml', media_type='text/yaml')


@app.get('/.well-known/ai-plugin.json', include_in_schema=False)
def serve_manifest():
    """Serve the plugin manifest for ChatGPT."""
    return FileResponse('.well-known/ai-plugin.json', media_type='application/json')
