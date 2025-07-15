import sqlite3

def init_db():
    conn = sqlite3.connect("skin_mappings.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS skin_mappings (
            normalized_name TEXT PRIMARY KEY,
            dmarket_name TEXT,
            skinport_name TEXT,
            condition TEXT,
            game_id TEXT,
            app_id TEXT
        )
    """)
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_normalized_name ON skin_mappings(normalized_name)")
    conn.commit()
    conn.close()

def save_mapping(normalized_name, dmarket_name, skinport_name, condition, game_id, app_id):
    conn = sqlite3.connect("skin_mappings.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR REPLACE INTO skin_mappings
        (normalized_name, dmarket_name, skinport_name, condition, game_id, app_id)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (normalized_name, dmarket_name, skinport_name, condition, game_id, app_id))
    conn.commit()
    conn.close()