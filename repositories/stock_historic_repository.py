"""Stock historic repository"""
from datetime import date, datetime

from models import StockHistoric
from schemas.stock_schema import StockHistoricSchemaInput
from sqlalchemy import func
from sqlalchemy.orm import Session


class StockHistoricRepository:
    """Stock historic repository."""

    def __init__(self, session: Session):
        """Initialize the repository.
        Args:
            session: The session to use.
        """
        self.session = session

    def get_all_by_stock_id(self, stock_id: int):
        """Get all stock historic by stock id.
        Args:
            stock_id: The id of the stock.
        """
        return (
            self.session.query(StockHistoric)
            .filter(StockHistoric.stock_id == stock_id)
            .all()
        )

    def create(self, stock_historic: StockHistoricSchemaInput, stock_id: int):
        """Create a new stock historic.
        Args:
            stock_historic: The stock historic to create.
            price: The price of the stock.
            stock_id: The id of the stock.
        """
        stock_historic_obj = StockHistoric(**stock_historic.dict(), stock_id=stock_id)
        self.session.add(stock_historic_obj)
        self.session.commit()
        return stock_historic_obj

    def get_reference_prices_today(self, stock_id: int):
        """Get reference prices today.
        Args:
            stock_id: The id of the stock.
        """
        stock_historics = (
            self.session.query(StockHistoric)
            .filter(
                StockHistoric.stock_id == stock_id,
                func.date(StockHistoric.datetime) == date.today(),
            )
            .all()
        )
        stock_historics_prices = [
            stock_historic.price for stock_historic in stock_historics
        ]
        price_min = min(stock_historics_prices) or 0
        price_max = max(stock_historics_prices) or 0
        price_avg = (sum(stock_historics_prices) / len(stock_historics_prices)) or 0

        return {
            "lowest": f"${price_min:.2f}",
            "highest": f"${price_max:.2f}",
            "average": f"${price_avg:.2f}",
        }
