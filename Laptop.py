import turtle

# Create screen
screen = turtle.Screen()
screen.bgcolor("white")

pen = turtle.Turtle()
pen.speed(3)
pen.color("black")
pen.pensize(2)

# Function to draw a rectangle
def draw_rectangle(width, height):
    for _ in range(2):
        pen.forward(width)
        pen.left(90)
        pen.forward(height)
        pen.left(90)

# Draw laptop screen
pen.penup()
pen.goto(-120, 50)
pen.pendown()
draw_rectangle(240, 150)

# Draw inner screen border
pen.penup()
pen.goto(-110, 60)
pen.pendown()
draw_rectangle(220, 130)

# Draw laptop base (keyboard area)
pen.penup()
pen.goto(-150, 50)
pen.pendown()
draw_rectangle(300, -50)

# Draw touchpad
pen.penup()
pen.goto(-40, 10)
pen.pendown()
draw_rectangle(80, -25)

# Hide turtle
pen.hideturtle()

# Keep window open
screen.mainloop()
