from turtle import Turtle
#Its better to define these variables at the top, so if needed to change
#We can change here
ALIGNMENT = "center"
FONT =("Courier",24,"normal") 


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score =0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.upadate_scoreboard()
        
        
    def upadate_scoreboard(self) :
        self.write(f"Score : {self.score}",align=ALIGNMENT,font=FONT)

    def game_over(self):
         self.goto(0,0)
         self.write("Game Over",align=ALIGNMENT,font=FONT)
    
    def increase_score(self):
        self.score +=1
        self.clear()
        self.upadate_scoreboard()
        
   
        