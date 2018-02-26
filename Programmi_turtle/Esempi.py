""" Una serie di esempi """
import turtle

# Preparazione  
screen = turtle.Screen()
screen.title('Square Demo')
screen.setup (1500, 1500, 0, 0)

silly = turtle.Turtle()
silly.color("green")
silly.pensize(10)

silly.up()
silly.setposition(-100, -100)
silly.down()

silly.forward(250)
silly.right(90)

silly.forward(250)
silly.right(90)

silly.forward(250)
silly.right(90)

silly.forward(250)
silly.right(90)

myTurtle = turtle.Turtle()

# Cambio il colore
myTurtle.color("red")

myTurtle.up()
myTurtle.setposition(-100, -10)
myTurtle.down()
myTurtle.circle(150)

myTurtle.up()
myTurtle.setposition(-100, -5)
myTurtle.down()

# Disegno un goniometro
for angle in range(0, 360, 15):
    turtle.setheading(angle)
    turtle.forward(100)
    turtle.write(str(angle) + 'Gradi')
    turtle.backward(100)

myTurtle.up()
myTurtle.setposition(-10, -5)
myTurtle.down()

myTurtle.write('Ciao', font=("Arial", 16, "normal"))

myTurtle.up()
myTurtle.setposition(-200, -200)
myTurtle.down()

myTurtle.write('Ciao anche a te!')
    
# Finito!
turtle.done()
