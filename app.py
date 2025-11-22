from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# database in the memory
todos = [
    {"id": 1, "task": "Finish Flask Task", "done": False},
    {"id": 2, "task": "Record Demo Video", "done": False}
]

# Route to GET all tasks
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify({"todos": todos})

# Route to ADD a new task
@app.route('/todos', methods=['POST'])
def add_todo():
    if not request.json or 'task' not in request.json:
        return jsonify({"error": "Task content is required"}), 400
    
    new_task = {
        "id": len(todos) + 1,
        "task": request.json['task'],
        "done": False
    }
    todos.append(new_task)

    return jsonify({"message": "Task added", "task": new_task}), 201

# Route to DELETE a task
@app.route('/todos/<int:task_id>', methods=['DELETE'])
def delete_todo(task_id):
    global todos
    # filter out the task with the given id
    todos = [t for t in todos if t['id'] != task_id]
    return jsonify({"message": "Task deleted"})

# Route to serve the frontend
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)