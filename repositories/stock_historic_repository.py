"""Stock historic repository"""
from sqlalchemy.orm import Session
from models import StockHistoric
from schemas.stock_schema import StockHistoricSchemaInput


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
        return self.session.query(StockHistoric).filter(StockHistoric.stock_id==stock_id).all()

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
