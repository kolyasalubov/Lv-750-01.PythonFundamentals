import tkinter as tk
from tkinter import font
from tkinter import messagebox
import weather

def get_weather():
    input_city = entry_field.get()
    if input_city != "":
        result = weather.checkWeather(input_city)
        my_var.set(result)
        entry_field.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")

HEIGHT = 350
WIDTH = 450

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
                   bg="gray", fg="black", 
                   font=('Courier', 8), 
                   command=get_weather)
                   #command=lambda: OWM.get_weather('Lviv'))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

my_var = tk.StringVar()
my_var.set("First click")
label = tk.Label(lower_frame, font=('Courier', 14), textvariable=my_var)
label.place(relx=0, rely=0, relwidth=1, relheight=1)
#label.pack()

root.mainloop()

