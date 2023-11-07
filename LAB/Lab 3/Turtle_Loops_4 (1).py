import turtle as t

n = int(input ('Enter the number of sides: '))

for _ in range(n):
    t.fd(100)
    t.left(360//n)

t.done()