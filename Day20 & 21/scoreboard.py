from turtle import Turtle
FONT = ("Courier", 16, "normal")
ALIGNMENT = "center"

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.speed("fastest")
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.pendown()
        self.pencolor("White")
        self.display_score()

    def display_score(self):
        self.write(f"Score: {self.score}", False, ALIGNMENT, FONT)

    def update(self):
        self.clear()
        self.score += 1
        self.display_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER.", False, ALIGNMENT, FONT)