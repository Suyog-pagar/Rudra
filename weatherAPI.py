

import requests


def weatherCheck():
    global wind_report, weather_report, pressure, humidity, temp_feel_like, temperature
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    CITY = "nashik"
    API_KEY = "3071548b8741c3acf8f65b063b361aef"
    URL = BASE_URL + "q=" + CITY + "&units=metric&APPID=" + API_KEY  # Fixed URL formatting
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        temperature = main['temp']  # Use 'temperature' here instead of 'temperatur'
        temp_feel_like = main['feels_like']
        humidity = main['humidity']
        pressure = main['pressure']
        weather_report = data['weather']
        wind_report = data['wind']

        print(f"{CITY:-^35}")
        print(f"City ID: {data['id']}")
        print(f"Temperature: {temperature}")  # Use 'temperature' here
        print(f"Feel Like: {temp_feel_like}")
        print(f"Humidity: {humidity}")
        print(f"Pressure: {pressure}")
        print(f"Weather Report: {weather_report[0]['description']}")
        print(f"Wind Speed: {wind_report['speed']}")
        print(f"Time Zone: {data['timezone']}")
    else:
        print("Error in the HTTP request")

    return temperature, temp_feel_like, humidity, pressure, weather_report, wind_report


if __name__ == '__main__':
    temp, tempFeelsLike, hum, pressure, weatherReport, wind = weatherCheck()

    print(f"Temperature: {temp}")
    print(f"Feel Like: {tempFeelsLike}")
    print(f"Humidity: {hum}")
    print(f"Pressure: {pressure}")
    print(f"Weather Report: {weatherReport}")
    print(f"Wind Speed: {wind}")
