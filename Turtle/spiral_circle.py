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



![spiral_circle](https://user-images.githubusercontent.com/105218699/167843371-d4f35854-e2d9-4e56-9de7-017f43662937.png)
