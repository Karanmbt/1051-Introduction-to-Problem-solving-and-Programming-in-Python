import random


def holdAt20(limit=20):
    turnTotal = 0
    while turnTotal < limit:
        roll = random.randint(1, 6)
        # print("Roll:", roll)
        if roll == 1:
            turnTotal = 0
            # print("Turn Total:", turnTotal)
            return turnTotal
        else:
            turnTotal += roll
    # print("Turn Total:", turnTotal)
    return turnTotal


def holdAt20Outcomes(trials):
    outcomes = {0: 0}
    for val in range(20, 26):
        outcomes[val] = 0
    for _ in range(trials):
        score = holdAt20()
        outcomes[score] += 1
    for score in outcomes:
        print(score, outcomes[score] / trials)


# 20 21 22 23 24 25
# 42 43 44 45 46 47


def holdAtXOutcomes(limit, trials):
    outcomes = {0: 0}
    for score in range(limit, limit + 6):
        outcomes[score] = 0
    for _ in range(trials):
        score = holdAt20(limit)
        outcomes[score] += 1
    for score in outcomes:
        print(score, outcomes[score] / trials)



def holdAt20orGoal(limit, score):
    turnTotal = 0
    while turnTotal < limit and turnTotal + score < 100:
        roll = random.randint(1, 6)
        # print("Roll:", roll)
        if roll == 1:
            turnTotal = 0
            return 0, score
        else:
            turnTotal += roll
    return turnTotal, score + turnTotal

#What is the expected number of turns per solitaire game with a hold-at-20-or-goal play policy? Simulate a given number of solitaire Pig games where a player rolls until a 1 (“pig”) is rolled, or the turn total is greater than or equal to 20, or the score plus the turn total is greater than or equal to 100. Report the average number of turns per game. 
def holdAt20orGoalOutcomes(trials):
    outcomes = {0: 0}
    for val in range(20, 26):
        outcomes[val] = 0
    for _ in range(trials):
        score = holdAt20orGoalGame()
        outcomes[score] += 1
    for score in outcomes:
        print(score, outcomes[score] / trials)



def holdAt20orGoalGame():
    playerScore = 0
    computerScore = 0
    playerTurn = True
    while playerScore < 100 and computerScore < 100:
        if playerTurn:
            turnTotal = 0
            while True:
                roll = random.randint(1, 6)
                print("Roll:", roll)
                if roll == 1:
                    turnTotal = 0
                    print("Turn Total:", turnTotal)
                    break
                else:
                    turnTotal += roll
                    print("Turn Total:", turnTotal)
                    print("Player Score:", playerScore)
                    print("Computer Score:", computerScore)
                    print()
                    if playerScore + turnTotal >= 100:
                        playerScore += turnTotal
                        print("Player Score:", playerScore)
                        print("Computer Score:", computerScore)
                        print("Player wins!")
                        return
                    elif turnTotal >= 20:
                        playerScore += turnTotal
                        print("Player Score:", playerScore)
                        print("Computer Score:", computerScore)
                        print()
                        break
            playerTurn = False
        else:
            turnTotal = 0
            while True:
                roll = random.randint(1, 6)
                print("Roll:", roll)
                if roll == 1:
                    turnTotal = 0
                    print("Turn Total:", turnTotal)
                    break
                else:
                    turnTotal += roll
                    print("Turn Total:", turnTotal)
                    print("Player Score:", playerScore)
                    print("Computer Score:", computerScore)
                    print()
                    if computerScore + turnTotal >= 100:
                        computerScore += turnTotal
                        print("Player Score:", playerScore)
                        print("Computer Score:", computerScore)
                        print("Computer wins!")
                        return
                    elif turnTotal >= 20:
                        computerScore += turnTotal
                        print("Player Score:", playerScore)
                        print("Computer Score:", computerScore)
                        print()
                        break
            playerTurn = True
