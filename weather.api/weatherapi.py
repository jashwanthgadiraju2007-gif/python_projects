import requests
import os

CURRENT_URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = os.getenv("OPENWEATHER_API_KEY")


def get_current_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(CURRENT_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        show_current_weather(data)
    else:
        print("❌ City not found or API issue.")


def show_current_weather(data):
    print("\n🌍 Location :", data["name"], ",", data["sys"]["country"])

    print("\n🌡️ Today Temperature")
    print("Current :", data["main"]["temp"], "°C")
    print("Min     :", data["main"]["temp_min"], "°C")
    print("Max     :", data["main"]["temp_max"], "°C")

    print("\n🌬️ Wind Speed :", data["wind"]["speed"], "m/s")
    print("☁️ Condition  :", data["weather"][0]["description"])


def main():
    city = input("Enter city name: ").strip()

    if not city:
        print("❌ City name cannot be empty.")
        return

    get_current_weather(city)


main()
