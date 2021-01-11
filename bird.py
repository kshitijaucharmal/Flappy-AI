import pygame
import numpy as np
from nn import NeuralNet
import random as rd

class Bird:
	def __init__(self, ds, color, x, y, size=20):
		self.ds = ds
		self.color = color
		self.color = (rd.randint(0, 255), rd.randint(0, 255), rd.randint(0, 255))
		self.size = size
		self.jumpForce = 0.6
		self.x = x
		self.y = y
		self.accy = 0.00298
		self.vely = 0.2 # gravity
		self.dead = False
		self.brain = NeuralNet(4, 4, 1, 0.3);
		pass

	def reset(self, ds, color, x, y, size=20):
		self.__init__(ds, color, x, y, size)
		pass

	def draw(self):
		pygame.draw.circle(self.ds, self.color, (self.x, self.y), self.size, 3)

	def update(self):
		if self.y > 600 or self.y < 0:
			self.color = (255, 0, 0)
			self.dead = True
			return
		self.vely += self.accy
		self.y += self.vely

	def think(self, pipes):

		# Find the closest pipe
		closest = None
		closestD = 1000000
		for i in range(len(pipes)):
			d = pipes[i].x - self.x
			if d < closestD and d > 0:
				closest = pipes[i]
				closestD = d

		inputs = []
		inputs.append(self.y / 600)
		inputs.append(closest.top / 600)
		inputs.append(closest.bottom / 600)
		inputs.append(closest.x / 350)

		output = self.brain.query(inputs).T[0][0]
		if(output < 0.5):
			self.jump()

	def jump(self):
		self.vely = -1 * self.jumpForce

	pass