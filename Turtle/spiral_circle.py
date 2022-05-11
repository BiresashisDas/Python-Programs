# Author :- Biresashis Das

# How to draw a Spiral Circle

from turtle import Turtle, Screen

screen = Screen()
bir = Turtle()
bir.color("darkorange")
bir.width(4)
bir.hideturtle()

radius = 10

for i in range(125):
    bir.circle(radius + i, 30)

screen.exitonclick()



