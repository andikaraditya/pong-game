from turtle import Turtle, Screen
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import random
import time 


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

# screen.tracer(0)

scoreboard = Scoreboard()
paddle = Paddle()
ball = Ball()

screen.listen()
screen.onkey(paddle.move_up, "Up")
screen.onkey(paddle.move_down, "Down")

while scoreboard.score_enemy < 5 and scoreboard.score_player < 5:
    paddle.enemy_ai(ball)
    ball.forward(10)
    if paddle.enemy.distance(ball) < 20:
        ball.bounce_right()
    elif paddle.enemy.distance(ball) < 50 and ball.xcor() < - 370:
        ball.bounce_right()
    if paddle.player.distance(ball) < 20:
        ball.bounce_left()
    elif paddle.player.distance(ball) < 50 and ball.xcor() > 370:
        ball.bounce_left()
        
    if ball.ycor() > 290:
        ball.bounce_down()
    if ball.ycor() < -290:
        ball.bounce_up()
        
    if ball.xcor() < -400:
        scoreboard.increase_score_player()
        ball.home()
        ball.setheading(random.randint(120,230))
        continue
    if ball.xcor() > 400:
        scoreboard.increase_score_enemy()
        ball.home()
        ball.setheading(random.randint(120,230))
        continue
    
final = Turtle()    
final.color("white")
final.penup()
final.hideturtle()
if scoreboard.score_enemy == 5:
    final.write("YOU LOSE", False, align="center", font=("Arial", 80, "normal"))
else:
    final.write("YOU WIN", False, align="center", font=("Arial", 80, "normal"))


screen.exitonclick()