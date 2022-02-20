import random
import turtle

bob = turtle.Turtle()
bob.shape("turtle")
bob.speed(200)
colours=["red","blue","green",]

def rhombus(aTurtle):
    for i in range(2):
        bob.forward(100)
        bob.right(60)
        bob.forward(100)
        bob.right(120)

for i in range(360):
    rhombus(bob)
    bob.right(1)
    bob.color(random.choice(colours))
