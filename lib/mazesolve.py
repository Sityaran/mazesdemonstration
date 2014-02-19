from random import randrange
trees = []

class Tree(object):
	def __init__(self):
		self.name = None
		self.pos = None
		self.bridge = None
		self.parent = None
		self.depth = None
		self.children = []

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
		solveq = []
		discovered = []
		stack.insert(0,start)
		name = 0
		root = Tree()
		root.name,root.pos,root.depth = name, start, 0
		trees.insert(0,root)
		while len(stack) is not 0:
			v = stack.pop()
			for t in trees:
				if t.pos == v:
					currentParent = t
			if v == goal:
				p = currentParent
				while True:
					if p.bridge is not None:
						solveq.append(p.bridge)
					solveq.append(p.pos)
					if p.parent is not None:
						p = p.parent
					else:
						break
				break
			try:
				discovered.index(v)
			except:
				discovered.append(v)
				adjacents =  DFS.adjacents(grid,v[0],v[1])
				for adj in adjacents:
					discovered.append((adj[0],adj[1]))
					stack.insert(0,(adj[2],adj[3]))
					name +=1
					p = currentParent
					t = Tree()
					t.name,t.bridge,t.pos,t.parent,t.depth = name,(adj[0],adj[1]),(adj[2],adj[3]),p,p.depth+1
					trees.append(t)
		return solveq