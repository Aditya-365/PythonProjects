from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

data = pandas.read_csv("/Adi/PythonCodes/flash-card-project/french_words.csv")
to_learn = data.to_dict(orient="records")


def next_card() : 
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    word = current_card["French"]
    canvas.itemconfig(card_background,image=card_front_img)
    canvas.itemconfig(canvas_text_title,text="French")
    canvas.itemconfig(canvas_text_word,text=word)
    flip_timer = window.after(3000,func=flip_card)


def flip_card() :
    word = current_card["English"]
    canvas.itemconfig(canvas_text_title,text="English")
    canvas.itemconfig(canvas_text_word,text=word)
    canvas.itemconfig(card_background,image=card_back_img)

def Exit() :
    window.destroy()
    
window = Tk()
window.title("Flash_Cards_API")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000,func=flip_card)

canvas = Canvas(width=800,height=526)
card_front_img = PhotoImage(file="/Adi/PythonCodes/flash-card-project/card_front.png")
card_back_img = PhotoImage(file="/Adi/PythonCodes/flash-card-project/card_back.png")
card_background = canvas.create_image(400,263,image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas_text_title = canvas.create_text(400,150,text="Title",font=("Arial",40,"italic"))
canvas_text_word = canvas.create_text(400,263,text="Word",font=("Arial",60,"bold"))
canvas.grid(column=0,row=0,columnspan=2)

cross_image = PhotoImage(file="/Adi/PythonCodes/flash-card-project/wrong.png")
unknown_image = Button(image=cross_image,highlightthickness=0,command=Exit)
unknown_image.grid(column=0,row=1)


check_image = PhotoImage(file="/Adi/PythonCodes/flash-card-project/right.png")
known_image = Button(image=check_image,highlightthickness=0,command=next_card)
known_image.grid(column=1,row=1)

next_card()

window.mainloop()