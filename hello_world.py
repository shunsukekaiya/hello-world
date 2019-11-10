import responder
import requests
import json

api = responder.API()

@api.route("/")
def hello_world(req, resp):
    tokyo = {'city': '130010'}
    url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
    response = requests.get(url, params=tokyo)
    weather_data = json.loads(response.text)
    print(weather_data['forecasts'][0]['telop'])

    resp.text = weather_data['forecasts'][0]['telop']

if __name__ == '__main__':
    api.run()
