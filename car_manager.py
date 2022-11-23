from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.counter = 0

    def create_car(self):
        chance = random.randint(1,6)
        if chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(1,2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            random_y = random.randint(-250,250)
            # random_x = random.randint(280,300)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        global STARTING_MOVE_DISTANCE
        chance = random.randint(1,60)
        if self.counter > 0 and chance == 1:
           STARTING_MOVE_DISTANCE += 1

        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)