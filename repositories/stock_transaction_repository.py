"""Stock transaction repository."""
from sqlalchemy.orm import Session
from sqlalchemy import case, func
from models.stock import Stock, StockTransaction
from schemas.enums import TransactionType
from schemas.stock_schema import StockTransactionSchemaInput

# CASE For Stock Transaction type multiplier factor
case_quantity_for_type_action = case(
    [
        (
            StockTransaction.transaction_type == TransactionType.SELL,
            StockTransaction.quantity * -1,
        ),
        (
            StockTransaction.transaction_type == TransactionType.BUY,
            StockTransaction.quantity,
        ),
    ]
)


class StockTransactionRepository:
    """Stock transaction repository."""

    def __init__(self, session: Session):
        """Initialize the repository.
        Args:
            session: The session to use.
        """
        self.session = session

    def get_total_shares_stock(self, stock_id: int):
        """Get total shares of a stock.
        Args:
            stock_id: The id of the stock.
        """
        return (
            self.session.query(func.sum(case_quantity_for_type_action))
            .filter(StockTransaction.stock_id == stock_id)
            .scalar()
        )

    def create(
        self, transaction: StockTransactionSchemaInput, price: float, stock_id: int
    ):
        """Create a new transaction.
        Args:
            transaction: The transaction to create.
        """
        if (
            transaction.transaction_type == TransactionType.SELL
            and not self._validate_transaction(transaction, stock_id)
        ):
            return None

        transaction_obj = StockTransaction(
            **transaction.dict(), stock_id=stock_id, price=price
        )

        self.session.add(transaction_obj)
        self.session.commit()

        return transaction_obj

    def _validate_transaction(
        self, transaction: StockTransactionSchemaInput, stock_id: int
    ):
        """Validate a transaction.
        Args:
            transaction: The transaction to validate.
        """
        total_share_stock = self.get_total_shares_stock(stock_id)

        if transaction.quantity >= total_share_stock:
            return False
        return True
