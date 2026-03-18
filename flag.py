import turtle

# Setup screen
screen = turtle.Screen()
screen.title("Kenyan Flag")

t = turtle.Turtle()
t.speed(0)

def draw_rectangle(color, width, height):
    t.begin_fill()
    t.fillcolor(color)
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()

# Move to starting position
t.penup()
t.goto(-200, 120)
t.pendown()

# Black stripe
draw_rectangle("black", 400, 80)

# White stripe
t.penup()
t.goto(-200, 40)
t.pendown()
draw_rectangle("white", 400, 20)

# Red stripe
t.penup()
t.goto(-200, 20)
t.pendown()
draw_rectangle("red", 400, 80)

# White stripe
t.penup()
t.goto(-200, -60)
t.pendown()
draw_rectangle("white", 400, 20)

# Green stripe
t.penup()
t.goto(-200, -80)
t.pendown()
draw_rectangle("green", 400, 80)

# Draw a simple oval (shield placeholder)
t.penup()
t.goto(0, 0)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(40)
t.end_fill()

t.hideturtle()
turtle.done()
