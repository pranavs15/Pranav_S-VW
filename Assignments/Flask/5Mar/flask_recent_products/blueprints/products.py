from flask import Blueprint, request, jsonify, session, make_response
from products_data import products

products_bp = Blueprint("products_bp", __name__, url_prefix="/products")

# Get all products
@products_bp.route("/", methods=["GET"])
def get_all_products():
    return jsonify(products)

# View product and update recently viewed products in cookie
@products_bp.route("/view/<int:product_id>", methods=["GET"])
def view_product(product_id):
    if "username" not in session:
        return jsonify({"error": "Login required"}), 401

    product = next((p for p in products if p["id"] == product_id), None)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    recent_cookie = request.cookies.get("recent_products")
    recent_products = [int(i) for i in recent_cookie.split(",")] if recent_cookie else []

    if product_id in recent_products:
        recent_products.remove(product_id)
    recent_products.append(product_id)

    if len(recent_products) > 5:
        recent_products = recent_products[-5:]

    resp = make_response(jsonify(product))
    resp.set_cookie("recent_products", ",".join(map(str, recent_products)))
    return resp

# Get recently viewed products
@products_bp.route("/recent", methods=["GET"])
def get_recent_products():
    recent_cookie = request.cookies.get("recent_products")
    recent_products_ids = [int(i) for i in recent_cookie.split(",")] if recent_cookie else []

    recent_products_details = []
    for pid in reversed(recent_products_ids):
        prod = next((p for p in products if p["id"] == pid), None)
        if prod:
            recent_products_details.append({"id": prod["id"], "name": prod["name"]})

    return jsonify(recent_products_details)