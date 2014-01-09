from random import randrange

class prims:
	walls = []
	
	@staticmethod
	def checkadjacents(grid, x, y): #try implementing the empty cell of a valid neighbor method from depthfirst class
		wall = []
		for i in [-1,1]:
			if not(grid[y+i][x]):
				wall.append((x,y+i,x,y+i+i))
			if not(grid[y][x+i]):
				wall.append((x+i,y,x+i+i,y))
		return wall
	
	@staticmethod
	def prims(graph, white, black): 
	# only meant to run once, modifying the graph once, but then 
	# every time it gets called again it s useless
	# fix that
		while len(prims.walls)>0:
			currentwall = prims.walls[randrange(len(prims.walls))]
			
			if not(graph[currentwall[3]][currentwall[2]]):
				graph[currentwall[1]][currentwall[0]] = white
				graph[currentwall[3]][currentwall[2]] = white
				prims.walls.remove(currentwall)
				for i in prims.checkadjacents(graph,currentwall[2],currentwall[3]):
					prims.walls.append(i)
			else:
				graph[currentwall[1]][currentwall[0]] = black
				prims.walls.remove(currentwall)
	
	@staticmethod
	def prims_animated(graph, white, black): # will be able to run every time it s called until walls==0
		if len(prims.walls)>0: 
			currentwall = prims.walls[randrange(len(prims.walls))]
			
			if not(graph[currentwall[3]][currentwall[2]]):
				graph[currentwall[1]][currentwall[0]] = white
				graph[currentwall[3]][currentwall[2]] = white
				prims.walls.remove(currentwall)
				for i in prims.checkadjacents(graph,currentwall[2],currentwall[3]):
					prims.walls.append(i)
			else:
				graph[currentwall[1]][currentwall[0]] = black
				prims.walls.remove(currentwall)
	
	@staticmethod
	def setup(graph, white, black, black2):
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
				
		for i in prims.checkadjacents(graph,1,1):
			prims.walls.append(i)

		graph[1][1] = white

class depthfirst:
	cells = []
	cell = []
	visited = []
	
	@staticmethod
	def neighbors(graph, x, y): #returns neighbors that are unvisited
		neighbors = []
		for i in [-1,1]:
			if not(graph[x][y+i]):
				if not(graph[x][y+i+i]):
					neighbors.append((x,y+i,x,y+i+i))
			if not(graph[x+i][y]):
				if not(graph[x+i+i][y]):
					neighbors.append((x+i,y,x+i+i,y))
		return neighbors
	
	@staticmethod
	def depthfirst(graph, white):
		while len(depthfirst.visited)>0:
			neighbors = depthfirst.neighbors(graph, depthfirst.cell[0], depthfirst.cell[1])

			if not(len(neighbors)):
				depthfirst.visited.remove(depthfirst.cell)
				if len(depthfirst.visited)>0:
					depthfirst.cell = depthfirst.visited[randrange(len(depthfirst.visited))]
				else:
					break
			else:
				neighbor = neighbors[randrange(len(neighbors))]
				graph[neighbor[0]][neighbor[1]] = white
				graph[neighbor[2]][neighbor[3]] = white
				depthfirst.cell = neighbor[2],neighbor[3]
				depthfirst.visited.append(depthfirst.cell)
				depthfirst.cells.remove(depthfirst.cell)
				
	@staticmethod
	def depthfirst_animated(graph, white):	
		if len(depthfirst.visited)>0:

			neighbors = depthfirst.neighbors(graph, depthfirst.cell[0], depthfirst.cell[1])

			if not(len(neighbors)):
				depthfirst.visited.remove(depthfirst.cell)
				if len(depthfirst.visited)>0:
					depthfirst.cell = depthfirst.visited[randrange(len(depthfirst.visited))]
			else:
				neighbor = neighbors[randrange(len(neighbors))]
				graph[neighbor[0]][neighbor[1]] = white
				graph[neighbor[2]][neighbor[3]] = white
				depthfirst.cell = neighbor[2],neighbor[3]
				depthfirst.visited.append(depthfirst.cell)
				depthfirst.cells.remove(depthfirst.cell)
	
	@staticmethod
	def setup(graph, white, black, black2):
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
				if (i%2) and (n%2) and (i<len(graph)-1) and (n<len(graph[i])-1):
					depthfirst.cells.append((i,n))
		graph[1][1] = white
		depthfirst.cell = (1,1)
		depthfirst.cells.remove((1,1))
		depthfirst.visited.append((1,1))
