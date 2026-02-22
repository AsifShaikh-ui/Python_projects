import sqlite3

file_name = "client_database.db"

def get_connect():
    return sqlite3.connect(file_name)

def create_table():

    conn = get_connect()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clients (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   phone_no TEXT NOT NULL,
                   email TEXT NOT NULL UNIQUE,
                   status TEXT NOT NULL CHECK(status IN("lead", "contacted", "converted", "lost")),
                   created_at TEXT DEFAULT CURRENT_TIMESTAMP
                   )
""")
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS interactions (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   client_id INTEGER NOT NULL,
                   note TEXT NOT NULL,
                   interaction_type TEXT NOT NULL CHECK(interaction_type IN("call", "email", "meeting")),
                   created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                   FOREIGN KEY (client_id) REFERENCES clients(id)
                   )
""")
    
    conn.commit()
    conn.close()

