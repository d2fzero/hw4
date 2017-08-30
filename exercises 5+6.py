#ex 5
import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.speed(90)
for i in range (100):
    tess.forward(10+i*2)
    tess.left(90)
tess.penup()
tess.forward(400)
tess.pendown()
for i in range (100):
    tess.forward(10+i*2)
    tess.left(91)
#ex 6
def draw_equitriangle(t, sz):
    for i in range (3):
        t.forward(sz)
        t.left(120)

