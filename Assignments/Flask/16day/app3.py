from flask import Flask, render_template

app = Flask(__name__)

# Hardcoded list of students
students = [
    {"name": "Pranav", "marks": 80},
    {"name": "Rohan", "marks": 70},
    {"name": "Prasad", "marks": 45},
    {"name": "Shubham", "marks": 55}
]

@app.route("/students")
def show_students():
    return render_template("students.html", students=students)

if __name__ == "__main__":
    app.run(debug=True)