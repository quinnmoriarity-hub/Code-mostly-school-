import turtle 
import random
t = turtle.Turtle()

#challenge 1: spiral
# for i in range(400):
#     t.left(5)
#     t.forward(i/30)








def star(points):
    for i in range(points):
        t.left(360/points)
        t.forward(70)
        t.right(360/points*2)
        t.forward(70)
star(6)
t.forward(70)
star()

def portal_to_hell(points,length,sharpness):
    if points == sharpness:
        sharpness += 7
    for i in range(points):
        t.forward(length)
        t.left(360/points*sharpness)

portal_to_hell(69, 42, 67,)
   
def drawcurve(size):
     l = random.randrange(6,8)
     for i in range(l):   
         t.left(20)
         t.forward(i*size)

drawcurve(11)


 

quit = input("press any key to quit")

