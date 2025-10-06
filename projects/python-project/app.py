# Example: simple SQL injection
import sqlite3

def get_user_data(user_input):
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

get_user_data("admin")
