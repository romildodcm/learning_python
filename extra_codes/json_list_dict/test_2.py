# {
#     'measurement': 'solar1',
#     'tags': {
#         'location': 'weather_station_id'
#         },
#     'time': '2021-07-29T00:49:55Z',
#     'fields': {
#         'value': 860.0
#         }
# }
# a_dictionary = {
#     'measurement': 'temperature_bmp',
#     'tags': {
#         'location': 'ws01'
#     },
#     'time': '2021-07-29T00:49:55Z',
#             'fields': {
#                 'value': 25.40
#     }
# }


# a_list = []

# dictionary_copy = a_dictionary.copy()
# a_list.append(dictionary_copy)

# a_dictionary = {"name": "Ro", "age": 24}

# dictionary_copy = a_dictionary.copy()
# a_list.append(dictionary_copy)

# print(a_list)
def checks_measurement(measurement: str, expected_type: str):
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
    elif expected_type == "int":
        measurement_verified = int(measurement)
    elif expected_type == "float":
        measurement_verified = float(measurement)

    return measurement_verified


def append_measurement(data_list: list,
                       measurement_dict: dict,
                       measurement_raw: str,
                       measurement_name: str,
                       data_type: str) -> list:

    # measurement_stamp = {
    #     'measurement': 'measurement_name',
    #     'tags': {
    #         'location': 'weather_station'
    #     },
    #     'time': 'ISO_timestamp',
    #     'fields': {
    #         'value': 42
    #     }
    # }
    measurement = checks_measurement(measurement_raw, data_type)

    # se measurement != "null" eu atualizo o json que entrou
    if measurement != "null":
        # debug

        print("Before data measurement_point:")
        print(measurement_dict)

        measurement_dict['measurement'] = measurement_name
        measurement_dict['fields']['value'] = measurement

        print("After data measurement_dict:")
        print(measurement_dict)

        data_list.append(measurement_dict.copy())

    return data_list


def data_processing(data_csv: str, weather_station: str) -> list:
    """
    Receives a csv string like:
    "20210726153318,38.64,98771.21,27.89,39.55,N,21.28,140.75,1" or
    "20210724201304,27.25,99085.42,27.26,45.89,NW,0.00,0.00,snr,snr,1",
    process the data and returns a JSON for database.

    Parameters:
        data_csv (str): data received via MQTT
        weather_station (str): MQTT topic/weather station id

    Returns:
        wind direction measure in degrees
    """

    data_names_9 = [
        "temperature_bmp",
        "pressure_bmp",
        "temperature_sht",
        "humidity_sht",
        "wind_direction",
        "anemometer",
        "pluviometer_raw",
        "sd_memory_status"
    ]

    data_names_11 = [
        "temperature_bmp",
        "pressure_bmp",
        "temperature_sht",
        "humidity_sht",
        "wind_direction",
        "anemometer",
        "pluviometer_raw",
        "serial_sensor1",
        "serial_sensor2",
        "sd_memory_status"
    ]

    data = data_csv.split(",")
    data_length = len(data)

    # If no solar data length = 9, if with solar data length = 11
    if data_length == 9:
        for i in range(1, 9):
            print(data_names_11[i])
            # fazer o processo de gerar o json
    elif data_length == 11:
        for i in range(1, 11):
            print(data_names_11[i])
            # fazer o processo de gerar o json





    time = '2021-07-29T00:49:55Z'
    location = 'ws_test'

    measurement_stamp = {
        'measurement': 'measurement_name',
        'tags': {
            'location': location
        },
        'time': time,
        'fields': {
            'value': 42
        }
    }

    a_list = []
    a_dictionary = {"name": "Ro", "age": 24}
    print(a_dictionary)
    # print(dictionary_copy)
    a_list.append(a_dictionary.copy())
    print(a_list)
    a_list = append_measurement(a_list,
                                measurement_stamp,
                                "25.60",
                                "temperature_sht",
                                "float")
    a_list = append_measurement(a_list,
                                measurement_stamp,
                                "860",
                                "solar1",
                                "float")
    print("Lista final:")
    print(a_list)
    print(*a_list, sep="\n")


sample_9 = "20210729021505,3.44,100447.61,5.10,66.85,SW,0.00,166.75,1"
sample_11 = "20210729021555,18.72,100546.48,18.51,45.57,NW,0.00,0.00,336,908,1"
weather_station_id = "ws_test"

data_processing(sample_11, weather_station_id)
