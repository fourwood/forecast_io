import urllib.request
import urllib.error
import json
from forecast_io.forecast import Forecast

URL_BASE = "http://api.forecast.io/forecast/"

def _make_url(api_key, lat, lon, time=None, **kwargs):
    url = "{0}/{1},{2}".format(api_key,lat,lon)

    if time is not None:
        url += ",{0}".format(time)

    options = ""
    for option, value in kwargs:
        options += "?{0}={1}".format(option, value)

    url = URL_BASE + url + options
    return url

def _retrieve_json(response):
    response_text = response.read().decode()
    forecast = json.loads(response_text)
    return forecast

def get_forecast(api_key, lat, lon, time=None, units='auto'):
    if time is not None:
        time = time.isoformat()
    url = _make_url(api_key, lat, lon, time)#, units=units)

    request = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(url)
    except urllib.error.URLError as error:
        if hasattr(error, 'reason'):
            print("Error: failed to reach the forecast.io server.")
            print("Reason: ", error.reason)
        elif hasattr(error, 'code'):
            print("Error: the server couldn\'t fulfill the request.")
            print("Error code: ", error.code)

    data = _retrieve_json(response)

    forecast = Forecast(data)
    return forecast
