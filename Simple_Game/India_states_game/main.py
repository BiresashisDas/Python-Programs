# Author :- Biresashis Das

# This is our main file. We will run this file to start our INDIA STATES GAME.

import turtle
import pandas

screen = turtle.Screen()
screen.title("INDIA STATES GAME")
image = "states_of_INDIA.gif"
screen.bgpic(image)
turtle.shape(image)

data = pandas.read_csv("states_and_UT.csv")
all_states = data.state.to_list()
guessed_places = []

while len(guessed_places) < 37:
    states = screen.textinput(title=f"{len(guessed_places)}/37 States and UT Correct",
                              prompt="Write the name of the state or UT?").title()

    if states == "Exit":
        break

    if states in all_states:
        guessed_places.append(states)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == states]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(states)

screen.exitonclick()







