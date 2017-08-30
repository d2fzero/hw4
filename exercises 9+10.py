import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.left(36)
for j in range (5):
    for i in range (5):
        tess.forward(100)
        tess.left(144)
    tess.penup()
    tess.forward(350)
    tess.right(144)
    tess.pendown()
wn.mainloop()

