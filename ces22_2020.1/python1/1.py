import turtle

def draw_square(turt, center, side):
    x, y = center

    x = x - side / 2
    y = y + side / 2

    turt.up()
    turt.goto(x, y)
    turt.down()

    for _ in range(4):
        turt.forward(side)
        turt.right(90)

def draw_n_squares(turt, n):
    for i in range(n):
        draw_square(turt, (0,0), 20 * (1+i))

turt = turtle.Turtle()
draw_n_squares(turt, 5)

turtle.Screen().exitonclick()