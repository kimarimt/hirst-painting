import turtle


def main():
    s = turtle.getscreen()
    t = turtle.Turtle()

    y = -300

    t.hideturtle()
    t.penup()
    t.goto(-325, y)
    t.shape('circle')
    t.fillcolor('red')
    t.pencolor('red')

    while t.ycor() < 340:
        t.stamp()

        while t.xcor() < 315:
            t.forward(40)
            t.stamp()

        y += 40
        t.goto(-325, y)

    s.exitonclick()


if __name__ == '__main__':
    main()
