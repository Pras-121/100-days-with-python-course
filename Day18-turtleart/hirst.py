# import colorgram
# colors = colorgram.extract("image.jpeg",20)
# # print(colors)
# color_in_rgb = []
# for color in colors:
#     # print(color.hsl)
#     r = color.rgb.r
#     b = color.rgb.b
#     g = color.rgb.g
#     color_in_rgb.append((r,g,b))
import turtle as timmy
import random as rand
timmy.colormode(255)
timmy.speed(0)
timmy.penup()
timmy.hideturtle()
color_List =  [(245, 235, 46), (195, 12, 34), (220, 160, 71), (42, 80, 177), (237, 40, 138), (32, 40, 156), (238, 229, 5), (40, 215, 69), (21, 150, 23), (209, 73, 21), (204, 32, 96), (66, 10, 28), (217, 163, 11), (218, 137, 191), (189, 15, 9), (55, 15, 10)]
# timmy.canvwidth = 1900
# timmy.canvheight = 1500
# #
def  dispRows():
        timmy.dot(20,rand.choice(color_List))
        timmy.forward(50)
####


def moveToNextRow():
        timmy.backward(50)
        timmy.setheading(90)
        timmy.forward(50)


def intiposition():
        timmy.lt(225)
        timmy.forward(200)
        timmy.setheading(0)


# print(timmy.pos())
intiposition()
for row in range(10):
    print(timmy.heading())
    for col in range(10):
        # timmy.pen(timmy.fillcolor(rand.choice(color_List)))
        dispRows()
    moveToNextRow()
    print(f"Row Number: {row}")
    if row % 2 == 0:
            print("Turn left")
            timmy.setheading(180)
    else:
            print("Turn right")
            timmy.setheading(0)
timmy.exitonclick()
