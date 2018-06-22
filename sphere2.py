from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
from PIL import Image as Image
import numpy

name = 'Navball'

def main():
	display = (800, 800)
	angle = 0

	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
	glutCreateWindow(name)

	glClearColor(0., 0., 0., 1.)
	glShadeModel(GL_SMOOTH)

	# glEnable(GL_CULL_FACE)
	# glEnable(GL_DEPTH_TEST)
	glEnable(GL_LIGHTING)

	# lightZeroPosition = [10., 4., 10., 1.]
	# lightZeroColor = [0.8, 1.0, 0.8, 1.0]

	# glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
	# glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
	# glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
	# glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
	# glEnable(GL_LIGHT0)

	# glMatrixMode(GL_PROJECTION)
	gluPerspective(40, (display[0]/display[1]), 0.1, 50.0)

	# glMatrixMode(GL_MODELVIEW)
	gluLookAt(0, 0, 3,
			  0, 0, 0,
			  0, 1, 0)

	# glPushMatrix()

	# Glut callbacks
	glutDisplayFunc(display_scene)
	glutTimerFunc(100, loop, 1)

	glutMainLoop()

def display_scene():
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

	sphere()

	glPopMatrix()
	glutSwapBuffers()

	glutTimerFunc(100, loop, 1)

	return

def sphere():
	glPushMatrix()

	tex = read_texture('navball2.png')
	qobj = gluNewQuadric()
	gluQuadricTexture(qobj, GL_TRUE)
	glEnable(GL_TEXTURE_2D)

	gluSphere(qobj, 1, 50, 50)
	gluDeleteQuadric(qobj)
	glDisable(GL_TEXTURE_2D)

def loop(angle):
	glRotatef(1, 3, 1, 1)
	display_scene()

	return

def read_texture(filename):
	img = Image.open(filename)
	img_data = numpy.array(list(img.getdata()), numpy.int8)
	textID = glGenTextures(1)
	glBindTexture(GL_TEXTURE_2D, textID)

	glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
	glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

	glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
	glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.size[0], img.size[1], 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)

	return textID

main()