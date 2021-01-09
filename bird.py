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

		inputs = np.random.rand(4)

		output = self.brain.query(inputs).T[0][0]
		if(np.random.random() < 0.005):
			self.jump()

	def jump(self):
		self.vely = -1 * self.jumpForce

	pass