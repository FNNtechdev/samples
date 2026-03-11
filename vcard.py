import turtle

# Screen setup
screen = turtle.Screen()
screen.bgcolor("lightyellow")
screen.title("Birthday Card")

# Turtle setup
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(3)
pen.color("purple")

# Write Happy Birthday text
pen.penup()
pen.goto(0, 100)
pen.write("🎉 Happy Birthday 🎉", align="center", font=("Arial", 28, "bold"))

pen.goto(0, 50)
pen.write("Wishing you a day filled with joy!", align="center", font=("Arial", 16, "normal"))

# Draw a simple cake
pen.goto(-50, -50)
pen.pendown()
pen.color("pink")
pen.begin_fill()

for i in range(2):
    pen.forward(100)
    pen.right(90)
    pen.forward(50)
    pen.right(90)

pen.end_fill()

# Draw candle
pen.penup()
pen.goto(0, 0)
pen.pendown()
pen.color("blue")
pen.left(90)
pen.forward(40)

# Draw flame
pen.color("orange")
pen.begin_fill()
pen.circle(5)
pen.end_fill()

# Balloons
colors = ["red", "blue", "green", "purple"]
x = -150

for c in colors:
    pen.penup()
    pen.goto(x, 50)
    pen.color(c)
    pen.begin_fill()
    pen.circle(20)
    pen.end_fill()
    
    pen.goto(x, 50)
    pen.pendown()
    pen.right(90)
    pen.forward(60)
    pen.left(90)
    
    x += 70

turtle.done()
