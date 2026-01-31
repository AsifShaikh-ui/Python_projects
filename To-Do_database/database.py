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

def add_task(task):

    conn = get_connect()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO task(task, status) VALUES (?,?)
""",(task,"Pending"))
    
    conn.commit()
    conn.close()

def get_task():

    conn = get_connect()
    cursor = conn.cursor()

    cursor.execute("""SELECT * FROM task""")
    data =  cursor.fetchall()

    conn.close()
    return data

def delete_task(task_id):

    conn = get_connect()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM task WHERE id = ?
""",(task_id, ))
    
    conn.commit()
    deleted = cursor.rowcount
    conn.close()

    return deleted

def mark_done(task_id):

    conn = get_connect()
    cursor = conn.cursor()

    cursor.execute("""
       UPDATE task SET status = ? WHERE id = ? 
""", ("Done", task_id))
    
    conn.commit()
    updated = cursor.rowcount
    conn.close()

    return updated