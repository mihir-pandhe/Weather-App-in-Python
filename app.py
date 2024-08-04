import requests


def get_weather(city):
    api_key = "f47667a6aac6467596b214543240907"
    base_url = "http://api.weatherapi.com/v1/current.json"
    complete_url = f"{base_url}?key={api_key}&q={city}"
    response = requests.get(complete_url)
    return response.json()


def display_weather(data):
    temp = data["current"]["temp_c"]
    humidity = data["current"]["humidity"]
    wind_speed = data["current"]["wind_kph"]
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} kph")


def main():
    cities = input("Enter city names separated by commas: ").split(",")
    for city in cities:
        weather_data = get_weather(city.strip())
        print(f"Weather in {city.strip()}:")
        display_weather(weather_data)
        print()


if __name__ == "__main__":
    main()
