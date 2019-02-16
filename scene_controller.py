from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
from PIL import Image as Image
import numpy
from navball import NavBall
from navball_controller import NavBallController

class SceneController():
	"""Main entry point"""

	def __init__(self):
		self.display = (800, 800)
		self.window_name = "Navball"
		self.navball_controller = NavBallController()

		self._init_glut()
		self._configure_gl()
		self._init_navball()

		glutMainLoop()

	def draw_scene(self):
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		self.draw_navball()
		glutSwapBuffers()

	def draw_navball(self):
		self.navball.create()
		self.navball_controller.rotate(1, 1, 1, 1)
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

	def _init_navball(self):
		self.navball = NavBall('images/navball4.jpg')
		self.navball.create()
		glRotatef(90, 0, 1, 0)
		glRotatef(180, 0, 0, 1)
		glRotatef(-10, 0, 1, 0)
		glPushMatrix()

		# TEST 1
		# KSP: 0.865,291.193,0.14

		# TEST 2
		# KSP: 352.605,159.433,296.727
		# x = 352.605x
		# x2 = -x
		# y = 159.433
		# y2 = 360 - y
		# z = 296.727
		# z2 = 360 - z
		# glRotatef(x, 1, 0, 0)
		# glRotatef(z, 0, 1, 0)
		# glRotatef(y, 0, 0, 1)