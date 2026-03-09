from flask import Blueprint, request, redirect

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/dashboard")
def dashboard():
    role = request.cookies.get("user_role")

    if role != "admin":
        return redirect("/")

    username = request.cookies.get("username")

    return f"""
    <h2>Admin Dashboard</h2>
    Welcome {username}<br><br>
    <a href="/logout">Logout</a>
    """