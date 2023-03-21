from pyowm import OWM


API_KEY = '78afeb17fba59dee035d9ca446615fee'
# ---------- FREE API KEY examples ---------------------

owm = OWM(API_KEY)
mgr = owm.weather_manager()

# Search for current weather in London (Great Britain) and get details

def observation(entry_field):
    observation_city = mgr.weather_at_place(entry_field)
    w = observation_city.weather
    return print(f"In {entry_field} the temperature is {w.temperature} ('celsius')"
                 f"Humidity - {w.humidity}"
                 f"Speed of wind - {w.wind} m/s")