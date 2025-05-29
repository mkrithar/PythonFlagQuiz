import random
import turtle
from sys import flags

bob = turtle.Turtle()


def estonia():
    bob.fillcolor("blue")
    bob.begin_fill()
    for i in range(2):
        bob.fd(150)
        bob.rt(90)
        bob.fd(30)
        bob.rt(90)
    bob.end_fill()

    bob.pu()
    bob.goto(0,-30)
    bob.pd()

    bob.fillcolor("black")
    bob.begin_fill()
    for i in range(2):
      bob.fd(150)
      bob.rt(90)
      bob.fd(30)
      bob.rt(90)
    bob.end_fill()

    bob.pu()
    bob.goto(0,-60)
    bob.pd()

    bob.fillcolor("white")
    bob.begin_fill()
    for i in range(2):
        bob.fd(150)
        bob.rt(90)
        bob.fd(30)
        bob.rt(90)
    bob.end_fill()
    bob.hideturtle()





def germany():
    bob.fillcolor("black")
    bob.begin_fill()
    for i in range(2):
        bob.fd(150)
        bob.rt(90)
        bob.fd(30)
        bob.rt(90)
    bob.end_fill()

    bob.pu()
    bob.goto(0,-30)
    bob.pd()

    bob.fillcolor("red")
    bob.begin_fill()
    for i in range(2):
      bob.fd(150)
      bob.rt(90)
      bob.fd(30)
      bob.rt(90)
    bob.end_fill()

    bob.pu()
    bob.goto(0,-60)
    bob.pd()

    bob.fillcolor("yellow")
    bob.begin_fill()
    for i in range(2):
        bob.fd(150)
        bob.rt(90)
        bob.fd(30)
        bob.rt(90)
    bob.end_fill()
    bob.hideturtle()




def russia():
    bob.fillcolor("white")
    bob.begin_fill()
    for i in range(2):
        bob.fd(150)
        bob.rt(90)
        bob.fd(30)
        bob.rt(90)
    bob.end_fill()

    bob.pu()
    bob.goto(0,-30)
    bob.pd()

    bob.fillcolor("blue")
    bob.begin_fill()
    for i in range(2):
      bob.fd(150)
      bob.rt(90)
      bob.fd(30)
      bob.rt(90)
    bob.end_fill()

    bob.pu()
    bob.goto(0,-60)
    bob.pd()

    bob.fillcolor("red")
    bob.begin_fill()
    for i in range(2):
        bob.fd(150)
        bob.rt(90)
        bob.fd(30)
        bob.rt(90)
    bob.end_fill()
    bob.hideturtle()

def italy():
    bob.fillcolor("green")
    bob.begin_fill()
    for i in range(2):
        bob.fd(80)
        bob.rt(90)
        bob.fd(160)
        bob.rt(90)
    bob.end_fill()

    bob.pu()
    bob.goto(80,0)
    bob.pd()

    bob.fillcolor("white")
    bob.begin_fill()
    for i in range(2):
      bob.fd(80)
      bob.rt(90)
      bob.fd(160)
      bob.rt(90)
    bob.end_fill()

    bob.pu()
    bob.goto(160,0)
    bob.pd()

    bob.fillcolor("red")
    bob.begin_fill()
    for i in range(2):
        bob.fd(80)
        bob.rt(90)
        bob.fd(160)
        bob.rt(90)
    bob.end_fill()
    bob.hideturtle()



def poland ():
    bob.fillcolor("white")
    bob.begin_fill()
    for i in range(2):
        bob.fd(150)
        bob.rt(90)
        bob.fd(30)
        bob.rt(90)
    bob.end_fill()

    bob.pu()
    bob.goto(0,-30)
    bob.pd()

    bob.fillcolor("red")
    bob.begin_fill()
    for i in range(2):
      bob.fd(150)
      bob.rt(90)
      bob.fd(30)
      bob.rt(90)
    bob.end_fill()

poland()
flags = [estonia,germany,russia,italy,poland]
life=3
points=0
while life > 0 and len(flags) > 0:
    bob.reset()
    flagchoice=random.choice(flags)
    flagchoice()
    answer=input("Poia einai h simaia")
    if answer == flagchoice.__name__:
        print("Bravo")
        points =points+1
        print("Your points:", points)
        print("Your lives:", life)
    else:
        print("You lost a life")
        life = life - 1

    flags.remove(flagchoice)
turtle.done()