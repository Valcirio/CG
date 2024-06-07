from OpenGL.GL import *

def displayDDA():
    glColor3f (0.0, 0.0, 0.0)
    # Desenhando os eixos
    # Definindo a espessura da linha
    glLineWidth(2.0)
    glBegin (GL_LINES)
    # Definindo a reta do eixo Y
    glVertex3i(0,0,0)
    glVertex3i(0,10,0)
    # Definindo a reta do eixo X
    glVertex3i(0,0,0)
    glVertex3i(10,0,0)
    glEnd()
    # Desenhando as pontas dos eixos
    glBegin(GL_TRIANGLES)
    # Triangulo do eixo Y
    glVertex3f(-0.2,10,0.0)
    glVertex3f(0.0,10.2,0.0)
    glVertex3f(0.2,10,0.0)
    #Triangulo do eixo X
    glVertex3f(10,0.2,0.0)
    glVertex3f(10,-0.2,0.0)
    glVertex3f(10.2,0.0,0.0)
    glEnd()
    # Desenhando os pontos (cor: vermelha)
    glColor3f(1.0,0.0,0.0)
    glPointSize(10.0)
    glBegin(GL_POINTS)
    glVertex3i(2,2,0)
    glEnd()
    glFlush() #Executa os comandos OpenGL para renderização