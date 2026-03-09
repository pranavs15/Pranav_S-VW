from flask import Flask
from config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from models import db
from routes import setup_routes

app = Flask(__name__)

# Config
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLALCHEMY_TRACK_MODIFICATIONS

# Initialize database
db.init_app(app)

# Setup routes
setup_routes(app)

# Create tables if not exist
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)