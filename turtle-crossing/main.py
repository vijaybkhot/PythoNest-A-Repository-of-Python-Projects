import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

# Keystroke event to move the turtle up
screen.onkey(fun=player.move, key="Up")
# Boolean to check if game is over
game_is_on = True
counter = 0  # Counter to delay car production

while game_is_on:
    time.sleep(0.1)
    screen.update()
    counter += 1
    if counter % 6 == 0:
        car_manager.create_car()
    car_manager.moving_cars()

    if player.ycor() > player.finish_line:
        player.level_upgrade()
        scoreboard.update_scorecard()

    for car in car_manager.cars:
        if player.distance(car) < 15:
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() > player.finish_line:
        player.level_upgrade()
        scoreboard.update_scorecard()
        car_manager.speed_cars()

screen.exitonclick()
