from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.speed("fast")
        self.color("white")
        self.setheading(random.randint(120,230))
        pass


    def bounce_up(self):
        if self.heading() > 270:
            new_heading = 360 - self.heading()
            self.setheading(new_heading)
            self.forward(10)
        elif self.heading() < 270:
            new_heading = 360 - self.heading()
            self.setheading(new_heading)
            self.forward(10)

    def bounce_down(self):
        if self.heading() < 90:
            new_heading = 360 - self.heading()
            self.setheading(new_heading)
            self.forward(10)
        elif self.heading() > 90:
            new_heading = 360 - self.heading()
            self.setheading(new_heading)
            self.forward(10)

    def bounce_right(self):
        if self.heading() > 90 and self.heading() < 180:
            self.setheading(random.randint(0,60))
            self.forward(10)
        if self.heading() > 180 and self.heading() < 270:
            self.setheading(random.randint(300,359))
            self.forward(10)
        

    def bounce_left(self):
        if self.heading() > 0 and self.heading() < 90:
            self.setheading(random.randint(120,180))
            self.forward(10)
        if self.heading() > 270 and self.heading() < 360:
            self.setheading(random.randint(180,250))
            self.forward(10)
