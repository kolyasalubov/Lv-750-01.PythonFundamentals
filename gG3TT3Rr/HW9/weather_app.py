import tkinter as tk
from tkinter import font
from pyowm import OWM

API_KEY = 'ef2206ff5da67de63306d0b143e20872'

owm = OWM(API_KEY)
mgr = owm.weather_manager()

HEIGHT = 550
WIDTH = 750

root = tk.Tk()
root.title("Weather Application")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

def get_weather():
    try:
        observation = mgr.weather_at_place(entry_field.get())
        w = observation.weather
        weather_info = f"Weather for {entry_field.get()}:\n {w.detailed_status}\n Wind: {w.wind()}\n Humidity: {w.humidity}\n Temperature: {w.temperature('celsius')['temp']}°C\n Rain: {w.rain}\n Heat Index: {w.heat_index}\n Clouds: {w.clouds}"
        label['text'] = weather_info
    except:
        label['text'] = "Could not retrieve weather information"

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command=get_weather)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier', 14), anchor='nw', justify='left')
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()