from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@localhost/task_manager"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    priority = db.Column(db.String(20), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())


@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.json
    task = Task(title=data["title"], priority=data["priority"])
    db.session.add(task)
    db.session.commit()
    return jsonify({"message": "Task created"})


@app.route("/tasks", methods=["GET"])
def get_tasks():
    priority = request.args.get("priority")
    completed = request.args.get("completed")

    query = Task.query

    if priority:
        query = query.filter_by(priority=priority)

    if completed:
        query = query.filter_by(completed=(completed.lower()=="true"))

    tasks = query.order_by(Task.created_at.desc()).all()

    result = []
    for t in tasks:
        result.append({
            "id": t.id,
            "title": t.title,
            "priority": t.priority,
            "completed": t.completed,
            "created_at": t.created_at
        })

    return jsonify(result)


@app.route("/tasks/<int:id>/toggle", methods=["PUT"])
def toggle_task(id):
    task = Task.query.get(id)
    task.completed = not task.completed
    db.session.commit()
    return jsonify({"message": "Task updated"})


@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted"})


if __name__ == "__main__":

    with app.app_context():
        db.create_all()
    app.run(debug=True)