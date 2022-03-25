"""Vest Virtual Trading"""
from fastapi import FastAPI

from services import NASDAQClient

app = FastAPI()

nasdaq = NASDAQClient()


@app.get("/")
async def root():
    stock_response = nasdaq.get_stock("AAPL")

    return {"stock": stock_response}
