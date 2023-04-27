
import os

# create folder structure
os.makedirs('realtime_weather_analysis/aws')
os.makedirs('realtime_weather_analysis/GOES_satellite_data')
os.makedirs('realtime_weather_analysis/fastapi')
os.makedirs('realtime_weather_analysis/airflow')

# create empty files
open('realtime_weather_analysis/aws/lambda.py', 'w').close()
open('realtime_weather_analysis/aws/kinesis.py', 'w').close()
open('realtime_weather_analysis/aws/s3.py', 'w').close()

open('realtime_weather_analysis/GOES_satellite_data/data_processing.py', 'w').close()

open('realtime_weather_analysis/fastapi/data_interface.py', 'w').close()

open('realtime_weather_analysis/airflow/data_processing_tasks.py', 'w').close()
open('realtime_weather_analysis/airflow/scheduling.py', 'w').close()
