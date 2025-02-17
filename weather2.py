import requests

api_key = "ff7eabb4b719111d9992a5c13f3e3ad5"  # Replace with your actual API key

place = input("Enter the city to find weather: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={place}&appid={api_key}"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    temp_kelvin = data["main"]["temp"]
    temp_celsius = temp_kelvin - 273.15
    temp_min_celsius = data["main"]["temp_min"] - 273.15
    temp_max_celsius = data["main"]["temp_max"] - 273.15
    humidity = data["main"]["humidity"]
    
    print(f"The temperature in {place} is {temp_celsius:.2f}°C")
    print(f"Minimum temperature: {temp_min_celsius:.2f}°C")
    print(f"Maximum temperature: {temp_max_celsius:.2f}°C")
    print(f"Humidity: {humidity}%")
else:
    print("Error fetching weather data. Please check the city name and try again.")
