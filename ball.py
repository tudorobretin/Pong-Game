from turtle import Turtle
from random import randint, choice
from scoreboard import Scoreboard

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.create_ball()
        self.speed = 3


    def create_ball(self):
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(choice([randint(0, 45), randint(135, 180),randint(180, 225), randint(315, 360)]))
        print(self.heading())

    def move(self):
        self.forward(self.speed)

    def reset_position(self):
        self.speed = 3
        self.goto(0, 0)

    def speed_increase(self):
        self.speed += 0.8


    def bounce(self, left, right):

        if self.ycor() >=290 or self.ycor() <= -290:
            if self.heading() >=0 and self.heading() < 90:
                self.setheading(360-self.heading())
                #1 quadrat
            elif self.heading() >=90 and self.heading() < 180:
                self.setheading(360 - self.heading())
                #2 quadran
            elif self.heading() >=180 and self.heading() < 270:
                self.setheading(180-(self.heading()-180))
                #3 quadran
            elif self.heading() >=270 and self.heading() <= 360:
                self.setheading(360 - self.heading())
                #4 quadran

        if self.xcor() >= 350 and self.distance(right)<=64:
            self.speed_increase()
            if self.heading() >= 0 and self.heading() < 90:
                self.setheading(180-self.heading())
            elif self.heading() >=270 and self.heading() <= 360:
                self.setheading(180+(360-self.heading()))

        elif self.xcor() <= -350 and self.distance(left) <= 64:
            self.speed_increase()
            if self.heading() >=90 and self.heading() < 180:
                self.setheading(180-self.heading())
            elif self.heading() >=180 and self.heading() < 270:
                self.setheading(360-(self.heading()-180))

