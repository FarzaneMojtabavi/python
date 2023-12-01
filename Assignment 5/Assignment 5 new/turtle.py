import turtle
t = turtle.Turtle()
t.shape('turtle')
t.shapesize(0.9)
t.lt(-150)
t.pencolor('red')
t.pensize(1)
r=32
for n in range(3, 10):
    for j in range(n):
        t.pendown()
        t.fd(r + n)
        t.rt(360 / n)
    t.penup()
    t.fd(r+10)
    t.rt(360 / n)
t.mainloop()
