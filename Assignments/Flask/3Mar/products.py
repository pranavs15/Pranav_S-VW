from flask import Flask, render_template, request

app = Flask(__name__)


products = [
    {"name": "Laptop", "category": "Electronics", "price": 1200, "available": True},
    {"name": "Mouse", "category": "Electronics", "price": 25, "available": True},
    {"name": "Keyboard", "category": "Electronics", "price": 45, "available": False},
    {"name": "Chair", "category": "Furniture", "price": 150, "available": True},
    {"name": "Table", "category": "Furniture", "price": 300, "available": False},
    {"name": "Notebook", "category": "Stationery", "price": 5, "available": True},
    {"name": "Pen", "category": "Stationery", "price": 2, "available": True},
]

@app.route("/products")
def list_products():
  
    category = request.args.get("category")
    availability = request.args.get("available")
    sort_order = request.args.get("sort")  # 'asc' or 'desc'

    filtered_products = products.copy()

 
    if category:
        filtered_products = [p for p in filtered_products if p["category"].lower() == category.lower()]


    if availability:
        if availability.lower() == "true":
            filtered_products = [p for p in filtered_products if p["available"]]
        elif availability.lower() == "false":
            filtered_products = [p for p in filtered_products if not p["available"]]

    if sort_order:
        reverse = True if sort_order.lower() == "desc" else False
        filtered_products.sort(key=lambda x: x["price"], reverse=reverse)

    total_count = len(filtered_products)

    return render_template("products.html", products=filtered_products, total_count=total_count)

if __name__ == "__main__":
    app.run(debug=True)