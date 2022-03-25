"""Stock historic model."""
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from db import Base


class StockHistory(Base):
    """Stock historic model."""

    __tablename__ = "stock_history"

    id = Column(Integer, primary_key=True, index=True)
    currency = Column(String, index=True)
    date = Column(DateTime(timezone=True), server_default=func.now())
    price = Column(Float, index=True)

    stock_id = Column(Integer, ForeignKey("stock.id"))
    stock = relationship("Stock", back_populates="stock_historics")
