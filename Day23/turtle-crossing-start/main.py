import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score = Scoreboard()
# Event listener
screen.listen()
screen.onkeypress(player.move_up, "Up")
screen.onkeypress(player.move_down, "Down")


def car_gen(lvl):
    time.sleep(lvl * 0.09)
    car_obj = CarManager()
    car_list.append(car_obj)


car_list = []
game_is_on = True
while game_is_on:
    time.sleep(0.2)
    screen.update()
    car_gen(score.lvl_no)

    for car in car_list:
        car.traffic_flow(score.lvl_no)
        if player.distance(car) < 20:
            game_is_on = False
            break

    if player.ycor() > 280:
        player.level_up()
        score.display_lvl()

    if not game_is_on:
        print("Game over")
        score.display_gameover()

screen.exitonclick()

