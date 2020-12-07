'''
I this class, the teacher had used as an example as Microsoft Azure
Computer Vision API, for that is necessary creates an account...

To practice, I chose with Mars Weather Service API of NASA Open APIs:
https://api.nasa.gov/

'''
import json
import requests

def elysiumWeather():
    """
    This function returns the weather condidions
    for Elysium Planitia region of Mars
    """

    api_url = r"https://api.nasa.gov/insight_weather/?api_key=DEMO_KEY&feedtype=json&ver=1.0"

    raw_data = requests.get(api_url)

    return json.loads(raw_data.text)

weather_data = elysiumWeather()

print(elysiumWeather())