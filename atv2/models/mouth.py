from OpenGL.GL import *
import math

class Mouth:

    @staticmethod
    def Minecraft():
        glBegin(GL_POLYGON)
        glColor3f(1.0, 0.49, 0.32)
        glVertex2f(-0.2,-0.2)
        glVertex2f(-0.2,-0.3)
        glVertex2f(0.2,-0.3)
        glVertex2f(0.2,-0.2)
        glEnd()

    @staticmethod
    def Beto():
        segmentos = 100
        glBegin(GL_LINE_STRIP)
        for i in range(segmentos):
            theta = math.pi * i / segmentos
            x = 0.4 * math.cos(theta)
            y = 0.4 * math.sin(theta)
            glVertex2f(x, y)
        glEnd()

    @staticmethod
    def Shrek():
        segmentos = 100
        glBegin(GL_LINE_STRIP)
        for i in range(segmentos):
            theta = math.pi * i / segmentos
            x = 0.4 * math.cos(theta)
            y = 0.4 * math.sin(theta)
            glVertex2f(x, y)
        glEnd()