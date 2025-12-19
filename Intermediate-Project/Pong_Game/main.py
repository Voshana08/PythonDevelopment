from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
#Creating the scoreboard object 
scoreboard = Scoreboard()
screen = Screen()
screen.bgcolor('black')
screen.title('Pong Game')
#setting the hieght and width of the screen.
screen.setup(width=800,height=600)
#This command turns off the animations.
screen.tracer(0)

#Creating the two paddles
r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball = Ball()


#This command is important to listen to keystrokes
screen.listen()

#Moving the right paddle 
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

#Moving the left paddle
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    #This upadates the screen as thr tracer is off.
    screen.update()
    ball.move()
    #Detecting collision with the wall
    if ball.ycor() >280 or ball.ycor() <-280:
        ball.bounce_y()
    #Detect collision with right paddle
    if ball.distance(r_paddle) <50 and ball.xcor() > 320 or ball.distance(l_paddle) <50 and ball.xcor() <-320 :
        ball.bounce_x()
        
    #Detect when the right paddle misses
    if ball.xcor() >380:
        ball.reset_position()
        scoreboard.l_point()
        scoreboard.upadate_scoreboard()
    #Detect the L paddle misses
    if ball.xcor() <-380:
        ball.reset_position()
        scoreboard.r_point()
        scoreboard.upadate_scoreboard()
screen.exitonclick()
