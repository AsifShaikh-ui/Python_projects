import sqlite3

file_name = "expense_manager.db"

def get_connection():
    return sqlite3.connect(file_name)

def create_table():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   amount REAL NOT NULL,
                   category TEXT NOT NULL,
                   date TEXT NOT NULL,
                   note TEXT
                   )
""")
    
    conn.commit()
    conn.close()

def add_expense(amount, category, date, note):

    if amount <= 0:
        return False

    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO expenses(amount, category, date, note)
                   VALUES (?, ?, ?, ?)
""",(amount, category, date, note))
    
    conn.commit()
    conn.close()
    return True

def get_total_expense():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT SUM(amount) FROM expenses
""")
    
    row = cursor.fetchone()
    total = row[0] if row[0] is not None else 0

    conn.close()
    return total