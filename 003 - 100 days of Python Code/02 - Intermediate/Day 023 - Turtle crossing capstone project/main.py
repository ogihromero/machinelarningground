import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


scoreboard = Scoreboard()
player = Player()
cars = CarManager()

# listening to events
screen.listen()
screen.onkeypress(fun=player.go_up, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # cars generation
    cars.create_car()
    cars.move_cars()

    # detect colision with car
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
            screen.update()
            game_is_on = False
    # detect if the turtle completed a level
    if player.is_at_finish_line():
        player.go_to_start()
        scoreboard.level_up()
        cars.speed_up()


screen.exitonclick()
