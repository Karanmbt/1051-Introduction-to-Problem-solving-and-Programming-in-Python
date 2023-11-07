#2.2 Spirals

#Note: Remove the "#" before the functions before running the code

import turtle as t



#Max Speed
t.speed(0)



#2.2.1 N Sided Polygon
def drawNgon(myTurtle, numSides, sideLength):
    for _ in range(numSides):
        myTurtle.fd(sideLength)
        myTurtle.left(360//numSides)

#drawNgon(t, 3, 100)



#2.2.2 Super Spiral
# draws a spiral of shapes.
# this is done by drawing a single polygon, rotating the turtle a bit,
# drawing another polygon until the spiral is completed.
# numSides defines the shape of the polygons
# sideLength defines how big each polygon is
# numShapes defines how many polygons make up the spiral
def drawNgonSpiral(myTurtle, numSides, sideLength, numShapes):
    for S in range(numShapes):
        drawNgon(myTurtle, numSides, sideLength)
        myTurtle.penup
        myTurtle.rt(720/numShapes)
        myTurtle.pendown

#drawNgonSpiral(t,6,100,35)



t.done()