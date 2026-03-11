from flask import Flask, request, render_template, redirect, url_for, session
from models import db, User, Employee
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated

def role_required(roles):
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            if session.get("role") not in roles:
                return "Access denied"
            return f(*args, **kwargs)
        return decorated
    return decorator

def setup_routes(app):

    @app.route("/login", methods=["GET","POST"])
    def login():
        if request.method=="POST":
            username = request.form["username"]
            password = request.form["password"]
            user = User.query.filter_by(username=username).first()
            if user and check_password_hash(user.password, password):
                session["user_id"] = user.id
                session["role"] = user.role
                return redirect(url_for("employees"))
            return "Invalid credentials"
        return render_template("login.html")

    @app.route("/employees")
    @login_required
    @role_required(["Admin","Manager"])
    def employees():
        all_employees = Employee.query.all()
        return render_template("employees.html", employees=all_employees)

    @app.route("/employee/<int:id>")
    @login_required
    def employee_view(id):
        employee = Employee.query.get(id)
        role = session.get("role")
        user_id = session.get("user_id")
        if role=="Employee" and user_id != id:
            return "Access denied"
        if role=="Manager" and employee.manager_id != user_id and employee.id != user_id:
            return "Access denied"
        return render_template("employee_view.html", employee=employee)

    @app.route("/employee/<int:id>/edit", methods=["GET","POST"])
    @login_required
    def employee_edit(id):
        employee = Employee.query.get(id)
        role = session.get("role")
        user_id = session.get("user_id")
        if role=="Employee" and user_id != id:
            return "Access denied"
        if role=="Manager" and employee.manager_id != user_id:
            return "Access denied"
        if request.method=="POST":
            employee.name = request.form["name"]
            employee.email = request.form["email"]
            employee.department = request.form["department"]
            db.session.commit()
            return redirect(url_for("employees"))
        return render_template("employee_edit.html", employee=employee)

    @app.route("/employee/<int:id>/delete", methods=["POST"])
    @login_required
    @role_required(["Admin"])
    def employee_delete(id):
        employee = Employee.query.get(id)
        db.session.delete(employee)
        db.session.commit()
        return redirect(url_for("employees"))