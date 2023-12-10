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


def convert(word):
    if word in double_vowels:
        return double_vowels[word]
    elif word in Vowels:
        return Vowels[word]
    elif word in Consonants:
        return Consonants[word]
    elif word in valid_chars:
        return word
    else:
        return ""
    

def check_valid(word):
    for char in word:
        if char not in valid_chars:
            print(f"{char} is not a valid character")
            return False
    return True


def check_consonants(word):
    for char in word:
        if char in Consonants:
            print(f"{char} is a consonant")
            return True
    return False


def check_vowels(word):
    for char in word:
        if char in Vowels:
            print(f"{char} is a vowel")
            return True
    return False


def check_double_vowels(word):
    for char in word:
        if char in double_vowels:
            print(f"{char} is a double vowel")
            return True
    return False

if check_valid(hw):
    if check_consonants(hw):
        if check_vowels(hw):
            if check_double_vowels(hw):
                for char in hw:
                    print(convert(char), end="")
            else:
                print("No double vowels")
        else:
            print("No vowels")
    else:
        print("No consonants")
        
        

again = input("Would you like to enter another word? (y/n): ")
while again == "y":
    hw = input("Enter a Hawaiian word: ")
    hw = hw.lower()
    check_valid(hw)
    check_consonants(hw)
    print()
    again = input("Would you like to enter another word? (y/n): ")
