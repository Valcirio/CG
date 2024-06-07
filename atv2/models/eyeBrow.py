from OpenGL.GL import *
import math

class EyeBrow:

    @staticmethod
    def Minecraft():
        glBegin(GL_QUADS)
        glColor3f(0.8, 0.48, 0.38)
        glVertex2f(-0.45,0.4)
        glVertex2f(-0.45,0.3)
        glVertex2f(0.45,0.3)
        glVertex2f(0.45,0.4)
        glEnd()

    @staticmethod
    def Beto():
        glBegin(GL_QUADS)
        glColor3f(0.098, 0.094, 0.082)
        glVertex2f(-0.45,0.4)
        glVertex2f(-0.45,0.3)
        glVertex2f(0.45,0.3)
        glVertex2f(0.45,0.4)
        glEnd()

    @staticmethod
    def Shrek():
        glBegin(GL_QUADS)
        glColor3f(0.098, 0.094, 0.082)
        glVertex2f(0.45,0.4)
        glVertex2f(0.45,0.3)
        glVertex2f(0.25,0.3)
        glVertex2f(0.25,0.4)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(0.098, 0.094, 0.082)
        glVertex2f(-0.45,0.4)
        glVertex2f(-0.45,0.3)
        glVertex2f(-0.25,0.3)
        glVertex2f(-0.25,0.4)
        glEnd()

    @staticmethod
    def Default():
        glBegin(GL_QUADS)
        glColor3f(0.098, 0.094, 0.082)
        glVertex2f(-0.45,0.4)
        glVertex2f(-0.45,0.3)
        glVertex2f(0.45,0.3)
        glVertex2f(0.45,0.4)
        glEnd()