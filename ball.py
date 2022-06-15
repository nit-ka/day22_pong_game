from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_cor_change = 10
        self.y_cor_change = 10
        self.move_speed = 0.1

    def move(self):
        self.goto(self.xcor() + self.x_cor_change,
                  self.ycor() + self.y_cor_change)
        if self.ycor() > 270 or self.ycor() < -270:
            self.y_cor_change *= -1

    def bounce(self):
        self.x_cor_change *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.home()
        self.move_speed = 0.1
        self.bounce()

