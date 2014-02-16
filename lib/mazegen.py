from random import randrange

class prims:
	walls = []
	grid = []
	
	@staticmethod
	def checkadjacents(x, y): #try implementing the empty cell of a valid neighbor method from depthfirst class
		wall = []
		for i in [-1,1]:
			if not(prims.grid[x][y+i]):
				wall.append((x,y+i,x,y+i+i))
			if not(prims.grid[x+i][y]):
				wall.append((x+i,y,x+i+i,y))
		return wall
	
	@staticmethod
	def prims(): 
	# only meant to run once, modifying the graph once, but then 
	# every time it gets called again it s useless
	# fix that
		drawq = []
		drawq.append((1,1))
		while len(prims.walls)>0:
			currentwall = prims.walls[randrange(len(prims.walls))]
			
			if not(prims.grid[currentwall[2]][currentwall[3]]):
				prims.grid[currentwall[0]][currentwall[1]] = 1
				prims.grid[currentwall[2]][currentwall[3]] = 1
				drawq.append( (currentwall[0],currentwall[1]) )
				drawq.append( (currentwall[2],currentwall[3]) )

				prims.walls.remove(currentwall)
				for i in prims.checkadjacents(currentwall[2],currentwall[3]):	
					prims.walls.append(i)
			else:
				prims.grid[currentwall[0]][currentwall[1]] = 3
				prims.walls.remove(currentwall)
		return drawq

	@staticmethod
	def setup(width,height):
		grid = [ [3] + [0]*(2*height - 1)  + [3] for x in range(width*2 - 1) ]
		grid.insert(0,[3]*(height*2 + 1))
		grid.insert(len(grid),[3]*(height*2 + 1))
		
		grid[1][1] = 1
		prims.grid = grid
		for i in prims.checkadjacents(1,1):
			prims.walls.append(i)
		
class depthfirst:
	cells = []
	cell = []
	visited = []
	grid = []
	
	@staticmethod
	def neighbors(x, y): #returns neighbors that are unvisited
		neighbors = []
		for i in [-1,1]:
			if not(depthfirst.grid[x][y+i]):
				if not(depthfirst.grid[x][y+i+i]):
					neighbors.append((x,y+i,x,y+i+i))
			if not(depthfirst.grid[x+i][y]):
				if not(depthfirst.grid[x+i+i][y]):
					neighbors.append((x+i,y,x+i+i,y))
		return neighbors
	
	@staticmethod
	def depthfirst():
		drawq = []
		drawq.append((1,1))
		while len(depthfirst.visited)>0:
			neighbors = depthfirst.neighbors(depthfirst.cell[0], depthfirst.cell[1])
			if not(len(neighbors)):
				depthfirst.visited.remove(depthfirst.cell)
				if len(depthfirst.visited)>0:
					depthfirst.cell = depthfirst.visited[randrange(len(depthfirst.visited))]
				else:
					break
			else:
				neighbor = neighbors[randrange(len(neighbors))]
				depthfirst.grid[neighbor[0]][neighbor[1]] = 1
				depthfirst.grid[neighbor[2]][neighbor[3]] = 1
				drawq.append((neighbor[0],neighbor[1]))
				drawq.append((neighbor[2],neighbor[3]))
				depthfirst.cell = neighbor[2],neighbor[3]
				depthfirst.visited.append(depthfirst.cell)
				depthfirst.cells.remove(depthfirst.cell)
				
		return drawq
				
	@staticmethod
	def setup(width,height):
		grid = [ [3] + [0]*(2*height - 1)  + [3] for x in range(width*2 - 1) ]
		grid.insert(0,[3]*(height*2 + 1))
		grid.insert(len(grid),[3]*(height*2 + 1))
		
		for i in range(len(grid)):
			for n in range(len(grid[i])):
				if not ( (i==0) or (i==len(grid)-1) ):
					if (i%2) and (n%2) and (i<len(grid)-1) and (n<len(grid[i])-1):
						depthfirst.cells.append((i,n))
		grid[1][1] = 1
		depthfirst.cell = (1,1)
		depthfirst.visited.append((1,1))
		depthfirst.grid = grid

