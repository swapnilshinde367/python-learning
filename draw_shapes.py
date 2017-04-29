# pylint: skip-file
# draw different shapes using turtle
import turtle

def handleDrawShape() :

    objWindow = turtle.Screen()
    objWindow.bgcolor('black')

    objTurtle = turtle.Turtle()
    objTurtle.color( 'white' )
    objTurtle.speed(100)
    objTurtle.shape('turtle')

    for intCount in range ( 0,36 ) :
        for intCount in range ( 0,4 ) :
            objTurtle.forward(100)
            objTurtle.right(90)
        objTurtle.right(10)

    objWindow.exitonclick()
# end of handleDrawShape

handleDrawShape()


def handleDrawInitials() :

    objWindow = turtle.Screen()
    objWindow.bgcolor('black')

    objTurtle = turtle.Turtle()
    objTurtle.color( 'white' )
    # objTurtle.speed(2)
    objTurtle.shape('turtle')

    for intCount in range(0,2):
        objTurtle.forward(100)
        objTurtle.left(90)
    # objTurtle.forward(100)
    # objTurtle.left(90)
    for intCount in range(0,2):
        objTurtle.forward(100)
        objTurtle.right(90)
    # objTurtle.forward(100)
    # objTurtle.right(90)
    objTurtle.forward(100)
    
       

    objWindow.exitonclick()
# end of handleDrawInitials

handleDrawInitials()


def handleDrawFlower() :

    objWindow = turtle.Screen()
    objWindow.bgcolor('black')

    objTurtle = turtle.Turtle()
    objTurtle.color( 'white' )
    objTurtle.speed(200)
    objTurtle.shape('turtle')

    for intCount in range ( 0,72 ) :
        for intCount in range ( 0,2 ) :
            objTurtle.forward(100)
            objTurtle.right(40)
            objTurtle.forward(100)
            objTurtle.right(140)
        objTurtle.right(5)
    
    objTurtle.right(90)
    objTurtle.forward(250)

    objWindow.exitonclick()
# end of handleDrawShape

handleDrawFlower()


def handleDrawFlower1() :

    objWindow = turtle.Screen()
    objWindow.bgcolor('black')

    objTurtle = turtle.Turtle()
    objTurtle.color( 'white' )
    objTurtle.speed(200)
    # objTurtle.shape('turtle')

    for intCount in range ( 0,36 ) :
        for intCount in range ( 0,2 ) :
            objTurtle.forward(50)
            objTurtle.right(10)
            objTurtle.forward(50)
            objTurtle.right(10)
        objTurtle.right(90)
    
    objWindow.exitonclick()
# end of handleDrawShape

handleDrawFlower1()

def handleDrawSmallTriangles(objTurtle):
    
    for intCount in range(0,2):
        objTurtle.left(120)
        objTurtle.forward(25)
    
    for intCount in range(0,2):
        objTurtle.right(120)
        objTurtle.forward(25)

    objTurtle.left(120)
    objTurtle.forward(25)

def handleDrawTriangles() :

    objWindow = turtle.Screen()
    objWindow.bgcolor('black')

    objTurtle = turtle.Turtle()
    objTurtle.color( 'white' )
    # objTurtle.speed(25)
    # objTurtle.shape('turtle')

    # for intCount in range ( 0,36 ) :
    #     for intCount in range ( 0,2 ) :
    for intCount in range(0,2):
        objTurtle.forward(100)
        objTurtle.right(120)
    # objTurtle.forward(100)
    # objTurtle.right(120)
    objTurtle.forward(100)
    #
    handleDrawSmallTriangles(objTurtle)
    objTurtle.left(120)
    objTurtle.forward(50)
    
    for intCount in range(0,2):
        objTurtle.right(120)
        objTurtle.forward(50)
    # objTurtle.right(120)
    # objTurtle.forward(50)
    ##
    handleDrawSmallTriangles(objTurtle)
    objTurtle.left(120)
    objTurtle.forward(75)
    objTurtle.left(120)
    objTurtle.forward(25)
    objTurtle.right(120)
    objTurtle.forward(25)
    objTurtle.right(120)
    objTurtle.forward(25)
    objTurtle.left(120)
    objTurtle.forward(25)

    #Second set
    objTurtle.right(300)
    objTurtle.forward(100)
    objTurtle.right(180)
    objTurtle.forward(100)

    ###
    handleDrawSmallTriangles(objTurtle)
    objTurtle.left(120)
    objTurtle.forward(50)
    objTurtle.right(120)
    objTurtle.forward(50)
    objTurtle.right(120)
    objTurtle.forward(50)
    ##
    handleDrawSmallTriangles(objTurtle)
    objTurtle.left(120)
    objTurtle.forward(75)
    objTurtle.left(120)
    objTurtle.forward(25)
    objTurtle.right(120)
    objTurtle.forward(25)
    objTurtle.right(120)
    objTurtle.forward(25)
    objTurtle.left(120)
    # objTurtle.left(120)

    #Third set
    # objTurtle.right(300)
    objTurtle.forward(125)
    ####
    handleDrawSmallTriangles(objTurtle)
    objTurtle.left(120)
    objTurtle.forward(50)
    objTurtle.right(120)
    objTurtle.forward(50)
    objTurtle.right(120)
    objTurtle.forward(50)
    ##
    handleDrawSmallTriangles(objTurtle)
    objTurtle.left(120)
    objTurtle.forward(75)
    objTurtle.left(120)
    objTurtle.forward(25)
    objTurtle.right(120)
    objTurtle.forward(25)
    objTurtle.right(120)
    objTurtle.forward(25)
    objTurtle.left(120)

    objWindow.exitonclick()
# end of handleDrawShape

handleDrawTriangles()