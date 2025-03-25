import sqlite3
import requests

DATABASE_FILE = requests.get('https://github.com/AmrinderG/test-ag03/raw/refs/heads/main/project_database.db')

conn = sqlite3.connect(DATABASE_FILE)
cursor = conn.cursor()

# Example table, modify as needed
cursor.execute("""
CREATE TABLE IF NOT EXISTS Central_Equipment (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Tag_No TEXT NOT NULL,
    Instrument_Type TEXT NOT NULL
)
""")

conn.commit()
conn.close()
