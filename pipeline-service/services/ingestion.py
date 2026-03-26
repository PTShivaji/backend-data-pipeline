import requests
from sqlalchemy.orm import Session
from models.customer import Customer
from datetime import datetime

FLASK_URL = "http://127.0.0.1:5000/api/customers"


def fetch_all_customers():
    page = 1
    all_data = []

    while True:
        res = requests.get(FLASK_URL, params={"page": page, "limit": 5})
        data = res.json()

        if not data["data"]:
            break

        all_data.extend(data["data"])
        page += 1

    return all_data


def upsert_customers(db: Session, customers):
    for c in customers:
        try:
            # Convert fields safely
            c["date_of_birth"] = datetime.strptime(c["date_of_birth"], "%Y-%m-%d").date()
            c["created_at"] = datetime.fromisoformat(c["created_at"])

            existing = db.query(Customer).filter_by(customer_id=c["customer_id"]).first()

            if existing:
                for key, value in c.items():
                    setattr(existing, key, value)
            else:
                db.add(Customer(**c))

        except Exception as e:
            print("Error processing record:", c["customer_id"], e)

    db.commit()