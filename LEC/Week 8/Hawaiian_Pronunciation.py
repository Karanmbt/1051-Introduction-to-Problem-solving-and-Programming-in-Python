# create a dictionary that maps each letter to its corresponding pronunciation in Hawaiian
hawaiian_dict = {
    'a': 'ah',
    'e': 'eh',
    'i': 'ee',
    'o': 'oh',
    'u': 'oo',
    'h': 'h',
    'k': 'k',
    'l': 'l',
    'm': 'm',
    'n': 'n',
    'p': 'p',
    'w': 'w',
}

# get user input
word = input("Enter a Hawaiian word: ")

# iterate over the letters in the user input and print out the corresponding pronunciation for each letter
for letter in word:
    print(hawaiian_dict.get(letter.lower(), letter), end='')
    
print()  # print a newline at the end

