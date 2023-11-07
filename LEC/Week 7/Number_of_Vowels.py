def numVowles(text):
    count = 0
    # do magic
    for char in text:
        #if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        #if char in ["a", "e", "i", "o", "u"]:
        if char in "aeiouAEIOU":
            count += 1
    # magic ends
    return count

answer = numVowles("This is an example sentence.")
print(answer)
# go over writing isFloat