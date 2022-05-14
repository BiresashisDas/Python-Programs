# Author :- Biresashis Das

# This is the food file. Here we will decide the shape and size pf our snake food's.

from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.6)
        self.color("blue")
        self.new()

    def new(self):
        x_axis = random.randint(-180,180)
        y_axis = random.randint(-180, 180)
        self.goto(x_axis, y_axis)
        
        
        
