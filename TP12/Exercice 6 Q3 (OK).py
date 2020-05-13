import turtle

#---ORDRE 0-----
def MotifOrdre0(turtle,l) :
    return turtle.forward(l/3)

#---ORDRE 1-----
def drawCurveTurtle(turtle,l) :
    l = l/3*n
    MotifOrdre0(turtle,l)
    turtle.left(60)
    MotifOrdre0(turtle,l)
    turtle.right(120)
    MotifOrdre0(turtle,l)
    turtle.left(60)
    MotifOrdre0(turtle,l)


def MotifOrdreN(turtle,l,n) :
    l = l/(3*n)
    if n >= 0 :
        drawCurveTurtle(turtle,l)
        turtle.left(60)
        drawCurveTurtle(turtle,l)
        turtle.right(120)
        drawCurveTurtle(turtle,l)
        turtle.left(60)
        drawCurveTurtle(turtle,l)
        turtle.right(120)
        if n>=0 :
            MotifOrdreN(turtle,l/(3*n),n-1)
    n = n - 1

def drawFullCurve(turtle,l,n) :
    while n >= 0 :
        MotifOrdreN(turtle,l/3**(n-1),n)

n = 6
l = 72
turtle.setup(800,400)
MotifOrdreN(turtle,l,n)
turtle.exitonclick()
