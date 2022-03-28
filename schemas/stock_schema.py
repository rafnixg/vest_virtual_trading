"""Stock Schema."""
from datetime import datetime

from pydantic import BaseModel

from .enums import TransactionType

# STOCK SCHEMA
class StockSchemaBase(BaseModel):
    """Stock Schema Base."""

    symbol: str
    name: str

class StockSchemaInput(StockSchemaBase):
    """Stock Schema Input."""

# STOCK TRANSACTION SCHEMA
class StockTransactionSchemaBase(BaseModel):
    """Base schema for a transaction."""

    symbol: str
    quantity: int
    transaction_type: TransactionType

class StockTransactionSchemaResponse(StockTransactionSchemaBase):
    """Schema for a transaction."""

    id: int
    price: str
    create_date: datetime
    stock: StockSchemaInput

    class Config:
        """Config."""
        orm_mode = True

class StockTransactionSchemaInput(StockTransactionSchemaBase):
    """Schema for a transaction input."""

# STOCK HISTROIC SCHEMA
class StockHistoricSchemaBase(BaseModel):
    """Base schema for a historic."""

    price: float

class StockHistoricSchemaInput(StockHistoricSchemaBase):
    """Schema for a historic input."""
    symbol: str

class StockHistoricSchemaResponse(StockHistoricSchemaBase):
    """Schema for a historic."""
    datetime: datetime

    class Config:
        """Config."""
        orm_mode = True

# STOCK HOLDER SCHEMA

class StockHolderPriceReferenceSchema(BaseModel):
    """Schema for a holder price reference."""

    lowest: str
    highest: str
    average: str

class StockHolderSchemaBase(BaseModel):
    """Base schema for a holder."""

    symbol: str
    name: str
    held_shares: int
    value_shares: str
    profit_loss: str
    current_price_reference: StockHolderPriceReferenceSchema

class StockHolderSchemaResponse(StockHolderSchemaBase):
    """Schema for a holder."""

    class Config:
        """Config."""
        orm_mode = True