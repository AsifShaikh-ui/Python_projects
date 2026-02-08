from database import (
    get_connection
)

def get_monthly_total(month):

    conn = get_connection()
    cursor = conn.cursor()
    pattern = month + "%"

    cursor.execute("""
        SELECT SUM(amount) FROM expenses WHERE date LIKE ? 
""",(pattern, ))
    
    row = cursor.fetchone()
    total = row[0] if row[0] is not None else 0
    
    conn.close()
    return total
