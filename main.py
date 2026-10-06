import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.setup(width=600, height=600)
screen.tracer(0)

# Move the turtle with a key press
player = Player()
screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Create and move cars
    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with cars
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
            screen.update()
            break
    if not game_is_on:
        break

    # Detect when turtle reaches the finish line
    if player.ycor() > FINISH_LINE_Y:
        player.reset_position()
        car_manager.increase_speed()
        scoreboard.increase_level()

    # Create a scoreboard to display the level
    scoreboard.update_scoreboard()
    screen.update()

screen.exitonclick()

            



