import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

# Fetch data from the database
def fetch_data():
    conn = sqlite3.connect('database/weather.db')
    df = pd.read_sql_query("SELECT * FROM daily_weather", conn)
    conn.close()
    return df

# Visualize the data
def visualize_weather():
    df = fetch_data()
    df['date'] = pd.to_datetime(df['date'])
    plt.figure(figsize=(10, 5))
    plt.plot(df['date'], df['average_temp'], marker='o', label='Average Temperature')
    plt.plot(df['date'], df['max_temp'], marker='o', label='Max Temperature')
    plt.plot(df['date'], df['min_temp'], marker='o', label='Min Temperature')
    plt.title('Daily Weather Summary')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    visualize_weather()
