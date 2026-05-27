from fastapi import FastAPI

app = FastAPI(
    title="Room API",
    description="Sala de Situação em Saúde do Município",
    version="0.1.0",
)


@app.get("/health")
async def health_check():
    return {"status": "ok"}
