from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-300, 300, -300, 300)

def main():
    glutInit()
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("haha")
    glutDisplayFunc(init)
    glutMainLoop()
main()