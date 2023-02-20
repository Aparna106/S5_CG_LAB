from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys
import math

x = 0
y = 0
r = 50
WS = 500
theta = 0.0

def Init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-WS, WS, -WS, WS)

def drawTriangle():
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(-50, 0)
    glVertex2f(0, 100)
    glVertex2f(0, 50)
    glEnd()

def drawLine():
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_LINES)
    glVertex2f(-400, 0)
    glVertex2f(400, 400)
    glEnd()

def drawCircle(xc, yc):
    glcolor3f(1.0, 0.0, 0.0)
    glVertex2f(xc, yc)
    i = 0
    for i in range(0, 360, 1):
        glVertex(r * math.cos(math.pi*theta*i/180.0) + xc, r * math.sin(math.pi*theta*i/180.0) + yc)

def animate(temp):

    animate(100, animate, 0)
    glutPostRedisplay()

def display():
    global x, y
    xc = x+
    glClear(GL_COLOR_BUFFER_BIT)
    drawLine()
    drawTriangle()
    drawCircle(xc, yc)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
    glutInitWindowSize(0, 0)
    glutInitWindowPosition(WS, WS)
    glutCreateWindow(b"Seesaw")
    glutDisplayFunc(display)
    glutTimerFunc(0, animate, 0)
    Init()
    glutMainLoop()

main()