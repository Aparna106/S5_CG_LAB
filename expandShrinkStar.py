from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys
import math

WINDOW_SIZE = 500
GLOBAL_R= 50
mode = 0

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-WINDOW_SIZE, WINDOW_SIZE, -WINDOW_SIZE, WINDOW_SIZE)

def drawStar():
    global GLOBAL_R
    glClear(GL_COLOR_BUFFER_BIT)

    x1 = GLOBAL_R*math.cos(math.pi*90/180)
    y1 = GLOBAL_R*math.sin(math.pi*90/180)
    x2 = GLOBAL_R*math.cos(math.pi*210/180)
    y2 = GLOBAL_R*math.sin(math.pi*210/180)
    x3 = GLOBAL_R*math.cos(math.pi*330/180)
    y3 = GLOBAL_R*math.sin(math.pi*330/180)

    glColor3f(0.0,0.0, 1.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glVertex2f(x3, y3)
    glEnd()

    xc1 = GLOBAL_R * math.cos(math.pi * 270 / 180.0)
    yc1 = GLOBAL_R * math.sin(math.pi * 270 / 180.0)
    xc2 = GLOBAL_R * math.cos(math.pi * (270 + 120) / 180.0)
    yc2 = GLOBAL_R * math.sin(math.pi * (270 + 120) / 180.0)
    xc3 = GLOBAL_R * math.cos(math.pi * (270 + 120 + 120) / 180.0)
    yc3 = GLOBAL_R * math.sin(math.pi * (270 + 120 + 120) / 180.0)

    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(xc1, yc1)
    glVertex2f(xc2, yc2)
    glVertex2f(xc3, yc3)
    glEnd()
    glutSwapBuffers()

def animate(temp):
    global mode

    global GLOBAL_R

    if GLOBAL_R == 0:
        mode = 0
    elif(GLOBAL_R == 350):
        mode = 1

    if mode == 0:
        GLOBAL_R+=1
    elif mode == 1:
        GLOBAL_R-=1

    glutTimerFunc(10, animate, 0)
    glutPostRedisplay()


def main():
    glutInit(sys.argv)
    glutInitWindowSize(WINDOW_SIZE, WINDOW_SIZE)
    glutInitWindowPosition(0,0)
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("Draw Star")
    glutDisplayFunc(drawStar)
    glutTimerFunc(0, animate, 0)
#   glutKeyboardFunc(keyboard)
    init()
    glutMainLoop()
main()