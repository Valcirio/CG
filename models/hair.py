from OpenGL.GL import *
import math

class Hair:

    @staticmethod
    def Minecraft():
        glBegin(GL_QUAD_STRIP)
        glColor3f(0.39, 0.26, 0.21)
        glVertex2f(-0.5,0.5)
        glVertex2f(0.5,0.5)
        glVertex2f(0.5,0.45)
        glVertex2f(-0.45,0.45)

        glVertex2f(0.5,0.45)
        glVertex2f(0.5,0.25)
        glVertex2f(0.45,0.25)
        glVertex2f(0.45,0.45)

        glVertex2f(-0.5,0.45)
        glVertex2f(-0.5,0.25)
        glVertex2f(-0.45,0.25)
        glVertex2f(-0.45,0.45)
        glEnd()

    @staticmethod
    def Beto():
        glBegin(GL_POLYGON)
        glColor3f(0.39, 0.26, 0.21)
        glVertex2f(-0.5,-0.5)

        glEnd()