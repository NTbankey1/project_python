import turtle

def setup_turtle():
    t = turtle.Turtle()
    t.speed(1)
    return t

def draw_square(t, size):
    for _ in range(4):
        t.forward(size)
        t.right(90)

def draw_circle(t, radius):
    t.circle(radius)

def draw_rectangle(t, width, height):
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)  
        t.right(90)

def draw_triangle(t, size):
    for _ in range(3):
        t.forward(size)
        t.right(120)

def draw_star(t, size):
    for _ in range(5):
        t.forward(size)
        t.right(144)
def draw_polygon(t, sides, size):
    angle = 360 / sides
    for _ in range(sides):
        t.forward(size)
        t.right(angle)

def draw_ellipse(t):
    for _ in range(2):
        t.circle(100,90)
        t.circle(50,90)