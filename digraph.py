"""
digraph

DAG -- directed acyclic graph 
topological sort -- redraw DAG so all edges points upward
"""

from graph import Graph

class Digraph(Graph):
	""""""

	def add_edge(self, v, w):
		""""""
		self.adjacent[v].add(w)

	def count_edges(self):
		"""Return total number of edges"""
		return sum(map(len, self.adjacent))

	def reverse(self):
		pass

	def out_degree(self):
		pass

	def in_degree(self):
		pass


queue = Queue()
discovered = Set()

root = "http://www.princeton.edu"
queue.enqueue(root)
discovered.add(root)

while queue:
	v = queue.dequeue()
	In in = new In(v)
	input = in.readAll()

	regexp = "http://(\\w+\\.)*(\\w+)"
	pattern = pattern.compile(regexp)
	matcher = pattern.matcher(input)
	while matcher.find():
		w = matcher.group()
		if not discovered.contains(w):
			discovered.add(w)
			queue.enqueue(w) 

"""topological sort"""
class Tpsort:
	def __init__(self, graph):
		reverse = Stack()
		marked = [False]*len(graph)
		for v in graph:
			if not marked: self.dfs(graph, v)

	def dfs(self, graph, v):
		marked[v] = True
		for w in graph.adjacent(v):
			if not marked[w]: self.dfs(graph, w)
		reverse.push(v)

	def reverse_post(self):
		return reverse 


#Kosaraju-Sharir algorithm 
#reverse graph has same strong components as original graph
#kernel DAG -- contract each strong component into a single vertex

#phase 1 -- compute reverse postorder in reverse graph 
#phase 2 -- run dfs in original graph, visiting unmarked vertices in reverse postorder of reverse graph 

class KosarajuSharirSCC:
	def __init__(self, graph):
		self.marked = [False] * len(graph)
		self.id = [None] * len(graph)
		self.count = 0
		dfs = depth_first(graph.reverse())
		for v in dfs.reversePost():
			if not self.marked[v]:
				self.dfs(graph, v)
				self.count += 1

	def dfs(self, graph, v):
		self.marked[v] = True
		self.id[v] = self.count 
		for w in graph.adj(v):
			if not marked[w]:
				self.dfs(graph, w)

	def stronglyConnected(self, v, w):
		return self.id[v] == self.id[w]

