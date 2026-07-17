import random
from turtle import Turtle , Screen
is_race_on = False
screen = Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your Bet ", prompt="Which Turtle will win the race? Enter a Turtle Color :")
colors = ["red","orange","yellow","green","blue","purple"]
y_positions = [75, 50, 25, 0, -25, -50]
all_turtles = []

for turtle_index in range(0 ,6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-230,y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:

        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've win!The {winning_color} Turtle is the Winner!")
            else:
                print(f"You've lost ! The {winning_color} Turtle is the Winner!")




        random_distance = random.randint(0,10)
        turtle.forward(random_distance)





screen.exitonclick()