# Q4

import turtle

turtle.bgcolor("#000000")  # This makes the background black
bob = turtle.Turtle()
bob.speed(0)

# Q1: What is iro?
# I have no idea what these are.
# Programmer said they are "traditional"
iro = ["#F08F90", "#F2EA0A", "#003171", "#A87CA0", "#8DB255", "#317589"]


excelsior = 360 / (len(iro)) + 7

# Q2: What is sky? What does changing it do?
# Programmer said it affected how "groovy" it was
sky = 6
# Q3: What is petal? What does changing it do?
# Programmer said that it affected how "awesome" it was
petal = 15
# Q4: What is style? What does changing it do?
# Programmer said "the variable explains itself".
# I'm beginning to think the programmer is a liar.
style = 150


# Q5: What does desegni do?  What does storony and pikkus affect?
# Seems so familiar, like the students of CIS 1051 have written this before...
def desegni(bob, storony, pikkus):
    for _ in range(storony):
        bob.forward(pikkus)
        bob.left(360 / storony)


# Q6: What does fnord do?
def fnord(bob):
    for i in iro:
        bob.pencolor(i)
        desegni(bob, sky, style)
        bob.left(excelsior)


for i in range(petal):
    fnord(bob)

turtle.done()


# Ans 1. iro is a list of hexadecimal colour number codes.

# Ans 2. sky determines the value for storony from the function desegni(), when it is called in the function fnord(),
# it uses the value of sky (6) to iterate the turtle (bob) going forward and turning left by 360 / storony or 6 in this case.
# (making bob do some super groovy stuff)

# Ans 3. petal's value determines how many times to iterate the function fnord(). 
# Changing this will increase or decrease the number of times the program runs the function being called "fnord(bob)"

# Ans 4. style, it determines the value of pikkus from the function desegni() which uses
# style's value to make the turtle (bob) go forward by 150.
# Changing this will make the size of the bigger or smaller.

# Ans 5. desegni() is a function that takes in 3 parameters, bob, storony, and pikkus.

# Ans 6. The fnord() function uses a for loop where the value of "i"  is determined by iro,
# it first sets the pen color to the value of i then calls the function desegni and gives "bob, sky, style"
# as inputs for its parameters bob being the turtle, sky for storony and style for pikkus.
# On the next like the turtle turns left by the value of excelsior which is 360 / the length of iro + 7.
