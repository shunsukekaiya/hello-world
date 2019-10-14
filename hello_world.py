import responder
import requests
import json

api = responder.API()

@api.route("/")
def hello_world(req, resp):
    odawara = {'city': '140020'}
    url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
    response = requests.get(url, params=odawara)
    weather_data = json.loads(response.text)
    print(weather_data['forecasts'][0]['telop'])

    resp.text = "hello,world!"

if __name__ == '__main__':
    api.run()
