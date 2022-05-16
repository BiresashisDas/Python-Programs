# Author :- Biresashis Das

from turtle import *

screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")

bir = Turtle()
bir.speed(15)
bir.goto(0, 100)
bir.color("red")
bir.hideturtle()

dist = 0
while dist < 200:
    bir.right(dist)
    bir.forward(dist * 2)
    dist += 1

screen.exitonclick()




