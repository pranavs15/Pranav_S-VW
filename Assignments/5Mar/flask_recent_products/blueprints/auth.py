from flask import Blueprint, request, session, jsonify

auth = Blueprint("auth", __name__, url_prefix="/auth")

@auth.route("/login", methods=["GET","POST"])
def login():
    username = request.args.get("username")
    if not username:
        return {"error":"username required"},400

    session["username"] = username
    return {"message": f"Logged in as {username}"}