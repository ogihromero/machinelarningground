from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")

# turn the animations off
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# listening to events
screen.listen()
screen.onkeypress(fun=r_paddle.go_up, key="Up",)
screen.onkeypress(fun=r_paddle.go_down, key="Down")
screen.onkeypress(fun=l_paddle.go_up, key="w",)
screen.onkeypress(fun=l_paddle.go_down, key="s")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # detect ball colision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce("y")

    # detect colision with paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320
            or ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce("x")

    # detect r_paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        ball.bounce("x")
        scoreboard.score_up("l")
    # detect l_paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        ball.bounce("x")
        scoreboard.score_up("r")
screen.exitonclick()
