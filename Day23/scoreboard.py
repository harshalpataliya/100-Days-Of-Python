from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-220, 250)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)