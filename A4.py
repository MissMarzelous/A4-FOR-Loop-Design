# PROGRAMMER:  Marlena Fabrick
# PROGRAM NAME: Graphic Design Using FOR Loop — Stop Sign
# DATE WRITTEN: 9/30/2020
# PURPOSE:      Uses the turtle graphics module to draw a stop sign
#               shape using a FOR loop with a user-defined number of sides.

import turtle


def setup_screen():
    """Sets up the turtle screen with background color and title."""
    screen = turtle.Screen()
    screen.bgcolor("light green")
    screen.title("Stop Sign — FOR Loop Design")
    return screen


def setup_pen():
    """Creates and configures the turtle pen."""
    pen = turtle.Turtle()
    pen.shape("circle")
    pen.pensize(3)
    pen.pencolor("red")
    pen.speed(5)
    return pen


def draw_shape(pen, how_many):
    """Draws a filled shape using a FOR loop with the given number of sides."""
    pen.fillcolor("red")
    pen.begin_fill()

    for count in range(1, how_many + 1):
        print("count = " + str(count))
        pen.forward(100)
        pen.left(45)

    pen.end_fill()


def draw_stop_text(pen):
    """Writes STOP text on the shape."""
    pen.pencolor("white")
    pen.penup()
    pen.goto(-55, 74)
    pen.write("STOP", font=("Arial", 60, "bold"))


def draw_pole(pen):
    """Draws the stop sign pole."""
    pen.penup()
    pen.goto(50, 0)
    pen.pendown()
    pen.pensize(10)
    pen.right(90)
    pen.forward(300)


def main():
    setup_screen()
    pen = setup_pen()

    # Ask user how many sides to draw
    how_many = int(input("Enter the number of sides for the design: "))

    draw_shape(pen, how_many)
    draw_stop_text(pen)
    draw_pole(pen)

    pen.hideturtle()
    turtle.done()


main()
