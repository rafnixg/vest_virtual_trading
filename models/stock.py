"""Stock model."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from db import Base
from models.stock_historic import StockHistoric
from models.stock_transacction import StockTransaction


class Stock(Base):
    """Stock model."""

    __tablename__ = "stock"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    symbol = Column(String, unique=True, index=True)

    stock_transactions = relationship(StockTransaction, back_populates="stock")
    stock_historics = relationship(StockHistoric, back_populates="stock")
