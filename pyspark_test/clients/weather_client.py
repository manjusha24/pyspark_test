import grequests
import json
from pyspark_test.settings import config
from datetime import datetime

wd_base_url = config.weather_data_api.base_url
api_key = config.API_KEY.api_key

def get_data(cities):
	urls=[]
	for city in cities:
		endpoint = "{weather_data_url}?q={city}&APPID={api_key}".format(weather_data_url=wd_base_url, city=city, api_key=api_key)
		urls.append(endpoint)

	try:
		rs = (grequests.get(url) for url in urls)
		responses = grequests.map(rs, exception_handler=exception_handler)
	except Exception:
		return {"Error": "Error occured during weather data get call"}

	with open('data.json', 'w') as output_file:
		date = str(datetime.now())
		json.dump(([{'temp':resp.json()['main']['temp'],'city':resp.json()['name'], 'date': date} for resp in responses if resp.status_code==200]), output_file)
	return True