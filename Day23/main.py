import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    #check player if its reach the finish line then goto its original position and increase level by at each finish cross
    if player.ycor() > 280 :
        player.goto_starting_position()
        scoreboard.increase_level()
        car_manager.level_up()

    # check collision between car and player
    for car in car_manager.cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()