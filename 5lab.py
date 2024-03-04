import turtle

# Set up the turtle environment
screen = turtle.Screen()
pen = turtle.Turtle()

# Set the fill color
pen.fillcolor("black")

# Start filling the figure
pen.begin_fill()

# Draw a pentagon
for i in range(5):
    pen.forward(100)  # Move forward by 100 units
    pen.right(72)     # Turn right by 72 degrees (360/5)

# End filling the figure
pen.end_fill()

# Hide the turtle
pen.hideturtle()

# Keep the window open
screen.mainloop()
