# Backend Data Pipeline Assignment

## Overview
This project implements a data pipeline using:
- Flask (Mock API)
- FastAPI (Ingestion Service)
- SQLite/PostgreSQL (Database)
- Docker (Containerization)

Flow:
Flask → FastAPI → Database → API Response

---

## Setup Instructions

### 1. Run Flask Server
cd mock-server
python app.py

### 2. Run FastAPI Server
cd pipeline-service
python -m uvicorn main:app --reload

---

## API Endpoints

### Flask (Mock Server)
- GET /api/customers?page=1&limit=5
- GET /api/customers/{id}
- GET /api/health

### FastAPI (Pipeline Service)
- POST /api/ingest
- GET /api/customers?page=1&limit=5
- GET /api/customers/{id}

---

## Testing

1. Start Flask server (port 5000)
2. Start FastAPI server (port 8000)
3. Open:
   http://127.0.0.1:8000/docs

4. Run:
   POST /api/ingest

5. Fetch data:
   GET /api/customers

---

## Features Implemented
- Pagination
- Data ingestion from external API
- Upsert logic
- REST APIs
- Database integration

---

## Tech Stack
- Python
- Flask
- FastAPI
- SQLAlchemy
- SQLite/PostgreSQL
- Docker

## Screenshots

### API Working (Swagger UI)

![API Screenshot] ![alt text](fast-api.png),![alt text](api-customers.png),![alt text](injest-Success.png)