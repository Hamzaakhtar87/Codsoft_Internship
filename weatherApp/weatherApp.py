from pyowm import OWM
from config import API_key

def get_weather_forecast(city_name):
    owm = OWM(API_key)
    mgr = owm.weather_manager()

    try:
        observation = mgr.weather_at_place(city_name)
        weather = observation.weather
        return weather
    except Exception as e:
        print("Error:", e)
        return None

def display_forecast(weather):
    temperature = weather.temperature(unit='celsius')
    wind = weather.wind()
    humidity = weather.humidity
    status = weather.status
    detailed_status = weather.detailed_status

    print("\nWeather Forecast:")
    print(f"Temperature: {temperature['temp']}°C")
    print(f"Wind Speed: {wind['speed']} m/s")
    print(f"Humidity: {humidity}%")
    print(f"Conditions: {status}, {detailed_status}")

if __name__ == "__main__":
    print("Weather Forecast Application")
    print("---------------------------")

    while True:
        city_name = input("Enter city name (or 'exit' to quit): ")
        
        if city_name.lower() == 'exit':
            print("Exiting the application.")
            break

        weather = get_weather_forecast(city_name)
        
        if weather:
            display_forecast(weather)
        
        repeat = input("Do you want to check weather for another city? (yes/no): ")
        if repeat.lower() != 'yes':
            print("Exiting the application.")
            break