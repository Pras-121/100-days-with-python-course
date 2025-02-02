from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake():

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        ##### alternative initial snake shape
        # tim.shape("square")
        # tim.resizemode("user")
        # tim.shapesize(1,3,1)
        # tim.color("white")
        #######
        for posi in STARTING_POSITION:
            self.add_segment(posi)


    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_pos = self.segments[seg - 1].position()
            self. segments[seg].goto(new_pos)
        self.segments[0].forward(MOVE_DIST)
        # self.segments[0].lt(90)

    def up(self):
        if self.head.heading() != DOWN:
             self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def add_segment(self, posi):
       segment = Turtle("square")
       segment.penup()
       segment.color("white")
       segment.goto(posi)
       self.segments.append(segment)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]


    def extend(self):
        self.add_segment(self.segments[-1].pos() )
        # add new segment to the snake


