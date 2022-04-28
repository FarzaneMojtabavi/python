import turtle
t = turtle.Turtle()
t.shape('turtle')
t.shapesize(0.7)
t.lt(150)
for n in range(3, 10):
    for j in range(n):
        t.fd(60+n)
        t.rt(360/n)
t.mainloop()