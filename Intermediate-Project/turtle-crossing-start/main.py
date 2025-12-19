import time
from turtle import Screen,Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)

player =Player()
carmanager = CarManager()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(player.go_up,"Up")
# controls how often the screen refreshes; lower values = faster animation
screen.tracer(0)

game_is_on = True


while game_is_on:
    time.sleep(0.1)
    screen.update()
    carmanager.create_car()
    carmanager.move_cars()
    #Detecting collision with car and the player
    for car in carmanager.all_cars:
        if car.distance(player) <20:
            game_is_on =False
    
    #Detect a succesful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        carmanager.level_up()
        scoreboard.update_scoreboard()
        scoreboard.increase_level()

scoreboard.game_over()
        
screen.exitonclick()
    