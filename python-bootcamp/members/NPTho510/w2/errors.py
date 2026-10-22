class InfeasiblePlan(Exception):
    def __init__(self, needed_h: float, available_h: float):
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(str(self))

    def __str__(self):
        return (f"Plan is infeasible: need {self.needed_h} hours, but only {self.available_h} hours are available.")


def check_feasible(tasks, available_h):
    needed_h = sum(task.effort_h for task in tasks)

    if needed_h > available_h:
        raise InfeasiblePlan(needed_h, available_h)