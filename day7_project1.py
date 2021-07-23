#Circle using radius function
from turtle import Turtle
t = Turtle()
t.circle(50)
t.clear()
#Circle without radius function
from turtle import Turtle 
t = Turtle()
for i in range(0,360):
  t.forward(1)
  t.left(1)