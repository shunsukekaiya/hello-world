import responder
import get_weather

api = responder.API()

@api.route("/")
def hello_world(req, resp):
    city = tokyo
    weather_data = get_weather(city)
    print(weather_data['forecasts'][0]['telop'])

    resp.text = weather_data['forecasts'][0]['telop']

if __name__ == '__main__':
    api.run()
