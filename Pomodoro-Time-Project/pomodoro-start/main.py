from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
#Naming the window title
window.title("Pomodoro")
#Configuring the padding on the window. 
window.config(padx=140,pady=60,bg=YELLOW)

canvas = Canvas(width=200,height=230,bg=YELLOW,highlightthickness=0)
#This is how you get the image to showup on the window, its done with a class called PhotoImage
tomato_ing=PhotoImage(file="tomato.png")

title_label = Label(text="Timer",fg=GREEN,font=(FONT_NAME,50),bg=YELLOW)
title_label.grid(column=1,row=0)
canvas.create_image(100,105,image=tomato_ing)
canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row= 1)

start_button=Button(text="Start",highlightthickness=0)
reset_button = Button(text="Reset",highlightthickness=0)
start_button.grid(column=0,row=2)
reset_button.grid(column=2,row=2)

check_marks=Label(text="✔",fg=GREEN,bg=YELLOW)
check_marks.grid(column=1,row=2)
window.mainloop()





