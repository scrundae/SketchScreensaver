import turtle
import random
import tkinter as tk

def close_window(event=None):
    """Function to close the Turtle graphics window."""
    turtle.bye()  # Close the turtle graphics window

def set_fullscreen():
    """Function to set the window to fullscreen and remove border."""
    screen = turtle.Screen()
    tk_window = screen._root  # Get the Tkinter window object
    tk_window.attributes('-fullscreen', True)  # Set fullscreen mode
    tk_window.overrideredirect(True)  # Remove window border and title bar

def setup_event_handlers():
    """Function to set up event handlers for closing the window."""
    screen = turtle.Screen()
    tk_window = screen._root  # Get the Tkinter window object
    
    # Bind any key press and mouse movement to close the window
    tk_window.bind("<KeyPress>", close_window)
    tk_window.bind("<Motion>", close_window)

# Set up the turtle screen
set_fullscreen()  # Make the turtle window fullscreen and borderless

screen = turtle.Screen()
screen.bgcolor("black")  # Set background color

# Set up the turtle
turtle.hideturtle()
turtle.speed(0)  # Fastest speed
turtle.colormode(255)  # Use 0-255 range for colors
turtle.pendown()

# Set up event handlers
setup_event_handlers()

# Run the drawing loop
while True:  # Draw 1000 lines
    turtle.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    turtle.goto(random.randint(-1000, 1000), random.randint(-1000, 1000))

# Finish drawing
turtle.done()
