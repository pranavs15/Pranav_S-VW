from flask import Blueprint, request, redirect

hr_bp = Blueprint("hr", __name__)

@hr_bp.route("/dashboard")
def dashboard():
    role = request.cookies.get("user_role")

    if role != "hr":
        return redirect("/")

    username = request.cookies.get("username")

    return f"""
    <h2>HR Dashboard</h2>
    Welcome {username}<br><br>
    <a href="/logout">Logout</a>
    """