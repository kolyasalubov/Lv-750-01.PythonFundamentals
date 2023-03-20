from pyowm import OWM


API_KEY = '78afeb17fba59dee035d9ca446615fee'
# ---------- FREE API KEY examples ---------------------

owm = OWM(API_KEY)
mgr = owm.weather_manager()

def observation(city):
    observation = mgr.weather_at_place(city)
    w = observation.weather
#     wind = w.wind()                  # {'speed': 4.6, 'deg': 330
#     temperature = w.temperature
#      # temperature_max = w.temperature('celsius')['temp_max'], 
    return print(f"Tempertuure - {w.temperature} ('celsius')", 
                 f"Wind - {w.wind}") 