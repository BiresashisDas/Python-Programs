# Author :- Biresashis Das

# How to draw a circle using turtle.

from turtle import Turtle, Screen

bir = Turtle()
screen = Screen()

# bir.shapesize(2)  # If u need the shape than comment out this line.

bir.color("red")
bir.width(12)
print(bir.circle(100))
bir.hideturtle()      # It is used to hide the arrow 

screen.exitonclick()



