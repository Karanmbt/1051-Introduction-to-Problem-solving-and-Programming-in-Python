import turtle as t

t.speed(0)

def tri(x):
    t.fd(x)
    t.left(120)

#Big
for i in range(3):
    tri(200)

#Small 1
for i in range(3):
    tri(100)

#Small 2
t.fd(100)
for i in range(3):
    tri(100)


#Small 3
t.setpos(50.00,86.60)
for i in range(3):
    tri(100)


t.done()