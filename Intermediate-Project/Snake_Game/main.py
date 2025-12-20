from turtle import Screen
from snake import Snake
from food import Food
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake game")
# This is a method called tracer() which can turn  off animations for the turtle
#It takes a int value 
screen.tracer(0)
#creating a snake object from the snake class 
snake = Snake()
#Creating the food object 
food = Food()
#Creating the scoreboard object 
scoreboard = Scoreboard()

# Listneing to key strokes
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on = True

while game_is_on:
    
    screen.update()
    time.sleep(0.1)
    
    snake.move()
 #Reacting to collition with food
    if snake.head.distance(food) <15:
        food.refresh()
        snake.extend()
        #Counting the food score
        scoreboard.increase_score()

    #Detect collition with wall
    if snake.head.xcor() >280 or snake.head.xcor() <-280 or snake.head.ycor()>280 or snake.head.ycor() <-280 :
        scoreboard.reset()
        snake.reset()
        
    #Detect collision with tail
    #if head collides with any segment in the tail 
        #trigger game_over()
    for segement in snake.segments[1:]:
        if segement == snake.head:
            pass
        elif snake.head.distance(segement)<10 :
           scoreboard.reset()
           snake.reset()
    


screen.exitonclick()
