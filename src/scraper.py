import requests
from urllib.parse import urlencode
from .auth import get_dmarket_headers, get_skinport_token

def fetch_dmarket_offers(public_key, private_key, game_id="a8db", price_from=0, price_to=5000, limit=100):
    endpoint = "/exchange/v1/market/items"
    query_params = urlencode({
        "gameId": game_id, "priceFrom": price_from, "priceTo": price_to,
        "limit": limit, "currency": "USD"
    })
    headers = get_dmarket_headers(public_key, private_key, "GET", endpoint, query_params)
    response = requests.get(f"https://api.dmarket.com{endpoint}?{query_params}", headers=headers)
    response.raise_for_status()
    return response.json().get("objects", [])

def fetch_dmarket_buy_orders(public_key, private_key, game_id="a8db", title=""):
    endpoint = "/marketplace-api/v1/market-depth"
    query_params = urlencode({"gameId": game_id, "title": title, "aggregatedData": "Orders"})
    headers = get_dmarket_headers(public_key, private_key, "GET", endpoint, query_params)
    response = requests.get(f"https://api.dmarket.com{endpoint}?{query_params}", headers=headers)
    response.raise_for_status()
    return response.json().get("orders", [])

def fetch_skinport_offers(client_id, client_secret, app_id="730", currency="USD"):
    token = get_skinport_token(client_id, client_secret)
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"https://api.skinport.com/v1/items?app_id={app_id}&currency={currency}", headers=headers)
    response.raise_for_status()
    return response.json()

def fetch_skinport_buy_orders(client_id, client_secret, app_id="730", currency="USD"):
    token = get_skinport_token(client_id, client_secret)
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"https://api.skinport.com/v1/buy-orders?app_id={app_id}&currency={currency}", headers=headers)
    response.raise_for_status()
    return response.json()