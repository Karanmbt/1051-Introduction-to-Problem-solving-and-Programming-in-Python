def is3DArmstrong(num):
    hund = num // 100
    tens = (num % 100) // 10
    ones = num % 10
    return num == hund ** 3 + tens ** 3 + ones ** 3

def riddler():
    for num in range(1001,10000,2):
        thousands = num // 1000
        hund = (num // 100) % 10
        tens = (num // 10) % 10
        ones = num % 10
        if thousands != hund and thousands != tens and thousands != ones and hund != tens and hund != ones and tens != ones:
            if is3DArmstrong(num):
                print(num)