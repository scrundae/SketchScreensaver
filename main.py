import turtle
import random
import tkinter

root = tkinter.Tk()
root.withdraw()  # Hide the root window

# Get screen resolution
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set up the turtle
turtle.hideturtle()
turtle.speed(0)  # Fastest speed
turtle.colormode(255)  # Use 0-255 range for colors
turtle.pendown()
turtle.bgcolor('black')

def set_fullscreen():
    # Access the underlying Tkinter window
    screen = turtle.Screen()
    tk_window = screen._root  # Get the Tkinter window object
    tk_window.attributes('-fullscreen', True)  # Set fullscreen mode

# Set up the turtle screen and background color
set_fullscreen()  # Make the turtle window fullscreen

# Run the drawing loop
for _ in range(1000):  # Draw 1000 lines
    turtle.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    turtle.pensize(random.randint(0, 10))
    turtle.goto(random.randint(-screen_width, screen_width), random.randint(-screen_height, screen_height))

turtle.done()  # Finish drawing
