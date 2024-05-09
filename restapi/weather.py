from typing import Dict, Any

import requests


def kelvin_to_celsius(kelvin_temperature: float) -> float:
    return round(kelvin_temperature - 273.15, 2)


def get_weather(city: str = "Toronto", country_code: str = "") -> Dict[str, Any]:
    api_key = "ec009e0b4a68a197698765ec1758ed7c"
    base_url = "https://api.openweathermap.org/data/2.5/weather?"

    complete_url = base_url + "appid=" + api_key + "&q=" + city + "," + country_code
    response = requests.get(complete_url)
    data = response.json()
    response_cod = data["cod"]
    response_message = data.get("message")
    country = data['sys']['country'] if data.get('sys') else None

    if response_cod != 200:
        print(f"An error occurred while getting weather information. Error: {response_cod} - {response_message}")
        return {
            "temperature": "Not available",
            "pressure": "Not available",
            "humidity": "Not available",
            "description": "Not available",
            "city": city,
            "country": country
        }
    else:
        main_data = data["main"]
        current_pressure = main_data["pressure"]
        current_humidity = main_data["humidity"]
        current_kelvin_temperature = main_data["temp"]
        weather_description = data["weather"][0]["description"]
        current_celsius_temperature = kelvin_to_celsius(current_kelvin_temperature)

        weather_data = {
            "temperature": current_celsius_temperature,
            "pressure": current_pressure,
            "humidity": current_humidity,
            "description": weather_description,
            "city": city,
            "country": country
        }

        return weather_data


if __name__ == "__main__":
    city = "rio"
    weather = get_weather(city)
    print(weather)
