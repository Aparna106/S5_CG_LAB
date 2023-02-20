from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

WINDOW_SIZE = 500
GLOBAL_X = 0.0
GLOBAL_Y = 0.0
GLOBAL_ANGLES = 90
GLOBAL_ANGLEM = 90


def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-WINDOW_SIZE, WINDOW_SIZE, -WINDOW_SIZE, WINDOW_SIZE)
    glPointSize(2)


def drawHand(x, y, s):
    global GLOBAL_ANGLES
    global GLOBAL_ANGLEM
    if s == 0:   #Minute hand
        y = 0
        x = 0
        x1 = 200 * math.cos(math.pi * GLOBAL_ANGLEM / 180.0) + x
        y1 = 200 * math.sin(math.pi * GLOBAL_ANGLEM/ 180.0) + y
        glColor3f(0.0, 0.0, 0.0)
        glBegin(GL_LINES)
        glVertex2f(x, y)
        glVertex2f(x1, y1)
        glEnd()

    else:   #Second Hand
        y = y
        x = x
        x2 = 150 * math.cos(math.pi * GLOBAL_ANGLES / 180.0) + x
        y2 = 150 * math.sin(math.pi * GLOBAL_ANGLES / 180.0) + y
        glColor3f(0.0, 0.0, 0.0)
        glBegin(GL_LINES)
        glVertex2f(x, y)
        glVertex2f(x2, y2)
        glEnd()



def drawCircle(x, y):
    i=0.0
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, y)
    for i in range(0, 361, 1):
        glVertex2f(200 * math.cos(math.pi * i / 180.0) + x, 200 * math.sin(math.pi * i / 180.0) + y)
    glEnd()


def drawClock():
    global GLOBAL_X
    global GLOBAL_Y
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 1.0, 0.0)
    drawCircle(GLOBAL_X, GLOBAL_Y)
    drawHand(GLOBAL_X, GLOBAL_Y, 0)
    drawHand(GLOBAL_X, GLOBAL_Y, 1)
    glutSwapBuffers()


def animate(key):
    global WINDOW_SIZE
    global GLOBAL_X
    global GLOBAL_Y
    global GLOBAL_ANGLES
    global GLOBAL_ANGLEM

    if key == 'd':
        if GLOBAL_ANGLES == 0:
            if GLOBAL_ANGLEM == 0:
                GLOBAL_ANGLEM == 360
            else:
                GLOBAL_ANGLEM-=6
            GLOBAL_ANGLES = 360
        else:
            GLOBAL_ANGLES -= 6

#    elif key == 'd':
#       if (GLOBAL_X + 100 < WINDOW_SIZE):
#
#            GLOBAL_X = GLOBAL_X + value
#            if GLOBAL_ANGLE == 360:
#                GLOBAL_ANGLE = 0
#            else:
#                GLOBAL_ANGLE = GLOBAL_ANGLE - 10
#        else:
#            GLOBAL_X = -400

    glutPostRedisplay()


def keyboard(key, x, y):
    key = key.decode()
    if key == 'd':
        animate('d')
    elif key == 'z':
        glutLeaveMainLoop()
    elif key == 'f':
        glutFullScreen()


def main():
    glutInit(sys.argv)
    glutInitWindowSize(WINDOW_SIZE, WINDOW_SIZE)
    glutInitWindowPosition(0, 0)
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("Clock")
    glutDisplayFunc(drawClock)
    glutKeyboardFunc(keyboard)
    init()
    glutMainLoop()
main()