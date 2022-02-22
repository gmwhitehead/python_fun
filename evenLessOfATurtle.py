import turtle
import random
from math import sin
from math import cos
from math import radians
# The below command makes the turtle module accept a sequence of ints (rather than floats)
# as RGB colour selection.
turtle.colormode(255)
colours=["red","blue","green"]

class betterTurtle(turtle.Turtle):
    def __init__(self,  turtleName):
        super().__init__()
        # So we've just let the Turtle class init as per normal, now let's tell it that _all_ betterTurtles 
        # are turtle shaped by default and know what their own name is!
        self.shape("turtle")
        self.name = turtleName
        
    def walkARhombus(self,  sideLength = 100,  initialAngle = 60):
        # The turtle will walk a rhombus and return to its
        # previous position.  Won't draw anything unless the pen is down!
        # Check that initial turn angle is less that 180 degrees, or this doesn't
        # make any sense!
        if initialAngle<=180:
           for i in range(2):
               self.forward(sideLength)
               self.right(initialAngle)
               self.forward(sideLength)
               self.right(180 - initialAngle)
        else:
            print("ERROR: no way I can turn 4 times if the first one is 180 degrees or more!")

    def spirograph(self,  turnValue = 2,  repetitions = 180,  offset = 0):
        print("I'm a turtle called %s and I am drawing a spirograph with turnValue: %d, repetitions: %d, offset: %d" % ( self.name,  turnValue,  repetitions,  offset))
        # Make a pattern based on the rhombus above
        for counter in range(repetitions):
            self.walkARhombus()
            self.right(turnValue)
            self.forward(offset)
            #self.color(random.choice(colours))
            self.color(self.totallyRandomColour())
            
    def walkRegularPolygon(self,  turns = 6,  sideLength = 100):
        for i in range(turns):
            self.forward(sideLength)
            self.right(360/turns)
            
    def totallyRandomColour(self):
        totallyRandomColour = (random.randrange(0, 255),  random.randrange(0, 255),  random.randrange(0, 255))
        #print("Totally random colour, Red: %d, Green: %d, Blue: %d" % totallyRandomColour)
        return totallyRandomColour
        
    def randomPenColour(self):
        self.color(self.totallyRandomColour())
        
        
    def plotSomethingCool(self,  degrees=360,  bigCogSize=250,  littleCogSize=55,  diameter = 125,  accuracy=3):
        ## Every statement in here featuring 'wn' is to speed up the drawing a bit.
        ## It will still work if you remove _all_ of them, but be a lot slower.
        self.pensize(1.5)
        wn = turtle.Screen()
        wn.tracer(0)
        self.penup()
        self.home()
        for i in range(0,  degrees,  accuracy):
            # If we've not moved yet, leave the pen up.
            if i == 0:
                self.penup()
            else:
                self.pendown()
            # Assume we've just plotted the previous point, 'cos it doesn't matter too much if we have.
            angle=radians(i)
            R = bigCogSize
            r = littleCogSize
            d = diameter
            x = (R - r) * cos(angle) + d * cos(((R-r)/r)*angle)
            y = (R - r) * sin(angle) - d * sin(((R-r)/r)*angle)
            self.color(self.totallyRandomColour())
            self.goto(x, y)
            wn.update()
            



bob = betterTurtle("Bob")

# Get bob to draw a rhombus
#bob.walkARhombus()

# Get bob to draw a bigger, narrower rhombus
#bob.walkARhombus(200, 30)

# And one with random size/angles
#bob.walkARhombus(random.random()*400,  random.random()*179)

#bob.spirograph()

# Maybe with some random shapes and sizes... ?
#bob.spirograph(random.randrange(1, 10),  random.randrange(1,  500), random.randrange(10))

# Tell bob to draw an arbitrary regular polygon (default inputs)
#bob.walkRegularPolygon()

# Tell bob to draw an abitrary regular polygon (with values we give him!)
#bob.walkRegularPolygon(7, 60)

bob.speed(500)

#bob.plotSomethingCool(3600)

# show off 20 different random ones
bob.hideturtle()
for i in range(20): 
    bob.clear()
    bigCogSize=random.randrange(40, 300)
    smallCogSize=random.randrange(40, 200)
    bob.plotSomethingCool(36000,  bigCogSize,  smallCogSize,  250 , 3)
