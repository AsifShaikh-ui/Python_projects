import sqlite3

file_name = "expenses_record.db"

def get_connect():
    return sqlite3.connect(file_name)

def create_table():

    conn = get_connect()
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

    conn = get_connect()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO expenses (amount, category, date, note)
                   VALUES (?,?,?,?)
""",(amount, category, date, note))
    
    conn.commit()
    conn.close()

def view_expense():

    conn = get_connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")
    result = cursor.fetchall()

    conn.close()
    return result

def delete_expense(expense_id):

    conn = get_connect()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))

    conn.commit()
    conn.close()
    