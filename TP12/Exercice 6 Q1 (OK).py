import turtle

#---ORDRE 0-----
def MotifOrdre0(turtle,l) :
    return turtle.forward(l/3)

#---ORDRE 1-----
def drawCurveTurtle(turtle,l) :
    l = l/3
    MotifOrdre0(turtle,l)
    turtle.left(60)
    MotifOrdre0(turtle,l)
    turtle.right(120)
    MotifOrdre0(turtle,l)
    turtle.left(60)
    MotifOrdre0(turtle,l)

l = 100
turtle.setup(800,400)
drawCurveTurtle(turtle,l)
turtle.exitonclick()
