"""Stock Schema."""
from datetime import datetime
from pydantic import BaseModel
from .enums import TransactionType


class StockSchemaBase(BaseModel):
    """Stock Schema Base."""

    symbol: str
    name: str


class StockSchemaInput(StockSchemaBase):
    """Stock Schema Input."""

    pass


class StockTransactionSchemaBase(BaseModel):
    """Base schema for a transaction."""

    symbol: str
    quantity: int
    transaction_type: TransactionType


class StockTransactionSchemaResponse(StockTransactionSchemaBase):
    """Schema for a transaction."""

    id: int
    price: float
    datetime: datetime
    stock: str

    class Config:
        orm_mode = True


class StockTransactionSchemaInput(StockTransactionSchemaBase):
    """Schema for a transaction input."""


class StockHistoricSchemaBase(BaseModel):
    """Base schema for a historic."""

    symbol: str
    price: float

class StockHistoricSchemaInput(StockHistoricSchemaBase):
    """Schema for a historic input."""

    pass