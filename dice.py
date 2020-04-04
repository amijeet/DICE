from random import seed
from random import randint
import sys
import time 
import pygame
from pygame.locals import*

pygame.init()
DISPLAY = pygame.display.set_mode((400,400))
GREEN	= (0,255,0)
RED		= (255,0,0)
WHITE	= (255,255,255)
clock = pygame.time.Clock()
BLACK = (0,0,0)
FPS = 30

#draws the called dice 
def dice(num):
	if num == 1:
		pygame.draw.rect(DISPLAY, GREEN, [150, 150, 100, 100], 0)
		pygame.draw.circle(DISPLAY, RED, (200, 200), 12, 0)
	if num == 2:
		pygame.draw.rect(DISPLAY, GREEN, [150, 150, 100, 100], 0)
		pygame.draw.circle(DISPLAY, RED, (175, 200), 12, 0)
		pygame.draw.circle(DISPLAY, RED, (225, 200), 12, 0)
	if num == 3 :
		pygame.draw.rect(DISPLAY, GREEN, [150, 150, 100, 100], 0)
		pygame.draw.circle(DISPLAY, RED, (200, 200), 12, 0)
		pygame.draw.circle(DISPLAY, RED, (170, 200), 12, 0)
		pygame.draw.circle(DISPLAY, RED, (230, 200), 12, 0)
	if num == 4:
		pygame.draw.rect(DISPLAY, GREEN, [150, 150, 100, 100], 0)
		pygame.draw.circle(DISPLAY, RED, (175, 175), 12, 0)
		pygame.draw.circle(DISPLAY, RED, (225, 175), 12, 0)
		pygame.draw.circle(DISPLAY, RED, (175, 225), 12, 0)
		pygame.draw.circle(DISPLAY, RED, (225, 225), 12, 0)
	if num == 5:
		pygame.draw.rect(DISPLAY, GREEN, [150, 150, 100, 100], 0)
		pygame.draw.circle(DISPLAY, RED, (200, 200), 12, 0)
		pygame.draw.circle(DISPLAY, RED, (175, 175), 12, 0)
		pygame.draw.circle(DISPLAY, RED, (225, 175), 12, 0)
		pygame.draw.circle(DISPLAY, RED, (175, 225), 12, 0)
		pygame.draw.circle(DISPLAY, RED, (225, 225), 12, 0)
	if num == 6:
		pygame.draw.rect(DISPLAY, GREEN, [150, 150, 100, 100], 0)
		pygame.draw.circle(DISPLAY, RED, (175, 170), 12, 0)
		pygame.draw.circle(DISPLAY, RED, (225, 170), 12, 0)
		pygame.draw.circle(DISPLAY, RED, (175, 230), 12, 0)
		pygame.draw.circle(DISPLAY, RED, (225, 230), 12, 0)
		pygame.draw.circle(DISPLAY, RED, (175, 200), 12, 0)
		pygame.draw.circle(DISPLAY, RED, (225, 200), 12, 0)

#Main game loop 
running = True
while(running) :
	clock.tick(FPS)
	for event in pygame.event.get() :
		if( event.type == QUIT ):
			pygame.quit()
			sys.exit()
		if event.type == KEYDOWN:
			if event.key == K_SPACE :
				DISPLAY.fill(BLACK)
				dice( randint(1,6) )
				pygame.display.update()
	pygame.display.update()