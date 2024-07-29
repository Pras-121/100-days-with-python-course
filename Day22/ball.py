from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        '''posi is a tuple specifying the position of the object'''
        super().__init__()
        self.dir_up= True
        self.x_move = 15
        self.y_move = 15
        self.create_ball()
        self.move_speed = 0.1

    def create_ball(self):
        # print(f"This: {paddle_count}")
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.goto(0,0)

    def move(self):
        # self.setheading(30)
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)
        # self.forward(25)

    def vbounce(self):
        self.y_move *= -1

    def hbounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.hbounce()


    # def speedup(self):
    #     self.x_move *= 1.2




    # def up(self):
    #     self.goto(self.xcor(), self.ycor() + 20)
    #
    # def down(self):
    #     self.goto(self.xcor(), self.ycor() - 20)
