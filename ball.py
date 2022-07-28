from turtle import Turtle
from random import choice
DIRECTIONS = (-1, 1)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("blue")
        self.x_move = 0.3
        self.y_move = 0.3

    def move(self):
        self.goto(x=self.xcor() + self.x_move, y=self.ycor() + self.y_move)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        if self.x_move < 0:
            self.x_move -= 0.2
        elif self.x_move > 0:
            self.x_move += 0.2

    def reset_position(self):
        self.goto(0, 0)
        self.x_move = 0.3 * choice(DIRECTIONS)
        self.y_move = 0.3 * choice(DIRECTIONS)
        self.bounce_x()



