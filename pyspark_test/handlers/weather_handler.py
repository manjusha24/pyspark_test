import json
import falcon
from pyspark_test.services import weather_service

class WeatherDataHandler():
    def on_get(self, req, resp):
        data = weather_service.get_weather_data()
        resp.status = falcon.HTTP_200
        resp.body = json.dumps({"weather_data": data})
