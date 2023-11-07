def beer(x):
    print(x, "bottles of beer on the wall,", x, "bottles of beer")
    x -= 1
    print("Take one down, pass it around,", x, "bottles of beer on the wall")


bottles = int(input("Enter the number of beers: "))

for i in range (bottles):
    beer(bottles)
    bottles -= 1