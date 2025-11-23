# bamboo.py
# Draw a bamboo tree using the turtle graphics module
# Run: python bamboo.py

import turtle
import random
import math

# --- Configuration ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
BACKGROUND_COLOR = "#eaf6ea"
BAMBOO_COLOR = "#2f7a2f"
NODE_COLOR = "#245c24"
LEAF_COLOR = "#2aa24a"
SEED = 42  # change for new random variations

random.seed(SEED)

# --- Helper drawing functions ---
def move_to(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_segment(t, length, thickness, curvature=0.0):
    """Draw a single bamboo segment as a slightly curved rectangle."""
    # Save state
    heading = t.heading()
    x0, y0 = t.position()

    # Draw center line with curvature
    steps = max(6, int(length / 5))
    dx = 0
    dy = 0
    points = []
    for i in range(steps + 1):
        frac = i / steps
        angle = math.radians(curvature * math.sin(frac * math.pi))
        dx = math.sin(angle) * 2  # small sideways shift
        dy = frac * length
        points.append((x0 + dx, y0 + dy))

    # Draw left edge
    t.fillcolor(BAMBOO_COLOR)
    t.begin_fill()
    t.penup()
    # move to first point left
    t.goto(points[0][0] - thickness/2, points[0][1])
    t.pendown()
    for (px, py) in points:
        t.goto(px - thickness/2, py)
    # draw right edge back down
    for (px, py) in reversed(points):
        t.goto(px + thickness/2, py)
    t.goto(points[0][0] - thickness/2, points[0][1])
    t.end_fill()

    # move turtle to top of segment
    t.penup()
    t.goto(points[-1])
    t.setheading(heading)
    t.pendown()

def draw_node(t, width):
    """Draw a ring/node on the bamboo."""
    t.fillcolor(NODE_COLOR)
    t.begin_fill()
    # draw small ellipse-like ring
    heading = t.heading()
    x, y = t.position()
    t.penup()
    t.goto(x - width * 0.6, y - 2)
    t.pendown()
    t.setheading(0)
    for _ in range(2):
        t.circle(width * 0.6, 90)
        t.circle(width * 0.3, 90)
    t.end_fill()
    t.setheading(heading)
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_leaf(t, length, angle):
    """Draw a single leaf as a filled curve."""
    t.fillcolor(LEAF_COLOR)
    t.begin_fill()
    heading = t.heading()
    t.setheading(angle)
    t.forward(length)
    t.right(160)
    t.forward(length * 0.6)
    t.right(40)
    t.goto(t.position())  # close shape
    t.end_fill()
    t.setheading(heading)

def draw_leaf_cluster(t, spread=60, count=5, base_angle=80):
    """Draw several leaves radiating from current turtle position."""
    for i in range(count):
        a = base_angle + (random.random() - 0.5) * spread
        l = random.uniform(30, 70)
        draw_leaf(t, l, a + (i - count/2) * (spread / count))

# --- Bamboo shoot (main trunk) ---
def draw_bamboo_trunk(t, x, y, segments=6, base_length=80, taper=0.9):
    """
    Draw a bamboo trunk starting at (x,y).
    segments: number of segments (nodes)
    base_length: approximate length of first segment
    taper: how quickly thickness/length reduce up the stalk
    """
    move_to(t, x, y)
    t.setheading(90)  # point up

    length = base_length
    thickness = 40
    curvature = random.uniform(-8, 8)

    for i in range(segments):
        # slight random variation for a natural look
        curv = curvature + random.uniform(-4, 4)
        draw_segment(t, length, thickness, curvature=curv)
        draw_node(t, thickness)

        # occasionally add a branch with leaves
        if random.random() < 0.6 and i > 1:
            branch_angle = random.choice([20, -20, 35, -35])
            draw_branch(t, branch_angle, length * 0.6)

        # move to next segment start (already at top)
        # slight shift to simulate leaning
        t.right(random.uniform(-3, 3))

        length *= taper * random.uniform(0.9, 1.05)
        thickness *= 0.85

# --- Branches ---
def draw_branch(t, angle, length):
    """Draw a slender branch with leaves starting from current position."""
    # save position and heading
    x0, y0 = t.position()
    h0 = t.heading()

    t.setheading(90 + angle)
    t.pensize(3)
    t.pencolor(BAMBOO_COLOR)
    # branch line
    t.forward(length * 0.7)

    # draw a few leaf clusters along the branch
    for i in range(2):
        if random.random() < 0.9:
            move_to(t, t.xcor(), t.ycor())
            draw_leaf_cluster(t, spread=70, count=random.randint(3,5), base_angle=90 + angle)

        # move outward a bit
        t.forward(length * 0.15)

    # return to trunk top
    move_to(t, x0, y0)
    t.setheading(h0)
    t.pensize(1)

# --- Scene setup and drawing multiple stalks ---
def draw_scene():
    screen = turtle.Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.title("Bamboo Tree")
    screen.bgcolor(BACKGROUND_COLOR)

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.pensize(1)
    t.pencolor(BAMBOO_COLOR)

    # Ground line
    move_to(t, -SCREEN_WIDTH//2 + 20, -SCREEN_HEIGHT//2 + 40)
    t.pensize(3)
    t.pencolor("#6b8e23")
    t.forward(SCREEN_WIDTH - 40)
    t.pensize(1)
    t.pencolor(BAMBOO_COLOR)

    # Draw several bamboo stalks with varying positions and heights
    stalks = [
        (-220, -250, 8, 110),
        (-120, -260, 6, 95),
        ( -30, -250, 7, 100),
        ( 80, -255, 5, 90),
        (200, -260, 6, 100),
    ]

    for (x, y, segs, base_len) in stalks:
        # small random offset so each run feels organic
        x += random.uniform(-15, 15)
        y += random.uniform(-8, 8)
        draw_bamboo_trunk(t, x, y, segments=segs, base_length=base_len, taper=0.88)

    # Add some foreground leaves
    t.penup()
    for i in range(8):
        px = random.uniform(-SCREEN_WIDTH/2 + 20, SCREEN_WIDTH/2 - 20)
        py = random.uniform(-SCREEN_HEIGHT/2 + 40, -50)
        move_to(t, px, py)
        draw_leaf_cluster(t, spread=90, count=random.randint(2,5), base_angle=random.choice([80,100,60,120]))

    # Finish
    t.hideturtle()
    screen.update()
    turtle.done()

if __name__ == "__main__":
    draw_scene()
