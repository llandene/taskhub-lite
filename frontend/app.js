const apiUrl = "http://127.0.0.1:5000/tasks";
const taskForm = document.getElementById("task-form");
const taskTitleInput = document.getElementById("task-title");
const taskList = document.getElementById("task-list");

async function loadTasks() {
  const response = await fetch(apiUrl);
  const data = await response.json();
  taskList.innerHTML = "";
  data.tasks.forEach(renderTask);
}

function renderTask(task) {
  const li = document.createElement("li");
  li.textContent = task.done ? `✅ ${task.title}` : task.title;

  const completeButton = document.createElement("button");
  completeButton.textContent = "Complete";
  completeButton.onclick = async () => {
    await fetch(`${apiUrl}/${task.id}`, { method: "PATCH" });
    loadTasks();
  };

  const deleteButton = document.createElement("button");
  deleteButton.textContent = "Delete";
  deleteButton.onclick = async () => {
    await fetch(`${apiUrl}/${task.id}`, { method: "DELETE" });
    loadTasks();
  };

  li.append(" ", completeButton, " ", deleteButton);
  taskList.appendChild(li);
}

taskForm.addEventListener("submit", async (event) => {
  event.preventDefault();
  await fetch(apiUrl, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title: taskTitleInput.value })
  });
  taskTitleInput.value = "";
  loadTasks();
});

loadTasks();