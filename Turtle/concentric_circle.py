# Author :- Biresashis Das

# Here I will show you how to create a concentric circle using circle() method.

from turtle import Turtle, Screen
import random

bir = Turtle()
screen = Screen()

colors = ["red", "orange", "blue", "violet", "deeppink"]

bir.penup()
bir.hideturtle()
bir.width(5)
for i in range(1, 300, 30):
    bir.right(90)    # Face South
    bir.forward(i)   # Move one radius
    bir.right(270)   # Back to start heading
    bir.pendown()    # Put the pen back down
    bir.circle(i)    # Draw a circle
    bir.penup()      # Pen up while we go home
    bir.home()       # Head back to the start pos
    bir.color(random.choice(colors))

screen.exitonclick()



