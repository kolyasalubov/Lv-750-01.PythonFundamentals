from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

# ---------- FREE API KEY examples ---------------------

owm = OWM('ef2206ff5da67de63306d0b143e20872')
mgr = owm.weather_manager()

input_city = input('Choose youp city:')
# Search for current weather in London (Great Britain) and get details
observation = mgr.weather_at_place(input_city)
w = observation.weather

cloud = w.detailed_status         # 'clouds'
wind = w.wind()                  # {'speed': 4.6, 'deg': 330}
humidity = w.humidity                # 87
temperature = w.temperature('celsius')['temp']  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
temperature_max = w.temperature('celsius')['temp_max']
temperature_min = w.temperature('celsius')['temp_min']
w.rain                    # {}
w.heat_index              # None
w.clouds                  # 75

print(f"In {input_city} the cloud {cloud}")
print(f"In {input_city} the wind speed {wind} m/h")
print(f"In {input_city} the cloud {temperature} C")
print(f"In {input_city} the temperature min {temperature_min} C")
print(f"In {input_city} the temperature max {temperature_max} C")