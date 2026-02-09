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

def get_category_summary(month):

    conn = get_connection()
    cursor = conn.cursor()
    pattern = f"{month}%"

    cursor.execute("""
        SELECT category, SUM(amount) FROM expenses WHERE date LIKE ? GROUP BY category
""",(pattern, ))

    summary = cursor.fetchall()

    conn.close()
    return summary

def get_top_category(month):

    conn = get_connection()
    cursor = conn.cursor()
    pattern = f"{month}%"

    cursor.execute("""
        SELECT category, SUM(amount) AS total FROM expenses WHERE date LIKE ? GROUP BY category 
                   ORDER BY total DESC LIMIT 3
""")

    top = cursor.fetchone()
    conn.close()

    if top:
        return top[0], top[1]
    return None

def compare_month(month):

    conn = get_connection()
    cursor = conn.cursor()
    
    split_string = month.split(sep="-")
    year = int(split_string[0])
    mon = int(split_string[1])

    if mon > 1:
        mon = mon - 1
    elif mon == 1:
        year = year - 1
        mon = 12
    new_year = str(year)
    new_month = str(mon)

    pattern = f"{new_year}-0{new_month}%"

    cursor.execute("""
        SELECT SUM(amount) FROM expenses WHERE date LIKE ?
""",(pattern, ))
    
    row = cursor.fetchone()
    prev_total = row[0] if row[0] is not None else 0

    conn.close()
    return  prev_total



    
