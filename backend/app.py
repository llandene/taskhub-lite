from flask import Flask, request
from flask_cors import CORS
from shared import task_schema

app = Flask(__name__)
CORS(app)

tasks = [
    task_schema.create_task(1, "Set up project structure"),
    task_schema.create_task(2, "Build basic Flask API")
]

@app.get("/")
def home():
    return {"message": "TaskHub Lite API is running"}

@app.get("/tasks")
def get_tasks():
    return {"tasks": list_tasks()}

@app.post("/tasks")
def create_task_route():
    data = request.get_json()
    title = data["title"]
    task = add_task(title)
    return task, 201

@app.patch("/tasks/<int:task_id>")
def complete_task_route(task_id):
    task = complete_task(task_id)
    if task is None:
        return {"error": "Task not found"}, 404
    return task

@app.delete("/tasks/<int:task_id>")
def delete_task_route(task_id):
    task = delete_task(task_id)
    if task is None:
        return {"error": "Task not found"}, 404
    return task

# Core operations of the app:
# 1. list tasks
def list_tasks():
    return tasks
# 2. create task
def add_task(title):
    task_id = len(tasks) + 1
    task = task_schema.create_task(task_id, title)
    tasks.append(task)
    return task
# 3. complete task
def complete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            return task
    return None
# 4. delete task
def delete_task(task_id):
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            return tasks.pop(index) #pop remove elemento na lista na posicao indicada pelo indice
    return None