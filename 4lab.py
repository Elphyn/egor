# Import necessary modules from Pygame and PyOpenGL
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Define the vertices for the cube
vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1),
)

# Define the edges connecting the vertices
edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7),
)

# Function to draw the cube using the vertices and edges
def draw_cube():
    glBegin(GL_LINES)  # Begin drawing lines
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])  # Specify the vertex for the line
    glEnd()  # Finish drawing lines

# Main function where the Pygame window and OpenGL rendering is set up
def main():
    pygame.init()  # Initialize Pygame
    display = (800, 600)  # Set the display resolution
    # Create a Pygame window with OpenGL and double buffering
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    # Set the perspective for the 3D scene (field of view, aspect ratio, near and far clipping planes)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)  # Move the camera back 5 units along the z-axis

    # Initialize the x and y rotation angles for the cube
    x_rot = 0
    y_rot = 0

    # Initialize a variable to control whether the cube should rotate
    rotate_cube = False

    # Main event loop
    while True:
        # Process events in the Pygame event queue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # If the user closes the window
                pygame.quit()  # Close Pygame
                quit()  # Exit the script
            # Check if the left mouse button is pressed
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    rotate_cube = True  # Set the rotate_cube variable to True
                    pygame.mouse.get_rel()  # Discard the relative mouse movement before starting rotation
            # Check if the left mouse button is released
            elif event.type == MOUSEBUTTONUP:
                if event.button == 1:  # Left mouse button
                    rotate_cube = False  # Set the rotate_cube variable to False

        # If the left mouse button is held down, update the rotation angles based on mouse movement
        if rotate_cube:
            x, y = pygame.mouse.get_rel()  # Get the relative mouse movement
            x_rot += y * 0.1  # Update the x rotation angle
            y_rot += x * 0.1  # Update the y rotation angle

        glPushMatrix()  # Save
        glPushMatrix()  # Save the current transformation matrix
        glRotatef(x_rot, 1, 0, 0)  # Apply rotation around the x-axis
        glRotatef(y_rot, 0, 1, 0)  # Apply rotation around the y-axis
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear the color and depth buffers

        draw_cube()  # Call the draw_cube function to draw the cube

        glPopMatrix()  # Restore the transformation matrix to its previous state

        pygame.display.flip()  # Swap the front and back buffers, displaying the rendered frame
        pygame.time.wait(10)  # Wait for 10 milliseconds to control the frame rate

if __name__ == "__main__":
    main()

