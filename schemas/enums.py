"""Custom Enums for the API."""
from enum import Enum


class TransactionType(Enum):
    """Transaction type."""
    BUY = "buy"
    SELL = "sell"
