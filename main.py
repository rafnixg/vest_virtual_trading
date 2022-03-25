"""Vest Virtual Trading"""
from fastapi import FastAPI

from routers import stocks

app = FastAPI(
    title="Vest Virtual Trading",
)

app.include_router(stocks.router)

@app.get("/status")
async def status_check():
    """Check the status of the API."""
    return {"status": "OK"}
