import re
import random

# Part 1 - Regex Dictionary


# 1.1
def animals():
    data = open("words.txt", "r")
    # pattern = "\w*cat\w*|\w*dog\w*"
    pattern = "cat|dog"
    text = data.read()
    answer = re.findall(pattern, text)
    # print(answer)
    print(len(answer))


# 1.2
def fourLetterWords():
    data = open("words.txt", "r")
    pattern = "\w{4}"
    text = data.read()
    text = text.lower()
    answer = re.findall(pattern, text)
    # print(answer)
    print(len(answer))


# 1.3
def findHun():
    data = open("words.txt", "r")
    pattern = "\w*hun\w*"
    text = data.read()
    text = text.lower()
    anwser = re.findall(pattern, text)
    # print(anwser)
    print(len(anwser))


# 1.4
def findIng():
    data = open("words.txt", "r")
    text = data.read()
    text = text.lower()
    pattern1 = "\w*ing"
    pattern2 = "\w*ion"
    answer1 = re.findall(pattern1, text)
    answer2 = re.findall(pattern2, text)
    # print(answer1, answer2)
    print(len(answer1), len(answer2))
    if len(answer1) > len(answer2):
        print("There are more words ending in ing")
    else:
        print("There are more words ending in ion")


# 1.5
def findQNotU():
    data = open("words.txt", "r")
    text = data.read()
    text = text.lower()
    pattern = "\w*[qQ][^u]"
    answer = re.findall(pattern, text)
    # print(answer)
    print(len(answer))


# 1.6
def noVowels():
    data = open("words.txt", "r")
    text = data.read()
    items = text.lower().split()
    pattern = "[^aeiouAEIOU]"
    answer = re.findall(pattern, text)
    print(answer)
    print(len(answer))


# 1.7
def onlyVowels():
    data = open("words.txt", "r")
    text = data.read()
    items = text.lower().split()
    pattern = "[aeiouAEIOU]*"
    answer = re.findall(pattern, text)
    print(answer)
    print(len(answer))


# 1.8
def findNot():
    data = open("words.txt", "r")
    text = data.read()
    text = text.lower()
    pattern = "\w*n't"
    answer = re.findall(pattern, text)
    # print(answer)
    print(len(answer))


# 1.9
def twoVowels():
    data = open("words.txt", "r")
    text = data.read()
    text = text.lower()
    # print(text)
    pattern = "\w*[aeiouAEIOU]{2}\w*"
    answer = re.findall(pattern, text)
    # print(answer)
    print(len(answer))

# 1.10
def leastTwoVowels():
    data = open("words.txt", "r")
    text = data.read()
    text = text.lower()
    pattern = "[aeiou]*"
    answer = re.findall(pattern, text)
    lst = []
    for i in answer:
        if len(i) >= 2:
            lst.append(i)
    # print(lst)
    print(len(lst))


# Part 2 - More Regex


# 2.1
def difference():
    print(".* selected everything, while .*? selects nothing")


# 2.2
def nakamoto(filename):
    data = open(filename, "r")
    text = data.read()
    pattern = "[A-Z][a-z]*\sNakamoto"
    answer = re.findall(pattern, text)
    return answer


# 2.3
def twentyToNinetyNine(filename):
    data = open(filename, "r")
    text = data.read()
    pattern = "[2-9][0-9]"
    answer = re.findall(pattern, text)
    print(answer)
    # print(len(answer))


def generateNumFile(num, outputFile):
    data = open(outputFile, "w")
    for i in range(num):
        data.write(str(i) + "\n")
    data.close()


# 2.4
def findDollar(filename):
    data = open(filename, "r")
    text = data.read()
    print(text)
    pattern = r"\$\d*(?:,\d{3})*\.?\d{2}?"
    answer = re.findall(pattern, text)
    return answer


# Part 3 - Strong Password Detection
def passwordCheck(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$"
    answer = re.findall(pattern, password)
    if len(answer) == 0:
        print("Not a strong password")
    else:
        print("Strong password")


# Part 4 - Regex Password
def passwordGenerator(filename, length):
    data = open(filename, "r")
    text = data.read()
    text = text.lower().split()
    password = ""
    for i in range(length):
        num = random.randint(0, len(text))
        password += text[num] + "-"
    password = password.strip("-")
    return password


print(passwordGenerator("words.txt", 4))
