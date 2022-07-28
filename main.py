from turtle import Screen
from paddle import Paddle
from screen_settings import ScreenSettings
from ball import Ball

screen = Screen()
screen.tracer(0)
screen.setup(600, 600)
screen.title("Paddle pong game")
screen.listen()
screen.bgcolor("black")
screen_settings = ScreenSettings()
ball = Ball()

block_right = Paddle((280, 0))
block_left = Paddle((-280, 0))

screen.onkeypress(key="Up", fun=block_right.up)
screen.onkeypress(key="Down", fun=block_right.down)
screen.onkeypress(key="w", fun=block_left.up)
screen.onkeypress(key="s", fun=block_left.down)


while screen_settings.who_wins():
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    elif ball.distance(block_right) < 50 and ball.xcor() > 270 or ball.distance(block_left) < 50 and ball.xcor() < -270:
        ball.bounce_x()
    elif ball.xcor() > 270:
        screen_settings.l_block_score()
        ball.reset_position()
    elif ball.xcor() < -270:
        screen_settings.r_block_score()
        ball.reset_position()
    screen.update()
    ball.move()

screen.exitonclick()
