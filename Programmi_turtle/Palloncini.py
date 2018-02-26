""" Disegniamo un palloncino """

import turtle

silly = turtle.Turtle()

# Ruota di 90 gradi in senso orario
silly.right(270)             
# Vai avanti
silly.forward(250)
# Disegna un cerchio
silly.circle(50)

i = 1
while i < 10:
    silly.up()
    silly.setposition(-10 * i, -10 * i)
    silly.down()

    silly.forward(250)
    silly.circle(50)
    i = i + 1

turtle.done()
