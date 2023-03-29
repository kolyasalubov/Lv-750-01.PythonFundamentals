import requests
from bs4 import BeautifulSoup
import random
import tkinter as tk

# Завантажуємо сторінку з топ 200 фільмів на IMDB
page = requests.get('https://www.imdb.com/chart/top') 
soup = BeautifulSoup(page.content, 'html.parser')  

# Знаходимо всі назви фільмів
movies = soup.select('td.titleColumn')
movie_titles = [movie.a.text for movie in movies] 

# Функція для випадкового вибору фільму
def pick_movie():
    random_movie = random.choice(movie_titles)
    return random_movie

# Створення вікна за допомогою бібліотеки tkinter
root = tk.Tk()
root.title('IMDB Top 200 Movie Picker')
root.geometry('300x100')

# Створення текстового віджету для відображення вибраної назви фільму
label = tk.Label(root, text='')
label.pack()

# Функція для відображення вибраної назви фільму
def show_movie():
    movie = pick_movie()
    label.config(text=movie)

# Створення кнопки для виклику функції випадкового вибору фільму
button = tk.Button(root, text='Підібрати фільм', command=show_movie)
button.pack()

# Запуск головного циклу програми
root.mainloop()