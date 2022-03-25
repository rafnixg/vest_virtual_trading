"""NASDAQ API Client Wrapper."""
import requests
from fastapi import HTTPException


class NASDAQClient:
    """NASDAQ API Client Wrapper."""

    def __init__(self):
        """Initialize the NASDAQ API wrapper."""
        self.api_url = "https://api.nasdaq.com/api"
        self.headers = {
            "user-agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                "AppleWebKit/537.36 (KHTML, like Gecko)"
                "Chrome/75.0.3770.142 Safari/537.36"
            )
        }

    def get_stock(self, symbol: str):
        """Get the stock information from NASDAQ API
        Args:
            symbol (str): The stock symbol.
        Returns:
            dict: The stock information.
        Raises:
            HTTPException: If the stock symbol is not found.
        """
        resource_url = f"{self.api_url}/quote/{symbol}/info?assetclass=stocks"
        response = requests.get(resource_url, headers=self.headers).json()

        if response["status"]["rCode"] != 200:
            raise HTTPException(
                status_code=response["status"]["rCode"],
                detail=response["status"]["bCodeMessage"][0]["errorMessage"],
            )
        return response
