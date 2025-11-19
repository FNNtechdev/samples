import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("lightblue")

# Create the turtle
t = turtle.Turtle()
t.speed(0)
t.left(90)       # Point upwards
t.color("brown")

def draw_branch(length):
    if length < 10:   # Stop when the branches get too small
        return
    
    # Draw branch
    t.forward(length)
    
    # Right branch
    t.right(30)
    t.color("green")
    draw_branch(length - 15)
    t.color("brown")
    
    # Left branch
    t.left(60)
    t.color("green")
    draw_branch(length - 15)
    t.color("brown")
    
    # Go back to the starting point of this branch
    t.right(30)
    t.backward(length)

# Start drawing
t.penup()
t.goto(0, -200)
t.pendown()

draw_branch(80)

turtle.done()
