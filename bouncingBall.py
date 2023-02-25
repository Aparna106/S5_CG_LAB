from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys
import math

r, x, y = 10, -90, 10
WS = 100
state = 1


def glClearScreen():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-WS, WS, -WS, WS)


def drawSphere(R, xc, yc):
    glColor3f(0.0, 1.0, 1.0)
    glVertex2f(xc, yc)
    i = 0
    glBegin(GL_TRIANGLE_FAN)
    for i in range(0, 361, 1):
        glVertex2f(R * math.cos(math.pi * i / 180) + xc, R * math.sin(math.pi * i / 180) + yc)
    glEnd()
    glFlush()


def animate(temp):
    global x, y, r, state
    glutPostRedisplay()
    glutTimerFunc(int(1000 / 60), animate, 0)
    if state == 1:
        if y < 70:
            y += 1.5
            x += 0.5
        else:
            state = 0
    else:
        if y > 10:
            y -= 1.5
            x += 0.5
        else:
            state = 1


def drawLine():
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_LINES)
    glVertex2f(-100, 0)
    glVertex2f(100, 0)
    glEnd()


def display():
    global r, x, y
    glClear(GL_COLOR_BUFFER_BIT)
    drawSphere(r, x, y)
    drawLine()
    glutSwapBuffers()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
    glutInitWindowPosition(0, 0)
    glutInitWindowSize(768, 768)
    glutCreateWindow("Bouncing ball")
    glutDisplayFunc(display)
    glutTimerFunc(0, animate, 0)
    glClearScreen()
    glutMainLoop()


main()