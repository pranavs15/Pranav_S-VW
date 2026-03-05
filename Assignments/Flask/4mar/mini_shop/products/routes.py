from flask import Blueprint, render_template, request, redirect, make_response
import json

products_bp = Blueprint("products", __name__)

# Dummy products
PRODUCTS = {
    "Laptop": 50000,
    "Mouse": 500,
    "Keyboard": 1000,
    "Headphones": 2000,
    "Monitor": 15000
}

@products_bp.route("/")
def show_products():
    return render_template("products.html", products=PRODUCTS)


@products_bp.route("/add/<product>")
def add_to_cart(product):
    cart = request.cookies.get("cart")

    if cart:
        cart = json.loads(cart)
    else:
        cart = {}

    cart[product] = cart.get(product, 0) + 1

    response = make_response(redirect("/cart"))
    response.set_cookie("cart", json.dumps(cart))

    return response