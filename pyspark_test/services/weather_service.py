import pyspark
from pyspark_test.clients import weather_client
from pyspark_test.util import cities
from pyspark.sql import SparkSession
from pyspark.sql.functions import min, max

def get_weather_data():
    weather_client.get_data(cities)
    temp_values = find_min_max_temps()
    return temp_values

def find_min_max_temps():
	spark = SparkSession.builder.appName("weather_data").getOrCreate()
	df = spark.read.json('data.json')
	df.write.mode('append').parquet("weather.parquet")
	pf = spark.read.parquet("weather.parquet")
	max_temp = pf.agg({'temp': 'max'}).collect()
	min_temp = pf.agg({'temp': 'min'}).collect()
	min_max = pf.select(min('temp').alias('min_temp'), max('temp').alias('max_temp')).collect()
	row = min_max[0].asDict()
	return {'Maximum Temperature': row['max_temp'], 'Minimum Temp': row['min_temp']}
