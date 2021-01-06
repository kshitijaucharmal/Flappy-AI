import pygame
import numpy as np

class Bird:
	def __init__(self, ds, color, x, y, size=20):
		self.ds = ds
		self.color = color
		self.size = size
		self.jumpForce = 0.6
		self.x = x
		self.y = y
		self.accy = 0.00298
		self.vely = 0.2 # gravity
		self.dead = False
		pass

	def reset(self, ds, color, x, y, size=20):
		self.__init__(ds, color, x, y, size)
		pass

	def draw(self):
		pygame.draw.circle(self.ds, self.color, (self.x, self.y), self.size)

	def update(self):
		if self.y > 600 or self.y < 0:
			self.color = (255, 0, 0)
			self.dead = True
			return
		self.vely += self.accy
		self.y += self.vely

	def jump(self):
		self.vely = -1 * self.jumpForce

	pass