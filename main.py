import tkinter as tk
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
TEXT_COLOR = "black"


# Unknown Button Pressed

def unknown_button_press():
    with open("./data/french_words.csv") as file:
        data = pandas.read_csv(file)
        random_french_word = random.choice(data["French"].to_list())
        assign_word(random_french_word)
        return random_french_word

def assign_word(random_word):
    canvas.itemconfig(word_text, text=random_word)


# Read the French words data


# UI Setup
window = tk.Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50)
window.configure(bg=BACKGROUND_COLOR)
canvas = tk.Canvas(width=800, height=526)



card_front = tk.PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=card_front)
canvas.create_text(400, 150, text="Turkish", font=("Ariel", 40, "italic"), fill=TEXT_COLOR)
word_text = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"), fill=TEXT_COLOR)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# language = tk.Label(text="Turkish")
# language.grid(column=1, row=0)

# word = tk.Label(text="word")
# word.grid(column=1, row=1)


wrong_icon = tk.PhotoImage(file="./images/wrong.png")
wrong_button = tk.Button(image=wrong_icon, highlightthickness=0, command=unknown_button_press)
wrong_button.grid(column=0, row=1)

right_icon = tk.PhotoImage(file="./images/right.png")
button = tk.Button(image=right_icon, highlightthickness=0)
button.grid(column=1, row=1)



canvas.itemconfig(word_text, text=unknown_button_press())


window.mainloop()