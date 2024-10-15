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

    reset_text = "00:00"
    reset_title = StringVar()
    reset_checkbox = StringVar()

    reset_title.set("Timer")
    reset_checkbox.set("")

    canvas.itemconfig(timer_text, text=reset_text)
    timer_label.config(textvariable=reset_title)
    check_marks.configure(textvariable=reset_checkbox)

    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    works_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 != 0:
        count_down(works_sec)
        new_text = StringVar()
        new_text.set("Work")
        timer_label.config(textvariable=new_text, fg=GREEN)
    elif reps == 8:
        count_down(long_break_sec)
        new_text = StringVar()
        new_text.set("Long Break")
        timer_label.config(textvariable=new_text, fg=RED)
    else:
        count_down(short_break_sec)
        new_text = StringVar()
        new_text.set("Short Break")
        timer_label.config(textvariable=new_text, fg=PINK)
        check_mark_symbol.set("✔")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = "0" + str(count_sec)

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        if reps % 2 == 0:
            check_mark_symbol.set("✔"*math.floor(reps/2))
            check_marks.config(textvariable=check_mark_symbol)
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Label for timer
timer_text = StringVar()
timer_text.set("Timer")
timer_label = Entry(textvariable=timer_text, font=(FONT_NAME, 40, "bold"), background=YELLOW, border=0, justify="center", fg=GREEN, width=13)
timer_label.grid(row=0, column=1)

# Label for checkmark
check_mark_symbol = StringVar()
check_marks = Entry(fg=GREEN, bg=YELLOW, border=0, font=(FONT_NAME, 28, "bold"), justify="center")
check_marks.grid(column=1, row=3)

# Start and reset buttons
start_button = Button(text="Start", fg=RED, bg=GREEN, border=0, pady=1, padx=1, font=(FONT_NAME, 14), command=start_timer)
reset_button = Button(text="Reset", fg=RED, bg=GREEN, border=0, pady=1, padx=1, font=(FONT_NAME, 14), command=reset_timer)

start_button.grid(row=2, column=0)
reset_button.grid(row=2, column=2)

#Setting up Canvas
canvas = Canvas(width=202, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


window.mainloop()