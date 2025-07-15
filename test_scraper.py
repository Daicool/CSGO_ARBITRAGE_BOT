import json
from src.scraper import fetch_dmarket_offers, fetch_skinport_buy_orders

with open("config.json", "r") as f:
    config = json.load(f)

# Test Dmarket offers
dmarket_items = fetch_dmarket_offers(
    config["dmarket_public_key"], config["dmarket_private_key"],
    price_from=1000, price_to=5000, limit=5
)
print("Dmarket Items:", json.dumps(dmarket_items, indent=2))

# Test Skinport buy orders
skinport_items = fetch_skinport_buy_orders(
    config["skinport_client_id"], config["skinport_client_secret"]
)
print("Skinport Buy Orders:", json.dumps(skinport_items, indent=2))