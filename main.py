"""Vest Virtual Trading"""
from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every

from db import Base, SessionMarkerFastAPI, engine
from repositories.stock_historic_repository import StockHistoricRepository
from repositories.stock_repository import StockRepository
from routers import stocks
from schemas.stock_schema import StockHistoricSchemaInput
from services import NASDAQClient
from utils import extrac_price

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Vest Virtual Trading",
)

app.include_router(stocks.router)
nasdaq = NASDAQClient()


@app.get("/status")
async def status_check():
    """Check the status of the API."""
    return {"status": "OK"}


@app.on_event("startup")
@repeat_every(seconds=60 * 60)  # 1 hour
def historic_stock_prices() -> None:
    with SessionMarkerFastAPI.context_session() as db:
        stock_repository = StockRepository(db)
        stock_historic_repository = StockHistoricRepository(db)
        stocks = stock_repository.get_all()
        for stock in stocks:
            stock_response = nasdaq.get_stock(stock.symbol)
            data = stock_response["data"]
            price = extrac_price(data)
            stock_historic = StockHistoricSchemaInput(symbol=stock.symbol, price=price)
            stock_historic_repository.create(stock_historic, stock.id)
