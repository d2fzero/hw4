#ex 1
from turtle import *
shape("turtle")
bgcolor("green")
color("pink")
for j in range (5):
    for i in range (4):
        forward(20)
        left(90)
    penup()
    forward(40)
    pendown()

penup()
forward(100)
pendown()
#ex 2
for i in range (5):
    for j in range (4):
        forward(20+40*i)
        left(90)
    penup()
    right(90)
    forward(20)
    right(90)
    forward(20)
    left(180)
    pendown()
mainloop()