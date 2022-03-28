"""Stock repository."""
from models.stock import Stock
from schemas.stock_schema import StockSchemaInput
from sqlalchemy.orm import Session


class StockRepository:
    """Stock repository."""

    def __init__(self, session: Session):
        """Initialize the repository.
        Args:
            session: The session to use.
        """
        self.session = session

    def get_by_id(self, stock_id: int):
        """Get a stock by its id.
        Args:
            stock_id: The id of the stock.
        """
        return self.session.query(Stock).filter_by(id=stock_id).first()

    def get_by_symbol(self, symbol: str):
        """Get a stock by its symbol.
        Args:
            symbol: The symbol of the stock.
        """
        symbol = symbol.strip().upper()
        return self.session.query(Stock).filter_by(symbol=symbol).first()

    def get_all(self):
        """Get all stocks."""
        return self.session.query(Stock).filter().all()

    def create(self, stock: StockSchemaInput):
        """Create a new stock.
        Args:
            symbol: The symbol of the stock.
        """
        stock_obj = Stock(**stock.dict())

        self.session.add(stock_obj)
        self.session.commit()

        return stock_obj

    def get_or_create(self, stock: StockSchemaInput):
        """Get or create a stock.
        Args:
            stock: The stock to get or create.
        """

        return self.get_by_symbol(stock.symbol) or self.create(stock)
