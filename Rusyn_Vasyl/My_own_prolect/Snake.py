class Snake:
    def __init__(self, BODY_PARTS, SPACE_SIZE,SNAKE_COLOR,canvas, ):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0,BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag='snake')
            self.squares.append(square)