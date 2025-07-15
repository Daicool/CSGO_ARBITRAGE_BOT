import json
from src.auth import get_dmarket_headers, get_skinport_token

with open("config.json", "r") as f:
    config = json.load(f)

# Test Dmarket headers
headers = get_dmarket_headers(
    config["dmarket_public_key"],
    config["dmarket_private_key"],
    "GET",
    "/exchange/v1/market/items",
    "gameId=a8db&limit=10"
)
print("Dmarket Headers:", headers)

# Test Skinport token
token = get_skinport_token(config["skinport_client_id"], config["skinport_client_secret"])
print("Skinport Token:", token)