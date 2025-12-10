from turtle import Turtle,Screen
import time
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake game")

#using tuples inside the array to create the coordinates
positions =[(0,0),(-20,0),(-40,0)]

# This is a method called tracer() which can turn  off animations for the turtle
#It takes a int value 
screen.tracer(0)

segments =[]

for i in range(3):
    new_segment=Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(positions[i])
    segments.append(new_segment)


game_is_on = True

while game_is_on:
    
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segments)-1,0,-1):
        new_x=segments[seg_num-1].xcor()
        new_y=segments[seg_num-1].ycor()

        segments[seg_num].goto(new_x,new_y)
        
    segments[0].forward(20)





screen.exitonclick()
