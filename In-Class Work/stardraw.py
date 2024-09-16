import turtle
t = turtle.Turtle()

t.pensize(2)
t.fillcolor("green")

t.begin_fill()

for i in range(5):
    t.forward(100)
    t.left(144)

t.end_fill()
