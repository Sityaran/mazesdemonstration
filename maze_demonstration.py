import pygame,sys
from pygame.locals import *
from lib.mazegen import *
from lib.mazesolve import *

# ################
# initialization #-
# ################
pygame.init()
#the number of cells being used, so not actually an accurate representation of width and height
width = int(raw_input("width: "))
height = int(raw_input("height: "))
window_scale = int(raw_input("window scale: "))

windowSurfaceObj = pygame.display.set_mode(((width*2 +1)*window_scale,(height*2 +1)*window_scale)) 
pygame.display.set_caption('Mazes')
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
red = pygame.Color(255,0,0)

graph = pygame.PixelArray(windowSurfaceObj)

prims.setup(width,height)
drawq = prims.prims()

#depthfirst.setup(width,height)
#drawq = depthfirst.depthfirst()
#solveq = DFS.solve(depthfirst.grid,(1,1),((width*2)-1,(height*2)-1))

# ##############
# main #
# ##############
solveq = []
gag = 0
while True:
	# draw
	graph = pygame.PixelArray(windowSurfaceObj)
	if len(drawq) > 0:
		x,y = drawq[0][0] * window_scale , drawq[0][1] * window_scale
		for xs in range(window_scale):
			for ys in range(window_scale): 
				graph[x + xs][y + ys] = white
		drawq.pop(0)
		del graph
	
	
	# solve
	if len(drawq) == 0:
		if gag == 0:
			solveq = DFS.solve(prims.grid,(1,1),((width*2)-1,(height*2)-1))
			gag+=1
		graph = pygame.PixelArray(windowSurfaceObj)
		if len(solveq) > 0:
			x,y = solveq[0][0] * window_scale , solveq[0][1] * window_scale
			for xs in range(window_scale):
				for ys in range(window_scale): 
					graph[x + xs][y + ys] = red
			solveq.pop(0)
			pygame.time.wait(20)
			del graph
			
	for g in [(1,1),((width*2)-1,(height*2)-1)]:
		x,y = g[0]*window_scale,g[1]*window_scale
		for xs in range(window_scale):
			for ys in range(window_scale): 
				graph = pygame.PixelArray(windowSurfaceObj)
				graph[x + xs][y + ys] = pygame.Color(0,0,255)
				del graph

	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				pygame.quit()
				sys.exit()

	pygame.display.update()