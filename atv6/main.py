import pygame
from OpenGL.GL import *
import math
from models import robot as rb

class Tela:
    def __init__(self) -> None:
        pygame.init()
        windowSize = (800, 800)
        pygame.display.set_mode(windowSize, pygame.OPENGL | pygame.DOUBLEBUF)
        self.clock = pygame.time.Clock()
        
        glClearColor(0.0, 0.5, 1.0, 1.0) # selecionar cor de fundo
        glOrtho (-1, 1,-1, 1, -1 ,1); # define as coordenadas do volume de recorte (clipping volume)
    	
        self.Loop()

    def Loop(self):
        running = True

        argsShape = {'leftShoulder': 0, 'rightShoulder': 0, 
                     'leftElbow': 0, 'rightElbow': 0,
                     'leftHand': 0, 'rightHand': 0}
        
        currentArm = 'leftShoulder'

        while running:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if movement.get(event.key):
                        print('parte', event.key)
                        currentArm = movement.get(event.key)
                    elif pygame.K_UP == event.key:
                        argsShape[currentArm] += 5 
                        print('horario', event.key, argsShape[currentArm])
                    elif pygame.K_DOWN == event.key:
                        argsShape[currentArm] -= 5
                        print('antihorario', event.key, argsShape[currentArm])



            
            # refresh
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            robot.body()
            robot.leftArm(argsShape['leftShoulder'], argsShape['leftElbow'], argsShape['leftHand'])
            robot.rightArm(argsShape['rightShoulder'], argsShape['rightElbow'], argsShape['rightHand'])

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    robot = rb.Robot()

    movement = {pygame.K_a: 'leftShoulder',  pygame.K_s: 'rightShoulder', pygame.K_n: 'leftElbow',
                 pygame.K_m: 'rightElbow', pygame.K_z: 'leftHand', pygame.K_x: 'rightHand'}
    
    myProject = Tela()