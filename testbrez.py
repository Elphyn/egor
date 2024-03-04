import pygame
import sys
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE
def bresenham_line(x0, y0, x1, y1):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    x, y = x0, y0
    sx = -1 if x0 > x1 else 1
    sy = -1 if y0 > y1 else 1

    if dx > dy:
        err = dx / 2.0
        while x != x1:
            yield x, y
            err -= dy
            if err < 0:
                y += sy
                err += dx
            x += sx
    else:
        err = dy / 2.0
        while y != y1:
            yield x, y
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy

    yield x, y

def draw_line(grid, x0, y0, x1, y1):
    for x, y in bresenham_line(x0, y0, x1, y1):
        grid[y][x] = 1

grid = [[0] * 10 for _ in range(10)]
draw_line(grid, 1, 1, 8, 6)

for row in grid:
    print(" ".join(map(str, row)))



def dda_line(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0
    steps = max(abs(dx), abs(dy))

    x_increment = dx / steps
    y_increment = dy / steps

    x, y = x0, y0
    for _ in range(steps + 1):
        yield round(x), round(y)
        x += x_increment
        y += y_increment

def draw_line_dda(grid, x0, y0, x1, y1):
    for x, y in dda_line(x0, y0, x1, y1):
        grid[y][x] = 1

grid_dda = [[0] * 10 for _ in range(10)]
draw_line_dda(grid_dda, 1, 1, 8, 6)

for row in grid_dda:
    print(" ".join(map(str, row)))




def draw_line(screen, x0, y0, x1, y1, color, cell_size, algorithm, offset_x=0):
    if algorithm == "bresenham":
        line_points = bresenham_line(x0, y0, x1, y1)
    elif algorithm == "dda":
        line_points = dda_line(x0, y0, x1, y1)
    else:
        raise ValueError("Invalid algorithm. Choose 'bresenham' or 'dda'.")

    for x, y in line_points:
        rect = pygame.Rect(x * cell_size + offset_x, y * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, color, rect)


def draw_grid(screen, cell_size, grid_color, offset_x=0):
    for x in range(offset_x, offset_x + screen.get_width() // 2, cell_size):
        for y in range(0, screen.get_height(), cell_size):
            rect = pygame.Rect(x, y, cell_size, cell_size)
            pygame.draw.rect(screen, grid_color, rect, 1)


def main():
    pygame.init()
    screen_size = (1000, 500)
    cell_size = 30
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Bresenham's and DDA Line Algorithms")

    background_color = (255, 255, 255)
    grid_color = (200, 200, 200)
    line_color = (0, 0, 0)

    x0, y0, x1, y1 = 1, 1, 8, 9

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        screen.fill(background_color)
        
        # Draw grids
        draw_grid(screen, cell_size, grid_color)
        draw_grid(screen, cell_size, grid_color, offset_x=screen_size[0] // 2)

        # Draw lines using Bresenham's and DDA algorithms
        draw_line(screen, x0, y0, x1, y1, line_color, cell_size, algorithm="bresenham", offset_x=0)
        draw_line(screen, x0, y0, x1, y1, line_color, cell_size, algorithm="dda", offset_x=screen_size[0] // 2)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

