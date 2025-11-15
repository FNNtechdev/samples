import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Trophy Drawing")

# Create turtle
pen = turtle.Turtle()
pen.speed(8)
pen.pensize(3)

# Draw base
pen.color("black", "brown")
pen.begin_fill()
pen.penup()
pen.goto(-50, -150)
pen.pendown()
for i in range(2):
    pen.forward(100)
    pen.left(90)
    pen.forward(30)
    pen.left(90)
pen.end_fill()

# Draw stand
pen.color("black", "darkgoldenrod")
pen.begin_fill()
pen.penup()
pen.goto(-30, -120)
pen.pendown()
for i in range(2):
    pen.forward(60)
    pen.left(90)
    pen.forward(50)
    pen.left(90)
pen.end_fill()

# Draw cup
pen.color("black", "gold")
pen.begin_fill()
pen.penup()
pen.goto(-100, -70)
pen.pendown()
pen.setheading(60)
pen.circle(120, 60)
pen.setheading(0)
pen.forward(200)
pen.setheading(-60)
pen.circle(120, 60)
pen.goto(-100, -70)
pen.end_fill()

# Draw handles
pen.color("gold")
pen.penup()
pen.goto(-100, 0)
pen.pendown()
pen.setheading(120)
pen.circle(60, 120)

pen.penup()
pen.goto(100, 0)
pen.pendown()
pen.setheading(60)
pen.circle(-60, 120)

# Write text
pen.penup()
pen.goto(-40, -130)
pen.color("white")
pen.write("CHAMPION", font=("Arial", 12, "bold"))

# Hide turtle
pen.hideturtle()

# Keep window open
turtle.done()
