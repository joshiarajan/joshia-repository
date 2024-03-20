from random import randint
from tkinter import *
from tkinter import ttk

def check_guess():
    global attempts
    guess = int(entry_guess.get())
    attempts += 1

    if guess == random_number:
        result_label["text"] = "You won!"
    elif guess < random_number:
        result_label["text"] = "Too low"
    elif guess > random_number:
        result_label["text"] = "Too high"

window = Tk()
window.geometry("400x400+200+50")
window.title("Number Guessing Game")

random_number = randint(1, 10)
attempts = 0

title_label = ttk.Label(window, text='Number Guessing Game', font=('Helvetica', 16, 'bold'))
title_label.place(x=70, y=20)

guess_label = ttk.Label(window, text="Guess a number:")
guess_label.place(x=50, y=80)

entry_guess = ttk.Entry(window)
entry_guess.place(x=200, y=80)

check_button = ttk.Button(window, text="Check", command=check_guess)
check_button.place(x=150, y=120)

result_label = ttk.Label(window, text="")
result_label.place(x=150, y=160)

window.mainloop()
