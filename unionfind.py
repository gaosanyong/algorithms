"""UNION-FIND
Union-Find is a data structure that tracks and merges "disjoint sets". Union-
Find operations include:

1) "find" which subset an element is in; 
2) "union" two subsets into one

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

class UnionFind:
	"""UnionFind abstracts union-find problem into a parent array, in 
	which two objects, p & q, are connected iff their roots	are the same.

	UnionFind (aka Quick Union) is a "lazy" approach.

	In addition, two techniques are used to improve performance: 
	1) find with path compression, which updates parent to root while search for it.
	2) uion with rank, which links smaller tree to larger tree;
	"""

	def __init__(self, n: int):
		"""Initialize a UnionFind object ~ O(N)
		In UnionFind, connected components are reflected in common roots. 
		"""
		self.parent = list(range(n)) # parent array (to reflect subsets)
		self.rank = [1] * n          # size of subtree

	def find(self, p: int, halving: bool=True) -> int:
		"""Find with path compression ~ O(1) on average."""
		if p != self.parent[p]:
			self.parent[p] = self.find(self.parent[p]) # path compression
		return self.parent[p]

	def union(self, p: int, q: int) -> bool:
		"""Union with rank ~ O(1) on average"""
		prt, qrt = self.find(p), self.find(q)
		if prt == qrt: return False # already linked
		if self.rank[prt] > self.rank[qrt]: prt, qrt = qrt, prt # rank[prt] <= rank[qrt]
		self.parent[prt] = qrt
		self.rank[qrt] += self.rank[prt]
		return True


if __name__ == "__main__": 
	"""Test client for UnionFind"""
	uf = UnionFind(10)
	uf.union(4, 3)
	uf.union(3, 8)
	uf.union(6, 5)
	uf.union(9, 4)
	uf.union(2, 1)
	print("8-9? ", uf.find(8) == uf.find(9)) # true
	print("5-0? ", uf.find(5) == uf.find(0)) # false
	uf.union(5, 0)
	uf.union(7, 2)
	uf.union(6, 1)
	print("5-0? ", uf.find(5) == uf.find(0)) # true