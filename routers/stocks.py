"""Router Stock for the API."""

from fastapi import APIRouter
from services import NASDAQClient


router = APIRouter(
    prefix="/stock",
    tags=["Stock"]
)

nasdaq = NASDAQClient()


@router.get("/trade")
async def stock_trade():
    response = nasdaq.get_stock('AAPL')
    data = response["data"]
    
    return {"trade": data}


@router.get("/hold")
async def stock_hold():
    return {"hold": "AAPL"}


@router.get("/history")
async def stock_history():
    return {"history": "AAPL"}
