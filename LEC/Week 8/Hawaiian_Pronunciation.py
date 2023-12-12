# Test word: humuhumunukunukuapua'a phonetic guide would be Hoo-moo-hoo-moo-noo-koo-noo-koo-ah-poo-ah’ah.

valid_chars = (
    "a",
    "e",
    "i",
    "o",
    "u",
    "p",
    "k",
    "h",
    "l",
    "m",
    "n",
    "w",
    " ",
    "'",
)

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

Vowels = {
    "a": "ah",
    "e": "eh",
    "i": "ee",
    "o": "oh",
    "u": "oo"
    }

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


def check_valid_chars(hw):
    for char in hw:
        if char not in valid_chars:
            return False
    return True


def check_valid_consonants(hw):
    for char in hw:
        if char not in Consonants:
            return False
    return True




if check_valid_chars(hw):
    if check_valid_consonants(hw):
        print("Valid Hawaiian word")
    else:
        print("Invalid Hawaiian word")
else:
    print("Invalid Hawaiian word")
