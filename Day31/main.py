from tkinter import *
import pandas
import random
import time
BACKGROUND_COLOR = "#B1DDC6"
#------Read CSV Data -------------#
try:
    df = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    df = pandas.read_csv("data/french_words.csv")
    # open("words_to_learn.csv", "w")
else:
    word_list = df.to_dict(orient="records")
# print(word_list)
chosen_word = {}
#--- Setting up output file for words to be learnt---#
#---- Random word Generation -----#
def genRandWords():
    global chosen_word, flip_timer
    tk.after_cancel(flip_timer)
    chosen_word = random.choice(word_list)
    # print(chosen_word["French"])
    canvas.delete("title")
    canvas.create_text(400, 150, tags="title", text="French", font=("Ariel","40","italic"), fill="black")
    canvas.itemconfig(card_word, text=chosen_word["French"], fill="black")
    canvas.itemconfig(canvas_image, image=white_card_img)
    flip_timer = tk.after(3000, func=flipcard)
    # tk.after_cancel()
    #tk.after(3000, showEnglishtranslation(chosen_word))


def flipcard():
    canvas.itemconfig(canvas_image, image=green_card_img)
    canvas.delete("title")
    canvas.create_text(400, 150, tags="title", text="English", font=("Ariel", "40", "italic"), fill="white")
    canvas.itemconfig(card_word, text=chosen_word["English"], fill="white")


def updateList():
    word_list.remove(chosen_word)
    genRandWords()
    updated_df = pandas.DataFrame(word_list)
    updated_df.to_csv("words_to_learn.csv", index=False)


#---------- UI Setup ------#
tk = Tk()
tk.title("Flashy")
tk.config(pady=50, padx=50, highlightthickness=0, bg=BACKGROUND_COLOR)
flip_timer = tk.after(3000, func=flipcard)
#---------#
canvas = Canvas(width=800, height=526)
white_card_img = PhotoImage(file="images/card_front.png")
green_card_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=white_card_img)
canvas.create_text(400, 150, tags="title", text="Title", font=("Ariel","40","italic"))
card_word = canvas.create_text(400, 263, tags="word", text="Word", font=("Ariel","60","bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,  column=0, columnspan=2, rowspan=2)
#-------#
tick_img = PhotoImage(file="images/right.png")
right_button = Button(image=tick_img, highlightthickness=0, command=updateList)
right_button.grid(row=2, column=1)
#---#
cross_img = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross_img, highlightthickness=0, command=genRandWords)
cross_button.grid(row=2, column=0)
#--------#
genRandWords()
tk.mainloop()