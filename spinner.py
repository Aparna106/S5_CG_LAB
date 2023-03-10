from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

WINDOW_SIZE = 500
x = 0
y = 0

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(-WINDOW_SIZE, WINDOW_SIZE, -WINDOW_SIZE, WINDOW_SIZE)

def drawShape():
    global x, y
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_QUADS)
    glVertex2f(x+5, y)
    glVertex2f(x+5, y-100)
    glVertex2f(x-5, y-100)
    glVertex2f(x-5, y)
    glEnd()
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_TRIANGLES)
    glVertex2f(x+50, y-100)
    glVertex2f(5, y-200)
    glVertex2f(x-50,y-100)
    glEnd()
    glutSwapBuffers()


def animate(temp):
    glRotatef(-1,0,0,1)
    glutTimerFunc(10, animate, 0)
    glutPostRedisplay()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(WINDOW_SIZE, WINDOW_SIZE)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Spinning Top")
    glutDisplayFunc(drawShape)
    glutTimerFunc(0, animate, 0)
    init()
    glutMainLoop()
main()