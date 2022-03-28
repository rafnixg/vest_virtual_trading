"""Stock historic model."""
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from db import Base


class StockHistoric(Base):
    """Stock historic model."""

    __tablename__ = "stock_historic"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, index=True)
    datetime = Column(DateTime(timezone=True), server_default=func.now())
    price = Column(Float, index=True)

    stock_id = Column(Integer, ForeignKey("stock.id"))
    stock = relationship("Stock", back_populates="stock_historics")
