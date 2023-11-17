import random_word
from random_word import RandomWords

randomWord = RandomWords()
lifeRemaining = 5


words = randomWord.get_random_word()
wordsCharacters = []

for letter in words:
    wordsCharacters.append(letter)
print(wordsCharacters)

letterInWord = len(wordsCharacters)
print(f'there are {letterInWord} letters')


def lettercheck():

    global lifeRemaining

    while True:
        if lifeRemaining == 0:
            break
    letterChosen = input("Choose a letter").lower()

    if letterChosen in wordsCharacters:
        print(f'letter {letterChosen} is a part of the letters')
        print("find the rest of the words.")
        lettercheck()

    elif letterChosen not in wordsCharacters:
        lifeRemaining =lifeRemaining -1
        print(f'letter{letterChosen} is not in the list')
        print(f'You have lost a life, you now have {lifeRemaining} lives')
        lettercheck()

lettercheck()
