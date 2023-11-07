initialPos = 7.0
velocity = 5.0
acceleration = 1.0

print("It's time to go on a scavenger hunt!")
print("You'd be amazed how many things can go wrong!")
time = int(input ("Please enter how long you want to travel for:"))

# there is a math error in here causing
# an incorrect answer in the line below
position = initialPos + velocity * time + (1 / 2) *acceleration*time*time

#if you are stuck on the math error, look at the footnote
print(position)