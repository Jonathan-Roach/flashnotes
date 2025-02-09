from tkinter import Tk, Canvas, PhotoImage, Button
import pandas as pd
from random import choice

# CHANGE NAME OF FILE TO CHANGE CSV
fileName = 'example.csv'


# Open and Save csv data
data = pd.read_csv(f"data/{fileName}")
df = data.to_dict(orient='records')

# Constants
BACKGROUND_COLOR = "#B1DDC6"
currentCard = {}
timesFlipped=0
categories = [key for key in df[0]]

def nextCard():
    global currentCard
    currentCard = choice(df)
    canvas.itemconfig(cardTitle, fill='black', text=categories[0])
    canvas.itemconfig(cardInfo, fill='black', text=currentCard[categories[0]])
    canvas.itemconfig(cardBackground, image=cardFront)

def flipCard():
    global timesFlipped
    timesFlipped+=1
    if timesFlipped % 2 == 0:
        canvas.itemconfig(cardTitle, fill='black', text=categories[0])
        canvas.itemconfig(cardInfo, fill='black', text=currentCard[categories[0]])
        canvas.itemconfig(cardBackground, image=cardFront)
    else:
        canvas.itemconfig(cardTitle, fill='white', text=categories[1])
        canvas.itemconfig(cardInfo, fill='white', text=currentCard[categories[1]])
        canvas.itemconfig(cardBackground, image=cardBack)


# Window init
window = Tk()
window.title('FlashNotes')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas details
canvas = Canvas(width=800, height=526)
cardFront = PhotoImage(file='images/card_front.png')
cardBack = PhotoImage(file='images/card_back.png')
cardBackground = canvas.create_image(400, 263, image=cardFront)
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.grid(row=0,column=0, columnspan=2)
cardTitle = canvas.create_text(400, 140, text="Title", font=("Arial", 40, 'italic'))
cardInfo = canvas.create_text(400, 263, text="Info", font=("Arial", 60, 'bold'))


# Buttons
arrowIcon = PhotoImage(file='images/arrow.png')
arrow = Button(image=arrowIcon, highlightthickness=0, borderwidth=0, command=nextCard)
arrow.grid(row=1, column=1)

flipIcon = PhotoImage(file='images/flip.png')
flip = Button(image=flipIcon, highlightthickness=0, borderwidth=0, command=flipCard)
flip.grid(row=1, column=0)

# Init flashcards
nextCard()

window.mainloop()
