import turtle
a=turtle.Turtle()
a.speed(15)
##for i in range(6):
##    a.color('blue')
##    for i in range(36):
##        a.forward(300)
##        a.left(170)
##    a.right(270)
##    a.penup()
##    a.forward(200)
##    a.pendown()
##    a.color('red')
##    for i in range(36):
##        a.forward(150)
##        a.left(170)
##    a.right(225)
##    a.penup()
##    a.forward(300)
##    a.pendown()

#########SOME DESIGN
for i in range(12):
    a.forward(200)
    a.color('blue')
    for i in range(36):
        a.forward(100)
        a.left(170)
    a.left(180)
    a.forward(200)
    a.left(180)
    a.left(30)

#a.forward(300)
#for i in range(4):
##a.left(60)
##a.forward(300)
##a.right(120)
##a.forward(300)
##a.right(150)
##a.forward(300)
##a.right(150)
##a.forward(225)
##a.right(150)
##a.forward(300)

turtle.done()
