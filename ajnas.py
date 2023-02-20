from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

x = 0
y = 0

angle = 0


def init():
    glClearColor(0, 0, 0, 0)
    gluOrtho2D(-1000, 1000, -1000, 1000)

    # elipse


# planets
def planets(r1, r2):
    global x, y
    glColor(0, 0, 1)
    x = r1 * math.cos(angle)
    y = r2 * math.sin(angle)
    glBegin(GL_TRIANGLE_FAN)

    for i in range(0, 361, 1):
        glVertex2f(50 * math.cos(math.pi * (i / 180)) + x, 50 * math.sin(math.pi * (i / 180)) + y)

    glEnd()
    glFlush()


def ellipse(r1, r2):
    glBegin(GL_POINTS)
    glColor(0, 1, 1)
    glVertex2f(0, 0)
    for i in range(0, 361):
        glVertex2f(r1 * math.cos(i), r2 * math.sin(i))
        i += .05
    glEnd()


def sun():
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1, 1, 0)
    glVertex2f(0, 0)
    for i in range(0, 361, 1):
        glVertex2f(100 * math.cos(math.pi * (i / 180)), 100 * math.sin(math.pi * (i / 180)))
    glEnd()

    # planet


def solar():
    global x, y
    glClear(GL_COLOR_BUFFER_BIT)

    sun()
    ellipse(200, 100)

    ellipse(400, 200)
    ellipse(600, 300)
    planets(200, 100)

    planets(400, 200)
    planets(600, 300)
    glutSwapBuffers()


def animate(value):
    global x, y, angle
    glutPostRedisplay()
    glutTimerFunc(int(5000 / 60), animate, int(0))
    x = 80 * math.cos(angle)
    y = 40 * math.sin(angle)
    angle = angle + 0.1


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(1000, 1000)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Solar")
    glutDisplayFunc(solar)
    glutTimerFunc(0, animate, 0)
    init()
    glutMainLoop()


main()