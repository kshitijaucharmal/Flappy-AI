import pygame, sys
from pygame.locals import *
from bird import Bird
from pipe import Pipe
from nn import NeuralNet
import random
import numpy as np

WIDTH = 350
HEIGHT = 600
FPS = 600
PIPE_GAP = 300
START_TIME = 500
MAX_POP = 50
DIFF = 100

fitness_values = []
generation = 0
print("Generation 0 started")

# colors  r    g    b
WHITE =  (0,   255, 0  )
BLACK =  (0,   0,   0  )
RED =    (255, 0,   0  )

ds = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy")
clock = pygame.time.Clock()

birds = []
bird = Bird(ds, RED, int(WIDTH/3), int(HEIGHT/4))
pipes = []

def setup():
	for i in range(MAX_POP):
		birds.append(Bird(ds, RED, int(WIDTH/3), int(HEIGHT/4)))
	pipes.append(Pipe(ds, WHITE, START_TIME + int(3 * WIDTH/4), random.randint(DIFF, HEIGHT-DIFF)))
	pipes.append(Pipe(ds, WHITE, START_TIME + int(3 * WIDTH/4) + PIPE_GAP, random.randint(DIFF, HEIGHT-DIFF)))
	pass

def reset():
	global fitness_values
	for bird in birds:
		fitness_values.append(bird.score)
		bird.reset(ds, RED, int(WIDTH/3), int(HEIGHT/4), brain=bird.brain)
	# print(f"Average Score : {np.sum(fitness_values)/len(fitness_values)}")
	fitness_values.sort()

	

	fitness_values = []
	pipes[0].reset(ds, WHITE, START_TIME + int(3 * WIDTH/4), random.randint(DIFF, HEIGHT-DIFF))
	pipes[1].reset(ds, WHITE, START_TIME + int(3 * WIDTH/4) + PIPE_GAP, random.randint(DIFF, HEIGHT-DIFF))
	pass

def all_dead():
	for bird in birds:
		if bird.dead:
			continue
		else:
			return False
	return True

def draw():
	for i in range(len(pipes)):
		if not pipes[i].destroyed:
			pipes[i].update()
		else:
			pipes[i] = Pipe(ds, WHITE, int(3 * WIDTH/4) + PIPE_GAP, random.randint(DIFF, HEIGHT-DIFF))

		for b in birds:
			if not b.dead:
				if(pipes[i].hits(b)):
					b.dead = True
		# if(pipes[i].hits(bird)):
		# 	reset()

	if not all_dead():
		for bird in birds:
			if not bird.dead:
				bird.think(pipes)
				bird.update()
				bird.draw()
	else:
		global generation
		print("All Dead")
		generation += 1
		print(f"Generation {generation} started")
		reset()
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

			#Heuristricsw
			# if event.type == KEYDOWN:
			# 	if event.key == K_w:
			# 		birds[0].jump()
		pygame.display.update()
		clock.tick(FPS)

	return

if __name__ == '__main__':
	main()
else:
	pygame.quit()
	exit()