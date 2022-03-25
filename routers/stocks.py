"""Router Stock for the API."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.stock_schema import StockTransactionSchemaInput, StockTransactionSchemaResponse
from services import NASDAQClient
from db import get_db


router = APIRouter(
    prefix="/stock",
    tags=["Stock"]
)

nasdaq = NASDAQClient()


@router.post("/trade")
async def stock_trade(
    stock_transaction: StockTransactionSchemaInput,
    db: Session = Depends(get_db)
):
    response = nasdaq.get_stock(stock_transaction.symbol)
    data = response["data"]

    return {"trade": data}


@router.get("/hold")
async def stock_hold():
    return {"hold": "AAPL"}


@router.get("/history")
async def stock_history():
    return {"history": "AAPL"}
