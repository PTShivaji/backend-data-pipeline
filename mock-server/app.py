from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Load data from JSON file
with open("data/customers.json") as f:
    customers = json.load(f)


# Health check
@app.route("/api/health")
def health():
    return {"status": "ok"}


# Get customers with pagination
@app.route("/api/customers")
def get_customers():
    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", 10))

    start = (page - 1) * limit
    end = start + limit

    return jsonify({
        "data": customers[start:end],
        "total": len(customers),
        "page": page,
        "limit": limit
    })


# Get single customer
@app.route("/api/customers/<customer_id>")
def get_customer(customer_id):
    customer = next((c for c in customers if c["customer_id"] == customer_id), None)

    if not customer:
        return {"error": "Not found"}, 404

    return customer


if __name__ == "__main__":
    app.run(port=5000)