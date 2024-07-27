from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

scr = Screen()
scr.setup(width=600, height=600)
scr.bgcolor("black")
scr.title("Snake Game")
scr.tracer(0)

#####
snake = Snake()
food = Food()
score = Score()

scr.listen()
scr.onkey(snake.up, "Up")
scr.onkey(snake.down, "Down")
scr.onkey(snake.left, "Left")
scr.onkey(snake.right, "Right")
game_is_on = True
while game_is_on:
    scr.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        score.update()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        score.game_over()

    # Detect collision with tail
    for segment in snake.segments[1::]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()


scr.exitonclick()