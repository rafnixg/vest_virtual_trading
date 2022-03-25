"""NASDAQ API Client Wrapper."""
import requests


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

    def get_stock(self, symbol):
        """Get the stock information from NASDAQ API
        Args:
            symbol (str): The stock symbol.
        """
        resource_url = f"{self.api_url}/quote/{symbol}/info?assetclass=stocks"
        response = requests.get(resource_url, headers=self.headers)
        return response.json()
