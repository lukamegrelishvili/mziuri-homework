import sqlite3

conn = sqlite3.connect("shop.db")
conn.execute("PRAGMA foreign_keys=ON;")

def create_table():
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS users ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            phonenumber TEXT,
            address TEXT
        );
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS products ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price INTEGER,
            user_id INTEGER, 
            FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE
        );
    """)

    conn.commit()

def add_user(username, phonenumber, address):
    c = conn.cursor()
    c.execute("""
        INSERT INTO users (username, phonenumber, address)
        VALUES (?, ?, ?)
    """, (username, phonenumber, address))
    conn.commit()

def delete_user(user_id):
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()

def update_user(user_id, username, phonenumber, address):
    c = conn.cursor()
    c.execute("""
        UPDATE users
        SET username = ?, phonenumber = ?, address = ?
        WHERE id = ?
    """, (username, phonenumber, address, user_id))
    conn.commit()
    conn.close()