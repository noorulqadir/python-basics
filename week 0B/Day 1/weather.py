import requests

city = input("Enter a city name: ")
url = f'https://wttr.in/{city}?format=3'

try:
    response = requests.get(url)
    response.raise_for_status()
    print(response.text)

except requests.RequestException as e:
    print("Error fetching weather: ", e)