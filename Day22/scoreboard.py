from turtle import Turtle
FONT = ("Courier", 18, "normal")
ALIGNMENT = "center"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.speed("fastest")
        self.hideturtle()
        self.pencolor("white")
        self.display_score()

    def display_score(self):
        self.clear()
        self.penup()
        self.goto(-100, 260)
        self.write(f"Player A: {self.l_score}", False, ALIGNMENT, FONT)
        # self.penup()
        self.goto(100,260)
        self.write(f"Player B: {self.r_score}", False, ALIGNMENT, FONT)

    def l_update(self):
        self.l_score += 1
        self.display_score()

    def r_update(self):
        self.r_score += 1
        self.display_score()