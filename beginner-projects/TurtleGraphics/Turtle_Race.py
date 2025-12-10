from turtle import Turtle,Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Which Turtle will win the race ?")
print(user_bet)

colors = ["red","blue","Yellow","Orange","White"]
y_positions=[-70,-40,0,30,80,80]
all_turtle=[]


for i in range(5):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_positions[i])
    all_turtle.append(new_turtle)
    
if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() >230:
            is_race_on = False
            winning_color=turtle.pencolor()
            if winning_color == user_bet:
            
                print("Your turtle won")
            else:
                print("Youve lost")
                print(winning_color)
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()



