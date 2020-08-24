"""UNDIRECTED GRAPH 

Graph is a set of vertices connected pairwise by edges; 

  representation | space | add edge | edge v-w  | iterate over v degree
---------------------------------------------------------------------
list of edges    | E     | 1        | E         | E
adjacency matrix | V**2  | 1        | 1         | V
adjacency lists* | E + V | 1        | degree(v) | degree(V)

   Euler tour - is there a cycle that uses each edge exactly once?
Hamilton tour - is there a cyCle that uses each vertex exactly once?

minimum spanning tree 

Mark-sweep algorithm (McCarthy, 1960)
* mark -- mark all reachable objects;
* sweep -- if object is unmarked, it is garbage (so add to free list)
"""

from linkedlist import Bag, Stack, Queue

class Graph:
	"""Graph in adjacency-list representation (array of linked lists)
	1) an array of vertices;
	2) a linked list of vertices that it connects to.
	"""
	def __init__(self, vertices):
		"""Initialize the graph with vertices"""
		self.vertices = vertices
		self.adjacent = [Bag()] * vertices

	def __iter__(self):
		"""Return iterator to loop through vertices"""
		return iter(self.vertices)

	def __len__(self):
		"""Return number of vertices"""
		return len(self.vertices)

	def __repr__(self):
		"""Return string representation of graph"""
		ans = ""
		for v in self:
			temp = []
			for w in self.adjacent(v):
				temp.append(w)
			ans += str(v) + ": " + ", ".join(temp) + "\n"
		return ans

	def add_edge(self, v, w):
		"""Add edge between vertices v and w"""
		self.adjacent[v].add(w) #add w to v's adjacent
		self.adjacent[w].add(v) #add v to w's adjacent

	def adjacent(self, v):
		"""Return the adjacent vertices of given vertex"""
		return self.adjacent[v]

	def count_edges(self):
		"""Return total number of edges"""
		return sum(map(len, self.adjacent))//2

	def degree(self, v):
		"""Return the degree of given vertex"""
		degree = 0
		for w in self.adjacent(v):
			degree += 1
		return degree

	def max_degree(self):
		"""Return the maximum degree of graph"""
		max_ = 0
		for v in self:
			degree = self.degree(v)
			if degree > max_: max_ = degree 
		return max_

	def avg_degree(self):
		"""Return the average degree of graph"""
		return 2.0 * self.count_edges()/len(self)

	def count_selfloops(self):
		"""Return count of self-loops"""
		count = 0
		for v in self:
			for w in self.adjacent(v):
				if v == w: 
					count += 1
		return count // 2


"""decouple graph data type from graph processing 
1) create a graph object;
2) pass the graph to a graph-processing routine;
3) query the graph-processing routine for information. 

depth-first search (DFS)
Tremaux maze exploration algorithm 
* unroll a ball of string behind you;
* mark each visited intersection and each visited passage;
* retrace steps when no unvisited options.
"""
class Traverse:
	def __init__(self, graph, source):
		"""Initialize depth-first search over graph on given source"""
		self.edgeto = [None] * len(graph)
		self.marked = [False] * len(graph)
		self.source = source
		self._traverse(graph, source)

	def _traverse(self, graph, s):
		pass

	def connected(self, v):
		"""Return True if source is linked to vertex"""
		return self.marked[v]

	def pathto(self, v):
		"""Return the paths to a vertex"""
		if not self.connected(v): return None
		path = Stack()
		while v != self.source:
			path.push(v)
			v = self.edgeto[v]
		path.push(v)
		return path 


class DFS(Traverse):
	"""Depth-First Search (Tremaux maze exploration)
	Algorithm
	1) use recursion (ball of string);
	2) mark each visited vertex (and keep track of edge taken to visit it);
	3) return (retrace steps) when no unvisited options.
	"""
	def _traverse(self, graph, s):
		"""DFS marks all vertices connected in time proportional to the sum 
		of degrees"""
		self.marked[v] = True
		for w in graph.adjacent(v):
			if not self.marked[w]:
				self._dfs(graph, w)
				self.edgeto[w] = v


class BFS(Traverse):
	"""Breadth-First Search
	Algorithm
	1) put s onto a FIFO queue, and mark s as visited
	2) repeat until the queue is empty:
	- remove the least recently added vertex v
	- add each of v's unvisited neighbors to the queue, and mark them as visited
	"""
	def _traverse(self, graph, s):
		queue = Queue()
		queue.enqueue(s)
		while queue:
			v = queue.dequeue()
			for w in graph.adjacent(v):
				if not marked[w]:
					queue.enqueue(w)
					marked[w] = True
					edgeto[w] = v 


"""
The relation "is connected to" is an equivalence relation:
1) reflexive: v is connected to v;
2) symmetric: if v is connected to w, then w is connected to v;
3) transitive: if v is connected to w and w is connected to x, v is connected to x.

A connected component is a maxial set of connected vertices. 
"""
class CComponent:
	"""Initialize all vertices v as unmarked.
	For each unmarked vertex v, run DFS to identify all vertices discovered as part of the same component.
	"""
	def __init__(self, graph):
		"""Initilize vertices as unmarked"""
		self.marked = [False]*len(graph)
		self.id = [None]*len(graph)
		self.count = 0
		for v in graph:
			if not self.marked[v]:
				self._dfs(graph, v)
				self.count += 1

	def _dfs(self, graph, v):
		"""Depth-first search"""
		self.marked[v] = True
		self.id[v] = count
		for w in graph.adjacent(v):
			if not marked[w]:
				self._dfs(graph, w)

	def connected(self, v, w):
		"""Return true if two vertices are connected"""
		return self.id[v] == self.id[w]

	def count(self):
		"""Return number of connected components"""
		return self.count

	def id(self, v):
		"""Return the connected component a vertex is in"""
		return self.id[v]


"""
1. any programmer could do it
2. diligent programmer could do it
3. hire an exper
4. intractable
5. no one knows
6. impossible 

challenge          | difficulty
-------------------------------
bipartitie         | 2
find a cycle       | 2
Euler tour         | 2
Hamiltonian tour   | 4 (traveling sales man)
graph isomorphism  | 5
planariry problem  | 3 (Tarjan)
"""