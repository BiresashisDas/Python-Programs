# Author :- Biresashis Das

from turtle import Turtle

Align = ("center")
Font = ("Arial", 20, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.color("green")
        self.hideturtle()
        self.penup()
        self.goto(0,215)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score}  High Score : {self.highscore}", align=Align, font=Font)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_score()

    def new_score(self):
        self.score += 1
        self.update_score()
        
        
        
        
