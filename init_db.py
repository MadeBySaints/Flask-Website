import sqlite3

# Connect to database (or create it if it doesn't exist)
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create users table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
''')

# Insert a default admin user
cursor.execute('''
    INSERT OR IGNORE INTO users (username, password)
    VALUES (?, ?)
''', ('admin', 'adminpass'))

# Save and close
conn.commit()
conn.close()

print("Database initialized and default user added.")
