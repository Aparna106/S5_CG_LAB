from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

WINDOW_SIZE = 500
GLOBAL_Y = -180
FPS = 60


def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-WINDOW_SIZE, WINDOW_SIZE, -WINDOW_SIZE, WINDOW_SIZE)


def drawBucket():
    global GLOBAL_Y
    x = 0.0
    y = 0.0

    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glLineWidth(5)
    glBegin(GL_LINES)
    glVertex2f(x + 100, y)
    glVertex2f(x + 100, y - 200)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(x + 105, y - 200)
    glVertex2f(x - 105, y - 200)
    glEnd()

    glBegin(GL_LINES)
    glVertex2f(x - 100, y - 200)
    glVertex2f(x - 100, y)
    glEnd()

    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_QUADS)
    glVertex2f(x + 100, y - 200)
    glVertex2f(x - 100, y - 200)
    glVertex2f(x - 100, GLOBAL_Y)
    glVertex2f(x + 100, GLOBAL_Y)
    glEnd()
    glutSwapBuffers()


def animate(temp):
    global GLOBAL_Y

    glutPostRedisplay()
    glutTimerFunc(int(1000 / FPS), animate, int(0))
    if GLOBAL_Y == 0:
        GLOBAL_Y = (-200)
    else:
        GLOBAL_Y += 1


def main():
    glutInit(sys.argv)
    glutInitWindowSize(WINDOW_SIZE, WINDOW_SIZE)
    glutInitWindowPosition(0, 0)
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("Bucket getting filled with water")
    glutDisplayFunc(drawBucket)
    glutTimerFunc(0, animate, 0)
    init()
    glutMainLoop()


main()