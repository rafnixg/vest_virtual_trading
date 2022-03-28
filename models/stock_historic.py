"""Stock historic model."""
from datetime import datetime

from db import Base
from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class StockHistoric(Base):
    """Stock historic model."""

    __tablename__ = "stock_historic"

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, index=True)
    datetime = Column(DateTime, default=datetime.now())
    price = Column(Float, index=True)

    stock_id = Column(Integer, ForeignKey("stock.id"))
    stock = relationship("Stock", back_populates="stock_historics")
