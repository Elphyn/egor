import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import sys


# Constants
WIDTH, HEIGHT = 800, 800
FPS = 60
ATOM_RADIUS = 20
ELECTRON_RADIUS = 5
NUM_ELECTRONS = 3
ORBIT_DISTANCES = [100, 150, 200]
ORBIT_SPEEDS = [0.02, 0.015, 0.01]

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Utility Functions
def create_sphere(radius):
    obj = gluNewQuadric()
    gluQuadricDrawStyle(obj, GLU_FILL)
    gluQuadricNormals(obj, GLU_SMOOTH)
    gluSphere(obj, radius, 64, 64)
    gluDeleteQuadric(obj)

def draw_sphere(x, y, z, radius):
    glPushMatrix()
    glTranslate(x, y, z)
    create_sphere(radius)
    glPopMatrix()

def draw_orbit(radius):
    glBegin(GL_LINE_LOOP)
    for i in range(360):
        angle = math.radians(i)
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        glVertex3f(x, y, 0)
    glEnd()

ORBIT_PLANES = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]

def main():
    pygame.init()
    pygame.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Atom Animation")

    gluPerspective(45, (WIDTH / HEIGHT), 0.1, 500.0)
    glTranslatef(0.0, 0.0, -400)

    clock = pygame.time.Clock()

    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glColor3ub(*BLUE)
        draw_sphere(0, 0, 0, ATOM_RADIUS)

        # Draw electrons and orbits
        for i, plane in enumerate(ORBIT_PLANES):
            angle = ORBIT_SPEEDS[i] * pygame.time.get_ticks()
            x = ORBIT_DISTANCES[i] * math.cos(angle) * plane[0]
            y = ORBIT_DISTANCES[i] * math.sin(angle) * plane[1]
            z = ORBIT_DISTANCES[i] * math.sin(angle) * plane[2]

            glColor3ub(*BLUE)
            draw_sphere(x, y, z, ELECTRON_RADIUS)
            glColor3ub(*WHITE)
            draw_orbit(ORBIT_DISTANCES[i])

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()

