from pathlib import Path
from .io_utils import load_tasks


def main() -> None:
    # Lấy đường dẫn tuyệt đối đến file sample.csv nằm cùng thư mục w2
    sample_path = Path(__file__).parent / "sample.csv"
    print(f"--- Đang đọc dữ liệu từ: {sample_path.name} ---")
    
    try:
        tasks = load_tasks(sample_path)
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. Tiêu đề: {task.title} | Độ quan trọng: {task.importance} | Effort: {task.effort_h}h | Deadline: {task.deadline}")
    except Exception as err:
        print(f"Lỗi khi đọc file: {err}")


if __name__ == "__main__":
    main()
