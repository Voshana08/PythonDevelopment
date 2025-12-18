from turtle import Turtle,Screen
from snake import Snake
import time


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake game")
# This is a method called tracer() which can turn  off animations for the turtle
#It takes a int value 
screen.tracer(0)
#creating a snake object from the snake class 
snake = Snake()


    


game_is_on = True

while game_is_on:
    
    screen.update()
    time.sleep(0.1)
    
    snake.move()
 





screen.exitonclick()
