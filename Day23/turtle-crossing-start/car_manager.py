import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(1,2,1)
        self.setheading(180)
        y_cor = random.randint(-260, 260)
        self.color(COLORS[random.randint(0, 5)])
        self.goto(290, y_cor)

    def traffic_flow(self,lvl):
        self.forward(STARTING_MOVE_DISTANCE + MOVE_INCREMENT * lvl)
