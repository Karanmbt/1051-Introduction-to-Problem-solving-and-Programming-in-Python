n = int(input("Enter number: "))

#note: def can't take variables from outside the function :FacePalm:

def sqr_sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i**2
    print(sum)

sqr_sum(n)