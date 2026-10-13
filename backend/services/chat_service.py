
from uuid import uuid4

from backend.schemas import AskRequest, AskResponse


def answer_question(request: AskRequest) -> AskResponse:
    """Trả phản hồi mẫu cho API hỏi đáp.

    Chưa truy xuất dữ liệu pháp luật hoặc xác minh trích dẫn.
    """
    return AskResponse(
        answer=(
            "Đây là phản hồi mẫu để kiểm tra API. "
            "Hệ thống chưa truy xuất văn bản pháp luật "
            "và chưa xác minh trích dẫn."
        ),
        citations=[],
        citation_status="NOT_VALIDATED",
        request_id=str(uuid4()),
    )
