# ###
# Score class  --> Set and display score
# gamelogic class -> intialises display, moves the pong hands
# pong movement class --> controls the ball movement
# ###
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time
scr = Screen()

## Initialise Display
scr.setup(width=1000, height=600)
scr.bgcolor("black")
scr.title("Pong")
scr.tracer(0)
paddle1 = Paddle((470, 0))  ## Right paddle
paddle2 = Paddle((-470, 0)) ## Left paddle
ball = Ball()
score = ScoreBoard()
#### Event Listener
scr.listen()
scr.onkey(paddle1.up, "Up")
scr.onkey(paddle1.down, "Down")
scr.onkey(paddle2.up, "w")
scr.onkey(paddle2.down, "s")
#### Game loop
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    print(ball.move_speed)
    ball.move()
    scr.update()

    # Detect collision with horizantal screen boundaries
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.vbounce()

    # Detect collision with vertical screen boundaries
    if ball.xcor() > 470:
        score.l_update()
        ball.reset()

    if ball.xcor() < -470:
        score.r_update()
        ball.reset()

    # Detect collision with paddle
    if (ball.distance(paddle1) < 50 and ball.xcor() > 445) or (ball.distance(paddle2) < 50 and ball.xcor() < -445):
        ball.hbounce()

    # Detect collision with paddle
    # print(f" Distance to paddle1:  {ball.distance(paddle1)}, x-ordinate {ball.xcor()}")
    # print(f" Distance to paddle2:  {ball.distance(paddle2)}")










scr.exitonclick()