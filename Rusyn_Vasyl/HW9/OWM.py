from pyowm import OWM


API_KEY = 'ef2206ff5da67de63306d0b143e20872'
# ---------- FREE API KEY examples ---------------------

owm = OWM(API_KEY)
mgr = owm.weather_manager()


# Search for current weather in London (Great Britain) and get details
def observation(place):
    observation = mgr.weather_at_place(place)
    w = observation.weather
    return f'Today is {w.detailed_status}, wind is {w.wind()["speed"]}, \n' \
           f'{w.humidity}% humidity and temperature is {w.temperature("celsius")["temp_max"]}'







