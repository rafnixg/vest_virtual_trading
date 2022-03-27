"""utilities"""

import re


def extrac_price(data):
    """Extract price from data."""
    price_str = data["primaryData"]["lastSalePrice"][1:]
    return float(price_str)

