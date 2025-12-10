# def write (obj):
#     print("This is write")
#     print(f'Hello {obj}')

# write("Voshana")

# Creating classes 
# class User:
#     def __init__(self,username,id):
#         self.username = username,
#         self.id = id 
#         self.followers = 0
# user1 = User("Voshana","008")

# print(user1.followers)

# from turtle import Turtle,Screen
# import random
# timmy = Turtle()

# timmy.shape('turtle')
# timmy.color('blue')

# #Making a square with Timmy
# # for i in range (4):
# #     timmy.forward(100)
# #     timmy.left(90)
# direction = [0,90,180,360]
# for i in range (200):
#     timmy.forward(30)
#     timmy.setheading(random.choice(direction))

# screen = Screen()
# screen.exitonclick()


from turtle import Turtle, Screen

timmy = Turtle()

screen = Screen()
screen.listen()
def move_forward():
    timmy.forward(10)
screen.onkey(key="space",fun=move_forward)
screen.exitonclick()