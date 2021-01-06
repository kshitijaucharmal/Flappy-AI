import pygame

class Pipe:
	def __init__(self, ds, color, x, y, size=(40, 600)):
		self.ds = ds
		self.color = color
		self.x = x
		self.y = y
		self.velx = -0.2
		self.width = size[0]
		self.height = size[1]
		self.gap = 200
		self.destroyed = False
		self.bottom = 0
		self.top = 0
		pass

	def reset(self, ds, color, x, y, size=(40, 600)):
		self.__init__(ds, color, x, y, size)
		pass

	def hits(self, bird):
		if(bird.y - bird.size < self.top or bird.y + bird.size > self.bottom):
			if(bird.x - bird.size < self.x + self.width and bird.x + bird.size > self.x):
				self.color = (255, 0, 0)
				return True
			else:
				self.color = (255, 255, 255)
				return False

		else:
			self.color = (255, 255, 255)
			return False

	def draw(self):
		x1 = self.x
		y1 = self.y - self.height - int(self.gap/2)
		x2 = self.x
		y2 = self.y + int(self.gap/2)
		self.bottom = y2
		self.top = y2 - self.gap

		pygame.draw.rect(self.ds, self.color, (x1, y1, self.width, self.height))
		pygame.draw.rect(self.ds, self.color, (x2, y2, self.width, self.height))

	def update(self):
		self.x += self.velx
		if(self.x + self.width < 0):
			self.destroyed = True
		else:
			self.draw()