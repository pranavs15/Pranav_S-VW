from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import csv
import io
import os

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

products = []

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/upload-products", methods=["POST"])
def upload_products():

    print("Request files:", request.files)
    print("Keys:", list(request.files.keys()))
    if 'file' in request.files:
        print("Filename:", request.files['file'].filename)
    # Debug: show received files
    print("Request files:", request.files)

    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400
    
    file = request.files['file']
    print("Filename received:", file.filename)

    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    # Save uploaded file
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    # Read CSV
    try:
        file.stream.seek(0)  # Reset stream to start
        stream = io.StringIO(file.read().decode("utf-8"), newline=None)
       
    except Exception as e:
        return jsonify({"error": f"Could not read file: {str(e)}"}), 400

    reader = csv.DictReader(stream)

    total_rows = 0
    products_added = 0
    failed_rows = 0

    for row in reader:
        total_rows += 1
        name = row.get("name", "").strip()
        price = row.get("price", "").strip()
        stock = row.get("stock", "").strip()

        # Validate row
        if not name:
            failed_rows += 1
            continue
        try:
            price = float(price)
            if price <= 0:
                failed_rows += 1
                continue
        except:
            failed_rows += 1
            continue
        try:
            stock = int(stock)
            if stock < 0:
                failed_rows += 1
                continue
        except:
            failed_rows += 1
            continue

        products.append({"name": name, "price": price, "stock": stock})
        products_added += 1

    return jsonify({
        "total_rows": total_rows,
        "products_added": products_added,
        "failed_rows": failed_rows
    }), 200

@app.route("/api/products", methods=["GET"])
def get_products():
    return jsonify(products), 200


if __name__ == "__main__":
    app.run(debug=True)