n = int(input("enter number: "))

def mult_table(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(i*j, end="\t")
        print()

mult_table(n)
