def count_even_digits(num):
    count = 0
    if num == 0:
        return 1
    if num < 0:
        num = -num
    while num > 0:
        digi = num % 10
        if digi % 2 == 0:
            count += 1
        num //= 10
    return count

x = count_even_digits(1234567890)
print(x)