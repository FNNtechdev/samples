import turtle

screen = turtle.Screen()
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(3)
t.pensize(3)
t.color("royal blue", "royal blue")   # Outline + Fill

# Draw bottle shape
t.penup()
t.goto(-50, -150)
t.pendown()

t.begin_fill()

# Left curve
t.left(90)
t.forward(200)
t.circle(40, 90)

# Neck
t.forward(80)
t.circle(20, 180)
t.forward(80)

# Right curve
t.circle(40, 90)
t.forward(200)

# Bottom
t.right(90)
t.forward(100)

t.end_fill()

# Draw bottle cap
t.penup()
t.goto(-30, 130)
t.pendown()
t.color("royal blue")
t.begin_fill()
t.forward(60)
t.left(90)
t.forward(20)
t.left(90)
t.forward(60)
t.left(90)
t.forward(20)
t.end_fill()

# Label rectangle
t.penup()
t.goto(-40, -20)
t.pendown()
t.color("white")
t.begin_fill()
for _ in range(2):
    t.forward(80)
    t.left(90)
    t.forward(40)
    t.left(90)
t.end_fill()

# Label text
t.penup()
t.goto(0, -10)
t.color("black")
t.write("FNNtec.dev", align="center", font=("Arial", 14, "bold"))

t.hideturtle()
turtle.done()
