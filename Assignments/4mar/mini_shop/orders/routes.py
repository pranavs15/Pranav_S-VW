from flask import Blueprint

orders_bp = Blueprint("orders", __name__)

@orders_bp.route("/")
def orders_home():
    return "Orders page (Future implementation)"