import random
import turtle

bob = turtle.Turtle()
bob.shape("turtle")
bob.speed(200)
colours=["red","blue","green",]

def rhombus(aTurtle):
    for i in range(2):
        aTurtle.forward(100)
        aTurtle.right(60)
        aTurtle.forward(100)
        aTurtle.right(120)

for i in range(360):
    rhombus(bob)
    bob.right(1)
    bob.color(random.choice(colours))
