import turtle

# Setup
t = turtle.Turtle()
t.speed(3)

# Draw square for the house body
for _ in range(4):
    t.forward(150)
    t.left(90)

# Draw roof
t.left(45)
t.forward(106)
t.right(90)
t.forward(106)
t.right(135)
t.forward(150)

# Move to door position
t.penup()
t.goto(50, 0)
t.pendown()

# Draw door
t.left(90)
t.forward(80)
t.right(90)
t.forward(50)
t.right(90)
t.forward(80)

# Move to window position
t.penup()
t.goto(20, 90)
t.pendown()

# Draw window
for _ in range(4):
    t.forward(30)
    t.right(90)

turtle.done()
