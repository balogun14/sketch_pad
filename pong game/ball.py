from turtle import *
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.color("white")
        self.goto(self.xcor(), self.ycor())
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        x_axis = self.xcor() + self.x_move
        y_axis = self.ycor() + self.y_move
        self.goto(x_axis, y_axis)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def refresh(self):
        self.goto(0, 0)
        self.move_speed = 0.1
