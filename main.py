import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from random import randint, choice


screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.setup(width=800, height=600)
screen.tracer(False)

player_1 = Paddle("left")
player_2 = Paddle("right")
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player_1.goup, "w")
screen.onkeypress(player_1.godown, "s")
screen.onkeypress(player_2.goup, "Up")
screen.onkeypress(player_2.godown, "Down")

game_on = True
while game_on:
    time.sleep(0.01) #bug occurs when sleep is deactivated and movement is done by forward command alone. Ball slows down depending on paddle position
    screen.update()
    ball.move()
    ball.bounce(player_1, player_2)

    if ball.xcor() >= 390:
        ball.setheading(choice([randint(135, 180), randint(180, 225)]))
        ball.reset_position()
        scoreboard.l_point()
    elif ball.xcor() <= -390:
        ball.setheading(choice([randint(0, 45), randint(315, 360)]))
        ball.reset_position()
        scoreboard.r_point()

#todo: make angle variation dependent on where the ball hits the paddle

screen.exitonclick()