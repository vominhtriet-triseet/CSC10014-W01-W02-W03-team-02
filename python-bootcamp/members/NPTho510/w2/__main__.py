from pathlib import Path
from .io_utils import load_tasks
from .errors import check_feasible, InfeasiblePlan

def main():
    sample_dir = Path(__file__).resolve().parents[3] / "samples"
    available_h = 10.0 #can be mannually changed

    for csv_path in sorted(sample_dir.glob("*.csv")):
        print(f"\nFile: {csv_path.name}")

        tasks = load_tasks(csv_path)

        try:
            check_feasible(tasks, available_h)
            print("The plan is feasible.")

        except InfeasiblePlan as error:
            print(error)

        for task in tasks:
            print(task)


if __name__ == "__main__":
    main()