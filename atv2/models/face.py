from OpenGL.GL import *
import math

class Faces:

    @staticmethod
    def Minecraft():
        glBegin(GL_QUADS)
        glColor3f(0.8, 0.48, 0.38)
        glVertex2f(-0.5,-0.5)
        glVertex2f(0.5,-0.5)
        glVertex2f(0.5,0.5)
        glVertex2f(-0.5,0.5)
        glEnd()

    @staticmethod
    def Shrek():
        segmentos = 100
        glBegin(GL_POLYGON)
        glColor3f(0.69, 0.76, 0.11)
        for i in range(segmentos):
            theta = (2.0*3.14*i)/ segmentos
            x = 0.5 * math.cos(theta)
            y = 0.56 * math.sin(theta)
            glVertex2f(x + 0, y + 0)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(0.69, 0.76, 0.11)
        glVertex2f(-0.45,-0.05)
        glVertex2f(-0.45,0.05)
        glVertex2f(-0.6,0.05)
        glVertex2f(-0.6,-0.05)
        glEnd()
        glBegin(GL_QUADS)
        glColor3f(0.69, 0.76, 0.11)
        glVertex2f(0.45,-0.05)
        glVertex2f(0.45,0.05)
        glVertex2f(0.6,0.05)
        glVertex2f(0.6,-0.05)
        glEnd()
        glBegin(GL_QUADS)
        glColor3f(0.69, 0.76, 0.11)
        glVertex2f(-0.6,-0.08)
        glVertex2f(-0.6,0.08)
        glVertex2f(-0.65,0.08)
        glVertex2f(-0.65,-0.08)
        glEnd()
        glBegin(GL_QUADS)
        glColor3f(0.69, 0.76, 0.11)
        glVertex2f(0.6,-0.08)
        glVertex2f(0.6,0.08)
        glVertex2f(0.65,0.08)
        glVertex2f(0.65,-0.08)
        glEnd()

    @staticmethod
    def Beto():
        segmentos = 100

        # Ouvidos
        glBegin(GL_POLYGON)
        glColor3f(0.74, 0.53, 0.11)
        for i in range(segmentos):
            theta = (2.0 * 3.14 * i )/ segmentos
            x = 0.13 * math.cos(theta)
            y = 0.13 * math.sin(theta)
            glVertex2f(x + 0.5, y + 0)
        glEnd()

        glBegin(GL_POLYGON)
        glColor3f(0.74, 0.53, 0.11)
        for i in range(segmentos):
            theta = (2.0 * 3.14 * i )/ segmentos
            x = 0.13 * math.cos(theta)
            y = 0.13 * math.sin(theta)
            glVertex2f(x - 0.5, y + 0)
        glEnd()

        # Cabeça
        glBegin(GL_POLYGON)
        glColor3f(0.94, 0.75, 0.32)
        for i in range(segmentos):
            theta = (2.0 * 3.14 * i )/ segmentos
            x = 0.5 * math.cos(theta)
            y = 0.7 * math.sin(theta)
            glVertex2f(x, y)
        glEnd()

    @staticmethod
    def Lua():
        segmentos = 100
        glBegin(GL_POLYGON)
        glColor3f(0.87, 0.68, 0.21)
        for i in range(segmentos):
            theta = (2.0 * 3.14 * i) / segmentos
            x = 0.5 * math.cos(theta)
            y = 0.5 * math.sin(theta)
            glVertex2f(x + 0, y + 0)

        glEnd()

    @staticmethod
    def Default():
        segmentos = 100
        glBegin(GL_POLYGON)
        glColor3f(0.87, 0.81, 0.74)
        for i in range(segmentos):
                theta = (2.0 * 3.14 * i) / segmentos
                x = 0.5 * math.cos(theta)
                y = 0.6 * math.sin(theta)
                glVertex2f(x + 0, y + 0)

        glEnd()

