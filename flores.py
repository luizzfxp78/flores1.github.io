from turtle import *
from colorsys import *
import turtle, math

bgcolor('black')
pu ()
setpos(190, -60)
pd()
width(5)
speed(15)
tracer(2)
h = 0

R = 1
G = 1
B = 0

for i in range(150):
    begin_fill()
    color((R, G, B))
    circle(150-i, 50)
    lt(80)
    circle(150-i, 50)
    rt(150)
    R -= 0.0065
    G -= 0.0065
    end_fill()

turtle.shape('turtle')
turtle.pencolor('orangered')
turtle.fillcolor('orange')
phi = 137.508 * (math.pi / 180.0)
for i in range(300):
    r = 4 * math.sqrt(i)
    theta = i * phi
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(i * 137.508)
    turtle.pendown()
    turtle.stamp()
done()