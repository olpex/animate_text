# Import the turtle module, which provides a simple graphics window and a turtle object that can be moved around in it.
import turtle

# Import the random module, which provides functionality for generating random numbers.
import random

# Create a new turtle screen and set its background color to light green.
window = turtle.Screen()
window.bgcolor("light green")

# Create a new turtle object and set its shape to a turtle, its color to blue, and its speed to 1 (slowest).
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.color("blue")
my_turtle.speed(1)

# Define a function called draw_square that takes a turtle object and a size as arguments.
# This function will draw a square of the given size using the provided turtle object.
def draw_square(turtle, size):
    # Repeat the following steps 4 times to draw a square.
    for _ in range(4):
        # Move the turtle forward by the given size.
        turtle.forward(size)
        # Turn the turtle right by 90 degrees.
        turtle.right(90)

# Define a function called ai_draw that takes a turtle object and a size as arguments.
# This function will draw a series of connected squares using the provided turtle object.
def ai_draw(turtle, size):
    # Repeat the following steps 10 times to draw a series of connected squares.
    for _ in range(10):
        # Randomly choose a direction (either 'left' or 'right').
        direction = random.choice(['left', 'right'])
        # If the chosen direction is 'left', turn the turtle left by 90 degrees.
        if direction == 'left':
            turtle.left(90)
        # If the chosen direction is 'right', turn the turtle right by 90 degrees.
        else:
            turtle.right(90)
        # Draw a square of the given size using the provided turtle object.
        draw_square(turtle, size)

# Call the ai_draw function with the my_turtle object and a size of 50.
ai_draw(my_turtle, 50)

# Start the turtle graphics event loop, which will wait for user events (such as key presses and mouse clicks).
window.mainloop()