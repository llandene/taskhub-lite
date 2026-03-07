from backend.app import app

def test_get_tasks():
    client = app.test_client()
    response = client.get("/tasks")
    assert response.status_code == 200

def test_create_task():
    client = app.test_client()
    response = client.post("/tasks", json={"title": "Write tests"})
    assert response.status_code == 201

def test_complete_task():
    client = app.test_client()
    response = client.patch("/tasks/2")
    assert response.status_code == 200

def test_delete_task():
    client = app.test_client()
    response = client.delete("/tasks/3")
    assert response.status_code == 200