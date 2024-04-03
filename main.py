from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
df = pd.read_csv("./data/french_words.csv")
to_learn = df.to_dict(orient="records")
random_dict = {}


def random_pair():
    global random_dict
    global timer

    window.after_cancel(timer)
    random_dict = random.choice(to_learn)
    random_word = random_dict["French"]
    canvas.itemconfig(canvas_word, text=random_word, fill="black")
    canvas.itemconfig(canvas_title, text="French", fill="black")
    canvas.itemconfig(canvas_img, image=card_front)
    timer = window.after(3000, change_side)


def change_side():
    canvas.itemconfig(canvas_img, image=card_back)
    canvas.itemconfig(canvas_title, text="English", fill="white")
    canvas.itemconfig(canvas_word, text=random_dict["English"], fill="white")


window = Tk()
window.title("Flash Cards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
timer = window.after(3000, change_side)

card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")

canvas = Canvas(width=800, height=526)
canvas_img = canvas.create_image(400, 263, image=card_front)
canvas_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"), fill='black')
canvas_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"), fill='black')
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=random_pair)
right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=random_pair)
wrong_button.grid(row=1, column=0)

random_pair()

window.mainloop()
