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


def MotifOrdre2(turtle,l,n) :
    l = l/(3*n)
    counter = 0
    while counter <= 4 :
        drawCurveTurtle(turtle,l)
        turtle.left(60)
        drawCurveTurtle(turtle,l)
        turtle.right(120)
        drawCurveTurtle(turtle,l)
        turtle.left(60)
        drawCurveTurtle(turtle,l)
        turtle.right(120)
        counter +=1



n = 4
l = 100
turtle.setup(800,400)
MotifOrdre2(turtle,l,n)
turtle.exitonclick()
