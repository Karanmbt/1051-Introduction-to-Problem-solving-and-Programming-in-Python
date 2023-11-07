def three_digi(number):
    if not isinstance(number, int):
        return False
    if number < 100 or number > 999:
        return False
    sum = 0
    temp = number
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if number == sum:
        return True
    else:
        return False
    
    
x = three_digi(371)
print(x)
