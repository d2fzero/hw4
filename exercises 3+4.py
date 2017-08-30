#ex 3
import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("green")

def draw_poly(t, n, sz) :
    for i in range (n):
        t.forward(sz)
        t.left(360/n)
draw_poly(tess,8,50)
tess.penup()
tess.forward(300)
tess.pendown()
#ex 4
for i in range (20):
    draw_poly(tess,4,50)
    tess.left(20)
