import tkinter as tk
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
TEXT_COLOR_DARK = "black"
TEXT_COLOR_LIGHT = "white"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# print(to_learn)
# Unknown Button Pressed

def is_known():
    print(current_card)
    to_learn.remove(current_card)
    df = pandas.DataFrame(to_learn)
    df.to_csv("data/words_to_learn.csv", index=False)



def card_flip():
    canvas.itemconfig(card_side, image=card_back)
    canvas.itemconfig(card_title, fill=TEXT_COLOR_LIGHT, text="English")
    canvas.itemconfig(card_word, fill=TEXT_COLOR_LIGHT, text=current_card["English"])


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    # print(current_card["French"])
    canvas.itemconfig(card_title, text="French", fill=TEXT_COLOR_DARK)
    canvas.itemconfig(card_word, text=current_card["French"], fill=TEXT_COLOR_DARK)
    canvas.itemconfig(card_side, image=card_front)
    current_card = current_card
    flip_timer = window.after(3000, card_flip)


# Read the French words data


# UI Setup
window = tk.Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50)
window.configure(bg=BACKGROUND_COLOR)
canvas = tk.Canvas(width=800, height=526)

card_front = tk.PhotoImage(file="./images/card_front.png")
card_back = tk.PhotoImage(file="./images/card_back.png")

card_side = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"), fill=TEXT_COLOR_DARK)
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"), fill=TEXT_COLOR_DARK)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# language = tk.Label(text="Turkish")
# language.grid(column=1, row=0)

# word = tk.Label(text="word")
# word.grid(column=1, row=1 )


wrong_icon = tk.PhotoImage(file="./images/wrong.png")
wrong_button = tk.Button(image=wrong_icon, highlightthickness=0, command=lambda: (next_card()))
wrong_button.grid(column=0, row=1)

right_icon = tk.PhotoImage(file="./images/right.png")
right_button = tk.Button(image=right_icon, highlightthickness=0, command=lambda: (next_card(), is_known()))
right_button.grid(column=1, row=1)

flip_timer = window.after(3000, card_flip)
next_card()
window.mainloop()
