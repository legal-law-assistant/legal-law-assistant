from fastapi import FastAPI

app = FastAPI(
    title="Legal Assistant API",
    description="Backend cho trợ lý tra cứu pháp luật",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "legal-assistant-backend",
    }
@app.get("/")
def home():
    return {
        "message": "Legal Assistant API is running",
        "docs": "/docs",
        "health": "/health",
    }