import turtle

# Create screen
screen = turtle.Screen()
screen.bgcolor("lightblue")

# Create turtle
pen = turtle.Turtle()
pen.speed(3)
pen.pensize(3)

# ---- Draw the square base ----
pen.color("black", "lightyellow")
pen.begin_fill()
for _ in range(4):
    pen.forward(200)
    pen.left(90)
pen.end_fill()

# ---- Draw the roof ----
pen.color("black", "brown")
pen.begin_fill()
pen.left(45)
pen.forward(140)
pen.right(90)
pen.forward(140)
pen.end_fill()

# Reset orientation
pen.left(45)

# ---- Draw the door ----
pen.penup()
pen.goto(70, 0)
pen.pendown()
pen.color("black", "darkred")
pen.begin_fill()
pen.left(90)
pen.forward(100)
pen.right(90)
pen.forward(60)
pen.right(90)
pen.forward(100)
pen.end_fill()

# ---- Draw windows ----
def draw_window(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color("black", "white")
    pen.begin_fill()
    for _ in range(4):
        pen.forward(40)
        pen.left(90)
    pen.end_fill()
    # window cross
    pen.forward(20)
    pen.left(90)
    pen.forward(40)
    pen.backward(20)
    pen.left(90)
    pen.forward(20)
    pen.backward(40)

# Left window
draw_window(20, 120)

# Right window
draw_window(140, 120)

pen.hideturtle()
turtle.done()
