import turtle as t


def hand():
    t.shape("turtle")
    t.penup()
    t.fd(75)
    t.pendown()
    t.fd(10)
    t.penup()
    t.fd(15)
    t.stamp()

for i in range(12):
    hand()
    t.setpos(0,0)
    t.left(30)

t.done()