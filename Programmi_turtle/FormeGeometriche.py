""" Disegno delle forme geometriche """
import turtle

silly = turtle.Turtle()

silly.up()
silly.setposition(-100, -100)
silly.down()

silly.forward(250)
silly.right(90)     # Rotate clockwise by 90 degrees

silly.forward(250)
silly.right(90)

silly.forward(250)
silly.right(90)

silly.forward(250)
silly.right(90)
 
myTurtle = turtle.Turtle()

myTurtle.up()
myTurtle.setposition(-100, -10)
myTurtle.down()

myTurtle.circle(150)

turtle.done()
