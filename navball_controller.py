from OpenGL.GL import *
from time import sleep

class NavBallController():
	"""Control the NavBall rotation"""
	def __init__(self):
		print("Navball controller")
		self.sleep_time = 0.01
		self.heading = (0, 0)

	def rotate(self, angle, x, y, z):
		glRotatef(angle, x, y, z)
		self.print_heading()
		self._sleep()

	def print_heading(self):
		print(self.heading)

	def _sleep(self):
		sleep(self.sleep_time)