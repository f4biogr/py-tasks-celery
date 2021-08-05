from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task

def salve_do_fabio():
    return "Um salve do Fábio!"

app.conf.beat_schedule = {
    "run-every-ten-seconds": {
        "task": "tasks.salve_do_fabio",
        "schedule": 10.0
    }
}