# Import the Turtle Graphics module
import turtle

# Define program constants
WIDTH = 500
HEIGHT = 500
DELAY = 10  # Milliseconds between screen updates


def move_turtle():
    my_turtle.forward(1)
    my_turtle.right(1)
    screen.update()
    screen.ontimer(move_turtle, DELAY)  # After `DELAY` milliseconds, call move_turtle() again


# Create a window where we will do our drawing
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)  # Set the dimensions of the window
screen.title("Turtle Animation")
screen.bgcolor("cyan")
screen.tracer(0)  # Turn off automatic animation

# Create a turtle to do our bidding
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.color("red")

# Set animation in motion
move_turtle()

# Finish nicely
turtle.done()
