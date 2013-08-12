forecast\_io
===========

Python3 handler library for forecast.io data.

Example usage:

    import forecast_io

    forecast = forecast_io.get_forecast(api_key, latitude, longitude)


The call to `get_forecast` returns a `Forecast` object containing properties corresponding to all the values present in the returned data, as specified in the API documentation.

See [the Forecast v2 API](https://developer.forecast.io/docs/v2) for details on the resulting data.
