from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from exo_fin_gpt.exo_interface_api.exo_interface_api import router

app = FastAPI()
app.include_router(router)

# serve manifest under well-known directory
app.mount("/.well-known", StaticFiles(directory=".well-known"), name="well-known")

@app.get("/openapi.yaml", include_in_schema=False)
def openapi_spec():
    """Serve the OpenAPI specification for plugin registration."""
    return FileResponse("openapi.yaml", media_type="text/yaml")

@app.get("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
