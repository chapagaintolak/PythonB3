import requests
api_key = "ff7eabb4b719111d9992a5c13f3e3ad5"

place = input("Enter the city to find weather: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={place}&appid={api_key}"

response = requests.get(url)

print(response.json()["main"]["temp"])  

convert_kelvin_to_celsius = response.json()["main"]["temp"] - 273.15

print(f"The temperature in {place} is {convert_kelvin_to_celsius: .2f} degree celsius")