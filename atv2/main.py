import pygame
from OpenGL.GL import *
import math

from models.face import Faces
from models.eye import Eyes
from models.eyeBrow import EyeBrow
from models.hair import Hair
from models.nose import Nose
from models.mouth import Mouth

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
        #                 Rosto   Cabelo       Olho         Sombrancelha   Nariz       Boca   
        argsShape = [pygame.K_F1, pygame.K_F7, pygame.K_1,  pygame.K_a,    pygame.K_z, pygame.K_q]

        while running:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    print('evento', event.key)
                    if dictFace.get(event.key):
                        argsShape[0] = event.key
                    elif dictHair.get(event.key):
                        argsShape[1] = event.key
                    elif dictEye.get(event.key):
                        argsShape[2] = event.key
                    elif dictEyeBrow.get(event.key):
                        argsShape[3] = event.key
                    elif dictNose.get(event.key):
                        argsShape[4] = event.key
                    elif dictMouth.get(event.key):
                        argsShape[5] = event.key


            
            # refresh
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            dictFace[argsShape[0]]()
            dictHair[argsShape[1]]()
            dictEye[argsShape[2]]()
            dictEyeBrow[argsShape[3]]()
            dictNose[argsShape[4]]()
            dictMouth[argsShape[5]]()

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    face = Faces()
    hair= Hair()
    eye = Eyes()
    eyeBrow = EyeBrow()
    nose = Nose()
    mouth = Mouth()

    dictFace = {pygame.K_F1: face.Minecraft,  pygame.K_F2: face.Beto, pygame.K_F3: face.Shrek,
                 pygame.K_F4: face.Shrek, pygame.K_F5: face.Shrek, pygame.K_F6: face.Default}
    
    dictHair = {pygame.K_F7: hair.Minecraft,  pygame.K_F8: hair.Beto, pygame.K_F9: hair.Beto, 
                pygame.K_F10: hair.Beto, pygame.K_F11: hair.Beto, pygame.K_F12: hair.Beto}
    
    dictEye = {pygame.K_1: eye.Minecraft,  pygame.K_2: eye.Beto, pygame.K_3: eye.Shrek,
                pygame.K_4: eye.Shrek, pygame.K_5: eye.Shrek, pygame.K_6: eye.Default}
    
    dictEyeBrow = {pygame.K_a: eyeBrow.Minecraft,  pygame.K_s: eyeBrow.Beto, pygame.K_d: eyeBrow.Shrek, 
                   pygame.K_f: eyeBrow.Shrek, pygame.K_g: eyeBrow.Shrek, pygame.K_h: eyeBrow.Default}
    
    dictNose = {pygame.K_z: nose.Minecraft,  pygame.K_x: nose.Beto, pygame.K_c: nose.Shrek, 
                pygame.K_v: nose.Shrek, pygame.K_b: nose.Shrek, pygame.K_n: nose.Shrek}
    
    dictMouth = {pygame.K_q: mouth.Minecraft,  pygame.K_w: mouth.Beto, pygame.K_e: mouth.Shrek, }
    
    myProject = Tela()