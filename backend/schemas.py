
from typing import Literal

from pydantic import BaseModel, Field, field_validator


# 1. Schema cho câu hỏi gửi lên Backend
class AskRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=1,
        max_length=2000,
        description="Câu hỏi pháp luật của người dùng",
        examples=[
            "Người lao động muốn đơn phương nghỉ việc thì phải báo trước bao nhiêu ngày?"
        ],
    )

    conversation_id: str | None = Field(
        default=None,
        description="Mã cuộc hội thoại, nếu có",
    )

    @field_validator("question")
    @classmethod
    def validate_question(cls, value: str) -> str:
        value = value.strip()

        if not value:
            raise ValueError("Câu hỏi không được để trống.")

        return value


# 2. Các trạng thái kiểm tra trích dẫn
CitationStatus = Literal[
    "NOT_VALIDATED",
    "VALID",
    "INVALID",
    "PARTIALLY_VALID",
]


# 3. Schema cho từng trích dẫn pháp luật
class Citation(BaseModel):
    document_name: str = Field(
        ...,
        description="Tên văn bản pháp luật",
    )

    document_number: str | None = Field(
        default=None,
        description="Số hiệu văn bản pháp luật",
    )

    article: str | None = Field(
        default=None,
        description="Điều được trích dẫn",
    )

    clause: str | None = Field(
        default=None,
        description="Khoản được trích dẫn",
    )

    point: str | None = Field(
        default=None,
        description="Điểm được trích dẫn",
    )

    url: str | None = Field(
        default=None,
        description="Đường dẫn đến văn bản nguồn",
    )

    excerpt: str = Field(
        ...,
        description="Đoạn nội dung được trích dẫn",
    )

    validation_status: CitationStatus = Field(
        default="NOT_VALIDATED",
        description="Trạng thái xác minh của trích dẫn",
    )


# 4. Schema cho kết quả trả về Frontend
class AskResponse(BaseModel):
    answer: str = Field(
        ...,
        description="Câu trả lời cho câu hỏi pháp luật",
    )

    citations: list[Citation] = Field(
        default_factory=list,
        description="Danh sách trích dẫn được sử dụng",
    )

    citation_status: CitationStatus = Field(
        default="NOT_VALIDATED",
        description="Trạng thái xác minh trích dẫn của câu trả lời",
    )

    request_id: str = Field(
        ...,
        description="Mã định danh của yêu cầu",
    )
