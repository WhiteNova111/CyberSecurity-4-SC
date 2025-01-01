import sqlite3
import bcrypt

def initialize_db():
    conn = sqlite3.connect("zta_users.db")
    cursor = conn.cursor()

    
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        username TEXT PRIMARY KEY,
                        password TEXT NOT NULL,
                        role TEXT NOT NULL
                    )''')

    
    users = [
        ("admin", bcrypt.hashpw("securepassword".encode(), bcrypt.gensalt()), "Admin"),
        ("employee", bcrypt.hashpw("employee123".encode(), bcrypt.gensalt()), "Employee"),
        ("guest", bcrypt.hashpw("guest123".encode(), bcrypt.gensalt()), "Guest")
    ]
    for user in users:
        cursor.execute("INSERT OR IGNORE INTO users VALUES (?, ?, ?)", (user[0], user[1], user[2]))

    conn.commit()
    conn.close()

initialize_db()
