from celery import Celery


app = Celery("tasks", broker="redis://localhost:6379/0")


@app.task
def example_task():
    return "Example Task Running"

@app.task
def example_task_2():
    return "Example Task 2 Running"


app.conf.beat_schedule = {
    "run-every-five-seconds": {"task": "tasks.example_task", "schedule": 5.0},
    "run-every-ten-seconds": {"task": "tasks.example_task_2", "schedule": 10.0}
}
