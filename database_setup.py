import sqlite3

# Connect to the SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect('database/weather.db')

# Create a cursor object
cursor = conn.cursor()

# Create a table to store daily weather summaries
cursor.execute('''
    CREATE TABLE IF NOT EXISTS daily_weather (
        id INTEGER PRIMARY KEY,
        date TEXT NOT NULL,
        average_temp REAL,
        max_temp REAL,
        min_temp REAL,
        dominant_condition TEXT
    )
''')

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database and table created successfully.")
