import tkinter as tk
from tkinter import font
from pyowm import OWM


API_KEY = 'ef2206ff5da67de63306d0b143e20872'
# ---------- FREE API KEY examples ---------------------

owm = OWM(API_KEY)
mgr = owm.weather_manager()

def get_weather():
# Search for current weather in the city and get details
    city = entry_field.get()
    observation = mgr.weather_at_place(city)
    w = observation.weather

    details = f"Conditions: {w.detailed_status}\n"         # 'clouds'
    details +=f"Wind: {w.wind()}\n"                        # {'speed': 4.6, 'deg': 330}
    details +=f"Humidity: {w.humidity}\n"                  # 87
    details +=f"Temperature: {w.temperature('celsius')}\n" # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    details +=f"Rain: {w.rain}\n"                          # {}
    details +=f"Heat index: {w.heat_index}\n"              # None
    details +=f"Clouds: {w.clouds}\n"                      # 75
    label['text'] = details

HEIGHT = 350
WIDTH = 1350


root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()


frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command=lambda: get_weather())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)



lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 10))
label.place(relx=0, rely=0, relwidth=1, relheight=1)



root.mainloop()

