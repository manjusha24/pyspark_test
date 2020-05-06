import falcon
import requests

from requests.packages.urllib3.exceptions import InsecureRequestWarning

from .handlers.weather_handler import WeatherDataHandler

# Turning off Insecure Request Warning for when we make calls with ssl issues or non-https
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
api = application = falcon.API()

api.add_route('/weather_data', WeatherDataHandler())

