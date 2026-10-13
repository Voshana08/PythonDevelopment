import turtle
from turtle import Screen
import pandas
screen = Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
correct_guesses = 0
turtle.shape(image)
#The bellow code was used to get the coordiantes of the states
#Inside the turtle screen.
# def get_mouse_coordinates(x,y):
#     print(x,y)

# #This is an event listener, and we are passing in the get_mouse_coordiantes function in
# turtle.onscreenclick(get_mouse_coordinates)
# #This will keep the screen open even if we click


answer_state = screen.textinput(title="Guess the state",prompt="Whats another state")

state_data = pandas.read_csv("50_states.csv")
# print(state_data)
all_states =state_data["state"].to_list()
if answer_state in all_states:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    final_data=state_data[state_data.state == answer_state]
    t.goto(final_data.x.item(),final_data.y.item())
    t.write(final_data.state)


turtle.mainloop()





