from typing import Any
from pandas import DataFrame, to_datetime, Series
from json import loads

def convert_and_clean_heartrate(workout_data: dict[str, Any]) -> Series:
    """This method gets the dictionary with the data from a single workout, and creates 
    a series where the values are the HeartBeats and the index is a timestamp. The 
    information regarding the unit of measure (which is expected to be 'bpm') is saved 
    in the `attrs` field of the Series.
    

    Parameters
    ----------
    workout_data : dict[str, Any]
        dictionary containing all of the information regarding a single workout data

    Returns
    -------
    Series
        the method returns a series with the heartbeats and the timestamp as the index
        
    Example
    -------
    >>> json_file_path: str = './HealthAutoExport-2022-05-05-2022-05-05.json'
    >>> list_of_series = json_get_heartrate(json_file_path)
    >>> list_of_series[0]
    date
    2022-05-05 10:53:40+02:00    82
    2022-05-05 10:53:45+02:00    82
    2022-05-05 10:53:47+02:00    82
    2022-05-05 10:53:55+02:00    73
    2022-05-05 10:53:56+02:00    72
                                ..
    2022-05-05 10:59:31+02:00    66
    2022-05-05 10:59:40+02:00    67
    2022-05-05 10:59:45+02:00    67
    2022-05-05 10:59:48+02:00    68
    2022-05-05 10:59:54+02:00    67
    Name: qty, Length: 75, dtype: int64
    >>> list_of_series[0].attrs
    {'unit': 'bpm'}

    Raises
    ------
    AttributeError
        If the 'heartRateData' field is not present, the method will fail
    """
    if workout_data.get('heartRateData', None) is None:
        raise AttributeError(f"Key 'heartRateData' not found in workout data.\
            \nKeys available: {workout_data.keys()}")
        
    heart_rate_data = DataFrame(workout_data['heartRateData'])
    heart_rate_data['date'] = to_datetime(heart_rate_data['date'])
    heart_rate_data = heart_rate_data.set_index('date')
    heart_rate_data.attrs['unit'] = heart_rate_data['units'].unique()[0]
    heart_rate_data = heart_rate_data.drop(columns=['units'])
    return heart_rate_data['qty']
    

def json_get_heartrate(json_file_path: str) -> list[Series]:
    """This method will read a json file with Health Data from the iPhone and Apple Watch,
    as exported by the [Auto Export](https://apps.apple.com/us/app/health-auto-export-json-csv/id1115567069) 
    application, and returns a list of Series, where each Series is the timeseries of 
    the heartbeat for a single workout. 

    Parameters
    ----------
    json_file_path : str
        path to the json file

    Returns
    -------
    list[Series]
        the method returns a list of Series, in order of workout for the timeframe selected
    """
    with open(json_file_path, 'r') as j:
        data: dict[str, Any] = loads(j.read())
    
    return [convert_and_clean_heartrate(workout_data) 
            for workout_data in data['data']['workouts']]
    