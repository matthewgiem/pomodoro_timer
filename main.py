from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    window.after_cancel(timer)
    global reps
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")
    title_label.config(text="Timer")


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_time():
    global reps
    if reps % 2 == 0:
        title_label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)
        reps += 1
    elif reps < 6:
        title_label.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
        reps += 1
    elif reps == 7:
        title_label.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
        reps += 1
    else:
        reset_timer()

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    time_left_min = int(count / 60)
    time_left_seconds = count % 60
    canvas.itemconfig(timer_text, text=f"{time_left_min:02d}:{time_left_seconds:02d}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        if reps % 2 != 0:
            number_of_checks = math.ceil(reps/2)
            check_marks.config(text=number_of_checks*"✔")
        start_time()


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


start_button = Button(text="Start", highlightthickness=0, command=start_time)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
