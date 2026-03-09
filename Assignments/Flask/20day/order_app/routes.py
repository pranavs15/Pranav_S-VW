from flask import Flask, request, jsonify
from models import db, Order
from sqlalchemy import func

def setup_routes(app):

    # Add an order
    @app.route("/orders", methods=["POST"])
    def add_order():
        data = request.get_json()
        product_name = data.get("product_name")
        quantity = data.get("quantity")
        price = data.get("price")

        if not product_name or quantity is None or price is None:
            return jsonify({"error": "All fields are required"}), 400

        order = Order(product_name=product_name, quantity=quantity, price=price)
        db.session.add(order)
        db.session.commit()
        return jsonify({"message": "Order added", "order_id": order.id}), 201

    # Display all orders with revenue per order
    @app.route("/orders", methods=["GET"])
    def list_orders():
        orders = Order.query.all()
        result = []
        for o in orders:
            revenue = o.price * o.quantity
            result.append({
                "id": o.id,
                "product_name": o.product_name,
                "quantity": o.quantity,
                "price": o.price,
                "revenue": revenue
            })
        return jsonify(result)

    # Display total revenue
    @app.route("/orders/total_revenue", methods=["GET"])
    def total_revenue():
        total = db.session.query(func.sum(Order.price * Order.quantity)).scalar() or 0
        return jsonify({"total_revenue": total})

    # Display orders where revenue > 2000
    @app.route("/orders/high_revenue", methods=["GET"])
    def high_revenue():
        orders = Order.query.all()
        result = []
        for o in orders:
            revenue = o.price * o.quantity
            if revenue > 2000:
                result.append({
                    "id": o.id,
                    "product_name": o.product_name,
                    "quantity": o.quantity,
                    "price": o.price,
                    "revenue": revenue
                })
        return jsonify(result)