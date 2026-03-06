from flask import Blueprint, request, redirect

employee_bp = Blueprint("employee", __name__)

@employee_bp.route("/dashboard")
def dashboard():
    role = request.cookies.get("user_role")

    if role != "employee":
        return redirect("/")

    username = request.cookies.get("username")

    return f"""
    <h2>Employee Dashboard</h2>
    Welcome {username}<br><br>
    <a href="/logout">Logout</a>
    """