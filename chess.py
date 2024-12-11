# Import the turtle package
import turtle

# Create screen object
sc = turtle.Screen()

# Create turtle object
pen = turtle.Turtle()

# Method to draw a square
def draw():
    for i in range(4):
        pen.forward(30)
        pen.left(90)

# Driver code
if __name__ == "__main__":
    # Set up the screen
    sc.setup(600, 600)
    sc.title("Checkerboard Pattern")

    # Set turtle object speed
    pen.speed(100)

    # Loops for board
    for i in range(8):
        # Not ready to draw
        pen.up()

        # Set position for every row
        pen.setpos(0, 30 * i)

        # Ready to draw
        pen.down()

        # Row
        for j in range(8):
            # Conditions for alternative color
            if (i + j) % 2 == 0:
                col = 'black'
            else:
                col = 'white'

            # Fill with the given color
            pen.fillcolor(col)

            # Start filling with color
            pen.begin_fill()

            # Call method to draw square
            draw()

            # Stop filling
            pen.end_fill()

    # Hide the turtle
    pen.hideturtle()

    # Keep the window open until clicked
    sc.mainloop()
