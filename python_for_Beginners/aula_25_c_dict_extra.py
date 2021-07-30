data_json = []
data_json = [
        {
            'measurement': "temperature_bmp",
            'tags': {
                'location': weather_station
            },
            "time": measurement_time,
            'fields': {
                'value': temperature_bmp
            }
        }
]

# em todos os dados muda apenas nome da medida e valor da medida
# se o valor for valido, não aridiona o json
# ou, se valor invalido, remove o item da lista
def checks_measurement(measurement: str, data_type: str):
    """
    Checks if the measurement received by the ESP8266 is a valid or a serial
    communication failure occurred between ESP8266 and others microcontrollers.
    If failure occurred the value received is equals "snr" (serial not received)

    Parameters:
        measurement received via MQTT (str)

    Returns:
        measurement (null, int, float or str)
    """
    # if "snr" or other error
    if not(measurement.replace(".", "", 1).isdigit()):
        measurement_verified = "null"
    elif data_type == "int":
        measurement_verified = int(measurement)
    elif data_type == "float":
        measurement_verified = float(measurement)

    return measurement_verified


def measurement_processing(json: list, measurement_raw: str, measurement_name: str, data_type: str) -> dict:
    measurement = checks_measurement(measurement_raw, data_type)

    if not(measurement == "null")
    json_measurement = json[1]
    json_measurement = {
            'measurement': "temperature_bmp",
            'tags': {
                'location': weather_station
            },
            "time": measurement_time,
            'fields': {
                'value': temperature_bmp
            }
    }

    return