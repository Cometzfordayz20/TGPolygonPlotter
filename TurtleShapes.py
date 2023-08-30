# This is a sample Python script.
import math
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import turtle
# Controlls The size of every polygon shape
size = 50
# Controlls number of polygons after square
numOfPolygons = 4

# Turtle Graphics Screen object
s = turtle.getscreen()
# Turtle Graphics Turtle object
t = turtle.Turtle()

t.penup()
t.setpos(-25, 200)
t.pendown()

t.rt(60)
t.fd(math.sqrt((size * size) + (size/2)))

t.lt(120)
t.fd(math.sqrt((size * size) + (size/2)))

t.rt(150)
t.fd(size)

t.rt(90)
t.fd(size)

t.rt(90)
t.fd(size)

for n in range(5, numOfPolygons + 4):
    
    currentAngle = ((n-2)*180)/n    # Derived from the equation to represent the interior angle of any polygon with sides n
    lastAngle = ((n-3)*180)/(n-1)   # Similar to CurrentAngle but gets the interior angle of the last polygon allowing us to compute turn angles 
    switch = currentAngle-lastAngle
    turnDeg = 180 - currentAngle
    if math.fmod(n, 2) != 0:
        t.lt(180-switch)
        t.fd(size)
        for i in range(n-2):
            t.lt(turnDeg)
            t.fd(size)
    else:
        t.rt(180-switch)
        t.fd(size)
        for i in range(n-2):
            t.rt(turnDeg)
            t.fd(size)


turtle.Screen().exitonclick()
