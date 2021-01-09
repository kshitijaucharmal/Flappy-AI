import pygame, sys
from pygame.locals import *
from bird import Bird
from pipe import Pipe
from nn import NeuralNet
import random

WIDTH = 350
HEIGHT = 600
FPS = 600
PIPE_GAP = 300
START_TIME = 500
score = 0
MAX_POP = 50

# colors  r    g    b
WHITE =  (255, 255, 255)
BLACK =  (0,   0,   0  )
RED =    (255, 0,   0  )

ds = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy")
clock = pygame.time.Clock()

birds = []
bird = Bird(ds, WHITE, int(WIDTH/3), int(HEIGHT/4))
pipes = []

def setup():
	for i in range(MAX_POP):
		birds.append(Bird(ds, WHITE, int(WIDTH/3), int(HEIGHT/4)))
	pipes.append(Pipe(ds, WHITE, START_TIME + int(3 * WIDTH/4), int(HEIGHT/2)))
	pipes.append(Pipe(ds, WHITE, START_TIME + int(3 * WIDTH/4) + PIPE_GAP, random.randint(0, HEIGHT)))
	pass

def reset():
	# global score
	# print(f"Total Score {score}")
	# score = 0
	# bird.reset(ds, WHITE, int(WIDTH/3), int(HEIGHT/4))
	pipes[0].reset(ds, WHITE, START_TIME + int(3 * WIDTH/4), int(HEIGHT/2))
	pipes[1].reset(ds, WHITE, START_TIME + int(3 * WIDTH/4) + PIPE_GAP, random.randint(40, HEIGHT-40))
	# print("You Lose")
	pass

def all_dead():
	for bird in birds:
		if not bird.dead:
			return False
		return True

def draw():
	global score
	for i in range(len(pipes)):
		if not pipes[i].destroyed:
			pipes[i].update()
		else:
			pipes[i] = Pipe(ds, WHITE, int(3 * WIDTH/4) + PIPE_GAP, random.randint(40, HEIGHT-40))

		# if(pipes[i].hits(bird)):
		# 	reset()

	if not all_dead():
		for bird in birds:
			bird.update()
			bird.draw()
	else:
		print("Dead")
		# reset()

	score += 1
	pass

def main():
	run = True

	setup()
	while run:
		ds.fill(BLACK)

		draw()

		for event in pygame.event.get():
			if event.type == QUIT:
				run = False

			# Heuristrics
			# if event.type == KEYDOWN:
			# 	if event.key == K_w:
			# 		bird.jump()
		pygame.display.update()
		clock.tick(FPS)

	return

if __name__ == '__main__':
	main()
else:
	pygame.quit()
	exit()