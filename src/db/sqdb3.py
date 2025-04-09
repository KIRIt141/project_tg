import sqlite3 as sq



def init_db():
    conn = sq.connect('my_database.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id_tg INTEGER UNIQUE,
        username TEXT NOT NULL,
        sleep_status TEXT NOT NULL DEFAULT 'unknown'
    )
    ''')

    conn.commit()
    conn.close()

def add_user(user_id: int, username: str):
    conn = sq.connect('my_database.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT OR IGNORE INTO Users (user_id_tg, username)
    VALUES (?, ?)
    ''', (user_id, username))

    conn.commit()
    conn.close()

def sleep_yes(user_id: int, username: str, sleep_status: str):
    conn = sq.connect('my_database.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT OR REPLACE INTO Users (user_id_tg, username, sleep_status)
    VALUES (?, ?, ?)
    ''', (user_id, username, sleep_status))

    conn.commit()
    conn.close()

def sleep_no(user_id: int, username: str, sleep_status: str):
    conn = sq.connect('my_database.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT OR REPLACE INTO Users (user_id_tg, username, sleep_status)
    VALUES (?, ?, ?)
    ''', (user_id, username, sleep_status))

    conn.commit()
    conn.close()

def all_users():
    with sq.connect('my_database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT user_id_tg, username, sleep_status FROM Users')
        return cursor.fetchall()     