"""Router Stock for the API."""

from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException

from db import get_db
from services import NASDAQClient
from repositories.stock_historic_repository import StockHistoricRepository
from repositories.stock_repository import StockRepository
from repositories.stock_transaction_repository import \
    StockTransactionRepository
from schemas.stock_schema import (StockSchemaInput,
                                  StockTransactionSchemaInput)
from utils import extrac_price

router = APIRouter(prefix="/stock", tags=["Stock"])

nasdaq = NASDAQClient()

#  TODO: Add response_model


@router.post("/trade")
async def stock_trade(
    stock_transaction: StockTransactionSchemaInput, db: Session = Depends(get_db)
):
    """Trade a stock route [POST]
    Args:
        stock_transaction: The stock transaction to trade.
        db: The database session.
    """
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
async def stock_hold(db: str = Depends(get_db)):
    """Get the stocks that the user is holding [GET]
    Args:
        db: The database session.
    """
    transaction_repository = StockTransactionRepository(db)
    stock_repository = StockRepository(db)
    stock_historic_repository = StockHistoricRepository(db)

    stocks_obj = stock_repository.get_all()
    stocks_info = []
    for stock in stocks_obj:
        stock_response = nasdaq.get_stock(stock.symbol)
        data = stock_response["data"]
        current_price = extrac_price(data)
        stock_info = {
            "symbol": stock.symbol,
            "name": stock.name,
            "held_shares": transaction_repository.get_total_shares_stock(stock.id),
            "value_shares": f"${transaction_repository.get_total_value_shares_stock(stock.id)}",
            "profit/loss": f"{transaction_repository.get_profit_loss(stock.id, current_price):.2f}%",
            "current_price_reference": stock_historic_repository.get_reference_prices_today(
                stock.id
            ),
        }
        stocks_info.append(stock_info)

    return {"stocks": stocks_info}


@router.get("/historic/{symbol}")
async def stock_historic(symbol: str, db: str = Depends(get_db)):
    """Get the historic of a stock [GET]
    Args:
        symbol: The symbol of the stock.
        db: The database session.
    """
    stock_repository = StockRepository(db)
    stock_obj = stock_repository.get_by_symbol(symbol)

    if not stock_obj:
        raise HTTPException(status_code=404, detail="Stock symbol not found")

    stock_historic_repository = StockHistoricRepository(db)
    stock_historics = stock_historic_repository.get_all_by_stock_id(stock_obj.id)

    return {
        "symbol": stock_obj.symbol,
        "name": stock_obj.name,
        "historics": [
            {"price": historic.price, "datetime": historic.datetime}
            for historic in stock_historics
        ],
    }
