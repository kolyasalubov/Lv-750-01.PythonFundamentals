from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

# ---------- FREE API KEY examples ---------------------

owm = OWM('ef2206ff5da67de63306d0b143e20872')
mgr = owm.weather_manager()

city = input("Enter citys's name: ")


# Search for current weather in London (Great Britain) and get details
observation = mgr.weather_at_place(city)
w = observation.weather

w.detailed_status         # 'clouds'
w_w = w.wind()['speed']                 # {'speed': 4.6, 'deg': 330}
w_h = w.humidity                # 87
w_t = w.temperature('celsius')['temp']  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
w.rain                    # {}
w.heat_index              # None
w.clouds                  # 75

print(f"The wind speed in {city} is |{w_w}| km/hours")
print(f"The humidity of the air in {city} is |{w_h}|")
print(f"The temperatura of the air in {city} is |{w_t}| degrees")

