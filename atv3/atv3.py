import pygame
from OpenGL.GL import *
import math

from DDA import displayDDA
from PM import displayPM

abs 

class Tela:
    def __init__(self, display) -> None:
        pygame.init()
        windowSize = (800, 800)
        pygame.display.set_mode(windowSize, pygame.OPENGL | pygame.DOUBLEBUF)
        self.clock = pygame.time.Clock()
        
        glClearColor(1.0, 1.0, 1.0, 0.0) #selecionar cor de fundo (Branco)
        glOrtho (-2, 12, -2, 12, -1 ,1)
        self.display = display
    	
        self.Loop()

    def Loop(self):
        running = True

        while running:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False
            
            # refresh
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            self.display()
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

if __name__=='__main__':
    disDDA = Tela(displayDDA)
    disPM = Tela(displayPM)