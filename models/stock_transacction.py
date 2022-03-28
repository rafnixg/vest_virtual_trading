"""Stock Transaction model."""
from datetime import datetime

from db import Base
from schemas.enums import TransactionType
from sqlalchemy import (Column, DateTime, Enum, Float, ForeignKey, Integer,
                        String)
from sqlalchemy.orm import relationship


class StockTransaction(Base):
    """Stock Transaction model."""

    __tablename__ = "stock_transaction"

    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer, index=True)
    symbol = Column(String, index=True)
    price = Column(Float, index=True)
    transaction_type = Column(Enum(TransactionType))
    create_date = Column(DateTime, default=datetime.now())

    stock_id = Column(Integer, ForeignKey("stock.id"))
    stock = relationship("Stock", back_populates="stock_transactions")
