import datetime

class Forecast:
    def __init__(self, data):
        self._json = data

        try:
            self.latitude = self._json['latitude']
        except:
            pass

        try:
            self.longitude = self._json['longitude']
        except:
            pass

        try:
            self.timezone = self._json['timezone']
        except:
            pass

        try:
            self.offset = self._json['offset']
        except:
            pass

        try:
            self.currently = DataPoint(self._json['currently'])
        except:
            pass

        try:
            self.minutely = DataBlock(self._json['minutely'])
        except:
            pass

        try:
            self.hourly = DataBlock(self._json['hourly'])
        except:
            pass

        try:
            self.daily = DataBlock(self._json['daily'])
        except:
            pass

        try:
            self.alerts = [Alert(alert) for alert in self._json['alerts']]
        except:
            pass

        try:
            self.flags = Flags(self._json['flags'])
        except:
            pass

    def __str__(self):
        return self._json.__str__()

class DataBlock:
    def __init__(self, data):
        self._json = data
        try:
            self.summary = data['summary']
        except:
            pass

        try:
            self.icon = data['icon']
        except:
            pass

        try:
            self.data = [DataPoint(point) for point in data['data']]
        except:
            pass

    def __str__(self):
        return self._json.__str__()

class DataPoint:
    def __init__(self, data):
        self._json = data
        try:
            time = int(data['time'])
            self.time = datetime.datetime.fromtimestamp(time)
        except:
            pass

        try:
            self.summary = data['summary']
        except:
            pass

        try:
            self.icon = data['icon']
        except:
            pass

        try:
            time = int(data['sunriseTime'])
            self.sunriseTime = datetime.datetime.fromtimestamp(time)
        except:
            pass

        try:
            time = int(data['sunsetTime'])
            self.sunsetTime = datetime.datetime.fromtimestamp(time)
        except:
            pass

        try:
            self.precipIntensity = data['precipIntensity']
        except:
            pass

        try:
            self.precipIntensityMax = data['precipIntensityMax']
        except:
            pass

        try:
            time = data['precipIntensityMaxTime']
            self.precipIntensityMaxTime = datetime.datetime.fromtimestamp(time)
        except:
            pass

        try:
            self.precipProbability = data['precipProbability']
        except:
            pass

        try:
            self.precipType = data['precipType']
        except:
            pass

        try:
            self.precipAccumulation = data['precipAccumulation']
        except:
            pass

        try:
            self.temperature = data['temperature']
        except:
            pass

        try:
            self.temperatureMin = data['temperatureMin']
        except:
            pass

        try:
            time = data['temperatureMinTime']
            self.temperatureMinTime = datetime.datetime.fromtimestamp(time)
        except:
            pass

        try:
            self.temperatureMax = data['temperatureMax']
        except:
            pass

        try:
            time = data['temperatureMaxTime']
            self.temperatureMaxTime = datetime.datetime.fromtimestamp(time)
        except:
            pass

        try:
            self.dewPoint = data['dewPoint']
        except:
            pass

        try:
            self.windSpeed = data['windSpeed']
        except:
            pass

        try:
            self.windBearing = data['windBearing']
        except:
            pass

        try:
            self.cloudCover = data['cloudCover']
        except:
            pass

        try:
            self.humidity = data['humidity']
        except:
            pass

        try:
            self.pressure = data['pressure']
        except:
            pass

        try:
            self.visibility = data['visibility']
        except:
            pass

        try:
            self.ozone = data['ozone']
        except:
            pass

    def __str__(self):
        return self._json.__str__()

class Alert:
    def __init__(self, data):
        self._json = data
        try:
            self.title = data['title']
        except:
            pass

        try:
            time = data['expires']
            self.expires = datetime.datetime.fromtimestamp(time)
        except:
            pass

        try:
            time = data['time']
            self.time = datetime.datetime.fromtimestamp(time)
        except:
            pass

        try:
            self.description = data['description']
        except:
            pass

        try:
            self.URI = data['uri']
        except:
            pass

    def __str__(self):
        return self._json.__str__()

class Flags:
    def __init__(self, data):
        self._json = data
        try:
            self.darksky_unavailable = data['darksky-unavailable']
        except:
            pass

        try:
            self.darksky_stations = data['darksky-stations']
        except:
            pass

        try:
            self.datapoint_stations = data['datapoint-stations']
        except:
            pass

        try:
            self.isd_stations = data['isd-stations']
        except:
            pass

        try:
            self.lamp_stations = data['lamp-stations']
        except:
            pass

        try:
            self.metar_stations = data['metar-stations']
        except:
            pass

        try:
            self.metno_license = data['metno-license']
        except:
            pass

        try:
            self.sources = data['sources']
        except:
            pass

        try:
            self.units = data['units']
        except:
            pass

    def __str__(self):
        return self._json.__str__()
