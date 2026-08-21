import turtle

# ---------------- SCREEN ----------------
screen = turtle.Screen()
screen.setup(900, 800)
screen.bgcolor("#10101c")
screen.title("Mahadev - Python Turtle Graphics")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# ---------------- HELPER FUNCTIONS ----------------
def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def line(points, color, width=4):
    t.color(color)
    t.pensize(width)
    move(*points[0])

    for p in points[1:]:
        t.goto(*p)

def circle(x, y, radius, color):
    t.penup()
    t.goto(x, y - radius)
    t.setheading(0)
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# ---------------- SHIV JI FACE ----------------
circle(0, 80, 170, "#d9d9d9")

# ---------------- JATA / HAIR ----------------
t.color("#3b2418")
t.pensize(18)

line([
    (-145, 180),
    (-185, 240),
    (-130, 220),
    (-95, 275),
    (-40, 235),
    (0, 295),
    (40, 235),
    (95, 275),
    (130, 220),
    (185, 240),
    (145, 180)
], "#3b2418", 18)

# Top hair bun
circle(0, 285, 55, "#3b2418")

# ---------------- EYES ----------------
line([(-90, 110), (-35, 110)], "#111111", 7)
line([(35, 110), (90, 110)], "#111111", 7)

# Eyebrows
line([(-95, 135), (-45, 150)], "#3b2418", 8)
line([(45, 150), (95, 135)], "#3b2418", 8)

# ---------------- THIRD EYE ----------------
t.color("#b00020")
t.pensize(6)

move(-18, 165)
t.setheading(45)
t.forward(35)

move(18, 165)
t.setheading(135)
t.forward(35)

circle(0, 165, 8, "#d00000")

# ---------------- NOSE ----------------
line([
    (0, 105),
    (-12, 55),
    (0, 45),
    (12, 55)
], "#555555", 5)

# ---------------- LIPS ----------------
line([(-35, 15), (0, 8), (35, 15)], "#7a3030", 5)

# ---------------- TILAK ----------------
line([(-12, 190), (12, 190)], "#b30000", 6)
line([(-12, 202), (12, 202)], "#b30000", 6)

# ---------------- NECK ----------------
t.color("#d9d9d9")
t.pensize(35)

line([
    (-70, -65),
    (-70, -190)
], "#d9d9d9", 35)

line([
    (70, -65),
    (70, -190)
], "#d9d9d9", 35)

# ---------------- RUDRAKSHA MALA ----------------
t.color("#6b3515")
t.pensize(3)

move(-115, -35)

for i in range(24):
    t.dot(12, "#7a3e18")
    t.forward(10)

# ---------------- SNAKE ----------------
t.color("#d4aa44")
t.pensize(8)

line([
    (95, 80),
    (130, 105),
    (155, 80),
    (130, 55),
    (155, 30),
    (130, 5)
], "#d4aa44", 8)

# Snake head
circle(155, 85, 15, "#d4aa44")

# Snake eyes
circle(150, 90, 3, "#111111")
circle(160, 90, 3, "#111111")

# ---------------- TRISHUL ----------------
# Main staff
line([
    (300, -230),
    (300, 280)
], "#f4c542", 8)

# Left trident
line([
    (300, 210),
    (245, 270),
    (265, 210)
], "#f4c542", 7)

# Right trident
line([
    (300, 210),
    (355, 270),
    (335, 210)
], "#f4c542", 7)

# Center trident
line([
    (300, 210),
    (300, 315)
], "#f4c542", 7)

# ---------------- DAMRU ----------------
t.color("#b85c38")
t.pensize(6)

line([
    (260, 60),
    (290, 40),
    (260, 20),
    (290, 0)
], "#b85c38", 7)

# Damru strings
line([(275, 45), (240, 80)], "#f4c542", 3)
line([(275, 15), (310, -20)], "#f4c542", 3)

# ---------------- OM SYMBOL ----------------
t.color("#e0b84b")
t.pensize(5)

move(-350, -260)
t.setheading(0)

# Simple Om-like decorative curve
t.circle(45, 180)
t.circle(-25, 180)
t.circle(35, 180)

# ---------------- TEXT ----------------
move(0, -330)
t.color("#f4c542")
t.write(
    "HAR HAR MAHADEV",
    align="center",
    font=("Arial", 24, "bold")
)

turtle.done()