from src.storage import init_db, save_mapping
import sqlite3

init_db()
save_mapping(
    "ak-47 vulcan ft", "AK-47 | Vulcan", "AK-47 | Vulcan (Field-Tested)",
    "field-tested", "a8db", "730"
)

# Check database
conn = sqlite3.connect("skin_mappings.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM skin_mappings")
print(cursor.fetchall())
conn.close()