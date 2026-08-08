from fastapi import FastAPI
from prometheus_client import Counter, generate_latest
from fastapi.responses import Response

app = FastAPI()

REQUESTS = Counter(
    "http_requests_total",
    "Total HTTP Requests"
)

@app.get("/")
def home():
    REQUESTS.inc()
    return {"message": "Cloud Engineering Lab"}

@app.get("/metrics")
def metrics():
    return Response(
        generate_latest(),
        media_type="text/plain"
    )
