import random


class Food:

    def __init__(self, GAME_WIDTH, GAME_HEIGHT,SPACE_SIZE, FOOD_COLOR, canvas):
        self.GAME_WIDTH = GAME_WIDTH
        self.GAME_HEIGHT = GAME_HEIGHT
        self.SPACE_SIZE = SPACE_SIZE
        self.FOOD_COLOR = FOOD_COLOR
        self.canvas = canvas

        x = random.randint(0,(GAME_WIDTH/ SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0,(GAME_HEIGHT / SPACE_SIZE)-1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = FOOD_COLOR,tag='food')