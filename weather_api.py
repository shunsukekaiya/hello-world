#encoding:utf-8
# import urllib2, sys
import requests
import json

odawara = {'city': '140020'}
url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
response = requests.get(url, params=odawara)
weather_data = json.loads(response.text)

print(weather_data['forecasts'][0]['telop'])

# # 読み込んだJSONデータをディクショナリ型に変換
# resp = json.loads(resp)
# print ('**************************')
# print(resp['title'])
# print ('**************************')
# print(resp['description']['text'])

# for forecast in resp['forecasts']:
#     print ('**************************')
#     print(forecast['dateLabel']+'('+forecast['date']+')')
#     print(forecast['telop'])
# print ('**************************')