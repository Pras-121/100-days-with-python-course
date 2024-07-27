from turtle import Turtle, Screen
from random import randint

# tim = Turtle(shape="turtle")
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)


def rot_ccw():
    tim.lt(10)


def rot_cw():
    tim.rt(10)


def clear():
    tim.reset()

def move_turtle():
    screen.listen()
    screen.onkey(key="w", fun=move_forwards)
    screen.onkey(key="s", fun=move_backwards)
    screen.onkey(key="a", fun=rot_ccw)
    screen.onkey(key="d", fun=rot_cw)
    screen.onkey(key="c", fun=clear)


# move_turtle()
########################
#### Turtle race
######################
screen.setup(width = 500, height = 400)
colors = ["violet","indigo", "blue", "green","yellow","orange", "red"]
is_race_on = False
user_choice = ""
turtleObjList = []
f_line = 230


def init_position():
    y = 125
    for indx in range(0,7):
        tim= Turtle(shape="turtle")
        tim.penup()
        tim.goto(-230, y)
        tim.color(colors[indx])
        turtleObjList.append(tim)
        y -= 40

def draw_finish_line():
    tim = Turtle()
    tim.penup()
    tim.goto(230,130)
    tim.setheading(270)
    tim.pendown()
    tim.forward(250)
    tim.hideturtle()


def race():
    for obj in turtleObjList:
        obj.forward(randint(1,10))
        if obj.pos()[0] >= f_line:
            return obj.pencolor()


while user_choice not in colors:
    user_choice = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race. Enter the color: ")
is_race_on = True
init_position()
draw_finish_line()
while is_race_on:
    winner_color= race()
    if winner_color is not None:
        is_race_on = False
        print(f"{winner_color} turtle won.")
        if winner_color == user_choice:
            print("Hurray! You won the bet.")
        else:
            print("Oops! You lost the bet.")

screen.exitonclick()


