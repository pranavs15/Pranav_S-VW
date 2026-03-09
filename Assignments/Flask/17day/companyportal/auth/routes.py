from flask import Blueprint, render_template, request, redirect, make_response

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        role = request.form["role"]
        remember = request.form.get("remember")

        response = make_response(redirect(f"/{role}/dashboard"))

        if remember == "on":
            response.set_cookie("username", username, max_age=7*24*60*60)
            response.set_cookie("user_role", role, max_age=7*24*60*60)
        else:
            response.set_cookie("username", username)
            response.set_cookie("user_role", role)

        return response

    return render_template("login.html")


# ✅ LOGOUT ROUTE
@auth_bp.route("/logout")
def logout():
    response = make_response(redirect("/"))
    response.delete_cookie("username")
    response.delete_cookie("user_role")
    return response