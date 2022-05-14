# Author :- Biresashis Das

from turtle import Turtle

Align = ("center")
Font = ("Arial", 20, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("green")
        self.hideturtle()
        self.penup()
        self.goto(0,215)
        self.update_score()

    def update_score(self):
        self.write(f"Score : {self.score}", align=Align, font=Font)

    def game_over(self):
        self.goto(0,0)
        self.color("red")
        self.write("Game Over", align=Align, font=Font)

    def new_score(self):
        self.score += 1
        self.clear()
        self.update_score()
        
        
        
        
