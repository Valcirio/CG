from OpenGL.GL import *
import math

class Nose:
   
    @staticmethod 
    def Minecraft():
        glBegin(GL_QUADS)
        glColor3f(0.73, 0.43, 0.32)
        glVertex2f(-0.2,0.0)
        glVertex2f(-0.2,-0.1)
        glVertex2f(0.2,-0.1)
        glVertex2f(0.2,0.0)
        glEnd()

    @staticmethod
    def Beto():
        segmentos = 100
        glBegin(GL_POLYGON)
        glColor3f(0.69, 0.76, 0.11)
        for i in range(segmentos):
            theta = (2.0*3.14*i)/ segmentos
            x = 0.3 * math.cos(theta)
            y = 0.35 * math.sin(theta)
            glVertex2f(x + 0, y + 0)
        glEnd()

    @staticmethod
    def Shrek():
        segmentos = 100
        glBegin(GL_POLYGON)
        glColor3f(0.69, 0.76, 0.11)
        for i in range(segmentos):
            theta = (2.0*3.14*i)/ segmentos
            x = 0.3 * math.cos(theta)
            y = 0.35 * math.sin(theta)
            glVertex2f(x + 0, y + 0)
        glEnd()