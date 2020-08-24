"""UNION-FIND
Union-Find is a data structure that tracks and merges "disjoint sets". Union-
Find operations include:

1) "count" number of disjoint components;
2) "connect" two disjoint components into one; 
3) "find" which subset an element is in; 
4) "union" two subsets into one

                     algorithm | worst-case time |
-------------------------------------------------|           
                    quick-find | MN              |
                   quick-union | MN              |
                   weighted QU | N + M logN      |
         QU + path compression | N + M logN      |
weighted QU + path compression | N + M lg*N      |
-------------------------------------------------|

lg*N is "iterated" logarithmic function, which is the number of times the 
logarithm function must be iteratively applied before the result is less 
than or equal to 1.

Reference:
[1] https://algs4.cs.princeton.edu/
"""

class QuickUnion:
	"""Quick-Union abstracts union-find problem into a parent array, in 
	which two objects, p & q, are connected iff their roots	are the same.

	Quick Union is a "lazy" approach.

	In addition, two 
	techniques are used to improve performance: 
	* weighting, which links root of smaller tree to root of larger tree;
	* path compression, which updates parent to root while search for it.
	"""

	def __init__(self, N: int):
		"""Initialize a Quick-Union object ~ O(N)
		In Quick-Union, connected components are reflected in common root. 
		"""
		self.count = N               #count of disjoint components
		self.parent = list(range(N)) #parent array (to reflect subsets)
		self.size = [1] * N          #size of subtree rooted at node 

	def __len__(self):
		"""Return number of nodes (not number of disjoint components)"""
		return len(self.parent)

	def __repr__(self):
		"""Return string representation of Quick-Union"""
		return str(self.parent)

	def connected(self, p: int, q: int) -> bool:
		"""Return True if p & q are connected ~ O(logN) on average"""
		return self.find(p) == self.find(q)

	def count(self) -> int:
		"""Return the number of disjoint components ~ O(1)"""
		return self.count

	def find(self, p: int, halving: bool=True) -> int:
		"""Return the root of object at p ~ O(logN) on average

		Arguments:
		halving -- a flag to turn on path halving (default to True) 
		"""
		while p != self.parent[p]:
			#update parent to grand parent (path halving)
			if halving: self.parent[p] = self.parent[self.parent[p]]
			p = self.parent[p]
		return p 

	def union(self, p: int, q: int, weighting: bool=True) -> None:
		"""Connect p & q ~ O(logN) on average

		Arguments:
		weighting -- a flag to turn on tree weighting

		If weighting is on, the smaller tree is always linked to the larger 
		tree to achieve better balance. If weighting is off, p-tree is linked 
		to q-tree (i.e. set parent of p-root to q-root).
		"""
		prt, qrt = self.find(p), self.find(q)
		if prt == qrt: return #already linked
		if weighting and self.size[prt] > self.size[qrt]: 
			prt, qrt = qrt, prt #p-tree is smaller 
		self.count -= 1
		self.parent[prt] = qrt #link small tree to large tree
		self.size[qrt] += self.size[prt] #update large tree size


class QuickFind:
	"""Quick-Find abstracts union-find problem into an identity array, in 
	which two objects, p & q, are connected iff their entries in the array 
	are the same.

	Quick-Find is a "gready" approach. 
	"""

	def __init__(self, N: int):
		"""Initialize a Quick-Find object ~ O(N)
		In Quick-Find, connected components are reflected in common id. 
		"""
		self.count = N
		self.id = list(range(N)) #identity array (to reflect membership)

	def __len__(self):
		"""Return number of nodes (not number of disjoint components)"""
		return len(self.id)

	def __repr__(self):
		"""Return string representation of Quick-Find"""
		return str(self.id)

	def connected(self, p: int, q: int) -> bool:
		"""Return True if p & q are connected ~ O(N)"""
		return self.id[p] == self.id[q]

	def count(self) -> int:
		"""Return the number of disjoint components ~ O(1)"""
		return self.count 

	def find(self, p: int) -> int:
		"""Return the membership of p ~ O(1)"""
		return self.id[p]

	def union(self, p: int, q: int) -> None:
		"""Connect p & q by setting id of p component to that of q ~ O(N)"""
		pid, qid = self.id[p], self.id[q]
		if pid == qid: return #already linked
		self.count -= 1
		for i, iid in enumerate(self.id):
			if iid == pid: self.id[i] = qid


class UnionFind(QuickUnion):
	pass 


if __name__ == "__main__": 
	"""Test client for QuickFind"""
	uf = QuickFind(10)
	uf.union(4, 3)
	uf.union(3, 8)
	uf.union(6, 5)
	uf.union(9, 4)
	uf.union(2, 1)
	print("8-9? ", uf.connected(8, 9)) #true
	print("5-0? ", uf.connected(5, 0)) #false
	uf.union(5, 0)
	uf.union(7, 2)
	uf.union(6, 1)
	print("5-0? ", uf.connected(5, 0)) #true


	"""Test client for QuickUnion"""
	uf = QuickUnion(10)
	uf.union(4, 3)
	uf.union(3, 8)
	uf.union(6, 5)
	uf.union(9, 4)
	uf.union(2, 1)
	print("8-9? ", uf.connected(8, 9)) #true
	print("5-0? ", uf.connected(5, 0)) #false
	uf.union(5, 0)
	uf.union(7, 2)
	uf.union(6, 1)
	print("5-0? ", uf.connected(5, 0)) #true