from rapidfuzz import fuzz
import re

condition_map = {
    "factory new": "fn", "minimal wear": "mw", "field-tested": "ft",
    "well-worn": "ww", "battle-scarred": "bs"
}

def normalize_name(name, condition=None):
    name = name.lower().replace("|", "").replace("™", "").replace("  ", " ").strip()
    if condition:
        name = f"{name} {condition.lower()}"
    for full, short in condition_map.items():
        name = name.replace(full, short)
    return name

def match_names(dmarket_name, skinport_name, threshold=90):
    return fuzz.ratio(normalize_name(dmarket_name), normalize_name(skinport_name)) > threshold