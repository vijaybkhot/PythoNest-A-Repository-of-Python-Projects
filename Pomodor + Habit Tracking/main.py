from tkinter import *
import math
from data_update import DataUpdate
from habit_tracker import HabitTracker
from notification import Notification
from datetime import datetime

"""

Here, I have developed a Pomodoro Python GUI application that follows the Pomodoro Technique, a time management 
method based on 25-minute work intervals followed by 5-minute breaks. After four work intervals, a longer break of 20 
minutes is taken.

This application integrates with the Pixela habit tracker API to track daily work sessions. Each completed work or 
break interval is recorded as 0.5 hours in the habit tracker, visualized in a graph. Additionally, the application 
sends an email notification at the end of each work session, summarizing the previous day's work and welcoming new 
users.

To use the application, simply click the 'Start' button to begin a work interval. The timer will count down, 
and when it reaches 0, a break will start automatically. Click 'Reset' to reset the timer and start a new work 
session. You can also pause the timer at any time by clicking 'Pause' and resume it by clicking 'Resume'.

"""

# ---------------------------- CONSTANTS ------------------------------- #
# Constants for colors, font, and durations
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 30  # Set work duration in minutes
SHORT_BREAK_MIN = 5  # Set short break duration in minutes
LONG_BREAK_MIN = 20  # Set long break duration in minutes

# Variables for tracking intervals, timer, checkmarks, and pause state
check_mark = ""  # Variable to store checkmarks for completed intervals
reps = 0  # Variable to track the number of intervals completed
timer = None  # Variable to store the timer instance
count = 0  # Variable to store the remaining time in seconds
paused = False  # Variable to track if the timer is paused

# Instances of custom classes for data update, habit tracking, and notifications
data_update = DataUpdate()
habit_tracker = HabitTracker()
notification = Notification()

# Get today's date in YYYY-MM-DD format
date = datetime.today().strftime("%Y-%m-%d")


def pause_timer():
    """Function to pause or resume the timer."""
    global paused
    paused = not paused
    if paused:
        pause_button.config(text="Resume")
    else:
        pause_button.config(text="Pause")
    count_down()


def raise_above_all(tk_window):
    """Function to bring the Tkinter window to the front."""
    tk_window.lift()
    tk_window.attributes('-topmost', True)
    tk_window.update()
    tk_window.attributes('-topmost', False)


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    """Function to reset the timer."""
    global reps, timer, check_mark, count
    reps = 0
    count = 0
    check_mark = ""
    tick_mark_label.config(text=check_mark)
    # Cancel the timer only if it is currently running
    if timer is not None:
        window.after_cancel(timer)
        timer = None
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    """Function to start the timer."""
    global reps, count

    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 10 == 0:
        # If 10 intervals completed, take a long break
        count = long_break_sec
        count_down()
        timer_label.config(text="Break", fg=RED)
        raise_above_all(window)
        window.bell()
    elif reps % 2 == 0:
        # If even intervals, take a short break
        count = short_break_sec
        count_down()
        timer_label.config(text="Break", fg=PINK)
        raise_above_all(window)
        window.bell()
    else:
        # If odd intervals, start working
        count = work_sec
        count_down()
        timer_label.config(text="Work", fg=GREEN)
        raise_above_all(window)
        window.bell()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down():
    """Function for countdown mechanism."""
    global count, paused
    if paused:
        return
    # Function for countdown mechanism
    count_min = math.floor((count / 60))
    count_sec = count % 60
    if count_sec <= 9:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        # Schedule the count_down function to be called after 1000 milliseconds (1 second)
        # Pass the decremented count value (count - 1) as an argument to the count_down function
        timer = window.after(1000, count_down)
        count = count - 1
    else:
        # When countdown reaches 0, start the next interval
        start_timer()
        if reps % 2 == 0:
            # If it's a break interval, update checkmarks
            global check_mark
            check_mark += "✔"
            tick_mark_label.config(text=check_mark)  # Update check mark on UI
            current_data = data_update.update_data_file()  # Update the data by adding 0.5 hrs to previous data

            # Notify the previous days data or send a welcome message
            if len(current_data) > 1 and current_data[0]['quantity'] == 0.5:
                notification.send_email(date=current_data[1]['date'], quantity=current_data[1]['quantity'], signal=1)
            elif len(current_data) == 1 and current_data[0]['quantity'] == 0.5:
                notification.send_email(date=current_data[0]['date'], quantity=current_data[0]['quantity'], signal=0)
            # print(current_data[0]['quantity'])
            # Update the pixel data in the Pixela graph
            habit_tracker.add_pixel(date=current_data[0]['date'].replace("-", ""), quantity=current_data[0]['quantity'])


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 112, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))  # Center the text
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50, "normal"), bg=YELLOW)
timer_label.grid(column=1, row=0)  # Place the label over the canvas

start_button = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start_button.grid(column=0, row=3)

reset_button = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(column=2, row=3)

pause_button = Button(text="Pause", highlightbackground=YELLOW, command=pause_timer)
pause_button.grid(column=1, row=3)

tick_mark_label = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 60, "bold"))
tick_mark_label.grid(column=1, row=2)

window.mainloop()
