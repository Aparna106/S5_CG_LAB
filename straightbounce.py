from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys
import math

globalx = 0.0
globaly = 0.0
state = 0


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-500, 500, -500, 500)


def ball():
    glClear(GL_COLOR_BUFFER_BIT)
    x = 0.0
    global globalx
    global globaly
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(globalx, globaly)
    for i in range(0, 361, 1):
        glVertex2f(50 * math.cos(math.pi * i / 180) + x, 50 * math.sin(math.pi * i / 180) + globaly)
    glEnd()
    glutSwapBuffers()


def animate(temp):
    global globaly, state
    glutPostRedisplay()
    glutTimerFunc(int(1000 / 60), animate, 0)
    if state == 1:
        if globaly < 300:
            globaly += 1.5
        else:
            state = 0
    else:
        if globaly > 50:
            globaly -= 1.5
        else:
            state = 1


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("ball")
    glutDisplayFunc(ball)
    glutTimerFunc(0, animate, 0)
    init()
    glutMainLoop()


main()