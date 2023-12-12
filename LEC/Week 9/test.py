import random

"""
Our first exercise is to simulate a single turn of Pig where a player rolls until
a 1 (“pig”) is rolled, or the turn total is greater than or equal to 20. We will
call this strategy Hold-at-20. The user doesn’t need to make any choices,
the computer will roll automagically, following the hold-at-20 strategy.
• For each roll, print a line with “Roll:” and the random die roll value
(1-6).
• After a “pig” roll of 1, or a “hold,” print a line with “Turn total:”
followed by the turn total. In the case of a “pig,” this turn total is 0.
"""

def rolld6():
    return random.randint(1,6)

# Hold-at-20 strategy
def holdAt20Turn():
    turnTotal = 0 # Initialize turn total
    while turnTotal < 20: # While turn total is less than 20
        roll = rolld6() # Roll die
        #print("Roll: " + str(roll)) # Print roll
        if roll == 1: # Pig
            turnTotal = 0 # Reset turn total
            break # Break out of loop
        else:
            turnTotal += roll # Add roll to turn total
    #print("Turn total: " + str(turnTotal)) # Print turn total
    return turnTotal # Return turn total

holdAt20Turn() # Test holdAt20Turn()

"""
imulate a given number of hold-at-20 turns, and report the estimated probabilities of the possible scoring outcomes.
Input
Enter a single positive integer indicating the number of turns simulated.
(Larger numbers will tend to yield better estimations.)
Output
• Initially, prompt the user with “Hold-at-20 turn simulations?”
• On the next line, print “Score” and “Estimated Probability” separated
by a tab.
• After the simulations, print a table line for each score outcome that
occurred in increasing order of score. For each score outcome, print
the score, a tab, and the fraction of turn simulations that yielded that
score.  
"""

"""def holdAt20Sim(Trials):
    
    num0 = 0 # Initialize number of 0s
    num20 = 0 # Initialize number of 20s
    num21 = 0 # Initialize number of 21s
    num22 = 0 # Initialize number of 22s
    num23 = 0 # Initialize number of 23s
    num24 = 0 # Initialize number of 24s
    num25 = 0 # Initialize number of 25s
    
    for i in range(Trials): # For each trial
        turnTotal = holdAt20Turn()
        if turnTotal == 0:
            num0 += 1
        elif turnTotal == 20:
            num20 += 1
        elif turnTotal == 21:
            num21 += 1
        elif turnTotal == 22:
            num22 += 1
        elif turnTotal == 23:
            num23 += 1
        elif turnTotal == 24:
            num24 += 1
        elif turnTotal == 25:
            num25 += 1
    print("Score\tEstimated Probability") # Print header
    print("0\t" + str(num0/Trials)) # Print 0
    print("20\t" + str(num20/Trials)) # Print 20
    print("21\t" + str(num21/Trials)) # Print 21
    print("22\t" + str(num22/Trials)) # Print 22
    print("23\t" + str(num23/Trials)) # Print 23
    print("24\t" + str(num24/Trials)) # Print 24
    print("25\t" + str(num25/Trials)) # Print 25"""
    
def holdAt20Sim(Trials):
    results = {0:0, 20:0, 21:0, 22:0, 23:0, 24:0, 25:0} # Initialize results
    for _ in range(Trials): # For each trial
        turnTotal = holdAt20Turn()
        results[turnTotal] += 1
        
    print("Score \tEstimated Probability") # Print header
    
    for score in sorted(results.keys()): # For each score
        int(results[score]) + "\t" + int(results[score]/Trials) # Print score and estimated probability
    
    return results
    
holdAt20Sim(100000) # Test holdAt20Sim()