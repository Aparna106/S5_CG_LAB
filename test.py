from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys
import math

WS = 500
x = 0
y = 0

def Init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-WS, WS, -WS, WS)

def drawShape():
    glClearColor(GL_COLOR_BUFFER_BIT)
    glColor3f
    glBegin(GL_POLYGON)

    glEnd()
    glutSwapBuffers()

def animate(temp):

    glutTimerFunc(1000, animate, 0)
    glutPostRedisplay()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(WS, WS)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"Testing")
    glutDisplayFunc(drawShape)
    glutTimerFunc(0, animate, 0)
    Init()
    glutMainLoop()

main()