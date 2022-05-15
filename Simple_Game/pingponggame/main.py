# Author :- Biresashis Das

# This is our main file. We will run this file to start our ping pong game. 
# As you guys can see how I have imported other python files in this file.


'''             For Right Paddle :-
                We will use upper arrow for upper direction
                Down arrow for lower direction
                For Left Paddle :-
                We will use 'R' key for upper direction 
                and 'F' key for lower direction                 '''


from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Ping Pong Game")
screen.tracer(0)

r_paddle = Paddle((370,0))
l_paddle = Paddle((-380,0))
play_ball = Ball()
paddle_hit = 0
score = Score()

screen.listen()
screen.onkeypress(r_paddle.up, "Up",)
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "r",)
screen.onkeypress(l_paddle.down, "f")

is_game_on = True
while is_game_on:
    screen.update()
    play_ball.move()
    time.sleep(0.05)

    # Detect collision with wall
    if play_ball.ycor() > 280 or play_ball.ycor() < -280:
        play_ball.bounce_y()

    # Detect collision with paddle
    right_side = play_ball.distance(r_paddle)
    left_side = play_ball.distance(l_paddle)
    new_x = play_ball.xcor()

    if paddle_hit == 0:

        if right_side < 50 and new_x > 340 or left_side < 50 and new_x < -350:
            play_ball.bounce_x()
            paddle_hit = 1
    else:
        if -350 < new_x < 340:
            paddle_hit = 0

    # Detect If right paddle misses the ball
    if play_ball.xcor() > 400:
        play_ball.reset_position()
        score.left_point()

    # Detect If left paddle misses the ball
    if play_ball.xcor() < -400:
        play_ball.reset_position()
        score.right_point()


screen.exitonclick()



