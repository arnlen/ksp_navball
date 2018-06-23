from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
from PIL import Image as Image
import numpy
from sphere import Sphere
from time import sleep

class SceneController():
	"""Main entry point"""

	def __init__(self):
		self.display = (800, 800)
		self.window_name = "Navball"

		self._init_glut()
		self._configure_gl()
		self._init_sphere()

		glutMainLoop()

	def draw_scene(self):
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		self.draw_sphere()
		glutSwapBuffers()

	def draw_sphere(self):
		self.sphere.create()
		glRotatef(1, 3, 1, 1)
		sleep(0.01)
		glutPostRedisplay()

	def _init_glut(self):
		glutInit(sys.argv)
		glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
		glutCreateWindow(self.window_name)

		gluPerspective(40, (self.display[0]/self.display[1]), 0.1, 50.0)
		gluLookAt(0, 0, 3,
				  0, 0, 0,
				  0, 1, 0)

		glutDisplayFunc(self.draw_scene)

	def _configure_gl(self):
		glClearColor(0., 0., 0., 1.)
		glEnable(GL_CULL_FACE)
		glEnable(GL_DEPTH_TEST)

	def _init_sphere(self):
		self.sphere = Sphere('navball2.png')