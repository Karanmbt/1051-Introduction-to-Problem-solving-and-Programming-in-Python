# importing the 'random' module to generate random choices for the coin flip
import random


# This function simulates the flipping of a coin and returns either "heads" or "tails" rubric #1
def coin_sides():
    return random.choice(["heads", "tails"])


# This function simulates flipping a coin 10 times and checks if the result is 5 "heads" and 5 "tails" rubric #2
def coin_flipping():
    heads_total = 0  # this stores the number of times the coin lands on heads in a single game of 10 flips rubric #3
    tails_total = 0  # this stores the number of times the coin lands on tails in a single game of 10 flips rubric #3
    for q in range(10):  #
        result = coin_sides()
        if result == "heads":  # if the result is "heads", increment the heads counter
            heads_total += 1
        else:
            tails_total += 1  # if the result is "tails", increment the tails counter

    # If the result is 5 "heads" and 5 "tails", the function returns True, otherwise it returns False rubric #4
    if heads_total == 5 and tails_total == 5:
        return True  # if the result is 5 heads and 5 tails, we win the game rubric #4
    else:
        return False  # if the result is not 5 heads and 5 tails, we lose the game rubric #4


# Initialize a counter for the number of wins rubric #6
wins = 0
# Simulate the coin flipping game 100,000 times rubric #5
for q in range(10000):
    # If the result of the game is a win, increment the wins counter
    if coin_flipping():
        wins += 1

# Print the odds of winning the game rubric #7
print(
    "The true odds of winning (this rigged game of computer randomness):",
    round(wins / 100000, 2),  # The proportion of games won
    "or 1 in",
    round(100000 / wins, 2),  # The ratio of games won : total games
    "times",
)
