# Author :- Biresashis Das

from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.goto(position)
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("blue")
        self.penup()

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


