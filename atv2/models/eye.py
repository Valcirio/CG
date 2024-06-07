from OpenGL.GL import *
import math

class Eyes:

    @staticmethod
    def Minecraft():

        # Globo Ocular
        glBegin(GL_QUADS)
        glColor3f(1.0, 1.0, 1.0)
        glVertex2f(-0.4,0.1)
        glVertex2f(-0.4,0.0)
        glVertex2f(-0.3,0.0)
        glVertex2f(-0.3,0.1)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(1.0, 1.0, 1.0)
        glVertex2f(0.4,0.1)
        glVertex2f(0.4,0.0)
        glVertex2f(0.3,0.0)
        glVertex2f(0.3,0.1)
        glEnd()
        
        # Íris
        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex2f(-0.3,0.1)
        glVertex2f(-0.3,0.0)
        glVertex2f(-0.2,0.0)
        glVertex2f(-0.2,0.1)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(0.0, 0.0, 0.0)
        glVertex2f(0.3,0.1)
        glVertex2f(0.3,0.0)
        glVertex2f(0.2,0.0)
        glVertex2f(0.2,0.1)
        glEnd()

    @staticmethod
    def Beto():
        segmentos = 50

        glBegin(GL_POLYGON)
        glColor3f(1.0, 1.0, 1.0)
        for i in range(segmentos):
            theta = (2.0 * 3.14 * i )/ segmentos
            x = 0.12 * math.cos(theta)
            y = 0.12 * math.sin(theta)
            glVertex2f(x - 0.2, y + 0)
        glEnd()

        glBegin(GL_POLYGON)
        glColor3f(1.0, 1.0, 1.0)
        for i in range(segmentos):
            theta = (2.0 * 3.14 * i )/ segmentos
            x = 0.12 * math.cos(theta)
            y = 0.12 * math.sin(theta)
            glVertex2f(x + 0.2, y + 0)
        glEnd()

        #Íris
        glBegin(GL_POLYGON)
        glColor3f(0.098, 0.094, 0.082)
        for i in range(segmentos):
            theta = (2.0 * 3.14 * i )/ segmentos
            x = 0.06 * math.cos(theta)
            y = 0.06 * math.sin(theta)
            glVertex2f(x - 0.15, y + 0)
        glEnd()

        glBegin(GL_POLYGON)
        glColor3f(0.098, 0.094, 0.082)
        for i in range(segmentos):
            theta = (2.0 * 3.14 * i )/ segmentos
            x = 0.06 * math.cos(theta)
            y = 0.06 * math.sin(theta)
            glVertex2f(x + 0.15, y + 0)
        glEnd()

    @staticmethod
    def Shrek():

        segmentos = 50

        glBegin(GL_POLYGON)
        glColor3f(1.0, 1.0, 1.0)
        for i in range(segmentos):
            theta = (2.0 * 3.14 * i )/ segmentos
            x = 0.12 * math.cos(theta)
            y = 0.12 * math.sin(theta)
            glVertex2f(x - 0.2, y + 0)
        glEnd()

        glBegin(GL_POLYGON)
        glColor3f(1.0, 1.0, 1.0)
        for i in range(segmentos):
            theta = (2.0 * 3.14 * i )/ segmentos
            x = 0.12 * math.cos(theta)
            y = 0.12 * math.sin(theta)
            glVertex2f(x + 0.2, y + 0)
        glEnd()

        glBegin(GL_POLYGON)
        glColor3f(0.0, 0.0, 0.0)
        for i in range(segmentos):
            theta = (2.0 * 3.14 * i )/ segmentos
            x = 0.06 * math.cos(theta)
            y = 0.06 * math.sin(theta)
            glVertex2f(x - 0.15, y + 0)
        glEnd()

        glBegin(GL_POLYGON)
        glColor3f(0.0, 0.0, 0.0)
        for i in range(segmentos):
            theta = (2.0 * 3.14 * i )/ segmentos
            x = 0.06 * math.cos(theta)
            y = 0.06 * math.sin(theta)
            glVertex2f(x + 0.15, y + 0)
        glEnd()

    @staticmethod
    def Default():
        segmentos = 50
        glBegin(GL_POLYGON)
        glColor3f(0.0, 0.0, 0.0)
        for i in range(segmentos):
            theta = (2.0 * 3.14 * i )/ segmentos
            x = 0.06 * math.cos(theta)
            y = 0.06 * math.sin(theta)
            glVertex2f(x - 0.18, y + 0)
        glEnd()

        glBegin(GL_POLYGON)
        glColor3f(0.0, 0.0, 0.0)
        for i in range(segmentos):
            theta = (2.0 * 3.14 * i )/ segmentos
            x = 0.06 * math.cos(theta)
            y = 0.06 * math.sin(theta)
            glVertex2f(x + 0.18, y + 0)
        glEnd()
