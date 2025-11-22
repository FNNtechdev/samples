# palace.py
# Draw a stylized palace using the turtle module

import turtle

# ---------- Setup ----------
screen = turtle.Screen()
screen.setup(width=1000, height=700)
screen.title("Palace Drawing")
screen.bgcolor("#87CEEB")  # sky blue

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(2)

def move(x, y):
    t.up()
    t.goto(x, y)
    t.down()

def rect(x, y, w, h, fill=None, outline="black"):
    move(x, y)
    if fill:
        t.fillcolor(fill)
        t.begin_fill()
    t.color(outline)
    for _ in range(2):
        t.forward(w)
        t.right(90)
        t.forward(h)
        t.right(90)
    if fill:
        t.end_fill()

def triangle(x, y, w, h, fill=None, outline="black"):
    move(x, y)
    if fill:
        t.fillcolor(fill)
        t.begin_fill()
    t.color(outline)
    t.forward(w/2)
    t.left(120)
    t.forward(h)
    t.left(120)
    t.forward(h)
    t.left(120)
    t.forward(w/2)
    if fill:
        t.end_fill()
    t.setheading(0)

def semicircle(x, y, radius, fill=None, outline="black"):
    move(x, y)
    t.setheading(0)
    if fill:
        t.fillcolor(fill)
        t.begin_fill()
    t.color(outline)
    t.circle(radius, 180)
    if fill:
        t.end_fill()
    t.setheading(0)

def tower(x, base_y, width, height, color):
    # base rectangle
    rect(x, base_y, width, height, fill=color)
    # battlements
    batt_w = width/5
    bx = x
    for i in range(5):
        rect(bx, base_y+height, batt_w, batt_w/1.8, fill="#ddd", outline="#777")
        bx += batt_w

def dome(x, y, radius, color):
    move(x, y)
    t.setheading(0)
    t.color("black")
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius, 180)
    t.end_fill()
    # small spire
    move(x+radius, y)
    t.setheading(90)
    t.forward(radius/3)
    t.right(90)
    t.circle(radius/12, 180)

def window(x, y, w, h):
    rect(x, y, w, h, fill="#fff", outline="#333")
    # cross panes
    move(x + w/2, y)
    t.setheading(90)
    t.forward(h)
    move(x, y + h/2)
    t.setheading(0)
    t.forward(w)

def flag(x, y, pole_h=40, color="#ff0000"):
    move(x, y)
    t.setheading(90)
    t.color("sienna")
    t.pensize(4)
    t.forward(pole_h)
    # flag
    move(x, y + pole_h)
    t.pensize(1)
    t.fillcolor(color)
    t.begin_fill()
    t.forward(30)
    t.right(120)
    t.forward(15)
    t.right(120)
    t.forward(30)
    t.end_fill()
    t.setheading(0)

# ---------- Draw ground ----------
rect(-500, -250, 1000, 200, fill="#3CB371", outline="#2E8B57")  # grass

# ---------- Main palace body ----------
main_x = -300
main_y = -50
main_w = 600
main_h = 220
rect(main_x, main_y, main_w, main_h, fill="#F5DEB3", outline="#8B5A2B")  # main hall

# central dome area (a raised platform)
rect(-100, main_y + main_h, 200, 30, fill="#DEB887", outline="#8B5A2B")
dome(-0, main_y + main_h + 30, 80, "#D2691E")

# main door
door_w = 100
door_h = 140
rect(-door_w/2, main_y, door_w, door_h, fill="#8B4513", outline="#4B2E12")
# arch above door
move(-door_w/2, main_y + door_h)
t.setheading(0)
t.color("#4B2E12")
t.fillcolor("#DEB887")
t.begin_fill()
t.forward(door_w)
t.left(90)
t.circle(door_w/2, 180)
t.left(90)
t.end_fill()
t.setheading(0)

# steps
step_w = 220
step_h = 12
sx = -step_w/2
for i in range(6):
    rect(sx - i*6, main_y - (i+1)*step_h, step_w + i*12, step_h, fill="#C0C0C0", outline="#888")

# windows on main hall
win_w, win_h = 40, 60
for i in range(3):
    wx = main_x + 80 + i*140
    wy = main_y + 80
    window(wx - win_w/2, wy - win_h/2, win_w, win_h)

# small decorative triangles (gables) above windows
for i in range(3):
    tx = main_x + 80 + i*140 - 20
    ty = main_y + 140
    triangle(tx, ty, 40, 40, fill="#DEB887", outline="#8B5A2B")
    t.setheading(0)

# ---------- Left and right towers ----------
tower(-420, main_y - 10, 120, 260, "#F5DEB3")
tower(300, main_y - 10, 120, 260, "#F5DEB3")

# small domes for towers
dome(-360, main_y + 250, 40, "#B55A1B")
dome(360, main_y + 250, 40, "#B55A1B")

# tower windows
for tx in (-360, 360):
    for i in range(3):
        window(tx - 15, main_y + 20 + i*60, 30, 40)

# flags
flag(-360 + 10, main_y + 300, pole_h=45, color="#FF0000")
flag(360 - 30, main_y + 300, pole_h=45, color="#0000FF")

# small minarets between towers and main building
for px in (-180, 180):
    rect(px - 15, main_y + main_h - 20, 30, 90, fill="#EED5B7", outline="#8B5A2B")
    semicircle(px + 15, main_y + main_h + 70, 15, fill="#B5651D")

# decorative roofline battlements
bx = main_x
for i in range(15):
    rect(bx + i*40, main_y + main_h, 24, 12, fill="#DEB887", outline="#8B5A2B")

# finishing touches: small windows and details
move(-460, main_y + 40)
t.color("#8B5A2B")
t.write("GRAND PALACE", font=("Arial", 18, "bold"))

# Done
t.penup()
move(0, -320)
t.pendown()
t.color("#333")
t.write("Press any key on the window to close.", align="center", font=("Arial", 12, "normal"))

# Wait for user to close
screen.exitonclick()
