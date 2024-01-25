from tkinter import *
import math

"""
Here, I have developed a Pomodoro python GUI application. This application helps you work on the Pomodoro principle.
The pomodoro principle The Pomodoro Technique is a time management method based on 25-minute stretches of focused work
broken by five-minute breaks. Longer breaks, 20 minutes, are taken after four consecutive work intervals.
"""

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 60  # Set work duration in minutes
SHORT_BREAK_MIN = 5  # Set short break duration in minutes
LONG_BREAK_MIN = 20  # Set long break duration in minutes
check_mark = ""  # Variable to store checkmarks for completed intervals
reps = 0  # Variable to track the number of intervals completed
timer = None  # Variable to store the timer instance


def raise_above_all(tk_window):
    # Function to bring the Tkinter window to the front
    tk_window.lift()
    tk_window.attributes('-topmost', True)
    tk_window.update()
    tk_window.attributes('-topmost', False)


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    # Function to reset the timer
    global reps
    reps = 0
    global timer
    global check_mark
    check_mark = ""
    tick_mark_label.config(text=check_mark)
    window.after_cancel(timer)
    timer = None
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    # Function to start the timer
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        # If 8 intervals completed, take a long break
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
        raise_above_all(window)
        window.bell()
    elif reps % 2 == 0:
        # If even intervals, take a short break
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
        raise_above_all(window)
        window.bell()
    else:
        # If odd intervals, start working
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)
        raise_above_all(window)
        window.bell()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    # Function for countdown mechanism
    count_min = math.floor((count / 60))
    count_sec = count % 60
    if count_sec <= 9:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        # When countdown reaches 0, start the next interval
        start_timer()
        if reps % 2 == 0:
            # If it's a break interval, update checkmarks
            global check_mark
            check_mark += "✔"
            tick_mark_label.config(text=check_mark)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=2)

timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50, "normal"), bg=YELLOW)
timer_label.grid(column=1, row=1)

start_button = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start_button.grid(column=0, row=3)

reset_button = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(column=2, row=3)

tick_mark_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
tick_mark_label.grid(column=1, row=4)

window.mainloop()
