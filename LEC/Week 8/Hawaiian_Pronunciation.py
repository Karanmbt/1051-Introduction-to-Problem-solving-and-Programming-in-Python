# Test word: humuhumunukunukuapua'a phonetic guide would be Hoo-moo-hoo-moo-noo-koo-noo-koo-ah-poo-ah’ah.

valid_chars = ("a","e","i","o","u","p","k","h","l","m","n","w"," ","'",)

Consonants = {
    "p": "p",
    "k": "k",
    "h": "h",
    "l": "l",
    "m": "m",
    "n": "n",
    "w": "w",
    "aw": "aw",
    "iw": "v",
    "ew": "v",
    "uo": "w",
    "ow": "w",
}

Vowels = {"a": "ah", "e": "eh", "i": "ee", "o": "oh", "u": "oo"}

double_vowels = {
    "ai": "eye",
    "ae": "eye",
    "ao": "ow",
    "au": "ow",
    "ei": "ay",
    "eu": "eh-oo",
    "iu": "ew",
    "oi": "oyo",
    "ou": "ow",
    "ui": "ooey",
}

hw = input("Enter a Hawaiian word: ")
hw = hw.lower()


# ask if they want to enter another word
again = input("Would you like to enter another word? (y/n): ")
while again == "y":
    hw = input("Enter a Hawaiian word: ")
    hw = hw.lower()
    check_valid(hw)
    check_consonants(hw)
    print()
    again = input("Would you like to enter another word? (y/n): ")
