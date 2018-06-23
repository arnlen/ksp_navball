from OpenGL.GLU import *
from OpenGL.GL import *
from PIL import Image as Image
import numpy

class NavBall():
	"""Sphere object, base of the Navball"""
	def __init__(self, texture_path):
		self.texture_path = texture_path
		self._read_texture_file()
		self._create_quadric_object()

	def create(self):
		gluSphere(self.sphere, 1, 50, 50)

	def _read_texture_file(self):
		img = Image.open(self.texture_path)
		img_data = numpy.array(list(img.getdata()), numpy.int8)
		texture_id = glGenTextures(1)

		glEnable(GL_TEXTURE_2D)
		glBindTexture(GL_TEXTURE_2D, texture_id)
		glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
		glTexImage2D(GL_TEXTURE_2D,
					 0,
					 GL_RGB,
					 img.size[0],
					 img.size[1],
					 0,
					 GL_RGB,
					 GL_UNSIGNED_BYTE,
					 img_data)

	def _create_quadric_object(self):
		self.sphere = gluNewQuadric()
		gluQuadricTexture(self.sphere, GL_TRUE)