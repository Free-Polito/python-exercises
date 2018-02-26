""" Disegno dei quadrati """

import turtle

silly = turtle.Turtle()

i=1
while i < 10:

    silly.up()
    silly.setposition(-10*i, -10*i)
    silly.down()

    j=1
    while j < 5:
        silly.forward(250)
        silly.right(90) # Rotate clockwise by 90 degrees
        j=j+1
        
    i=i+1

turtle.done()
