from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys
import math

WINDOW_SIZE = 500
GLOBAL_ANGLE = 45

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-WINDOW_SIZE, WINDOW_SIZE, -WINDOW_SIZE, WINDOW_SIZE)

def drawSquare():
    global GLOBAL_ANGLE
    glClear(GL_COLOR_BUFFER_BIT)
    x = 150*math.cos(math.pi*GLOBAL_ANGLE/180.0)
    y = 150*math.sin(math.pi*GLOBAL_ANGLE/180.0)

    glColor3f(0.0,0.0, 1.0)
    glBegin(GL_QUADS)
    glVertex2f(x, y)
    glVertex2f(y, -x)
    glVertex2f(-x,-y)
    glVertex2f(-y, x)
    glEnd()
    glutSwapBuffers()

def animate(temp):

    global GLOBAL_ANGLE

    if GLOBAL_ANGLE==360:
        GLOBAL_ANGLE=0
    else:
        GLOBAL_ANGLE-=1

    glutTimerFunc(10, animate, 0)
    glutPostRedisplay()


def main():
    glutInit(sys.argv)
    glutInitWindowSize(WINDOW_SIZE, WINDOW_SIZE)
    glutInitWindowPosition(0,0)
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("Draw Square")
    glutDisplayFunc(drawSquare)
    glutTimerFunc(0, animate, 0)
#   glutKeyboardFunc(keyboard)
    init()
    glutMainLoop()
main()