import turtle
t = turtle.Turtle()
turtle.bgcolor("pink")

t.color("blue")
t.speed(15)
t.pensize(5)
for i in range(12):
    t.circle(90)
    t.right(30)
    
t.penup()
t.forward(250)
t.pendown()
t.color("black")
t.pensize(4)
length = 50
for j in range(30):
    t.forward(length)
    t.right(60)
    length = length + 3
    
t.pencolor("orange")
t.left(120)
for k in range(10):
    t.forward(length)
    t.right(120)
    length = length + 9

t.color("red")
t.left(180)
length = 30
for l in range(30):
    t.forward(length)
    t.right(90)
    length = length + 5
t.color("green")
t.left(-150)
t.penup()
t.forward(150)
t.pendown()
radius = 3
angle = 30
steps = 40
for m in range(steps):
    t.circle(radius,extent=angle)
    radius += 3
t.hideturtle()  
turtle.mainloop()