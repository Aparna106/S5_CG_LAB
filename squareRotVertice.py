from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math

WINDOW_SIZE = 500   # Global value of window size
x = 50.0   # Global origin x value
y = 50.0   # Global origin y value

def Init():   # Function called last in main()
    glClearColor(0.0, 0.0, 0.0, 0.0)   # background colour
    gluOrtho2D(-WINDOW_SIZE, WINDOW_SIZE, -WINDOW_SIZE, WINDOW_SIZE)   # Window size wrt to coord-axis

def drawShape():
    global x, y
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_QUADS)
    glVertex2f(x+50, y+50)
    glVertex2f(x+50, y-50)
    glVertex2f(x-50, y-50)
    glVertex2f(x-50, y+50)
    glEnd()
    glutSwapBuffers()


def animate(temp):
    glRotatef(-1,0,0,1)
    glutTimerFunc(10, animate, 0)
    glutPostRedisplay()

def main():
    glutInit(sys.argv)   # Initialize GLUT library
    glutInitDisplayMode(GLUT_RGB)   # Display Mode (GLUT_RGB)
    glutInitWindowSize(WINDOW_SIZE, WINDOW_SIZE)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Memorising Stuff")
    glutDisplayFunc(drawShape)
    glutTimerFunc(0, animate, 0)
    Init()   # Initializes screen
    glutMainLoop()

main()