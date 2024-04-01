from tkinter import *
import pandas as pd
import random

def random_pair():
    df = pd.read_csv("./data/french_words.csv")
    list_of_dicts = [{row[df.columns[0]]: row[df.columns[1]]} for row in df.to_dict(orient='records')]
    random_dict = random.choice(list_of_dicts)
    random_word = next(iter(random_dict))
    canvas.delete(french_word)
    canvas.create_text(400, 263, text=f"{random_word}", font=("Ariel", 60, "bold"), fill='black')

BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Flash Cards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")

canvas = Canvas(width=800, height=526)
canvas.create_image(400, 263, image=card_front)
canvas.create_text(400, 150, text="French", font=("Ariel", 40, "italic"), fill='black')
french_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"), fill='black')
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=random_pair)
right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=random_pair)
wrong_button.grid(row=1, column=0)

window.mainloop()
