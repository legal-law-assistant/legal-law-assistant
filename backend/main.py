
from uuid import uuid4

from fastapi import FastAPI
from fastapi.responses import JSONResponse

from schemas import AskRequest, AskResponse


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
    request_id = str(uuid4())

    # PHẢN HỒI MẪU:
    # Chưa gọi RAG, Agent hoặc Citation Validator.
    # Không sử dụng nội dung này làm câu trả lời pháp luật thật.
    response = AskResponse(
        answer=(
            "Đây là phản hồi mẫu để kiểm tra API. "
            "Hệ thống chưa truy xuất văn bản pháp luật "
            "và chưa xác minh trích dẫn."
        ),
        citations=[],
        citation_status="NOT_VALIDATED",
        request_id=request_id,
    )

    return JSONResponse(
        status_code=200,
        content=response.model_dump(),
    )
