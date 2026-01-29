import sqlite3

file_name = "task_list.db"

def get_connect():
    return sqlite3.connect(file_name)

def create_table():

    conn = get_connect()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS task(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   task TEXT NOT NULL,
                   status TEXT NOT NULL
                   )
""")
    
    conn.commit()
    conn.close()

create_table()