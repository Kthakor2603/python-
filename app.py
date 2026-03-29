from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# In-memory list to store tasks
tasks = []
next_id = 1

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def add_task():
    global next_id
    data = request.get_json()
    task_text = data.get("task", "").strip()

    if not task_text:
        return jsonify({"error": "Task cannot be empty!"}), 400

    task = {
        "id": next_id,
        "task": task_text,
        "done": False
    }
    tasks.append(task)
    next_id += 1
    return jsonify(task), 201

@app.route("/tasks/<int:task_id>/done", methods=["PUT"])
def mark_done(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = not task["done"]
            return jsonify(task)
    return jsonify({"error": "Task not found!"}), 404

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(i)
            return jsonify({"message": "Task deleted!"})
    return jsonify({"error": "Task not found!"}), 404

if __name__ == "__main__":
    app.run(debug=True)
