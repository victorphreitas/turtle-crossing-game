from turtle import Turtle, Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from road import Road

# screen
screen = Screen()
screen.setup(600,600)
screen.tracer(0)
screen.bgcolor("black")

# road
road_manager = Road()
road_manager.make_road()
road_manager.side_walk()

# player
player = Player()

# score system goes here
score_system = Scoreboard()
score_system.show_score()

# listening to the screen event
screen.listen()
screen.onkeypress(player.move,"Up")

# Keep the game on
turned_on = True
game_over = False


# car manager
car_manager = CarManager()

while turned_on and not game_over:
    time.sleep(0.1)
    screen.update()
    # creating cars at random locations
    car_manager.create_car()
    car_manager.move_cars()
    # winning situation when turtle manages to cross the road
    if int(player.pos()[1]) >= 280:
        car_manager.counter += 1
        player.restart_game()
        score_system.increment_score()

    # game over situation when turtle crashes against any car on the road
    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            score_system.game_over()
            game_over = True




# to lock the screen
screen.exitonclick()




