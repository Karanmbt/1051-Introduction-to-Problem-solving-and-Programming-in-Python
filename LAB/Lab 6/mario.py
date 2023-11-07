height = int(input("Enter a positive integer between 1 and 8: ")) # for the height of the blocks

if 8 >= height <= 1:
    print("the number should be between 1 and 8, enter again")
else:
    for i in range(height+1):
    
#let’s allow the user to decide just how tall the pyramids should be by first prompting them for a positive integer between, say, 1 and 8, inclusive.
        for j in range(height-i):
            print(" ", end="")
        for k in range(i):
            print("#", end="")
        print("  ", end="")
        for l in range(i):
            print("#", end="")
        print()