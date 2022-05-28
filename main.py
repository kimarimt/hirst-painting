import turtle
import random
import colorgram


def change_color(object, colors):
    color = random.choice(colors)
    code = color.rgb
    object.fillcolor(code.r, code.g, code.b)
    object.pencolor(code.r, code.g, code.b)


def main():
    colors = colorgram.extract('hirst.jpg', 50)
    s = turtle.getscreen()
    s.colormode(255)
    t = turtle.Turtle()

    y = -300

    t.hideturtle()
    t.penup()
    t.goto(-325, y)
    t.shape('circle')

    while t.ycor() < 340:
        change_color(t, colors)
        t.stamp()

        while t.xcor() < 315:
            change_color(t, colors)
            t.forward(40)
            t.stamp()

        y += 40
        t.goto(-325, y)

    s.exitonclick()


if __name__ == '__main__':
    main()
