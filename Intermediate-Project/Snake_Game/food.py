from turtle import Turtle
import random

class Food(Turtle) :
    def __init__(self):
        #inheritance from the turtle super class 
        super().__init__()
            
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
        
        
        
        
        #This method will refresh the food once its been eaten
        #It randomises the location of the food.
        #The screen is 300px therefore we will only take upto 280px to avoid 
        #Food being at the edge of the screen
    def refresh(self):
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x,random_y)