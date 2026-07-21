from turtle import  Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.title("PONG GAME")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)


right_paddle=Paddle(360 , 0)
left_paddle=Paddle(-365 , 0)
ball=Ball()
score=Score()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")


game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with  right_paddle and left paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        

    # detect right paddle misses
    if ball.xcor() > 380 :
        ball.reset_position()
        score.l_point()

    # detect left paddle misses
    if ball.xcor() < -380 :
        ball.reset_position()
        score.r_point()


screen.exitonclick()