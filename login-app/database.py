import sqlite3

conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
""")
conn.commit()
conn.close()

def insert_user(username, password):
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        return {"id": cursor.lastrowid, "username": username, "password": password}
    except:
        return None
    finally:
        conn.close()

def login_user(username, password):
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()
    return result is not None and result[0] == password

def get_all_users():
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return [{"id": u[0], "username": u[1], "password": u[2]} for u in users]

def get_user_by_id(id):
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (id,))
    user = cursor.fetchone()
    conn.close()
    if user:
        return {"id": user[0], "username": user[1], "password": user[2]}
    return None

def delete_user_by_id(id):
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (id,))
    conn.commit()
    deleted = cursor.rowcount
    conn.close()
    return deleted > 0

def update_username_by_id(id, new_username):
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE users SET username = ? WHERE id = ?", (new_username, id))
        conn.commit()
        updated = cursor.rowcount
        return updated > 0
    except:
        return False
    finally:
        conn.close()
