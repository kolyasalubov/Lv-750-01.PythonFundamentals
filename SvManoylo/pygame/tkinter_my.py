from tkinter import *
from random import randrange as rnd, choice
import time

CONST_NEGATIVE = -1000
# створюємо вікно
root = Tk()

root.geometry('800x600')

# задаємо назву вікна
root.title("Caught the BALL")
 
canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)
 
colors = ['red','orange','yellow','green','blue']
def new_ball():
    global x,y,r,ball
    canv.delete(ball)
    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(30,50)
    ball = canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0)
    root.after(1000,new_ball)

     
     
def click(event):
    global points, x, text
    if (event.y - y)**2 + (event.x - x)**2 <= r**2:
        points += 1
        x = CONST_NEGATIVE
#видалення круга при кліку
        canv.delete(text)
        canv.delete(ball)
        text = canv.create_text(60,20,text="Score: " + str(points), font = 'Arial 20')
 
        

#щоб не можна було «накручувати» очки, 
# клікаючи багато разів по кругу, 
# поки він не зникне

#Після кліку круг не зникає і це не ok.
#Можна видалити все 
# canv.delete(ALL), 
# але тоді буде видалятись і рахунок

#краще дати імена всім графічним примітивам
# (тексту text і кулі ball) і видаляти їх окремо один від одного:
 
#щоб можна було видалити ball, треба перед викликом 
#функції ball() намалювати цей ball
ball = canv.create_oval(-100,0,0,0)
text = canv.create_text(60,20,text="Score: " + str(0), font = 'Arial 20')
points = 0
new_ball()
canv.bind('<Button-1>', click)


mainloop()