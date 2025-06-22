import re
from .utils import is_amharic

def clean_price(price_str):
    price = re.sub(r"[^0-9.]", "", price_str)
    return float(price) if price else 0.0

def clean_data(products):
    cleaned = []
    for p in products:
        if is_amharic(p["title"]):
            cleaned.append({
                "title": p["title"].strip(),
                "price": clean_price(p["price"])
            })
    return cleaned