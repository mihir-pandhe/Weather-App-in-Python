import requests
import json
import os

CACHE_FILE = "weather_cache.json"


def get_weather(city):
    api_key = "f47667a6aac6467596b214543240907"
    base_url = "http://api.weatherapi.com/v1/current.json"
    complete_url = f"{base_url}?key={api_key}&q={city}"
    try:
        response = requests.get(complete_url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None


def display_weather(data):
    if "current" in data:
        temp = data["current"]["temp_c"]
        humidity = data["current"]["humidity"]
        wind_speed = data["current"]["wind_kph"]
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} kph")
    else:
        print("Error: Invalid data format received.")


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
                    if weather_data:
                        cache_weather(city, weather_data)
                if weather_data:
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
