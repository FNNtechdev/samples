import turtle

pen = turtle.Turtle()
pen.speed(3)
pen.width(4)

# Function to move without drawing
def move(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()

# Draw F
move(-300, 0)
pen.left(90)
pen.forward(100)
pen.right(90)
pen.forward(50)
pen.backward(50)
pen.right(90)
pen.forward(50)
pen.left(90)
pen.forward(40)

# Draw A
move(-200, 0)
pen.left(75)
pen.forward(105)
pen.right(150)
pen.forward(105)
pen.backward(50)
pen.left(75)
pen.forward(45)

# Draw I
move(-80, 0)
pen.left(90)
pen.forward(100)

# Draw T
move(0, 100)
pen.right(90)
pen.forward(80)
pen.backward(40)
pen.right(90)
pen.forward(100)

# Draw H
move(120, 0)
pen.left(90)
pen.forward(100)
pen.backward(50)
pen.right(90)
pen.forward(50)
pen.left(90)
pen.forward(50)
pen.backward(100)

pen.hideturtle()
turtle.done()
