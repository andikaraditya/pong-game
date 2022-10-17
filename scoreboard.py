from turtle import Turtle

class Scoreboard:
    def __init__(self):
        self.line = Turtle()
        self.line.color("white")
        self.line.penup()
        self.line.hideturtle()
        self.line.goto(0, 300)
        self.line.setheading(270)
        self.line.pensize(4)
        self.line.speed(0)
        self.create_line()

        self.score_enemy = 0
        self.score_player = 0
        self.score_display = Turtle()
        self.score_display.hideturtle()
        self.score_display.penup()
        self.score_display.color("white")
        self.score_display.goto(x=0, y=225)
        self.update_score()
        pass


    def create_line(self):
        for i in range(15):
            self.line.pendown()
            self.line.fd(20)
            self.line.penup()
            self.line.fd(20)


    def update_score(self):
        self.score_display.clear()
        self.score_display.write(f"{self.score_enemy} {self.score_player}", False, align="center", font=("Arial", 50, "normal"))
        
    def increase_score_enemy(self):
        self.score_enemy +=1
        self.update_score()
        
    def increase_score_player(self):
        self.score_player +=1
        self.update_score()