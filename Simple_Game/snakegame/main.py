# Author :- Biresashis Das

# This is our main file. We will run this file to start our snake game. 
# As you guys can see how I have imported other python files in this file.

from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width=500, height=500)
screen.title("Welcome to the Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move_forward()

    # Eating the food
    if snake.top.distance(food) < 15:
        food.new()
        snake.size_increase()
        score.new_score()

    # Collision with wall
    if snake.top.xcor() > 240 or snake.top.xcor() < -240 or snake.top.ycor() > 240 or snake.top.ycor() < -240:
        is_game_on = False
        score.game_over()

    # Collision with tail
    for segment in snake.segments[1:]:
        if snake.top.distance(segment) < 10:
            is_game_on = False
            score.game_over()


screen.exitonclick()






