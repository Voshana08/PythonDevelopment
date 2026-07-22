from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None  # ← NEW: stores the timer so we can cancel it

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps, timer
    
    # Step 1 - Cancel the countdown that is currently running
    window.after_cancel(timer)
    
    # Step 2 - Reset the display back to 00:00
    canvas.itemconfig(timer_text, text="00:00")
    
    # Step 3 - Reset the title label back to Timer
    title_label.config(text="Timer", fg=GREEN)
    
    # Step 4 - Clear the checkmarks
    check_marks.config(text="")
    
    # Step 5 - Reset the reps counter back to 0
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Short Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer  # ← NEW: we need access to timer variable
    
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        # ← NEW: store the return value of after() into timer
        timer = window.after(1000, count_down, count - 1)
    else:
        # ← NEW: when countdown hits 0, start next session
        start_timer()
        # ← NEW: add a checkmark for every completed work session
        if reps % 2 != 0:
            marks = "✔" * math.floor(reps / 2)
            check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=140, pady=60, bg=YELLOW)

canvas = Canvas(width=200, height=230, bg=YELLOW, highlightthickness=0)
tomato_ing = PhotoImage(file="tomato.png")

title_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
title_label.grid(column=1, row=0)
canvas.create_image(100, 105, image=tomato_ing)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)  # ← NEW: connected reset_timer
start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()