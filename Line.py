from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    gluOrtho2D(300, -300, 300, -300)


def plotline(x1, x2, y1, y2):
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)
    glPointSize(5)
    glBegin(GL_LINES)
    glVertex2i(x1, y1)
    glVertex2i(x2, y2)
    glEnd()
    glFlush()

def main():
    glutInit(sys.argv)
    print("Enter the values")
    x1 = int(input("Enter the value of x1: "))
    y1 = int(input("Enter the value of y1: "))
    x2 = int(input("Enter the value of x2: "))
    y2 = int(input("Enter the value of y2: "))
    glutInitDisplayMode(GLUT_RGB)
    glutCreateWindow("Line")
    glutInitWindowSize(300, 300)
    glutInitWindowPosition(0, 0)
    glutDisplayFunc(lambda: plotline(x1, y1, x2, y2))
    glutIdleFunc(lambda: plotline(x1, y1, x2, y2))
    init()
    glutMainLoop()

main()