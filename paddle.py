from turtle import Turtle
import random
STARTING_POSITION = [(-380,0), (380,0)]


class Paddle:
    def __init__(self):
        self.paddles = []
        self.create_paddle()
        self.player = self.paddles[1]
        self.enemy = self.paddles[0]

    def create_paddle(self):
        for i in STARTING_POSITION:
            new_paddle = Turtle("square")
            new_paddle.penup()
            new_paddle.color("white")
            new_paddle.shapesize(stretch_wid=1, stretch_len=5)
            new_paddle.goto(i)
            new_paddle.setheading(90)
            self.paddles.append(new_paddle)

    def move_up(self):
        self.player.forward(15)

    def move_down(self):
        self.player.backward(15)

    def enemy_ai(self, ball):
        while self.enemy.ycor() > ball.ycor():
            self.enemy.backward(10)
        while self.enemy.ycor() < ball.ycor():
            self.enemy.forward(10)