from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(turtle.move_forward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.drive_left()

    for car in car_manager.all_cars:
        if turtle.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    if turtle.is_at_end():
        scoreboard.increase_level()
        car_manager.accelerate()
        turtle.return_to_start()

screen.exitonclick()