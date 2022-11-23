from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-210,250)

    def increment_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))

    def show_score(self):
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))


    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Score: {self.score}\nGame Over!", align="center", font=("Courier", 24, "normal"))
