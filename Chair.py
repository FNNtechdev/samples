import turtle

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Chair Drawing")

# Create turtle
pen = turtle.Turtle()
pen.speed(3)
pen.pensize(3)

# Function to draw a rectangle
def draw_rectangle(width, height, color="brown"):
    pen.fillcolor(color)
    pen.begin_fill()
    for _ in range(2):
        pen.forward(width)
        pen.left(90)
        pen.forward(height)
        pen.left(90)
    pen.end_fill()

# Draw seat of the chair
pen.penup()
pen.goto(-50, -50)
pen.pendown()
draw_rectangle(100, 20)  # width=100, height=20

# Draw backrest
pen.penup()
pen.goto(-50, -30)
pen.pendown()
draw_rectangle(100, 80)  # width=100, height=80

# Draw left leg
pen.penup()
pen.goto(-50, -50)
pen.pendown()
draw_rectangle(10, -50)  # width=10, height=50

# Draw right leg
pen.penup()
pen.goto(40, -50)
pen.pendown()
draw_rectangle(10, -50)  # width=10, height=50

# Draw back left leg
pen.penup()
pen.goto(-50, 30)
pen.pendown()
draw_rectangle(10, -30)  # width=10, height=30

# Draw back right leg
pen.penup()
pen.goto(40, 30)
pen.pendown()
draw_rectangle(10, -30)  # width=10, height=30

# Hide turtle and finish
pen.hideturtle()
turtle.done()
