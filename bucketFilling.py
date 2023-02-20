from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys
import math

x = 0
y = 0

def Init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-500, 500, -500, 500)

def bucket():
    global x, y
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(5)

    glBegin(GL_QUADS)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2i(x, y)
    glVertex2i(x + 100, y)
    glVertex2i(x + 100, y + 200)
    glVertex2i(x, y + 200)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2i(x + 100, y)
    glVertex2i(x + 200, y)
    glVertex2i(x + 200, y + 50)
    glVertex2i(x + 100, y + 50)
    glEnd()

    glBegin(GL_QUADS)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2i(x + 200, y)
    glVertex2i(x + 300, y)
    glVertex2i(x + 300, y + 200)
    glVertex2i(x + 200, y + 200)
    glEnd()
    glFlush()

def animate(temp):

    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_QUADS)
    glVertex2f(x+100, y)
    glVertex2f(x+200, y)
    glVertex2f(x+200, y+50)
    glVertex2f(x+100, y+50)
    glEnd()
    glutTimerFunc(100, animate, 1)
    glutPostRedisplay()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("Bucket")
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutDisplayFunc(bucket)
    glutIdleFunc(bucket)
    glutTimerFunc(0, animate, 0)
    Init()
    glutMainLoop()


main()