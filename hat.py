import turtle

# Setup screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create turtle
pen = turtle.Turtle()
pen.speed(3)
pen.pensize(3)

# Draw brim of the hat
pen.penup()
pen.goto(-150, -50)
pen.pendown()
pen.forward(300)

# Draw top rectangle (hat body)
pen.penup()
pen.goto(-80, -50)
pen.pendown()

pen.left(90)
pen.forward(120)
pen.right(90)
pen.forward(160)
pen.right(90)
pen.forward(120)
pen.right(90)
pen.forward(160)

# Hide turtle and finish
pen.hideturtle()
turtle.done()
