from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    error = ""
    email = ""
    password = ""

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if email == "" or password == "":
            error = "Fields should not be blank"

        elif "@" not in email:
            error = "Email should contain @"

        elif len(password) < 5 or len(password) > 8:
            error = "Password must be 5 to 8 characters"

        else:
            return "Form Submitted Successfully"

    return render_template("form.html",
                           error=error,
                           email=email,
                           password=password)

if __name__ == "__main__":
    app.run(debug=True)