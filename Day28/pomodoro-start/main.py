from tkinter import Tk, Canvas, PhotoImage, Label, Button
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
timer = None
start_button_clicked = False

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    check_answer.config(text="")
    lbl.config(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps, start_button_clicked
    if not start_button_clicked:
        start_button_clicked = True
    else:
        reset()
        # exit()

    reps += 1
    work_reps = [1,3,5,7]
    short_break_reps = [2,4,6]
    long_break = 8
    if reps in work_reps:
        lbl.config(text="Work", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
        count_down(WORK_MIN * 60)
    elif reps in short_break_reps:
        lbl.config(text="Short Break", bg=YELLOW, fg=PINK, font=(FONT_NAME, 35, "bold"))
        count_down(SHORT_BREAK_MIN * 60)
    elif reps == long_break:
        lbl.config(text="Long Break", bg=YELLOW, fg=RED, font=(FONT_NAME, 35, "bold"))
        count_down(LONG_BREAK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
# import time
# count = 25
# while True:
#     time.sleep(1)
#     count-=1
# def count_down(time_min, time_sec):
def count_down(count):
    global timer
    time_min = math.floor(count / 60)
    time_sec =  count % 60

    # if time_min == 0 and time_sec == 0:

    if time_sec >= 0 and time_sec < 10:
        time_sec = f"0{time_sec}"

    canvas.itemconfig(timer_text, text=f"{time_min}:{time_sec}")
    if count > 0:
        timer = window.after(1000,count_down, count-1 )
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✅"
        check_answer.config(text=marks)

    # if time_sec > 0:
    #     window.after(1000,count_down, time_min, time_sec - 1)
    # elif time_sec == 0:
    #     time_min -= 1
    #     time_sec = 59
    #     window.after(1000, count_down, time_min, time_sec)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
#-------------#
lbl = Label()
lbl.config(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
lbl.grid(column=2, row=0)
#-------------#
canvas = Canvas(width= 200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=50)
#-------------#
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0,row=100)
#-------------#
reset_button = Button(text="Reset", highlightthickness=0, command=reset)
reset_button.grid(column=5, row=100)
# canvas.pack()
#-------------#
check_answer = Label(fg=GREEN, bg=YELLOW)
check_answer.grid(column=2, row=100)




window.mainloop()
