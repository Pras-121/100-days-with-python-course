from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, posi):
        '''posi is a tuple specifying the position of the object'''
        super().__init__()
        self.loc = posi
        self.create_paddle()

    def create_paddle(self):
        # print(f"This: {paddle_count}")
        self.shape("square")
        self.color("white")
        self.resizemode("user")
        self.shapesize(5, 1, 1)
        self.penup()
        self.goto(self.loc)


    def up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        self.goto(self.xcor(), self.ycor() - 20)
