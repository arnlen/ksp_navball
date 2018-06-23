from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from PIL import Image
import numpy
import math

class NavBall:
    def __init__(self):
        self.texture_id = 0
        self.angle = 0

    def run_scene(self):
        glutInit()
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowSize(400, 400)
        glutCreateWindow(b'Minimal sphere OpenGL')
        self.lightning()
        self.texture_id = self.read_texture('navball.png')
        glutDisplayFunc(self.draw_sphere)
        glMatrixMode(GL_PROJECTION)
        gluPerspective(40, 1, 1, 40)
        glutMainLoop()

    def lightning(self):
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glEnable(GL_BLEND)
        glLightfv(GL_LIGHT0, GL_POSITION, [10, 4, 10, 1])
        glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.8, 1, 0.8, 1])
        glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
        glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
        glEnable(GL_LIGHT0)
        return

    def read_texture(self, filename):
        img = Image.open(filename)
        img_data = numpy.array(list(img.getdata()), numpy.int8)
        texture_id = glGenTextures(1)
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.size[0], img.size[1], 0,
                     GL_RGB, GL_UNSIGNED_BYTE, img_data)
        return texture_id

    def draw_sphere(self):
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(math.cos(self.angle)*4, math.sin(self.angle)*4, 0, 0, 0, 0, 0, 0, 1)
        self.angle = self.angle+0.04
        glEnable(GL_DEPTH_TEST)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glBindTexture(GL_TEXTURE_2D, self.texture_id)

        glEnable(GL_TEXTURE_2D)

        qobj = gluNewQuadric()
        gluQuadricTexture(qobj, GL_TRUE)
        gluSphere(qobj, 1, 50, 50)
        gluDeleteQuadric(qobj)

        glDisable(GL_TEXTURE_2D)

        glutSwapBuffers()
        glutPostRedisplay()