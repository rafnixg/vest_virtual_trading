# Vest Virtual Trading

Web service (API) that simulates a test environment for trade stocks where a user can buy/sell stocks, hold stocks and track portfolio performance.

## Tech Stack

- Language: Python 3.9
- Framework: FastAPI
- Database: SQLite3

## Endpoints
- POST - /stock/trade
- /stock/hold
- /stock/historic

## Installation

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

## Testing
- TODO

## With Docker
- TODO
