import ephem
import math
from ephem import Angle
from datetime import datetime, timedelta


class PhotoVoltaic:
    def __init__(self, latitude, longitude, full_power: float):
        self.latitude = latitude
        self.longitude = longitude
        self.full_power = full_power

    def calculate_sun_position(self, date_time: datetime):
        observer = ephem.Observer()
        observer.lat = str(self.latitude)
        observer.lon = str(self.longitude)
        observer.date = date_time

        sun = ephem.Sun(observer)
        altitude = sun.alt
        azimuth = sun.az

        return (altitude, azimuth)

    def power(self, date_time: datetime) -> float:
        altitude, azimuth = pv.calculate_sun_position(date_time)
        return math.sin(altitude) * self.full_power

    def toFixed(self, numObj, digits=0):
        return f'{numObj:.{digits}f}'


# Specify your location and time
lat = 50.06164479035707
long = 19.93741239489708

pv = PhotoVoltaic(lat, long, 7)

dt1 = datetime(2023, 6, 8, 8, 00)
dt2 = datetime(2023, 6, 8, 16, 00)  # for 8th June 2023, 13:45

print(f'Power is {pv.toFixed(pv.power(dt1), 4)} Kw')
print(f'Power is {pv.toFixed(pv.power(dt2), 4)} Kw')



start = datetime(2023, 6, 8, 6, 0)
end = datetime(2023, 6, 8, 18, 0)

step = timedelta(minutes=1)
summ = 0

while start <= end:
    power_current = pv.power(start)
    kWh = power_current / 60
    summ += kWh
    # print(f'{kWh}Kw || {start}')
    start += step

print(summ, 'Kw')

# print(f'Altitude is {altitude} {type(altitude)} // Azimuth is {azimuth} {type(azimuth)}')

