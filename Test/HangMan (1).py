import random
import tkinter as tk
import pygame
import time
import sys
import os
import math

#make a list of words


#make a function to choose a random word from the list
def choose_word():
    word = random.choice(words)
    return word.upper()

#make a function to play the game
def play(word)


#make a canvas for the game
root = tk.Tk()
canvas = tk.Canvas(root, width=600, height=600, bg="white")
canvas.pack()

#make a frame for the game
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

#make a label for the game
label = tk.Label(frame, text="Hangman", bg="white")
label.place(relwidth=1, relheight=0.1)

#make a button for the game
button = tk.Button(frame, text="Start", bg="white")
button.place(relwidth=0.2, relheight=0.1, relx=0.4, rely=0.2)

#make a canvas for the hangman
canvas = tk.Canvas(frame, width=400, height=400, bg="white")
canvas.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

#make a label for the word
label = tk.Label(frame, text="Word", bg="white")
label.place(relwidth=0.8, relheight=0.1, relx=0.1, rely=0.1)

#make a label for the letters
label = tk.Label(frame, text="Letters", bg="white")
label.place(relwidth=0.8, relheight=0.1, relx=0.1, rely=0.3)

#make a label for the guesses
label = tk.Label(frame, text="Guesses", bg="white")
label.place(relwidth=0.8, relheight=0.1, relx=0.1, rely=0.5)

#make a label for the result
label = tk.Label(frame, text="Result", bg="white")
label.place(relwidth=0.8, relheight=0.1, relx=0.1, rely=0.7)
