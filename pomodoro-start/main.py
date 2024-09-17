from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#FFAAC9"
MAROON = "#B71375"
GREEN = "#22A699"
WHITE = "#F7F1E5"
YELLOW = "#f7f5dd"
CREAM = "#ECE5C7"
DARK_BLUE = "#1B6B93"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer() :
    window.after_cancel(timer)
    title_label.config(text="Timer",fg=DARK_BLUE)
    canvas.itemconfig(timer_text,text="00:00")
    checkmarks.config(text="",bg=CREAM)
    global reps 
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer() :
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0 :
        count_down(long_break_sec)
        title_label.config(text="Break",fg=MAROON)
    elif reps % 2 == 0 :
        count_down(short_break_sec)
        title_label.config(text="Break",fg=PINK)
    else :
        count_down(work_sec)
        title_label.config(text="Work",fg=GREEN)

    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count) :

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0 :
        count_sec == "00"
    if len(str(count_sec)) == 1 :
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text,text=f"{count_min} : {count_sec}")
    if count > 0 :
        global timer
        timer = window.after(1000, count_down ,count - 1)
    else :
        start_timer()
        marks = ""
        work_sessions = (math.floor(reps/2))
        for _ in range(work_sessions) :
            marks = "✓"
            checkmarks.config(text=marks,fg=DARK_BLUE,bg=CREAM)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=10,pady=10,bg=CREAM)

title_label = Label(text="Timer",font=("Arial",24,"bold"), fg=DARK_BLUE,bg=CREAM)
title_label.grid(column=1,row=0)

start = Button(text="Start",command=start_timer)
start.grid(column=0,row=2,)
start.config(highlightthickness=0)

reset = Button(text="Reset",command=reset_timer)
reset.grid(column=2,row=2)
reset.config(highlightthickness=0)

checkmarks = Label(fg=DARK_BLUE)
checkmarks.grid(column=1,row=3)
checkmarks.config(fg=DARK_BLUE,bg=CREAM,highlightthickness=0,font=("Arial",10,"bold"))

canvas = Canvas(width=200,height=184,highlightthickness=0)
pomodoro_img = PhotoImage(file="/Adi/PythonCodes/pomodoro-start/pomodoro.png")
canvas.create_image(100,92,image=pomodoro_img)
timer_text = canvas.create_text(100,97,text="00:00",fill=WHITE,font=("Arial",18,"bold"))
canvas.grid(column=1,row=1)






window.mainloop()