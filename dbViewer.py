import sqlite3


def display_db_content():
    try:
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM students")
        rows = c.fetchall()
        for row in rows:
            print(row)
        conn.close()
    except Exception as e:
        print("Error occurred:", e)


display_db_content()
