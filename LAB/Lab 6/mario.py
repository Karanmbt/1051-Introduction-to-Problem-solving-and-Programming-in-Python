while True:
    height = int(input("Enter a positive integer between 1 and 8: "))  # for the height of the blocks

    if height < 1 or height > 8:
        print("The number should be between 1 and 8, enter again")
    else:
        break

for i in range(1, height + 1):
    for j in range(height - i):
        print(" ", end="")
    for k in range(i):
        print("#", end="")
    print("  ", end="")
    for l in range(i):
        print("#", end="")
    print()