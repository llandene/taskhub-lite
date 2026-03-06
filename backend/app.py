from flask import Flask
from shared.task_schema import create_task

app = Flask(__name__)

tasks = [
    create_task(1, "Set up project structure"),
    create_task(2, "Build basic Flask API")
]

@app.get("/")
def home():
    return {"message": "TaskHub Lite API is running"}

@app.get("/tasks")
def get_tasks():
    return {"tasks": tasks}