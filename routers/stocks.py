"""Router Stock for the API."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.stock_schema import (
    StockSchemaInput,
    StockTransactionSchemaInput,
    StockTransactionSchemaResponse,
)
from services import NASDAQClient
from db import get_db
from repositories.stock_repository import StockRepository
from repositories.stock_transaction_repository import StockTransactionRepository
from utils import extrac_price

router = APIRouter(prefix="/stock", tags=["Stock"])

nasdaq = NASDAQClient()


@router.post("/trade")
async def stock_trade(
    stock_transaction: StockTransactionSchemaInput, db: Session = Depends(get_db)
):
    response = nasdaq.get_stock(stock_transaction.symbol)
    data = response["data"]

    # Create Stock
    stock = StockSchemaInput(
        symbol=data["symbol"],
        name=data["companyName"],
    )
    stock_repository = StockRepository(db)
    stock_obj = stock_repository.get_or_create(stock)

    # Create Stock Transaction
    price = extrac_price(data)
    transaction_repository = StockTransactionRepository(db)
    transaction_obj = transaction_repository.create(
        stock_transaction, price, stock_obj.id
    )

    if not transaction_obj:
        raise HTTPException(
            status_code=422, detail="You don't have enough shares to sell"
        )
    return transaction_obj


@router.get("/hold")
async def stock_hold():
    return {"hold": "AAPL"}


@router.get("/historic")
async def stock_history():
    return {"history": "AAPL"}
