from turtle import Turtle, Screen
import random
import math
timmy = Turtle ()
screen = Screen()
screen.colormode(255)
# timmy.shape("turtle")
# for i in range(4):
#     print(i)
#     timmy.forward(100)
#     timmy.rt(90)

# for i in range(15):
#     timmy.forward(10)
#     if timmy.isdown():
#         timmy.penup()
#     else:
#         timmy.pendown()

## mutiple shapes
def giveColor():
    lst = []
    for i in range(3):
        lst.append(random.randint(1,255))
    y = tuple(lst)
    # print(y)
    return y
##
# totangle =360
# sides =[3,4,5,6,7,8,9,10,20]
# for side in sides:
#     currAngle = totangle / side
#     timmy.pencolor(giveColor())
#     for i in range(side):
#         timmy.rt(currAngle)
#         timmy.forward(100)

## random walk
# currPenSize = timmy.pensize(10)
# screen.colormode(255)
# for _ in range(100):
#     timmy.pencolor(giveColor())
#     currSpeed = timmy.speed()
#     timmy.speed(1.2*currSpeed)
#     # timmy.rt(random.randint(0,90))
#     timmy.rt(random.choice([0, 90, 180, -90, -360]))
#     timmy.forward(50)

### Spirograph
def draw_spirograph(steps):
    angle = 360 / steps
    timmy.speed("fastest")
    # timmy.circle(50,360,100)
    for i in range(int(angle)):
        timmy.pencolor(giveColor())
        timmy.circle(100)
        # timmy.penup()
        # timmy.lt(angle)
        # timmy.pendown()
        ## alternate method is to use heading
        timmy.setheading(timmy.heading()+ steps)
# def draw_spirograph(no_of_circles):
#     angle = 360 / no_of_circles
#     timmy.speed("fastest")
#     for i in range(no_of_circles):
#         timmy.pencolor(giveColor())
#         timmy.circle(100)
#         timmy.penup()
#         timmy.lt(angle)
#         timmy.pendown()
draw_spirograph(5)




















screen.exitonclick()
