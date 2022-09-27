from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=r_paddle.down, key="Down")
screen.onkey(fun=l_paddle.up, key="w")
screen.onkey(fun=l_paddle.down, key="s")

ball = Ball()
scoreboard = Scoreboard()

game_on = True
while game_on:
    time.sleep(ball.time_speed)
    screen.update()
    ball.move()
    # Detect wall and bounce off of it
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect paddles and bounce off of it
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() > 420:
        scoreboard.l_point()
        ball.restart()
    elif ball.xcor() < -420:
        scoreboard.r_point()
        ball.restart()

screen.exitonclick()
