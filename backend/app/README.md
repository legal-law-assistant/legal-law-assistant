# Backend - Legal Assistant

## 1. Giới thiệu

Backend sử dụng FastAPI để cung cấp API cho hệ thống trợ lý tra cứu pháp luật.

**Trạng thái hiện tại:** API hỏi đáp đang sử dụng phản hồi mẫu (mock). Hệ thống chưa tích hợp RAG, Agent hoặc cơ chế xác minh trích dẫn pháp luật.

## 2. Yêu cầu

- Python đã được cài đặt.
- Các thư viện trong `backend/requirements.txt` đã được cài đặt.
- Đang làm việc tại thư mục gốc của repository.

## 3. Cài đặt môi trường

Tạo môi trường ảo nếu chưa có:

```powershell
python -m venv .venv
```

Kích hoạt môi trường ảo trên Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

Cài đặt thư viện:

```powershell
python -m pip install -r backend/requirements.txt
```

## 4. Chạy Backend

Tại thư mục gốc repository, chạy:

```powershell
python -m uvicorn backend.main:app --reload
```

Mặc định, API chạy tại `http://127.0.0.1:8000`.

## 5. Các endpoint

| Method | Endpoint | Mục đích |
|---|---|---|
| GET | `/` | Kiểm tra trang gốc |
| GET | `/health` | Kiểm tra trạng thái Backend |
| POST | `/api/v1/ask` | API hỏi đáp mẫu |

## 6. Kiểm tra bằng Swagger UI

Mở trình duyệt tại:

`http://127.0.0.1:8000/docs`

Chọn `POST /api/v1/ask`, nhấn **Try it out** và nhập:

```json
{
  "question": "Người lao động muốn đơn phương nghỉ việc thì phải báo trước bao nhiêu ngày?",
  "conversation_id": null
}
```

Nhấn **Execute** để kiểm tra phản hồi.

Phản hồi hiện tại chỉ phục vụ kiểm tra API, không phải tư vấn pháp luật thực tế.

## 7. Chạy kiểm thử

Tại thư mục gốc repository, chạy:

```powershell
python -m pytest -v
```

Kiểm tra các thư viện:

```powershell
python -m pip check
```

## 8. Cấu trúc chính

```text
backend/
├── main.py
├── schemas.py
├── README.md
├── services/
│   └── chat_service.py
└── tests/
    └── test_main.py
```

## 9. Lưu ý

- API hiện dùng phản hồi mẫu.
- `citations` đang là danh sách rỗng.
- `citation_status` là `NOT_VALIDATED`.
- Chưa được coi phản hồi mẫu là câu trả lời pháp luật đã xác minh.
- Đường dẫn API hiện tại là `/api/v1/ask`; mọi thay đổi cần phù hợp với hợp đồng API được nhóm thống nhất.