import turtle
Lift = False
t = turtle.Turtle()
turtle.listen()

position = t.pos
def lift_pen():
    t.up()
    Lift = True
    
def lower_pen():

  t.down()

def turn_blue():
    t.color('blue')
def turn_yellow():
    t.color('yellow')
def turn_green():
    t.color('green')
def turn_red():
    t.color('red')


def draw_a_circle():
    
    t. teleport(10)
    t.circle(20)

def move_up():
    t.seth(90)
    t.forward(10)
    
def move_down():
    t.seth(270)
    t.forward(10)
    
def move_left():   
    t.seth(180)
    t.forward(10)
    
def move_right():
    t.seth(0)
    t.forward(10)
    


turtle.onkeypress(move_up,'w')
turtle.onkeypress(move_left, 'a')
turtle.onkeypress(move_down, 's')
turtle.onkeypress(move_right,'d')
turtle.onkeypress(lift_pen, 'space')
turtle.onkeypress(lower_pen, 'l')
turtle.onkeypress(turn_blue,'1')
turtle.onkeypress(turn_red, '2')
turtle.onkeypress(turn_green, '3')
turtle.onkeypress(turn_yellow,'4')
turtle.onkeypress(draw_a_circle, 'm')

quit = input("press any key to quit")