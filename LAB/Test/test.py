import random


def averagePiggamestowin(limit):
    score = 0
    turns = 0
    games = 0
    for _ in range(limit):
        while score < 100:
            games += 1
            turnTotal = 0
            while turnTotal < 20 and turnTotal + score < 100:
                turns += 1
                roll = random.randint(1, 6)

                if roll == 1:
                    turnTotal = 0
                    score = 0
                    break
                else:
                    turnTotal += roll
        score = score + turnTotal
    return turns/games


print(averagePiggamestowin(1000))