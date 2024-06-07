import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def dda(x1, y1, x2, y2):
    # Calcula a diferença em x e y
    dx = x2 - x1
    dy = y2 - y1

    # Determina o número de passos necessários
    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)

    # Calcula o incremento em x e y por cada passo
    x_increment = dx / float(steps)
    y_increment = dy / float(steps)

    # Inicializa a posição atual
    x = x1
    y = y1

    # Usa uma lista para armazenar os pontos calculados
    points = []

    # Calcula todos os pontos da linha
    for i in range(steps + 1):
        points.append((x, y))
        x += x_increment
        y += y_increment

    return points

def draw_line(points):
    glBegin(GL_POINTS)
    for point in points:
        glVertex2f(point[0], point[1])
    glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluOrtho2D(0, 800, 0, 600)

    x1, y1 = 100, 100
    x2, y2 = 700, 500

    points = dda(x1, y1, x2, y2)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glColor3f(1.0, 1.0, 1.0)
        draw_line(points)

        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()

if __name__ == "__main__":
    main()