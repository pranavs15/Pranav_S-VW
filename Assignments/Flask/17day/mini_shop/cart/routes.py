from flask import Blueprint, request, render_template, redirect, make_response
import json

cart_bp = Blueprint("cart", __name__)

PRODUCTS = {
    "Laptop": 50000,
    "Mouse": 500,
    "Keyboard": 1000,
    "Headphones": 2000,
    "Monitor": 15000
}

@cart_bp.route("/")
def view_cart():
    cart = request.cookies.get("cart")

    if not cart:
        return "Your cart is empty"

    cart = json.loads(cart)

    total = 0
    for item, qty in cart.items():
        total += PRODUCTS[item] * qty

    return render_template("cart.html", cart=cart, prices=PRODUCTS, total=total)


@cart_bp.route("/increase/<product>")
def increase(product):
    cart = json.loads(request.cookies.get("cart"))
    cart[product] += 1

    response = make_response(redirect("/cart"))
    response.set_cookie("cart", json.dumps(cart))
    return response


@cart_bp.route("/decrease/<product>")
def decrease(product):
    cart = json.loads(request.cookies.get("cart"))

    if cart[product] > 1:
        cart[product] -= 1
    else:
        del cart[product]

    response = make_response(redirect("/cart"))
    response.set_cookie("cart", json.dumps(cart))
    return response


@cart_bp.route("/clear")
def clear_cart():
    response = make_response(redirect("/cart"))
    response.delete_cookie("cart")
    return response