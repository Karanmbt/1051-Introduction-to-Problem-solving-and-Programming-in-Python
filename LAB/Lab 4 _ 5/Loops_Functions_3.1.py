#3 Bonus

#3.1 Hourglass
n = 5 
print('|', '"' * (n*2), "|", sep='')
for i in range(n-1, 0, -1):
    for j in range(n-i):
        print(" ", end='')  
    print('\\', end='')

    for j in range(1, 2*i):
        print(":", end='')
    print('/', end='')
    print( )    

# Lower-Half
for i in range(2, n+1):
    for j in range(n-i):
        print(" ", end="")
    print('/', end='')
    for j in range(1, 2*i):
        print(":", end="")
    print('\\', end='')
    print()
print('|' * ((n*2)+2))