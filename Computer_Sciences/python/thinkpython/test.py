import math
import turtle
t= turtle.Turtle()
t.hideturtle()

   

# turtle point vers droite initialement 
def slash(t):
    t.lt(70)
    t.fd(100)
    t.lt(180)
    t.fd(100)
    t.lt(110)

def back_slash(t):
    t.lt(110)
    t.fd(100)
    t.lt(180)
    t.fd(100)
    t.lt(70)

def up_hline(t):
   t.lt(90) 
   t.pu()
   t.fd(100)
   t.pd()
   t.rt(90)
   t.fd(100)
   t.lt(180)
   t.fd(100)
   t.lt(90)
   t.pu()
   t.fd(100)
   t.pd()
   t.lt(90)

def down_hline(t):
   t.fd(100)
   t.lt(180)
   t.fd(100)
   t.lt(180)

def mid_hline(t):
   t.lt(90) 
   t.pu()
   t.fd(50)
   t.pd()
   t.rt(90)
   t.fd(100)
   t.bk(100)
   t.lt(90)
   t.pu()
   t.fd(50)
   t.pd()
   t.lt(90)

def hline(t):
   t.lt(90)
   t.fd(100)
   t.bk(100)
   t.rt(90)
def A(t):
   slash(t)
   t.pu()
   t.fd(72)
   t.pd()
   back_slash(t)
   t.pu()
   t.bk(72)
   t.pd()
   mid_hline(t)

def E(t):

A(t)

turtle.done()