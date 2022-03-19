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
    canvas.itemconfig(timer_text,text="00:00")
    label.config(text="")
    label_1.config(text="Timer")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sce = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label_1.config(text="break",fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sce)
        label_1.config(text="Break",fg=PINK)
    else:
        count_down(work_sec)
        label_1.config(text="work",fg=YELLOW)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = canvas.after(1000,count_down, count-1)
    else:
        start_timer()
        label.config(text="✓")
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomadoro")
window.config(padx=100, pady=125, bg=GREEN)

canvas = Canvas(width=203, height=250, bg=GREEN, highlightthickness=0)#png image
my_tomato = PhotoImage(file="tomato.png")
canvas.create_image(103, 100, image=my_tomato)
timer_text = canvas.create_text(103, 115, text="00:00", fill="white", font=(FONT_NAME,30,"bold"))
canvas.grid(column=1, row=1)

button = Button(text="start", highlightthickness=0, command=start_timer)#start button
button.grid(column=0, row=3)

label_1= Label(fg=YELLOW, text="Timer", bg=GREEN,font=(FONT_NAME, 50,  "bold"))#label Timer
label_1.grid(column=1, row=0)

button2 = Button(text="reset",bg=RED, highlightthickness=0, command=reset_timer)#reset button
button2.grid(column=3, row=3)


label = Label(fg=RED, bg=GREEN)#i use this label for check mark
label.grid(column=1, row=3)

window.mainloop()
