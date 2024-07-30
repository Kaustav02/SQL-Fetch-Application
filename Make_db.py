import sqlite3
import json
import random

# Step 1: Set up the SQLite database
def setup_database():
    conn = sqlite3.connect('db/test.db')
    cursor = conn.cursor()
    
    # Create a table
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
(id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
    
    # Insert some sample data
    for i in range(1, 101):
        name = f'User{i}'
        age = random.randint(18, 70)
        cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
    
    
    conn.commit()
    conn.close()
    
setup_database()