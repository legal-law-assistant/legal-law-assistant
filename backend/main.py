


from fastapi import FastAPI

from backend.schemas import AskRequest, AskResponse
from backend.services.chat_service import answer_question



app = FastAPI(
    title="Legal Assistant API",
    description="Backend cho trợ lý tra cứu pháp luật",
    version="0.1.0",
)


# 1. Kiểm tra trạng thái hoạt động của Backend
@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "legal-assistant-backend",
    }


# 2. Trang gốc giới thiệu API
@app.get("/")
def home():
    return {
        "message": "Legal Assistant API is running",
        "docs": "/docs",
        "health": "/health",
    }


# 3. API hỏi đáp pháp luật
@app.post("/api/v1/ask", response_model=AskResponse)
def ask_question(request: AskRequest):
    return answer_question(request)