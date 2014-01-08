import pygame,sys
from pygame.locals import *
from random import randrange

# ################
# initialization #
# ################
pygame.init()

#the number of cells being used, so not actually an accurate representation of width and height
width = int(raw_input("width: "))
height = int(raw_input("height: "))

windowSurfaceObj = pygame.display.set_mode((width*2 +1,height*2 +1)) 
pygame.display.set_caption('Mazes')
black = pygame.Color(0,0,0)
black2 = pygame.Color(0,0,1) #for indicating borders and irrelevant grid points
white = pygame.Color(255,255,255)
red = pygame.Color(255,0,0)

walls = [] 
graph = pygame.PixelArray(windowSurfaceObj)

# ###########
# functions #
# ###########

#prims
def checkadjacents(grid,x,y):
	wall = []
	for i in [-1,1]:
		if not(grid[y+i][x]):
			wall.append((x,y+i,x,y+i+i))
		if not(grid[y][x+i]):
			wall.append((x+i,y,x+i+i,y))
	return wall
	
def prims(grid,walls): 
# only meant to run once, modifying the graph once, but then 
# every time it gets called again it s useless
# fix that
	while len(walls)>0:
		currentwall = walls[randrange(len(walls))]
		
		if not(graph[currentwall[3]][currentwall[2]]):
			graph[currentwall[1]][currentwall[0]] = white
			graph[currentwall[3]][currentwall[2]] = white
			walls.remove(currentwall)
			for i in checkadjacents(graph,currentwall[2],currentwall[3]):
				walls.append(i)
		else:
			graph[currentwall[1]][currentwall[0]] = black2
			walls.remove(currentwall)

def prims_animated(graph,walls): # will be able to run every time it s called until walls==0
	if len(walls)>0: 
		currentwall = walls[randrange(len(walls))]
		
		if not(graph[currentwall[3]][currentwall[2]]):
			graph[currentwall[1]][currentwall[0]] = white
			graph[currentwall[3]][currentwall[2]] = white
			walls.remove(currentwall)
			for i in checkadjacents(graph,currentwall[2],currentwall[3]):
				walls.append(i)
		else:
			graph[currentwall[1]][currentwall[0]] = black2
			walls.remove(currentwall)
			
def setup(graph):
	for i in range(len(graph)):
		for n in range(len(graph[i])):
			if (i==0) or (i==len(graph)-1):
				graph[i][n] = black2
			elif (n==0) or (n==len(graph[i])-1):
				graph[i][n] = black2
			elif not(i%2) and not(n%2):
				graph[i][n] = black2
			else:
				graph[i][n] = black
			
	for i in checkadjacents(graph,1,1):
		walls.append(i)

	graph[1][1] = white

#initial setup
setup(graph)

# ##############
# main program #
# ##############

while True:
	graph = pygame.PixelArray(windowSurfaceObj)
	
	prims(graph, walls)
	
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