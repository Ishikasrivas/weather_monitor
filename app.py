import requests
import time
import datetime
import logging
import sqlite3

def insert_daily_summary(date, average_temp, max_temp, min_temp, dominant_condition):
    conn = sqlite3.connect('database/weather.db')
    cursor = conn.cursor()
    # Convert date to string in 'YYYY-MM-DD' format
    date_str = date.strftime('%Y-%m-%d')
    cursor.execute('''
        INSERT INTO daily_weather (date, average_temp, max_temp, min_temp, dominant_condition)
        VALUES (?, ?, ?, ?, ?)
    ''', (date_str, average_temp, max_temp, min_temp, dominant_condition))
    conn.commit()
    conn.close()

# Configure logging
logging.basicConfig(filename='weather_alerts.log', level=logging.INFO)

# Define your API key and cities
API_KEY = '93beb7c274211130c0c9cdb622c92fdb'  # Use your actual API key
cities = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
temperature_threshold = 26.0  # Set your threshold for alerts

# Keep track of alerts triggered for the current day
alerts_triggered = {city: False for city in cities}
last_checked_date = datetime.date.today()

# Function to fetch weather data
def fetch_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    print(f"Making request to: {url}")
    response = requests.get(url)
    return response.json()

# Function to process weather data
def process_weather_data(weather_data):
    main_data = weather_data['main']
    weather_condition = weather_data['weather'][0]['description']
    average_temp = main_data['temp']
    max_temp = main_data['temp_max']
    min_temp = main_data['temp_min']
    
    return {
        'date': datetime.date.today(),
        'average_temp': average_temp,
        'max_temp': max_temp,
        'min_temp': min_temp,
        'dominant_condition': weather_condition,
    }

# Main loop
while True:
    all_daily_summaries = []
    
    # Check if the date has changed to reset alerts
    current_date = datetime.date.today()
    if current_date != last_checked_date:
        alerts_triggered = {city: False for city in cities}
        last_checked_date = current_date

    for city in cities:
        weather_data = fetch_weather_data(city)
        
        if 'main' in weather_data:
            daily_summary = process_weather_data(weather_data)
            all_daily_summaries.append(daily_summary)

            # Insert the daily summary into the database
            insert_daily_summary(
                daily_summary['date'],
                daily_summary['average_temp'],
                daily_summary['max_temp'],
                daily_summary['min_temp'],
                daily_summary['dominant_condition']
            )

            # Check if the average temperature exceeds the threshold
            if daily_summary['average_temp'] > temperature_threshold and not alerts_triggered[city]:
                alert_message = f"Alert! The average temperature in {city} has exceeded the threshold: {daily_summary['average_temp']}°C"
                print(alert_message)
                logging.info(alert_message)

                # Mark the alert as triggered for the city
                alerts_triggered[city] = True

            print(f"Daily Summary for {city}: {daily_summary}")
        else:
            print(f"Error fetching data for {city}: {weather_data.get('message', 'No error message')}")
    
    print(f"All Daily Summaries: {all_daily_summaries}")

    # Sleep for 5 minutes before the next iteration
    time.sleep(300)
