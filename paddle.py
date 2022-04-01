from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, which_argument):
        super().__init__()

        self.which_argument = which_argument
        self.ypos = 0
        self.xpos = 0
        self.create_paddle()

    def which_player(self, which_argument):
        if which_argument.lower() == "right":
            self.xpos = 370
        else:
            self.xpos = -370

    def create_paddle(self):
        self.which_player(self.which_argument)

        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=6, stretch_len=1)
        self.penup()
        self.goto(self.xpos, self.ypos)

    def goup(self):
        if self.ycor() < 240:
            new_ycor = self.ycor() + 40
            self.goto(self.xpos, new_ycor)

    def godown(self):
        if self.ycor() > -240:
            new_ycor = self.ycor() - 40
            self.goto(self.xpos, new_ycor)








