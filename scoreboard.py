from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")


class Scoreboard(Turtle):

    def __init__(self,high):
        super().__init__()

        self.high_score=high
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.score = 0
        self.update()


    def refresh_score(self):
        self.score += 1
        self.update()

    def update(self):
        self.clear()
        self.write(arg=f"Score={self.score}  high score{self.high_score}",move= False, align=ALIGNMENT, font=FONT)

    def reset(self):

        if self.score>self.high_score:
            self.high_score=self.score
        self.score=0
        self.update()
