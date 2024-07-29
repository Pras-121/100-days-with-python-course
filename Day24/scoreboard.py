from turtle import Turtle
FONT = ("Courier", 16, "normal")
ALIGNMENT_1 = "center"

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        try:
            with open("snake_highscore.txt") as file:
                self.high_score = int(file.read())
        except:
            with open("snake_highscore.txt", "w") as file:
                file.write(str(self.high_score))

        self.speed("fastest")
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.pendown()
        self.pencolor("White")
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", False, ALIGNMENT_1, FONT)
    def update(self):
        self.score += 1
        self.display_score()

    # def game_over(self):
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        with open("snake_highscore.txt", "w") as file:
            file.write(str(self.high_score))
        self.display_score()