import pandas as pd
import random
from datetime import datetime, timedelta

# Generate a list of random cities
cities = ["Delhi","Mumbai","Chennai","Kolkata"]

# Weather conditions
weather_conditions = ["Sunny", "Cloudy", "Rainy", "Stormy", "Snowy", "Foggy", "Windy"]

# Date range (one year)
start_date = datetime(2025, 2, 1)
num_days = 28

# Generate dataset
data = []

for day in range(num_days):
    for city in cities:
        date = start_date + timedelta(days=day)
        temperature = round(random.uniform(-5, 40), 1)  # Temperature range (-5°C to 40°C)
        humidity = random.randint(20, 100)  # Humidity (20% to 100%)
        wind_speed = round(random.uniform(0, 50), 1)  # Wind speed (0 to 50 km/h)
        condition = random.choice(weather_conditions)

        data.append([date.strftime("%Y-%m-%d"), city, temperature, humidity, wind_speed, condition])

# Create DataFrame
df = pd.DataFrame(data, columns=["Date", "City", "Temperature(°C)", "Humidity(%)", "Wind Speed(km/h)", "Condition"])

# Save to CSV
df.to_csv("weather_dataset.csv", index=False)

print("Weather dataset generated and saved as 'weather_dataset.csv'.")
