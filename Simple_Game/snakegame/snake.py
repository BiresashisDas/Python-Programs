from turtle import Turtle

new_position = [(0,0), (-20,0), (-40,0)]
up_direction = 90
down_direction = 270
left_direction = 180
right_direction = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.another_snake()
        self.top = self.segments[0]

    def another_snake(self):
        for i in new_position:
            self.add_segment(i)

    def add_segment(self, i):
        bir = Turtle("square")
        bir.penup()
        bir.color("darkgreen")
        bir.goto(i)
        self.segments.append(bir)

    def size_increase(self):
        self.add_segment(self.segments[-1].position())

    def move_forward(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            x_axis = self.segments[seg - 1].xcor()
            y_axis = self.segments[seg - 1].ycor()
            self.segments[seg].goto(x_axis, y_axis)

        self.top.forward(20)

    def up(self):
        if self.top.heading() != down_direction:
            self.top.setheading(up_direction)

    def down(self):
        if self.top.heading() != up_direction:
            self.top.setheading(down_direction)

    def left(self):
        if self.top.heading() != right_direction:
            self.top.setheading(left_direction)

    def right(self):
        if self.top.heading() != left_direction:
            self.top.setheading(right_direction)