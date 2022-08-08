import time
from turtle import *
from paddle import *
from ball import *
from scoreboard import *

MOVE_DISTANCE = 20
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)
ball = Ball()
r_paddle = Paddle(place=350, senc=0)
l_paddle = Paddle(place=-350, senc=0)
score = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "x")
screen.onkey(l_paddle.go_down, "w")
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() > -340:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.refresh()
        score.l_point()

    if ball.xcor() < -380:
        ball.refresh()
        score.r_point()

screen.exitonclick()
