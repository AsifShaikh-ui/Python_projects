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
                   ORDER BY total DESC LIMIT 1
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

    pattern = f"{new_year}-{new_month:02d}%"

    cursor.execute("""
        SELECT SUM(amount) FROM expenses WHERE date LIKE ?
""",(pattern, ))
    
    row = cursor.fetchone()
    prev_total = row[0] if row[0] is not None else 0

    conn.close()
    return  prev_total


def get_last_n_month_totals(month, n):

    split_string = month.split(sep="-")
    year = int(split_string[0])
    month_num = int(split_string[1])

    month_list = []
    month_list.append(month)

    for _ in range(n):

        if month_num > 1:
            month_num -= 1

        elif month_num == 1:
            month_num = 12
            year -= 1
        new_year = str(year)
        new_month = str(month_num)

        month_format = f"{new_year}-{month_num:02d}"
        
        month_list.append(month_format)
    
    month_list.reverse()

    n_month_summary = []
    for month_str in month_list:

        total = get_monthly_total(month_str)
        n_month_summary.append((month_str, total))

    return n_month_summary 

        
def analyze_trend(month_totals):

    result = {
        "current_month" : None,
        "current_total" : None,
        "previous_total" : None,
        "change" : None,
        "percent_change" : None,
        "trend" : "Insufficient_Data"
    }
    
    if len(month_totals) < 2:
        return result
    
    current_month, current_total = month_totals[-1]
    previous_month, previous_total = month_totals[-2]

    result["current_month"] = current_month
    result["current_total"] = current_total
    result["previous_total"] = previous_total

    if previous_total == 0:
        return result
    
    change = current_total - previous_total
    percent_change = round(((change/previous_total)*100),2)
    
    result["change"] = change
    result["percent_change"] = percent_change

    if percent_change > 5:
        result["trend"] = "Increasing"
    elif percent_change < -5:
        result["trend"] = "Decreasing"
    else:
        result["trend"] = "Stable"
    
    return result
    
    
