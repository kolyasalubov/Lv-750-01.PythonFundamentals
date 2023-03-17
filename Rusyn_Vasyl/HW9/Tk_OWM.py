import tkinter as tk
from tkinter import font
import OWM

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

def submit(entry_field):
    entry_field = entry_field.get()
    weather = OWM.observation(entry_field)
    label= tk.Label(text=weather, fg='red')
    label.pack()

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command=lambda: submit(entry_field))
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)



lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')




root.mainloop()

