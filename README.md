# Vest Virtual Trading

Web service (API) that simulates a test environment for trade stocks where a user can buy/sell stocks, hold stocks and track portfolio performance.

## Project Structure
```
├── db.py
├── docker-compose.yml
├── Dockerfile
├── LICENSE.txt
├── main.py
├── models
│   ├── __init__.py
│   ├── stock_historic.py
│   ├── stock.py
│   └── stock_transacction.py
├── README.md
├── repo-image.jpg
├── repositories
│   ├── __init__.py
│   ├── stock_historic_repository.py
│   ├── stock_repository.py
│   └── stock_transaction_repository.py
├── requirements.txt
├── routers
│   ├── __init__.py
│   └── stocks.py
├── schemas
│   ├── __init__.py
│   ├── enums.py
│   └── stock_schema.py
├── services
│   ├── __init__.py
│   ├── nasdaq.py
│   └── __pycache__
├── tests
│   ├── __init__.py
│   ├── conftest.py
│   └── test_stock.py
├── utils.py
```

## Tech Stack

- Language: Python3.8
- Framework: FastAPI
- Database: SQLite3
- Lib's: SQLAlchemy (ORM), fastapi_utils (Repeat Task), Pytest

## Endpoints
- **POST** - /stock/trade             (Endpoint for transaction Buy/Sell)
- **GET** - /stock/hold               (Endpoint for view info of hold stock)
- **GET** - /stock/historic/{symbol}  (Endpoint for view historic of a stock by symbol)

## Installation

Cloning repository
```bash
$ git clone https://github.com/rafnixg/vest_virtual_trading.git
$ cd vest_virtual_trading
```

Create virtual enviroment and install requirements.txt
```bash
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ pip3 install -r requirements.txt

```

## Usage
Running with uvicorm server development(reload)
```bash
$ source venv/bin/activate
(venv) $ uvicorn main:app --reload
```
Running with uvicorm server production
```bash
$ source venv/bin/activate
(venv) $ uvicorn main:app
```
Show API Docs
[http://localhost:8000/docs](http://localhost:8000/docs)

## Testing
Running test in virtual enviroment
```bash
$ source venv/bin/activate
(venv) $ pytest
```
Running test in Docker
```bash
$ docker-compose up -d  # Run container in background
$ docker exec -it vest_virtual_trading pytest  # Run test in container
$ docker-compose stop
```
## With Docker
Need to be installed Docker and Docker-compose for run
```bash
$ docker-compose build  # Build docker image
$ docker-compose up     # Run docker container
```
Show API Docs http://localhost:8000/docs

For run docker container in background
```bash
$ docker-compose up  -d    # Run docker container
```

For Stop docker container
```bash
$ docker-compose stop     # Stop docker container
```

## Developer Info
- Rafnix Gabriel Guzmán Garcia, @rafnixg - rafnixg[at]gmail[dot]com
