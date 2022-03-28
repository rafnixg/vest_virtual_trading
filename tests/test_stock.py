"""Test for the stock endpoints."""
from repositories.stock_historic_repository import StockHistoricRepository
from repositories.stock_repository import StockRepository
from schemas.stock_schema import StockHistoricSchemaInput
def test_status(client):
    """Test the status of the API."""
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}


def test_stock_trade_buy(client):
    """Test the stock trade route [POST] with a buy."""
    data = {"symbol": "AAPL", "quantity": 10, "transaction_type": "buy"}
    response = client.post("/stock/trade", json=data)
    assert response.status_code == 200
    assert response.json()["symbol"] == "AAPL"
    assert response.json()["quantity"] == 10
    assert response.json()["transaction_type"] == "buy"


def test_stock_trade_buy_error_symbol(client):
    """Test the stock trade route [POST] with an error in buy."""
    data = {"symbol": "RAFNIXG", "quantity": 10, "transaction_type": "buy"}
    response = client.post("/stock/trade", json=data)
    assert response.status_code == 400
    assert response.json()["detail"] == "Symbol not exists."


def test_stock_trade_sell_without_shares(client):
    """Test the stock trade route [POST] with an error in sell."""
    data = {"symbol": "AAPL", "quantity": 10, "transaction_type": "sell"}
    response = client.post("/stock/trade", json=data)
    assert response.status_code == 422
    assert response.json()["detail"] == "You don't have enough shares to sell"


def test_stock_trade_sell_with_buy(client):
    """Test the stock trade route [POST] with a sell."""
    data = {"symbol": "AAPL", "quantity": 10, "transaction_type": "buy"}
    client.post("/stock/trade", json=data)
    data = {"symbol": "AAPL", "quantity": 5, "transaction_type": "sell"}
    response = client.post("/stock/trade", json=data)
    assert response.status_code == 200
    assert response.json()["symbol"] == "AAPL"
    assert response.json()["quantity"] == 5
    assert response.json()["transaction_type"] == "sell"


def test_stock_hold(client):
    """Test the stock hold route [GET]."""
    data_transaction_one = {"symbol": "AAPL", "quantity": 4, "transaction_type": "buy"}
    data_transaction_two = {"symbol": "AAPL", "quantity": 6, "transaction_type": "buy"}
    data_transaction_three = {
        "symbol": "TSLA",
        "quantity": 20,
        "transaction_type": "buy",
    }
    client.post("/stock/trade", json=data_transaction_one)
    client.post("/stock/trade", json=data_transaction_two)
    client.post("/stock/trade", json=data_transaction_three)

    response = client.get("/stock/hold")
    assert response.status_code == 200

    assert response.json()[0]["symbol"] == "AAPL"
    assert response.json()[0]["held_shares"] == 10

    assert response.json()[1]["symbol"] == "TSLA"
    assert response.json()[1]["held_shares"] == 20


def test_stock_hold_without_stock(client):
    """Test the stock hold route [GET] with an error."""
    response = client.get("/stock/hold")
    assert response.status_code == 422
    assert response.json()["detail"] == "You don't have any stock to hold"

def test_stock_historic_without_records(client):
    """Test the stock historic route [GET] without data."""

    response = client.get("/stock/historic/AAPL")
    assert response.status_code == 404

def test_stock_historic_with_records(client, db_session):
    """Test the stock historic route [GET] with data."""
    data_transaction_one = {"symbol": "AAPL", "quantity": 2, "transaction_type": "buy"}
    response = client.post("/stock/trade", json=data_transaction_one)
    stock_repository = StockRepository(db_session)
    stock = stock_repository.get_by_symbol("AAPL")

    stock_historic_data_one = StockHistoricSchemaInput(price=100, symbol="AAPL")
    stock_historic_data_two = StockHistoricSchemaInput(price=101, symbol="AAPL")

    stock_historic_repository = StockHistoricRepository(db_session)
    stock_historic_repository.create(stock_historic_data_one, stock.id)
    stock_historic_repository.create(stock_historic_data_two, stock.id)

    response = client.get("/stock/historic/AAPL")
    assert response.status_code == 200
