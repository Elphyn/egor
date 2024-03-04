import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import math



# Define the cube vertices and edges

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

# Function to draw the cube
def draw_cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

# Initialize Pygame and create a window
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

# Setup OpenGL
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

# Set initial rotation
rotation_x, rotation_y = 0, 0
rotate = False

# Variables for time-based rotation
current_time = pygame.time.get_ticks()
rotation_speed = 0.001

def rotation_matrix(angle_x, angle_y):
    cos_x = math.cos(math.radians(angle_x))
    sin_x = math.sin(math.radians(angle_x))
    cos_y = math.cos(math.radians(angle_y))
    sin_y = math.sin(math.radians(angle_y))

    rot_x = np.array([
        [1, 0, 0, 0],
        [0, cos_x, -sin_x, 0],
        [0, sin_x, cos_x, 0],
        [0, 0, 0, 1]
    ])

    rot_y = np.array([
        [cos_y, 0, sin_y, 0],
        [0, 1, 0, 0],
        [-sin_y, 0, cos_y, 0],
        [0, 0, 0, 1]
    ])

    return np.dot(rot_y, rot_x)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Clear buffers
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # Calculate rotation based on formulas
    time_elapsed = pygame.time.get_ticks() - current_time
    angle_x = math.sin(time_elapsed * rotation_speed) * 360
    angle_y = math.cos(time_elapsed * rotation_speed) * 360

    # Apply rotation matrix
    rot_matrix = rotation_matrix(angle_x, angle_y)
    glPushMatrix()
    glMultMatrixf(rot_matrix.T.flatten())

    # Draw the cube
    draw_cube()

    # Reset rotation
    glPopMatrix()

    # Swap buffers
    pygame.display.flip()
    pygame.time.wait(10)
