import json
from src.auth import get_dmarket_headers, get_skinport_headers

# Load config
with open('config.json', 'r') as f:
    config = json.load(f)

# Test Dmarket headers
dmarket_headers = get_dmarket_headers(
    config["dmarket_public_key"],
    config["dmarket_private_key"],
    "GET",
    "/items"
)
print("Dmarket Headers:", dmarket_headers)

# Test Skinport headers
skinport_headers = get_skinport_headers(
    config["skinport_client_id"],
    config["skinport_client_secret"]
)
print("Skinport Headers:", skinport_headers)
