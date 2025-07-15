import json
from src.scraper import fetch_dmarket_offers, fetch_skinport_buy_orders
from src.name_normalizer import normalize_name, match_names
from src.storage import init_db, save_mapping

def load_config():
    with open("config.json", "r") as f:
        return json.load(f)

def update_skin_mappings():
    config = load_config()
    dmarket_items = fetch_dmarket_offers(
        config["dmarket_public_key"], config["dmarket_private_key"],
        price_from=config["min_price_usd"]*100, price_to=config["max_price_usd"]*100, limit=100
    )
    skinport_items = fetch_skinport_buy_orders(
        config["skinport_client_id"], config["skinport_client_secret"]
    )
    
    init_db()
    for d_item in dmarket_items:
        d_name = d_item["title"]
        d_condition = d_item.get("extra", {}).get("exterior", "")
        d_normalized = normalize_name(d_name, d_condition)
        
        for s_item in skinport_items:
            s_name = s_item["market_hash_name"]
            if match_names(d_name + " " + d_condition, s_name):
                save_mapping(
                    d_normalized, d_name, s_name, d_condition, "a8db", "730"
                )

if __name__ == "__main__":
    update_skin_mappings()