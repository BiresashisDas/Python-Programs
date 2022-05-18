# Author :- Biresashis Das

from turtle import Turtle, Screen
import random

bir = Turtle()

colour = ["red", "green", "violet", "orange", "yellow", "brown"]

def diagrams(num_of_sides):
    for i in range(num_of_sides):
        angle = 360 / num_of_sides
        bir.forward(100)
        bir.left(angle)

for i in range(3,9):
    bir.color(random.choice(colour))
    bir.width(4)
    diagrams(i)


screen = Screen()
screen.exitonclick()




