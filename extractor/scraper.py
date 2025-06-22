import requests
from bs4 import BeautifulSoup
from .config import BASE_URL, PRODUCT_LISTING_PATH, HEADERS

def scrape_products():
    url = BASE_URL + PRODUCT_LISTING_PATH
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")

    products = []
    for item in soup.select(".product-card"):
        title = item.select_one(".title").text.strip()
        price = item.select_one(".price").text.strip()
        products.append({"title": title, "price": price})
    return products