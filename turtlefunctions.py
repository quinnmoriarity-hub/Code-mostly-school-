import turtle


def star(t,points):
    print star
    for i in range(points):
        t.left(360/points)
        t.forward(70)
        t.right(360/points*2)
        t.forward(70)



def portal_to_hell(t,points,length,sharpness):
    if points == sharpness:
        sharpness += 7
    for i in range(points):
        t.forward(length)
        t.left(360/points*sharpness)

   
def drawcurve(t,size):
     l = random.randrange(6,8)
     for i in range(l):   
         t.left(20)
         t.forward(i*size)



 



