
from tkinter import *
import pandas as pd
import random


BACKGROUND_COLOR = "#B1DDC6"
FONT_TITLE = ("Arial", 40, "italic")
FONT_WORD = ("Arial", 60, "bold")
RANDOM_NUMBER = None


# ----------------------------- Create Random Number ---------------------- #
def random_number():
    global RANDOM_NUMBER
    RANDOM_NUMBER = random.randint(1, 5000)
    return RANDOM_NUMBER


# -------------- == Create Random word from 50k word English == -------------- #
def show_word():
    global fill_timer
    window.after_cancel(fill_timer)

    read_photo.config(file="images/card_back.png")
    canvas_photo.itemconfig(title, text="English")
    canvas_photo.itemconfig(word,fill="white")

    df = pd.read_csv("data/50k word English - Sheet1.csv")
    random_number()  # توليد رقم عشوائي جديد

    display_words = df.iloc[RANDOM_NUMBER, 0]
    canvas_photo.itemconfig(word, text=display_words)
    fill_timer = window.after(3000, translation)
    


# ------------------------ == Show Translate Word == ------------------------- #

def translation():
    df = pd.read_csv("data/50k word English - Sheet1.csv")
    display_words = df.iloc[RANDOM_NUMBER, 1]
    read_photo.config(file="images/card_front.png")
    canvas_photo.itemconfig(title, text="اللغه العربيه")
    canvas_photo.itemconfig(word, text=display_words, fill=BACKGROUND_COLOR)


# -------------------------- == Create Window == --------------------------------$

window = Tk()
window.title("FLASH CARDS")
window.minsize(width=700, height=700)
window.config(background=BACKGROUND_COLOR, padx=70, pady=50)
fill_timer = window.after(3000, translation)

# --------------------------- == Create Canvas == -------------------------------$

canvas_photo = Canvas(width=790, height=520, highlightthickness=0, background=BACKGROUND_COLOR)
read_photo = PhotoImage(file="images/card_back.png")
canvas_photo.create_image(400, 265, image=read_photo)

# ----------------------- Create Text in Flash Card ----------------------------#

title = canvas_photo.create_text(400, 150, text="", fill="black", font=FONT_TITLE)
word = canvas_photo.create_text(400, 283, text="", fill="white", font=FONT_WORD)
canvas_photo.grid(column=1, row=0, columnspan=2)

# ---------------------------- Create Buttons ----------------------------#

read_photo_right = PhotoImage(file="images/right.png")
read_photo_wrong = PhotoImage(file="images/wrong.png")

button_right = Button(image=read_photo_right, highlightthickness=0, background=BACKGROUND_COLOR, command=show_word)
button_right.grid(column=1, row=1)

button_wrong = Button(image=read_photo_wrong, highlightthickness=0, background=BACKGROUND_COLOR, command=show_word)
button_wrong.grid(column=2, row=1)


show_word()
window.mainloop()