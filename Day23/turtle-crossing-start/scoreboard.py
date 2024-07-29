from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280,260)
        self.lvl_no = 0
        self.display_lvl()

    def display_lvl(self):
        self.clear()
        self.lvl_no += 1
        self.write(f"Level: {self.lvl_no}",False,"left",FONT)

    def display_gameover(self):
        self.goto(0, 0)
        self.write(f"GAME OVER.", False, "center", FONT)
