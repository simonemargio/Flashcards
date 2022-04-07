from tkinter import *
import random
import pandas

# Put the path of the file containing the questions/objects to learn
file_words = "data/english_words.csv"
# put the path of the file where you want to save the wrong elements and that you have to repeat better
file_learn = "data/words_to_learn.csv"
# time you have (in milliseconds) to respond.
time = 3000
# title you want to give to the front and back card
text_card = "English"
text_card_flip = "Italian"

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}


def flip_card():
    """
    Show the back of the current card
    """
    global current_card
    c.itemconfig(card_background, image=image_card_back)
    c.itemconfig(card_title, text=text_card_flip, fill="white")
    c.itemconfig(card_word, text=current_card[text_card_flip], fill="white")


def set_new_card():
    """
    Prepare and show the next card
    """
    global current_card
    current_card = new_card()
    print(current_card)
    c.itemconfig(card_title, text=text_card, fill="black")
    c.itemconfig(card_word, text=current_card[text_card], fill="black")
    w.after(time, func=flip_card)
    c.itemconfig(card_background, image=image_card_front)


def new_card():
    """
    Prepare and show the next card
    :return: random card
    """
    return random.choice(data)


def is_know():
    """
    Known card. Save the remaining cards not yet released in the specific file used later for the repetitions
    """
    global current_card
    data.remove(current_card)
    data_to_save = pandas.DataFrame(data)
    data_to_save.to_csv(file_learn)
    set_new_card()

# File management
try:
    data_csv = pandas.read_csv(file_learn)
except FileNotFoundError:
    original_data = pandas.read_csv(file_words)
    data = original_data.to_dict(orient="records")
else:
    data = data_csv.to_dict(orient="records")

# GUI
w = Tk()
w.title("Flash Cards")
w.config(padx=50, pady=50, background=BACKGROUND_COLOR)
c = Canvas(width=800, height=526, highlightthickness=0)
image_card_front = PhotoImage(file="images/card_front.png")
image_card_back = PhotoImage(file="images/card_back.png")
card_background = c.create_image(400, 263, image=image_card_front)
c.config(bg=BACKGROUND_COLOR)
c.grid(column=0, row=0, columnspan=2)

card_title = c.create_text(400, 150, text=text_card, font=("Ariel", 40, "italic"))
card_word = c.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))

image_button_wrong = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=image_button_wrong, highlightthickness=0, command=set_new_card)
button_wrong.grid(column=0, row=1)

image_button_correct = PhotoImage(file="images/right.png")
button_correct = Button(image=image_button_correct, highlightthickness=0, command=is_know)
button_correct.grid(column=1, row=1)

# Engine
set_new_card()

w.mainloop()
