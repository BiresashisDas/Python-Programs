from turtle import Turtle, Screen

screen = Screen()

bir = Turtle()
bir.color('black', 'blue')
bir.begin_fill()

def rectangle_1():
    bir.right(90)
    bir.forward(50)

def rectangle_2():
    bir.right(90)
    bir.forward(100)

bir.forward(100)
rectangle_1()
rectangle_2()
rectangle_1()

bir.end_fill()
screen.exitonclick()