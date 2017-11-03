def square(t,d):
    for times in range(4):
        t.forward(d)
        t.right(90)

def triangle(t,d):
    for times in range(3):
        t.forward(d)
        t.left(120)

def polygon(t,s,d):
    sides=s
    a=360/sides
    for times in range(s):
        t.forward(d)
        t.left(a)
    
def polygonfill(t,s,d,c):
    sides=s
    a=360/sides
    t.color(c)
    t.begin_fill()
    for times in range(s):
        t.forward(d)
        t.left(a)
    t.end_fill()

def jump(t,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def cool(t,d,c1,c2):
    t.color(c1)
    polygon(t,4,d)
    t.color(c2)
    polygon(t,3,d)

def petal(t, size):
    dt = 255 /  size
    for times in range(size):
        t.color(times * dt, 0, 0)
        t.begin_fill()
        polygon(t, times * 2, 3)
        t.end_fill()
        t.forward(4)
        t.left(3)

def rose(t):
    for times in range(30):
        petal(t, 40  - times)
        t.left(31)
        t.forward(times + 10)

def flower(t):
    for times in range(40):
        t.home()
        t.left(times * 32)
        petal(t, 45  - times)
        t.forward(times + 10)


def char(t):
    t.begin_fill()
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(10)
    t.right(90)
    t.forward(10)
    t.end_fill()

def chard(t):
    t.begin_fill()
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(10)
    t.end_fill()
