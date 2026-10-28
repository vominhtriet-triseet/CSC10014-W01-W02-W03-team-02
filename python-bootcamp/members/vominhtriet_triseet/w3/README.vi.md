# Week 3 cá nhân — `vominhtriet_triseet`

Thư mục này hoàn thành W3-1 (`parse_due`), W3-2 (`analyse`), W3-3 (CLI) và W3-4 (type hints, docstrings, Ruff, kiểm thử).

## Chạy bài và kiểm tra

Mở terminal tại thư mục `python-bootcamp`:

```bash
python -m members.vominhtriet_triseet.w3.cli samples/tasks.csv --hours 2 --today 2026-10-26
python -m pytest members/vominhtriet_triseet/w3 -q
python -m ruff check members/vominhtriet_triseet/w3
```

CLI dùng `load_tasks` trong W2 cá nhân, cùng các hàm `prioritise` và `allocate` của study planner dùng chung. `--today` nhận ngày `YYYY-MM-DD`; nếu bỏ qua, CLI dùng ngày hiện tại. File không tồn tại, CSV rỗng/sai định dạng hoặc giờ học không hợp lệ sẽ in thông báo trên stderr và trả mã `1`.

## Nội dung bài

- `dates.py`: chấp nhận ngày ISO, `tomorrow`, `in N days` và tên đầy đủ/viết tắt của ngày trong tuần. Ngày trong tuần là lần xuất hiện kế tiếp; nếu trùng với hôm nay thì lấy tuần sau.
- `log_stats.py`: đếm request theo route, tính p95 theo nearest-rank và trả route có p95 cao nhất. Với input rỗng, trả `slowest: None`.
- `cli.py`: nhận file CSV, `--hours` và `--today`, rồi in kế hoạch học theo thứ tự ưu tiên.
- `test_w3.py`: kiểm tra phrase ngày, dữ liệu latency hợp lệ/không hợp lệ, p95, CLI thành công, file thiếu, CSV rỗng và tham số lỗi.

## Ghi chú cho PR

Trong mô tả PR, viết ba dòng bằng trải nghiệm thật của bạn về điểm khác nhau giữa Python và C++. Không dùng phần gợi ý nếu nó không đúng với điều bạn thực sự thấy khác biệt.
