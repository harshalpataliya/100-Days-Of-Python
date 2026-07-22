from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        if random.randint(1, 6) == 1:
            car = Turtle()
            car.shape("square")
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.goto(300, random.randint(-200, 200))
            self.cars.append(car) 

    def move_cars(self):
        for car in self.cars:
            current_x = car.xcor() - self.car_speed
            y = car.ycor()
            car.goto(current_x, y)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT - 5






