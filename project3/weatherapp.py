import requests
import json

# Function to fetch weather data
def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    forecast_url = "http://api.openweathermap.org/data/2.5/forecast?"

    # Construct final url
    complete_url = base_url + "q=" + city_name + "&appid=" + api_key + "&units=metric"
    complete_forecast_url = forecast_url + "q=" + city_name + "&appid=" + api_key + "&units=metric"

    # Get the response from the server
    response = requests.get(complete_url)
    forecast_response = requests.get(complete_forecast_url)

    # Check the response status code
    if response.status_code == 200:
        # Parse the JSON data
        data = response.json()
        forecast_data = forecast_response.json()

        # Extract relevant data
        main = data['main']
        weather = data['weather'][0]
        wind = data['wind']

        current_weather = {
            "Temperature": main['temp'],
            "Humidity": main['humidity'],
            "Pressure": main['pressure'],
            "Weather Description": weather['description'],
            "Wind Speed": wind['speed']
        }

        forecast_list = forecast_data['list']
        forecast = []
        for item in forecast_list:
            forecast.append({
                "Date": item['dt_txt'],
                "Temperature": item['main']['temp'],
                "Weather Description": item['weather'][0]['description']
            })

        return current_weather, forecast
    else:
        return None, None

# Function to display weather data
def display_weather(city_name, current_weather, forecast):
    print(f"\nWeather in {city_name.capitalize()}:\n")
    print(f"Current Temperature: {current_weather['Temperature']}°C")
    print(f"Humidity: {current_weather['Humidity']}%")
    print(f"Pressure: {current_weather['Pressure']} hPa")
    print(f"Weather Description: {current_weather['Weather Description']}")
    print(f"Wind Speed: {current_weather['Wind Speed']} m/s")
    
    print(f"\nWeather Forecast:\n")
    for day in forecast:
        print(f"Date: {day['Date']}, Temperature: {day['Temperature']}°C, Weather: {day['Weather Description']}")

# Main function
def main():
    api_key = "32ac197e3408d1952522386fef82f40e"
    city_name = input("Enter city name: ")

    current_weather, forecast = get_weather(city_name, api_key)

    if current_weather:
        display_weather(city_name, current_weather, forecast)
    else:
        print("City Not Found or API Error")

if __name__ == "__main__":
    main()
