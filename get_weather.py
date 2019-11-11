import requests
import json

def get_weather(city):
    if city == tokyo:
        city_id = {'city': '130010'}
        url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
        response = requests.get(url, params=city_id)
        weather_data = json.loads(response.text)
        return weather_data
