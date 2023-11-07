# Test word: humuhumunukunukuapua'a phonetic guide would be Hoo-moo-hoo-moo-noo-koo-noo-koo-ah-poo-ah’ah.

valid_chars = ('a', 'e', 'i', 'o', 'u', 'p', 'k', 'h', 'l', 'm', 'n', 'w', ' ', "'") #valid characters

Consonants = {
    'p':'p',
    'k':'k',
    'h':'h',
    'l':'l',
    'm':'m',
    'n':'n',
    'w':'w',
    'aw':'aw',
    'iw':'v',
    'ew':'v',
    'uo':'w',
    'ow':'w'
            }

Vowels = {
    'a':'ah',
    'e':'eh',
    'i':'ee',
    'o':'oh',
    'u':'oo'
            }

hw = input("Enter a Hawaiian word: ")
hw = hw.lower()

#function to check for valid characters
def check_valid(hw):
    for char in hw:
        if char not in valid_chars:
            print("Invalid character: " + char)
            again = input("Would you like to enter another word? (y/n): ")
            while again == 'y':
                hw = input("Enter a Hawaiian word: ")
                hw = hw.lower()
                check_valid(hw)
                check_consonants(hw)
                print()
                again = input("Would you like to enter another word? (y/n): ")
  
#function to check for valid consonant combinations
def check_consonants(hw):
    for char in hw:
        if char in Consonants:
            print(Consonants[char], end='')
        elif char in Vowels:
            print(Vowels[char], end='-')
        else:
            print(char, end='')

check_valid(hw)
check_consonants(hw)
print()

#ask if they want to enter another word
again = input("Would you like to enter another word? (y/n): ")
while again == 'y':
    hw = input("Enter a Hawaiian word: ")
    hw = hw.lower()
    check_valid(hw)
    check_consonants(hw)
    print()
    again = input("Would you like to enter another word? (y/n): ")