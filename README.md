# Weather Monitoring Project

## Overview
This project is a real-time data processing system for monitoring weather conditions in major Indian metros. The system retrieves weather data from the OpenWeatherMap API and provides summarized insights using rollups and aggregates.

## Features
- Real-time weather data retrieval for cities: Delhi, Mumbai, Chennai, Bangalore, Kolkata, and Hyderabad.
- Daily weather summaries including average, maximum, and minimum temperatures.
- Alerts for temperature thresholds.
- Visualization of weather data and historical trends.

## Technologies Used
- Python 3.x
- SQLite (or your preferred database)
- OpenWeatherMap API
- Matplotlib/Seaborn (for visualizations)

## Installation

### Prerequisites
- Python 3.x installed on your machine.
- A valid API key from OpenWeatherMap. You can sign up for a free account [here](https://openweathermap.org/).

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Ishikasrivas/weather_monitoring.git
Navigate to the project directory:
bash
Copy code
cd weather_monitoring
Create a virtual environment:
bash
Copy code
python -m venv venv
Activate the virtual environment:
On Windows:
bash
Copy code
venv\Scripts\activate
On macOS/Linux:
bash
Copy code
source venv/bin/activate
Install the required packages:
bash
Copy code
pip install -r requirements.txt
Configuration
Configure the API key in the app.py or create a .env file to store sensitive information.
Adjust the update interval in the application code as needed (default is set to every 5 minutes).
Usage
Run the application:

bash
Copy code
python app.py
The application will start fetching weather data and display daily summaries. Alerts will be triggered based on the configured thresholds.

Database
Daily weather summaries are stored in an SQLite database. You can modify the database settings in the application code if needed.

Testing
Ensure to run the following test cases:

Verify the application starts successfully.
Confirm data retrieval and parsing from the API.
Check temperature conversion functionality.
Validate daily weather summary calculations.
Test alerting thresholds for specified weather conditions.
Visualizations
The project includes visualizations for daily weather summaries and historical trends. Ensure you have the required libraries installed (Matplotlib/Seaborn).

Bonus Features
Additional weather parameters (e.g., humidity, wind speed) can be incorporated into the rollups/aggregates.
Explore functionalities for weather forecasts and summaries based on predicted conditions.
Non-Functional Considerations
Implemented basic error handling for API requests.
Performance optimizations for data retrieval intervals.
