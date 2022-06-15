from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.penup()
        self.setposition(self.x_pos, self.y_pos)
        self.shape("square")
        self.turtlesize(5, 1)
        self.color("white")

    def move_up(self):
        if self.ycor() < 240:
            self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        if self.ycor() > -240:
            self.goto(self.xcor(), self.ycor() - 20)
