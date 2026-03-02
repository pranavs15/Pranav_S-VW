from flask import Flask, render_template, request

app = Flask(__name__)

users = [
    {"name": "Pranav", "position": "Developer", "salary": 80000},
    {"name": "Rohan", "position": "Manager", "salary": 90000},
    {"name": "Prasad", "position": "Designer", "salary": 70000},
    {"name": "Shubham", "position": "Tester", "salary": 60000},
]

@app.route("/dashboard")
def dashboard():
    # Get role from query parameter
    role = request.args.get("role", "Employee").capitalize()  # Default to Employee


    permissions = {
        "Admin": {
            "show_salary": True,
            "show_delete": True,
            "nav_links": ["Home", "Users", "Reports", "Settings"]
        },
        "Manager": {
            "show_salary": True,
            "show_delete": False,
            "nav_links": ["Home", "Team", "Reports"]
        },
        "Employee": {
            "show_salary": False,
            "show_delete": False,
            "nav_links": ["Home", "Profile"]
        }
    }

    role_permissions = permissions.get(role, permissions["Employee"])

    page_title = f"{role} Dashboard"

    return render_template(
        "dashboard.html",
        users=users,
        role=role,
        permissions=role_permissions,
        page_title=page_title
    )

if __name__ == "__main__":
    app.run(debug=True)