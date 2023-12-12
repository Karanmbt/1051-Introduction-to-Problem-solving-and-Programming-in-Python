def Valid_Hawaiian():
    valid_chars = ["a", "e", "i", "o", "u", "p", "k", "h", "l", "m", "n", "w", " ", "'"]
    while True:  # while valid input is TRUE
        Hawaiian_Word_To_Translate = input(
            "Input a VALID Hawaiian word for the Hawaiian Word Pronouncer:"
        )
        Hawaiian_Word_To_Translate = Hawaiian_Word_To_Translate.lower()
        HWTT = []
        for letter in Hawaiian_Word_To_Translate:
            HWTT.append(letter)
        Check = HWTT
        valid_input = True
        for character in Check:
            if character not in valid_chars:
                valid_input = False
                print(
                    "WARNING: The input has offending characters, please put in a different input"
                )
                break
        if valid_input:
            return Hawaiian_Word_To_Translate


def Translate_Hawaiian(HWTT):
    Hawaiian_dictionary_vowels_or_consonants = {
        "a": "ah",
        "e": "eh",
        "i": "ee",
        "o": "oh",
        "u": "oo",
        "p": "p",
        "k": "k",
        "h": "h",
        "l": "l",
        "m": "m",
        "n": "n",
        "w": "w",
    }
    Hawaiian_dictionary_double_vowels = {
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
    W_special = {"aw": "w", "iw": "iv", "ew": "ev", "uw": "uw", "ow": "ow"}
    Translation = ""
    Full_Translation = ""
    for characters in range(len(HWTT) - 1):  # subtract 1 from the range
        while characters <= len(HWTT) - 1:  # subtract 1 from the length
            if HWTT[characters] == "w" and HWTT[characters + 1] in ["i", "e"]:
                Translation = (
                    Translation
                    + "v"
                    + Hawaiian_dictionary_vowels_or_consonants[HWTT[characters + 1]]
                    + "-"
                )
                characters = characters + 2

            elif HWTT[characters] == "w" and HWTT[characters + 1] in ["a", "u", "o"]:
                Translation = (
                    Translation
                    + "w"
                    + Hawaiian_dictionary_vowels_or_consonants[HWTT[characters + 1]]
                    + "-"
                )
                characters = characters + 2

            elif HWTT[characters : characters + 2] in Hawaiian_dictionary_double_vowels:
                Translation = (
                    Translation
                    + Hawaiian_dictionary_double_vowels.get(HWTT[characters], '')
                    + "-"
                )
                characters = characters + 2

            elif HWTT[characters] in Hawaiian_dictionary_vowels_or_consonants:
                Translation = (
                    Translation
                    + Hawaiian_dictionary_vowels_or_consonants[HWTT[characters]]
                    + "-"
                )
                characters = characters + 1

            elif HWTT[characters] == " ":
                Translation = Translation + " "
                characters += 1

            elif HWTT[characters] == "'":
                Translation = Translation + "'"
                characters += 1

        Full_Translation += Translation
    return Full_Translation


def Redo():
    while True:
        print("This Hawaiian word is pronounced", Translate_Hawaiian(Valid_Hawaiian()))
        retry = input("Do you want to put in another word? (Y/YES or N/NO):")
        if retry.upper() not in ["Y", "YES"]:
            break
        else:
            Valid_Hawaiian()


Redo()
