"""MINIMUM SPANNING TREE
A spanning tree of a undirected graph is a subgraph that is both a tree 
(connected and acyclic) and spanning (including all vertices). 

A minimum spanning tree is the minimal way to connect a graph. 

APPLICATIONS
* dithering
* cluster analysis
* max bottleneck paths
* real-time face verification
* LDPC codes for error correction
* image registration with Renyi entropy
* find road networks in satellite and aerial imagery 
* reducing data storage in sequencing amino acid in a protein
* model locality of particle interactions in turbulent fluid flows
* autoconfig protoclol for ethernet briding to avoid cycles in a network
* approximation algorithsm for NP-hard problems (e.g. TSP, Steiner tree)
* network design (communication, electrical, hydraulic, computer, road)
"""

#GREEDY ALGORITHM
#A cut in a graph is a partition of its vertices into two (nonempty) sets
#A cross edge connects a vertex in one set with a vertex in the other
#Given any cut, the crossing of min weight is in the MST

#Weighted edge API 
class Edge:
	def __init__(self, v, w, weight):
		"""Create a weighted edge v-w"""
		self._v = v
		self._w = w
		self._weight = weight

	def either(self):
		"""either point"""
		return self._v

	def other(self, vertex):
		"""the end point that is not v"""
		if vertex == self._v:
			return self._w 
		else:
			return self._v 

	def __eq__(self, edge):
		return self._weight == edge._weight 

	def __ne__(self, edge):
		return self._weight != edge._weight

	def __lt__(self, edge):
		return self._weight < edge._weight

	def __le__(self, edge):
		return self._weight <= edge._weight

	def __gt__(self, edge):
		return self._weight > edge._weight

	def __ge__(self, edge):
		return self._weight >= edge._weight 

	def weight(self):
		"""Return the weight"""
		return self._weight 

	def __str__(self):
		"""Return string representation of an edge"""
		return f"{self._v} - {self._w} {self._weight}"


"""
Edge-weighted graph -- adjacency-lists representation 
Maintain a vertex-indexed array of edge list
"""
class EdgeWeightedGraph:
	def __init__(self, V):
		"""Initialize an empty graph with given vertices"""
		self._V = V
		self._adj = [Bag()] * V

	def add_edge(self, edge):
		"""Add weighted edge to graph"""
		v = edge.either()
		w = edge.other(v)
		self._adj[v].append(edge)
		self._adj[w].append(edge)

	def adj(self, vertex):
		"""Returns edges incident to given vertex"""
		return self._adj[vertex]

	def edges(self):
		"""Return all edges in the graph"""
		pass

	def V(self):
		"""Return number of vertices"""
		pass

	def E(self):
		"""Return number of edges"""
		pass

	def __str__(self):
		"""Return string representation of graph"""
		pass

class MST:
	def __init__(self, graph):
		
		self.graph = graph
	
	def edges(self):
		"""Return edges in MST"""
		pass

	def weight(self):
		"""Return weight of MST"""
		pass

#Kruskal's algorithm (1956)
#Consider edges in ascending order of weight, and add next edge to tree unless 
#doing so would create a cycle.

from containers import Queue, UnionFind
from tree import MinQueue

class Kruskal:
	"""Kruskal's algorithm for minimum spanning tree"""
	mst = Queue() #mst -- a queue of edges 
	def __init__(self, graph):
		"""Kruskal's algorithm computes MST in time proportional to Elog(E)"""
		pq = MinQueue()
		for edge in graph.edges(): #build prioirty queue ~ O(E)
			pq.insert(edge)
		uf = UnionFind(len(graph))
		while pq and len(mst) < len(graph) - 1:	
			edge = pq.del_min() #delete-min ~ O(log(E))
			v = edge.either()
			w = edge.other(v)
			if not uf.connectged(v, w): #connected ~ O(log*(V))
				uf.union(v, w) #union ~ O(log*(V))
				mst.enqueue(edge)

#Prim's algorithm (Jarnik 1930, Dijkstra 1957, Prim 1959)
#Start with vertex 0 and greedily grow tree by adding the shortest edge 
#connecting a tree vertex with a non-tree vertex.

#lazy vs eager implementation 
#Maintain a priority queue of edges by weight with (at least) one endpoint on tree
#delete-min to determine next edge e=v-w to add to tree
#Disregard if both endpoints v and w are on tree
#Otherwise, let w be the vertex not on tree
# - add to priority queue any edge incident to w (assuming other endpoint not on tree)
# - add w to tree 

from tree import MinQueue
from containers import Queue

"""
------------------------------------
 operation | frequency | binary heap
delete min | E         | log(E)
    insert | E         | log(E)
------------------------------------    
"""

class Prim:
	"""Lazy implementation of Prim algorithm"""
	def __init__(self, graph):
		self.pq = MinQueue() #priority queue of edges
		self.mst = Queue()   #MST edges
		self.marked = [False] * len(graph) #MST vertices
		self.visit(graph, 0) #assuming graph is connected

		while self.pq:
			edge = self.pq.del_min() #repeatedly delete min edge from pq
			v = edge.either()
			w = edge.other(v)
			if self.marked[v] and self.marked[w]: continue #ignore if both endpoints on tree
			self.mst.enqueue(edge)
			if not self.marked[v]: self.visit(graph, v) #add v to tree
			if not self.marked[w]: self.visit(graph, w) #add w to tree

	def visit(self, graph, v):
		"""put vertex on the tree and its incident edges on priority queue"""
		self.marked[v] = True #add vertex to tree
		for edge in graph.adj(v):
			if not self.marked[edge.other(v)]:
				self.pq.insert(edge) #add w to pq if not in tree


"""Eager implementation
Challenge -- find min weight edge with exactly one endpoint in tree

Eager solution -- maintain a proirity queue of vertices connected by an edge
to tree where priority of vertex v = weight of shortest edge connecting v to tree.

Algorithm:
1) start with vertex 0 and greedily grow tree;
2) add to tree the min weight edge with exactly one endpoint in tree;
3) repeat until V - 1 edges. 
"""

"""Index priority queue
Associate an index between 0 and N-1 with each key in a proirity queue
- client can insert and delete-the-minimum;
- client can change the key by specifying the index.
"""
class IndexMinPQ:
	"""Associate an index between 0 and N-1 with each key in a priority queue"""
	def __init__(self, N):
		"""Create indexed priority with indices 0, 1, ..., N-1
		maintain parallel arrays keys[i], pq[i] and qp[i] so that 
		- keys[i] is the priority of i
		- pq[i] is the index of the key in heap position i
		- qp[i] is the heap position of the key with index i
		"""
		self.N = N

	def insert(self, i, key):
		"""Associate key with index i"""
		pass

	def decrease_key(self, i, key):
		"""Decrease the key associated with index i"""
		pass

	def __contains__(self, i):
		"""Return True if index i is in the queue"""
		pass

	def del_min(self):
		"""Remove a minimal key and return its associated index"""
		pass

	def __len__(self):
		"""Return number of entries in the priority queue"""
		pass

"""
---------------------------------------------------------------------
PQ implementation | insert  | delete-min | decrease-key | total
---------------------------------------------------------------------
            array | 1       | V          | 1            | V**2
      binary heap | log(V)  | log(V)     | log(V)       | Elog(V)
       d-way heap | logd(V) | dlogd(V)   | logd(V)      | ElogE/V(V)
   fibonacci heap | 1       | log(V)     | 1            | E + Vlog(V)
---------------------------------------------------------------------
Bottom line:
* array implementation optimal for dense graphs;
* binary heap much faster for sparse graphs;
* 4-way heap worth the trouble in performance-critical situations;
* fibonacci heap best in theory, but not worth implementing. 
"""

"""
Linear-time MST?
-------------------------------------------------------
year | worst case          | discovered by 
-------------------------------------------------------
1975 | Elog(log(V))        | Yao
1976 | Elog(log(V))        | Cheriton-Tarjan
1984 | Elog*(V), E+Vlog(V) | Fredman-Tarjan
1986 | Elog(log*(V))       | Gabow-Galil-Spencer-Tarjan
1997 | Ea(V)log(a(V))      | Chazelle
2000 | Ea(V)               | Chazelle
2002 | optimal             | Pettie-Ramachandran 
20xx | E                   | ???
-------------------------------------------------------
"""

"""Euclidean MST
Given N points in the plane, find MST connecting them, where the distances
between point pairs are their Euclidean distances. 
- Voronoi diagram (delaunay triangle)
"""

"""single-link cluster -- given an integer k, find k-clustering that maximizes
the distance between two closest clusters.
* form V clusters of one object each;
* find the closest pair of objects such that each object is in a different cluster, and merge the two clsuter;
* repeat until there are exactly k clusters.
-- this is Kruskal's algorithm (stopping at k)
-- alternatively, run Prim's algorithm and delete k-1 max weight edges
"""


"""SHORTEST-PATH PROBLEM
source-sink -- from one vertex to another
single source -- from one vertex to every other
all pairs -- between all pairs of vertices 

A shortest-path tree (SPT) solution exists. 
one can represent the SPT with two vertex-indexed array:
- dist_to[v] is length of shortest path from s to v;
- edge_to[v] is last edge on shortest path from s to v. 
"""

class DirectredEdge:
	"""docstring for DirectredEdge"""
	def __init__(self, v, w, weight):
		"""Weighted edge v->w"""
		self.v = v
		self.w = w
		self.weight = weight

	def from_(self):
		"""vertex v"""
		return self.v

	def to(self):
		"""vertex w"""
		return self.w

	def weight(self):
		"""Weight"""
		return self.weight

	def __str__(self):
		return f"{self.from_} -> {self.to}, {self.weight}"


class EdgeWeightedDigraph:
	"""edge weighted digraph represented by adjacency-list"""
	def __init__(self, V):
		"""Edge weighted digraph with V vertices"""
		self.V = V
		self.adj[v] = [Bag() for _ in range(V)]

	def add_edge(self, edge):
		"""Add weighed directed edge"""
		v = edge.from_()
		self.adj[v].add(edge)

	def adj(self, v):
		"""Return edges pointing from v"""
		return self.adj[v] #add edge v->w to only v's adjacency list

	def V(self):
		"""Return number of vertices"""
		pass 

	def E(self):
		"""Return number of edges"""
		pass

	def edges(self):
		"""Return all edges"""
		pass
		
	def __str__(self):
		"""Return string representation"""
		pass 


class ShortestPath:
	"""Shortest path from source s in graph"""
	def __init__(self, graph, s):
		self.graph = graph
		self.s = s
		
	def dist_to(self, v):
		return self.dist_to[v]

	def path_to(self, v):
		path = Stack()
		edge = self.edge_to[v]
		while edge:
			path.push(edge)
			edge = self.edge_to[edge.from_()]
		return path 

	def has_path_to(self, v):
		pass

	def has_negcycle(self):
		pass

	def negcycle(self):
		pass


#client 
sp = ShortestPath(graph, source)
for v in range(graph.V()):
	print(f"{s} to {v}  ({sp.dist_to(v)})")
	for edge in sp.path_to(v):
		print(edge, end=" ")

"""Edge relaxation
relax edge e=v->w
* dist_to[v] is length of shortest konwn path from s to v;
* dist_to[w] is length of shortest known path from s to w; 
* edge_to[w] is last edge on shortest known path from s to w.
if e=v->w gives shorter path to w through v, update both dist_to[w] and edge_to[w].
"""
def relax(self, edge):
	v = edge.from_()
	w = edge.to()
	if dist_to[w] > dist_to[v] + edge.weight():
		dist_to[w] = dist_to[v] + edge.weight()
		edge_to[w] = edge

"""Optimality condition
Let G be a edge-weighted digraph. dist_to[] are the shortest path distances from s iff:
* dist_to[s] = 0
* for each vertex v, dist_to[v] is the length of some path from s to v;
* for each edge e = v->w, dist_to[w] <= dist_to[v] + e.weight()

GENERIC SHORTEST-PATHS ALGORITHM
Initialize dist_to[s] = 0 and dist_to[v] = infinity for all vertices;
Repeat until optimaility conditions are satisfied -- relax any edge. 

How to choose which edge to relax?
- Dijkstra's algorithm (nonnegative weights)
- topological sort algorithm (no directed cycles)
- Bellman-Ford algorithm (no negative cycles)

DIJKSTRA'S ALGORITHM
* consider vertices in increasing order of distances from s;
* add vertex to tree and relax all edges pointing from that vertex.

Dijkstra's algorithm computes a SPT in any edge-weighted digraph with nonnegative weights. 
"""

class DijkstraSP:
	"""Dijkstra's short-paths algorithm"""
	def __init__(self, digraph, source):
		self.edge_to = [None] * digraph.V()
		self.dist_to = [float("inf")] * digraph.V()
		pq = IndexMinPQ(digraph.V())

		self.dist_to[source] = 0

		pq.insert(source, 0.0)
		while pq:
			v = pq.del_min()
			for edge in digraph.adj(v):
				self.relax(edge)

	def relax(self, edge):
		v = e.from_()
		w = e.to()
		if self.dist_to[w] > self.dist_to[v] + edge.weight():
			self.dist_to[w] = dist_to[v] + edge.weight()
			self.edge_to[w] = edge 
			if w in self.pq: self.pq.decrease_key(w, self.dist_to[w])
			else: self.pq.insert(w, self.dist_to[w])

"""Acyclic shortest-paths (DAG)
1) consider vertices in topological order;
2) relax all edges pointing from that vertex. 
"""

class AcyclicSP:
	"""Compute shortest paths in edge-weighted DAG"""
	def __init__(self, digraph, source):
		self.edge_to = [None] * len(digraph)
		self.dist_to = [float("inf")] * len(digraph)

		topological = Topological(digraph)
		for v in topological.order():
			for edge in digraph.adj[v]:
				self.relax(edge)

#CPM -- critical path method 

#A negative cycle is a directed cycle whose sum of edge weights is negative. 
#A SPT exists iff no negative cycles. 
"""Bellman-Ford algorithm (aka dynamic programming)
Initialize dist_to[s] = 0 and dist_to[v] = infinity for all other vertices;
Repeat V times by relaxing each edge. 

If dist_to[v] doesn't change during pass i, no need to relax any edge pointing from v in pass i+1.

             algorithm | restriction         | typical case | worst case | extra space
             -------------------------------------------------------------------------
      topological sort | no directed cycles  | E + V        | E + V      | V
Dijkstra (binary heap) | no negative weights | Elog(V)      | Elog(V)    | V
          Bellman-Ford | no negative cycles  | E * V        | E * V      | V
  Bellman-Ford (queue) | no negative cycles  | E + V        | E * V      | V


"""


"""
s: source; t: target

MINIMUM CUT (find a cut of minimum capacity)
A st-cut is a partition of the vertices into two disjoint sets with s in one set A and t in the other set B.
Its capacity is the sum of the capacities of the edges from A to B. 

MAXIMUM FLOW (find a flow of maximum value)
An st-flow is an assignment of values to the edges such that:
* capacity constaint: 0 <= edge's flow <= edge's capacity;
* local equilibrium: inflow = outflow at every vertex (except s & t)
The value of a flow is the inflow at t.

These two problems are dual!

FORD-FULKERSON ALGORITHM (1956) 
Start with 0 flow.
While there exists an augmenting path:
* find an augmenting path
* compute bottleneck capacity
* increase flow on that path by bottleneck capacity

augmenting path -- the path along with one can augment flow, i.e. 
find an undirected path from s to t such that:
* can increase flow on forward edges (not full)
* can decrease flow on backward edges (not empty)
Termination -- all paths from s to t are blocked by either a 
* full forward edge;
* empty backward edge. 


flow-value lemma: Let f be any flow and let (A,B) be any cut. Then the net flow across (A,B) equals the value of f. 
Corollary. Outflow of s = inflow of t = value of flow. 

Weak duality. Let f be any flow and let (A, B) be any cut. Then, the value of the flow <= the capacity of the cut. 

AUGMENTING PATH THEOREM. 
A flow f is a maxflow iff no augmenting paths.

MAXFLOW-MINCUT THEOREM. 
Value of the maxflow = capacity of mincut. 

1) there exists a cut whose capacity equals the value of the flow f;
2) f is a maxflow;
3) there is no augmenting path with respect to f.  

SPECIAL CASE
edge capacities are integer-valued (between 1 and U);
flow is integer-valued;
number of augmentations <= the value of the maxflow; 

INTEGRALITY THEOREM
There exists an integer-valued maxflow

augmenting path | number of paths | implementation
---------------------------------------------------
  shortest path | <= 1/2 * E * V  | queue (BFS)
   fattest path | <= E * ln(E*U)  | priority queue
    random path | <= E * U        | randomized queue
       DFS path | <= E * U        | stack (DFS)
"""

class FlowEdge:
	"""flow-edge v->w"""
	def __init__(self, v, w, capacity):
		"""Create a flow edge v->w"""
		self.v = v
		self.w = w
		self.capacity = capacity

	def from_(self):
		return self.v

	def to(self):
		return self.w

	def capacity(self):
		return self.capacity

	def flow(self):
		return self.flow

	def other(self, vertex):
		if vertex == self.v: 
			return self.w 
		elif vertex == self.w: 
			return self.v
		else: 
			raise ValueError("Illegal endpoint")

	def residual_capacity(self, vertex):
		if vertex == self.v: #backward edge
			return self.flow
		elif vertex == self.w: #forward edge
			return self.capacity - self.flow
		else:
			raise ValueError("Illegal endpoint")

	def add_residual_flow(self, vertex, delta):
		if vertex == self.v: #backward edge
			self.flow -= delta
		elif vertex == self.w: #forward edge
			self.flow += delta
		else:
			raise ValueError(Illegal endpoint)


class FlowNetwork:
	"""Same as EdgeWeightedGraph but adjacency list of FlowEdges instead of Edges"""
	def __init__(self, V):
		"""Create an empty flow network with V vertices"""
		self.V = V
		
	def add_edge(self, edge):
		"""Add flow edge to flow network"""
		v = edge.from_()
		w = edge.to()
		self.adj[v].add(edge) #add forward edge
		self.adj[w].add(edge) #add backward edge

	def adj(self, v):
		"""Return forward and backward edges incident to given vertex"""
		pass

	def edges(self):
		"""Return all edges in this flow network"""
		pass

	def __len__(self):
		"""Return number of vertices"""
		pass

	def E(self):
		"""Return number of edges"""
		pass

	def __str__(self):
		"""Return string representation of flow network"""
		pass

class FordFulkerson:
	"""Ford-Fulkerson implementation"""
	def __init__(self, graph, s, t):
		""""""
		self.marked = [False] * len(graph)
		self.value = 0
		while self.has_augpath(graph, s, t):
			bottle = float('inf')
			v = t 
			#compare bottleneck capacity
			while v:
				bottle = min(bottle, self.edge_to[v].residual_capacity_to(v))
				v = self.edge_to[v].other(v)
			#augment flow
			v = t
			while v:
				self.edge_to[v].add_residual_flow_to(v, bottle)

			self.value += bottle

	def has_augpath(self, graph, s, t):
		"""Breadth-first search"""
		self.edge_to = [False] * len(graph)
		self.marked = [False] * len(graph)
		q = Queue()
		q.enqueue(s)
		self.marked[s] = True

		while q:
			v = q.dequeue()
			for edge in graph.adj(v):
				w = edge.other(v)
				if edge.residual_capacity_to(w) > 0 and not self.marked[w]:
				#found path from s to w in the residual network?
					self.edge_to[w] = edge #save last edge on path to w
					self.marked[w] = True  #mark w
					q.enqueue(w)           #add w to queue

		return self.marked[t] #is t reachable from s in residual network?

	def value(self):
		return self.value

	def in_cut(self, v):
		"""Return True if given vertex is reachable from s in residual network"""
		return self.marked[v]

"""
MAXIMUM FLOW ALGORITHMS
year | method                   | worst case                 | discovered by 
-----------------------------------------------------------------------------------
1951 | simplex                  | E**3 * U                   | Danzig
1955 | augmenting path          | E**2 * U                   | Ford-Fulkerson
1970 | shortest augmenting path | E**3                       | Dinitz, Edmonds-Karp 
1970 | fattest augmenting path  | E**2 * log(E) * log(E*U)   | Dinitz, Edmonds-Karp
1977 | blocking flow            | E**(5/2)                   | Cherkasky
1978 | blocking flow            | E**(7/3)                   | Galil
1983 | dynamic trees            | E**2*log(E)                | Sleator-Tarjan 
1985 | capacity scaling         | E**2 * log(U)              | Gabow
1997 | length function          | E**(3/2) * log(E) * Log(U) | Goldberg-Rao
2012 | compact network          | E**2 / log(E)              | Orlin 
"""