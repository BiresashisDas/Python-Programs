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
    bir.right(90)    
    bir.forward(i)   
    bir.right(270)   
    bir.pendown()    
    bir.circle(i)  
    bir.penup()      
    bir.home()       
    bir.color(random.choice(colors))

screen.exitonclick()



