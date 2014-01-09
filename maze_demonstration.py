import pygame,sys
from pygame.locals import *
from lib.mazegen import *

# ################
# initialization #-
# ################
pygame.init()
#the number of cells being used, so not actually an accurate representation of width and height
width = int(raw_input("width: "))
height = int(raw_input("height: "))

windowSurfaceObj = pygame.display.set_mode((width*2 +1,height*2 +1)) 
pygame.display.set_caption('Mazes')
black = pygame.Color(0,0,0)
black2 = pygame.Color(0,0,1) # for indicating borders and irrelevant grid points
white = pygame.Color(255,255,255)
red = pygame.Color(255,0,0)

graph = pygame.PixelArray(windowSurfaceObj)
depthfirst.setup(graph, white, black, black2)
#prims.setup(graph, white, black, black2)

# unanimated version, to be run once

#depthfirst.depthfirst(graph, white) 
#prims.prims(graph, white, black2)


# ##############
# main #
# ##############

while True:
	graph = pygame.PixelArray(windowSurfaceObj)
	
	# animated versions
	#prims.prims_animated(graph, white, black2)
	depthfirst.depthfirst_animated(graph, white)
	
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_SPACE: #debugging, recommended not to use for large mazes
				for x in range(len(graph)):
					for y in range(len(graph[x])):
						if graph[x][y] == 1:
							print 1,
						else:
							print ' ',
					print
			
			if event.key == K_ESCAPE:
				pygame.quit()
				sys.exit()

	pygame.display.update()