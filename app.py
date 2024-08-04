import requests


def get_weather(city):
    api_key = "f47667a6aac6467596b214543240907"
    base_url = "http://api.weatherapi.com/v1/current.json"
    complete_url = f"{base_url}?key={api_key}&q={city}"
    response = requests.get(complete_url)
    return response.json()


def main():
    city = input("Enter city name: ")
    weather_data = get_weather(city)
    print(weather_data)


if __name__ == "__main__":
    main()
