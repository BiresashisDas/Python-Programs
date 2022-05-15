# Author :- Biresashis Das

from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 70, "normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.add_score()

    def add_score(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.left_score, align=ALIGN, font=FONT)
        self.goto(100, 200)
        self.write(self.right_score, align=ALIGN, font=FONT)

    def left_point(self):
        self.left_score += 1
        self.add_score()

    def right_point(self):
        self.right_score += 1
        self.add_score()
        
        
        
