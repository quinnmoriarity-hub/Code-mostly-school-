import turtle
t = turtle.Turtle()
import random

Start_x_y = [random.randint(-100,100), random.randint(-100, 100)] # Generates a random integer
t.teleport(Start_x_y[0],Start_x_y[1])# teleports to the random integer
Center =[Start_x_y[0]  + 100 /2,Start_x_y[1] +  100 /2]# is the middle of the square
for i in range(4): #creates the square
    t.forward(100)
    t.left(90)
t.teleport(Center[0],Center[1]) # teleports to the middle
for i in range(500):
    t.left(5)
    t.forward(i/75)

    if t.pos()[0] >= (Start_x_y[0]) and t.pos()[0] <=  (Start_x_y[0] +100) and t.pos()[1] >= (Start_x_y[1]) and t.pos()[1] <=  (Start_x_y[1] +100):
        t.down()
        print("this is working man")
    else:
        print("Idk brug")
        t.up()

 




quit = input("press any key to quit")





