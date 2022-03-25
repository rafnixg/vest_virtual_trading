"""Stock Transaction model."""
from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    Float,
    String,
    DateTime,
    Enum,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from db import Base

from schemas.enums import TransactionType


class StockTransaction(Base):
    """Stock Transaction model."""

    __tablename__ = "stock_transaction"

    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer, index=True)
    symbol = Column(String, index=True)
    price = Column(Float, index=True)
    transaction_type = Column(Enum(TransactionType))
    create_date = Column(DateTime(timezone=True), server_default=func.now())

    stock_id = Column(Integer, ForeignKey("stock.id"))
    stock = relationship("Stock", back_populates="stock_transactions")
