import turtle as t

def circle():
    t.circle(side, extent=None, steps=8)

def octside(x):
    t.fd(side/10)
    t.left(360//x)

side = int(input("Enter the side length: "))

for i in range (side):
    octside(side)

t.done()