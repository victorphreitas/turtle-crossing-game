from turtle import Turtle

STRECH_HEIGHT = 0.5
STRECH_WIDTH = 3

class Road(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(STRECH_WIDTH,STRECH_HEIGHT)
        self.right(-90)
        self.x_min = -300
        self.all_lines = []

    def make_road(self):
        for i in range(6):
            new_line = Road()
            new_line.goto(self.x_min,0)
            self.x_min += 150
            self.all_lines.append(new_line)

    def side_walk(self):
        for i in range(2):
            lower_side_walk = Road()
            lower_side_walk.color("brown")
            lower_side_walk.shapesize(2,60)
            lower_side_walk.penup()
            lower_side_walk.right(-90)
            if i == 0:
                lower_side_walk.goto(0,-280)
            else:
                lower_side_walk.goto(0,280)
