import turtle
import math

# ---------------- SCREEN ----------------
screen = turtle.Screen()
screen.setup(900, 900)
screen.bgcolor("#0b1026")
screen.title("Mahadev - Turtle Graphics")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# ---------------- HELPERS ----------------
def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def line(x1, y1, x2, y2, width=3):
    t.penup()
    t.goto(x1, y1)
    t.pendown()
    t.pensize(width)
    t.goto(x2, y2)

def circle(x, y, r, fill=None, color="white", width=3):
    move(x, y-r)
    t.pencolor(color)
    t.pensize(width)
    if fill:
        t.fillcolor(fill)
        t.begin_fill()
    t.circle(r)
    if fill:
        t.end_fill()

def polygon(points, fill, outline="white", width=3):
    move(*points[0])
    t.pencolor(outline)
    t.pensize(width)
    t.fillcolor(fill)
    t.begin_fill()
    for p in points[1:]:
        t.goto(*p)
    t.goto(*points[0])
    t.end_fill()

# =================================================
#                TRISHUL
# =================================================

# Trishul center
line(0, 80, 0, 390, 8)

# Left spear
line(0, 300, -70, 390, 7)
line(-70, 390, -95, 350, 7)
line(-70, 390, -35, 365, 7)

# Right spear
line(0, 300, 70, 390, 7)
line(70, 390, 95, 350, 7)
line(70, 390, 35, 365, 7)

# Center spear
line(0, 300, 0, 430, 8)
line(0, 430, -22, 390, 7)
line(0, 430, 22, 390, 7)

# Trishul ring
circle(0, 285, 18, None, "#d4af37", 5)

# =================================================
#                DAMRU
# =================================================

polygon(
    [(-42, 230), (-15, 250), (15, 250), (42, 230),
     (15, 210), (-15, 210)],
    "#8B4513", "#D4AF37", 3
)

line(-42, 230, 42, 230, 3)

# Damru ropes
line(-25, 220, -65, 190, 2)
line(25, 220, 65, 190, 2)

circle(-68, 188, 8, "#D4AF37", "#D4AF37", 2)
circle(68, 188, 8, "#D4AF37", "#D4AF37", 2)

# =================================================
#                JATA / HAIR
# =================================================

# Outer hair
circle(0, 100, 190, "#171717", "#9E9E9E", 5)

# Hair strands
for y in [130, 150, 170, 190]:
    line(-145, y, 145, y, 4)

# Side hair locks
for x in [-150, -130, 130, 150]:
    line(x, 100, x + (20 if x < 0 else -20), -10, 7)

# =================================================
#                FACE
# =================================================

# Face
circle(0, 20, 125, "#B98262", "#E0B090", 5)

# Ears
circle(-125, 20, 25, "#B98262", "#E0B090", 4)
circle(125, 20, 25, "#B98262", "#E0B090", 4)

# =================================================
#                CRESCENT MOON
# =================================================

circle(70, 125, 32, "#F5F5DC", "#F5F5DC", 2)
circle(82, 135, 32, "#171717", "#171717", 2)

# =================================================
#                EYES
# =================================================

# Left eye
move(-75, 55)
t.setheading(-10)
t.pensize(5)
t.pencolor("#111111")
t.circle(55, 40)

# Right eye
move(75, 55)
t.setheading(190)
t.circle(55, 40)

# Pupils
circle(-45, 50, 8, "#111111", "#111111", 2)
circle(45, 50, 8, "#111111", "#111111", 2)

# =================================================
#                THIRD EYE
# =================================================

# Third eye
move(-18, 88)
t.setheading(0)
t.pensize(5)
t.pencolor("#C62828")
t.forward(36)

circle(0, 88, 6, "#FF5722", "#FF5722", 2)

# =================================================
#                NOSE
# =================================================

move(0, 45)
t.setheading(-90)
t.pensize(4)
t.pencolor("#704C3A")
t.forward(35)

# =================================================
#                MOUTH
# =================================================

move(-35, -45)
t.setheading(-5)
t.pensize(4)
t.pencolor("#5D3025")
t.circle(38, 20)

# =================================================
#                TILAK
# =================================================

line(-35, 105, 35, 105, 5)
line(-25, 115, 25, 115, 4)
line(-15, 125, 15, 125, 3)

# =================================================
#                RUDRAKSHA MALA
# =================================================

for angle in range(200, 341, 10):
    rad = math.radians(angle)
    x = 95 * math.cos(rad)
    y = -20 + 75 * math.sin(rad)
    circle(x, y, 7, "#6D4C41", "#3E2723", 2)

# =================================================
#                NECK
# =================================================

polygon(
    [(-70, -80), (70, -80), (90, -180),
     (-90, -180)],
    "#8E604A", "#E0B090", 4
)

# Blue poison mark
polygon(
    [(-55, -110), (55, -110), (45, -155),
     (-45, -155)],
    "#1565C0", "#42A5F5", 3
)

# =================================================
#                SHOULDERS
# =================================================

# Left shoulder
circle(-125, -190, 70, "#8E604A", "#E0B090", 4)

# Right shoulder
circle(125, -190, 70, "#8E604A", "#E0B090", 4)

# =================================================
#                NAG (SNAKE)
# =================================================

move(-110, -110)
t.setheading(40)
t.pensize(5)
t.pencolor("#D4AF37")

for i in range(90):
    t.forward(2)
    t.left(4)

# Snake head
circle(-65, -45, 12, "#D4AF37", "#D4AF37", 2)

# =================================================
#                DECORATION
# =================================================

# Om symbol style curves
move(-350, -330)
t.pencolor("#D4AF37")
t.pensize(5)

t.setheading(0)
t.circle(50, 300)

move(-300, -350)
t.setheading(90)
t.forward(80)

# Stars
for x, y in [
    (-350, 300), (330, 300), (-380, 100),
    (370, 100), (-330, -100), (330, -100)
]:
    circle(x, y, 5, "#FFD700", "#FFD700", 1)

# ---------------- FINAL ----------------

move(0, -400)
t.color("#FFD700")
t.write(
    "ॐ नमः शिवाय",
    align="center",
    font=("Arial", 24, "bold")
)

turtle.done()