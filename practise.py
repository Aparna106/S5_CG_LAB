from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

WS = 500
X = 0.0
Y = 0.0

def Init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-WS, WS, -WS, WS)

def drawShape():
    global X, Y
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_TRIANGLE_FANS)

