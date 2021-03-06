'''
I this class, the teacher had used as an example as Microsoft Azure
Computer Vision API, for that is necessary creates an account...

To practice, I chose with Mars Weather Service API of NASA Open APIs:
api.nasa.gov
api.nasa.gov/assets/insight/InSight%20Weather%20API%20Documentation.pdf
'''
import os
import json
import requests
from colorama import init, Fore
from dotenv import load_dotenv
from requests import api
from time import sleep

load_dotenv()
nasa_api_key = os.getenv('APIKEY')

def elysiumWeather():
    """
    This function returns the weather condidions
    for Elysium Planitia region of Mars
    """

    api_url = r"https://api.nasa.gov/insight_weather/?api_key="
    api_url = api_url + nasa_api_key + r'&feedtype=json&ver=1.0'

    raw_data = requests.get(api_url)
    # JSON to Python dictionaryand return as result
    return json.loads(raw_data.text)

while(1):
    weather_data = elysiumWeather()

    # Check the last SOL data
    last_sol_index = len(weather_data["sol_keys"]) - 1
    sol_key = str(weather_data["sol_keys"][last_sol_index])

    season = weather_data[sol_key]["Season"]
    pressure_average = str(weather_data[sol_key]["PRE"]["av"])
    last_time = weather_data[sol_key]["Last_UTC"]

    print('---', end = ' ')
    print(Fore.RED + 'InSight - Mars Weather Service', end = ' ')
    print(Fore.WHITE + '---')
    print(Fore.BLUE + f'SOL: {sol_key}\nSeason: {season}')
    print(Fore.BLUE + "Atmospheric pressure (Pa): " + str(pressure_average))
    print(Fore.BLUE + "Last UTC time: " + last_time)

    print('Validity checks/SOLs checkeds:')
    for item in weather_data["validity_checks"]["sols_checked"]:
        print(item, end = ' ')
    print(Fore.WHITE + '\n--------------------------------------')
    
    sleep(60)