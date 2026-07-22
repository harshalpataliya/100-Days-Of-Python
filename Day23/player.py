from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.speed('fastest')
        self.goto_starting_position()

    def up(self):
        self.setheading(90)
        self.forward(MOVE_DISTANCE)

    def down(self):
        self.setheading(270)
        self.forward(MOVE_DISTANCE)

    def goto_starting_position(self):
            self.goto(STARTING_POSITION)