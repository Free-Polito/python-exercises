from time import sleep
from turtle import * 

screen = Screen()
screen.addshape("ball.gif")

color("red", "red")
shape("ball.gif")
shapesize(1,1,1)

x = 0
y = -200
penup()

while y < 200:
    y = y+10
    goto(x,y)
    # Slow down the movement
    sleep(0.1)

