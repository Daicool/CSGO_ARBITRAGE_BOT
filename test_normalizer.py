from src.name_normalizer import normalize_name, match_names

# Test normalize_name
dmarket_name = "AK-47 | Vulcan"
dmarket_condition = "field-tested"
skinport_name = "AK-47 | Vulcan (Field-Tested)"
print("Normalized Dmarket:", normalize_name(dmarket_name, dmarket_condition))
print("Normalized Skinport:", normalize_name(skinport_name))
print("Match:", match_names(dmarket_name + " " + dmarket_condition, skinport_name))