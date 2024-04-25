from turtle import *
screensize(1000,1000)
n = 20
tracer(1000)
left(90)
up()
for x in range(-10,10):
    for y in range(-10,10):
        goto(x*n,y*n)
        dot(2,'green')
home()
left(90)
tracer(5)
down()
for i in range(4):
    for j in range(3):
        forward(2*n)
        right(270)
    forward(5*n)
up()
done()

