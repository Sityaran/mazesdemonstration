from random import randrange

class Astar:

	def __init__(self, grid):
		self.grid = grid
		
	def astar(self,start,goal):
		closedset = []
		openset = [].append(start) #openset should work in (f_score,x,y)
		path_navigated = []
		g_score = 0
		f_score = 1
		while len(openset) > 0:
			currentnode = 1
			
class DFS:
	@staticmethod
	def adjacents(grid,x,y):
		adj = []
		for i in [-1,1]:
			if grid[x][y+i] == 1:
				if grid[x][y+i+i] == 1:
					adj.append((x,y+i,x,y+i+i))
			if grid[x+i][y] == 1:
				if grid[x+i+i][y] == 1:
					adj.append((x+i,y,x+i+i,y))
		return adj
	
	@staticmethod
	def solve(grid, start, goal):
		stack = []
		discovered = []
		stack.insert(0,start)
		while len(stack) is not 0:
			v = stack.pop()
			if v == goal:
				discovered.append(v)
				break
			try:
				discovered.index(v)
			except:
				discovered.append(v)
				adjacents =  DFS.adjacents(grid,v[0],v[1])
				for adj in adjacents:
					discovered.append((adj[0],adj[1]))
					stack.insert(0,(adj[2],adj[3]))
			
		return discovered