import requests
import json
import os

CACHE_FILE = "weather_cache.json"


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


def cache_weather(city, data):
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as file:
            cache = json.load(file)
    else:
        cache = {}
    cache[city] = data
    with open(CACHE_FILE, "w") as file:
        json.dump(cache, file)


def get_cached_weather(city):
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as file:
            cache = json.load(file)
        if city in cache:
            return cache[city]
    return None


def main():
    favorite_cities = []
    while True:
        command = input("Enter command (weather, add_favorite, show_favorites, quit): ")
        if command == "weather":
            cities = input("Enter city names separated by commas: ").split(",")
            for city in cities:
                city = city.strip()
                weather_data = get_cached_weather(city)
                if not weather_data:
                    weather_data = get_weather(city)
                    cache_weather(city, weather_data)
                print(f"Weather in {city}:")
                display_weather(weather_data)
                print()
        elif command == "add_favorite":
            city = input("Enter city name to add to favorites: ").strip()
            if city not in favorite_cities:
                favorite_cities.append(city)
                print(f"{city} added to favorites.")
            else:
                print(f"{city} is already in favorites.")
        elif command == "show_favorites":
            print("Favorite Cities:")
            for city in favorite_cities:
                print(city)
        elif command == "quit":
            break


if __name__ == "__main__":
    main()
