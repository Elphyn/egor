import pygame

# Функция рисования линии
def draw_line(surface, x1, y1, x2, y2, color):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = -1 if x1 > x2 else 1
    sy = -1 if y1 > y2 else 1
    err = dx - dy

    while True:
        surface.set_at((x1, y1), color)

        if x1 == x2 and y1 == y2:
            break

        e2 = 2 * err

        if e2 > -dy:
            err -= dy
            x1 += sx

        if e2 < dx:
            err += dx
            y1 += sy

# Fill color
def fill(surface, x, y, fill_color):
    target_color = surface.get_at((x, y))

    if target_color == fill_color:    
        return

    stack = [(x, y)]

    while stack:
        x, y = stack.pop()

        if surface.get_at((x, y)) == target_color:
            surface.set_at((x, y), fill_color)

            if x > 0:
                stack.append((x - 1, y))
            if x < surface.get_width() - 1:
                stack.append((x + 1, y))
            if y > 0:
                stack.append((x, y - 1))
            if y < surface.get_height() - 1:
                stack.append((x, y + 1))

pygame.init()

width = 640 
height = 480 
screen = pygame.display.set_mode((width, height)) 

surface = pygame.Surface((width, height)) 
surface.fill((0, 0, 0))

drawing = False  
start_pos = None

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Левая кнопка мыши - начало рисования
                drawing = True
                start_pos = event.pos
            elif event.button == 3:  # Правая кнопка мыши - заливка затравкой
                fill_color = (255, 0, 0)  # Цвет заливки
                x, y = pygame.mouse.get_pos()
                fill(surface, x, y, fill_color)
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Левая кнопка мыши - конец рисования
                drawing = False
                end_pos = event.pos
                draw_line(surface, start_pos[0], start_pos[1], end_pos[0], end_pos[1], (255, 255, 255))
        elif event.type == pygame.MOUSEMOTION:
            if drawing:  # Рисование линии при движении мыши с зажатой левой кнопкой
                end_pos = event.pos
                draw_line(surface, start_pos[0], start_pos[1], end_pos[0], end_pos[1], (255, 255, 255))
                start_pos = end_pos

    screen.blit(surface, (0, 0))
    pygame.display.update()