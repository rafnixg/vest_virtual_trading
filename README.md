# Vest Virtual Trading

Web service (API) that simulates a test environment for trade stocks where a user can buy/sell stocks, hold stocks and track portfolio performance.

## Tech Stack

- Language: Python3.8
- Framework: FastAPI
- Database: SQLite3
- Lib's: SQLAlchemy (ORM), fastapi_utils (Repeat Task), Pytest

## Endpoints
- POST - /stock/trade
- GET - /stock/hold
- GET - /stock/historic/{symbol}

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
Running test
```bash
$ source venv/bin/activate
(venv) $ pytest
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
