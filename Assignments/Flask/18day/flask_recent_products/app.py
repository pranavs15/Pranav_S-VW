from flask import Flask
from flask_cors import CORS
from blueprints.auth import auth
from blueprints.products import products_bp

app = Flask(__name__)
CORS(app)
app.secret_key = "supersecretkey"

app.register_blueprint(auth)
app.register_blueprint(products_bp)

@app.route("/")
def home():
    return "Flask server is running!"

if __name__ == "__main__":
    app.run(debug=True)