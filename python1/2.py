import turtle

def draw_poly(t, n, sz):
    for _ in range(n):
        t.fd(sz)
        t.rt(180 - 180*(1-2/n))

tortuguita = turtle.Turtle()

draw_poly(tortuguita, 8, 50)

turtle.Screen().exitonclick()