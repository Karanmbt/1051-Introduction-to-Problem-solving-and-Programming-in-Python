#2.1 Stairs

#Note: Remove the "#" before the functions before running the code

import turtle as t



#Max Speed
t.speed(0)



#2.1.1 DrawSquare
# myTurtle is the turtle doing the drawing
# size is the length of each of the sides of the square.
def drawSquare(myTurtle, squareSize):
    for S in range (4):
        myTurtle.fd(squareSize)
        myTurtle.lt(90)

#drawSquare(t, 100)



# 2.1.2  Drawing a Row of Squares
# draws a row of squares
# myTurtle is the turtle doing the drawing
# length is how many squares are in the row
# squareSize is the length of each of the sides of each square.
def drawRow(myTurtle, length, squareSize):
    for R in range (length):
        drawSquare(myTurtle, squareSize)
        myTurtle.fd(squareSize)

#drawRow(t, 5, 50)



#2.1.3 Drawing a Grid
# myTurtle is the turtle doing the drawing
# the grid will be "size" squares wide and "size" squares tall
# squareSize is the length of each of the sides of each individual square.
def drawGrid(myTurtle, size, squareSize):
    for G in range (size):
        drawRow(myTurtle, size, squareSize)
        myTurtle.penup()
        myTurtle.rt(180)
        myTurtle.fd(squareSize*size)
        myTurtle.lt(90)
        myTurtle.fd(squareSize)
        myTurtle.lt(90)
        myTurtle.pendown() #fixed the extra line, like why work hard :skull: lol

#drawGrid(t, 4, 50)



#2.1.4 Drawing a Stair of Squares
# myTurtle is the turtle doing the drawing
# height is how tall the stairs are going to be
# squareSize is the length of each of the sides of each square.
def drawSquareStairs(myTurtle, height, squareSize):
    for G in range (height):
        drawRow(myTurtle, height, squareSize)
        myTurtle.penup()
        myTurtle.rt(180)
        myTurtle.fd(squareSize*height)
        myTurtle.rt(90)
        myTurtle.fd(squareSize)
        myTurtle.rt(90)
        myTurtle.pendown()
        height -= 1     #for the steps 

drawSquareStairs(t, 6, 50)



t.done()