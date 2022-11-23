from turtle import Turtle
import random

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(-210,200)

    def increment_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))

    def show_score(self):
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))


    def game_over(self):
        for i in range(10):
            rand_pos_y = random.randint(-100,100)
            rand_pos_x = random.randint(-100,100)
            self.clear()
            self.goto(rand_pos_x,rand_pos_y)
            self.write(f"Score: {self.score}\nGame Over!", align="center", font=("Courier", 28, "bold"))
