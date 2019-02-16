from numpy import matrix
from math import *

class CoordinateConvertor():
	"""Conversion of Left-Handed Coordinates to Right-Handed Coordinates"""
	def __init__(self, angle):
		self.heading = heading_matrix_for(angle)
		# 
		# STOOOOOOOOPED BY MY WIFE!!!! HERE
		# 

	def heading_matrix_for(self, angle):
		matrix([[cos(angle),	0,	sin(angle)],
				[0,				1,	0],
				[-sin(angle),	0,	cos(angle)]])

	def pitch_matrix_for(self, angle):
		matrix([[1,		0,			0],
				[0,		cos(angle),	-sin(angle)],
				[0,		sin(angle),	cos(angle)]])

	def bank_matrix_for(self, angle):
		matrix([[cos(angle),	-sin(angle),	0],
				[sin(angle),	cos(angle),		0],
				[0,				0,				1]])