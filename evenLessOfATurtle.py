import turtle
import random
turtle.colormode(255)
colours=["red","blue","green"]

def totallyRandomColour():
    totallyRandomColour = (random.randrange(0, 255),  random.randrange(0, 255),  random.randrange(0, 255))
    print("Totally random colour, Red: %d, Green: %d, Blue: %d" % totallyRandomColour)
    return totallyRandomColour

class betterTurtle(turtle.Turtle):
    def __init__(self,  turtleName):
        super().__init__()
        # So we've just let the Turtle class init as per normal, now let's tell it that _all_ betterTurtles 
        # are turtle shaped by default and have a speed of 200 (we can still change those later in the 
        # instantiated object!)
        self.shape("turtle")
        self.name = turtleName
        
    def walkARhombus(self,  sideLength = 100,  initialAngle = 60):
        # The turtle will walk a rhombus and return to its
        # previous position.  Won't draw anything unless the pen is down!
        # Check that initial turn angle is less that 180 degrees, or we can't do this!
        if initialAngle<=180:
           for i in range(2):
               self.forward(sideLength)
               self.right(initialAngle)
               self.forward(sideLength)
               self.right(180 - initialAngle)
        else:
            print("ERROR: no way I can turn 4 times if the first one is 180 degrees or more!")

    def spirograph(self,  turnValue = 2,  repetitions = 180,  offset = 0):
        print("My name is %s and I am drawing a spirograph with turnValue: %d, repetitions: %d, offset: %d" % ( self.name,  turnValue,  repetitions,  offset))
        # Make a pattern based on the rhombus above
        for counter in range(repetitions):
            self.walkARhombus()
            self.right(turnValue)
            self.forward(offset)
            #self.color(random.choice(colours))
            self.color(totallyRandomColour())


bob = betterTurtle("Bob")
bob.speed(10)

# Get bob to draw a rhombus
bob.walkARhombus()

# Get bob to draw a bigger, narrower rhombus
bob.walkARhombus(200, 30)
bob.walkARhombus(random.random()*400,  random.random()*179)

bob.spirograph()

# Maybe with some random shapes and sizes... ?
bob.spirograph(random.randrange(1, 10),  random.randrange(1,  500), random.randrange(50))
