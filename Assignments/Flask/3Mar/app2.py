from flask import Flask, render_template

app = Flask(__name__)


names_list = ["Arun", "Amit", "Priya"]

@app.route("/names")
def show_names():
 
    upper_names = [name.upper() for name in names_list]
    return render_template("names.html", names=upper_names)

if __name__ == "__main__":
    app.run(debug=True)