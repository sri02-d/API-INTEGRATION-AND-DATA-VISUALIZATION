import requests
import matplotlib.pyplot as plt
import seaborn as sns

# ===== Step 1: Set API Key and City =====
API_KEY = 'b5bd98a7a7725dbec59c41f20b4e6b77'  # Replace this with your actual OpenWeatherMap API key
CITY = 'Mumbai'  # You can change this to any city

# ===== Step 2: Create the API URL =====
URL = f'https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'

# ===== Step 3: Fetch data from the API =====
response = requests.get(URL)
data = response.json()

# ===== Step 4: Extract required weather information =====
temp = data['main']['temp']
humidity = data['main']['humidity']
pressure = data['main']['pressure']

# ===== Step 5: Display the fetched data =====
print(f"City: {CITY}")
print(f"Temperature: {temp}°C")
print(f"Humidity: {humidity}%")
print(f"Pressure: {pressure} hPa")

# ===== Step 6: Prepare data for visualization =====
labels = ['Temperature (°C)', 'Humidity (%)', 'Pressure (hPa)']
values = [temp, humidity, pressure]

# ===== Step 7: Plot the data =====
sns.set(style="whitegrid")
plt.figure(figsize=(8, 5))
sns.barplot(x=labels, y=values, palette="viridis")
plt.title(f"Current Weather in {CITY}")
plt.ylabel("Values")
plt.xlabel("Parameters")
plt.tight_layout()
plt.show()

# ===== Optional: Save the chart to a file =====
# plt.savefig("weather_chart.png")
