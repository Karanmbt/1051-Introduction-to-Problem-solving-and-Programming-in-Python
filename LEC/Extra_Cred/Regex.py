# Q1. I like animals. How many words contain the word ’cat’ or ’dog’ in them?
def cat_dog():
    file = open("LEC\Extra_Cred\words.txt", "r")
    words = file.read().split()
    file.close()
    count = 0
    for word in words:
        if "cat" in word or "dog" in word:
            count += 1
    print("There are", count, "words that contain cat or dog in them")


cat_dog()
print()


# Q2. Four letters words are supposedly naughty. How many four letter words are there?
def naughty_4Lwords():
    file = open("LEC\Extra_Cred\words.txt", "r")
    words = file.read().split()
    file.close()
    count = 0
    for word in words:
        if len(word) == 4:
            count += 1
    print("There are", count, "naughty words")


naughty_4Lwords()
print()


# Q3. I am scared of pyramid schemes and mlms. How many words contain ‘hun’ in them?
def pyramid_schemes():
    file = open("LEC\Extra_Cred\words.txt", "r")
    words = file.read().split()
    file.close()
    count = 0
    for word in words:
        if "hun" in word:
            count += 1
    print("There are", count, "words that contain hun in them")


pyramid_schemes()
print()


# Q4. Do more words end in “ing” or “ion?”
def ing_ion():
    file = open("LEC\Extra_Cred\words.txt", "r")
    words = file.read().split()
    file.close()
    ing_count = 0
    ion_count = 0
    for word in words:
        if word.endswith("ing"):
            ing_count += 1
        elif word.endswith("ion"):
            ion_count += 1
    print("There are", ing_count, "words that end in ing")
    print("There are", ion_count, "words that end in ion")

    if ing_count > ion_count:
        print("There are more words that end in ing")
    elif ion_count > ing_count:
        print("There are more words that end in ion")
    else:
        print("There are an equal amount of words that end in ing and ion")


ing_ion()
print()


# Q5. How many words contain a “q” not immediately followed by a “u.”
def q_but_no_u():
    file = open("LEC\Extra_Cred\words.txt", "r")
    words = file.read().split()
    file.close()
    count = 0
    for word in words:
        if "q" in word and "qu" not in word:
            count += 1
    print("There are", count, "words that contain q not immediately followed by u")

q_but_no_u()


# Q6. How many words have no vowels?
def no_vowels():
    file = open("LEC\Extra_Cred\words.txt", "r")
    words = file.read().split()
    file.close()
    count = 0
    for word in words:
        if "a" not in word and "e" not in word and "i" not in word and "o" not in word and "u" not in word:
            count += 1
    print("There are", count, "words that contain no vowels")
    
no_vowels()
print()


# Q7. How many words consist of only vowels?
def only_vowels():
    file = open("LEC\Extra_Cred\words.txt", "r")
    words = file.read().split()
    file.close()
    count = 0
    for word in words:
        if "a" in word and "e" in word and "i" in word and "o" in word and "u" in word:
            count += 1
    print("There are", count, "words that contain only vowels")

only_vowels()
print()


# Q8. How many words are contracted with “not,” meaning they end with“’nt”
def not_contracted():
    file = open("LEC\Extra_Cred\words.txt", "r")
    words = file.read().split()
    file.close()
    count = 0
    for word in words:
        if word.endswith("n't"):
            count += 1
    print("There are", count, "words that are contracted with not")
    
not_contracted()
print()


# Q9. How many words with two vowels in a row are there?
def two_vowels_in_a_row():
    file = open("LEC\Extra_Cred\words.txt", "r")
    words = file.read().split()
    file.close()
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    for word in words:
        for i in range(len(word) - 1):
            if word[i] in vowels and word[i + 1] in vowels:
                count += 1
                break
    print("There are", count, "words that contain two vowels in a row")
    
two_vowels_in_a_row()
print()


# Q10. How many words with at least two vowels are there? The vowels need not be adjacent, like in the previous problem.